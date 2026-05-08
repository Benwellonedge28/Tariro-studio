import os
import json
import hmac
import hashlib
import time
import logging
from typing import Dict, List, Tuple, Any, Set, Optional

logger = logging.getLogger("RbacManager")

# Global constant, assumed to be set by the main studio_v3.py
# This WORKSPACE path must be consistent with studio_v3.py and Dockerfile VOLUME
WORKSPACE = os.getenv("WORKSPACE", "/app/workspace")
ADMINS_FILE = os.path.join(WORKSPACE, "admins.json")
DEFAULT_ROOT_ADMIN = "Samuel Mukandara" # hardcoded, immutable root admin

# Permissions for roles
# Define comprehensive permissions that align with system capabilities
ROLE_PERMS: Dict[str, Set[str]] = {
    "root": {"system_mutation", "deployment", "governance", "user_admin", "view_architecture", 
             "admin_chat_access", "debug_access", "full_override", "audit_access", "read_any_log"},
    "sysop": {"deployment", "code_generation", "view_logs", "admin_chat_access", "read_own_logs"},
    "analyst": {"run_queries", "view_dashboard", "admin_chat_access"},
    "developer": {"code_generation", "view_logs", "test_execution"},
    "user": set() # Standard users have no special permissions by default
}

# Reference to the policy_audit_trail module for logging actions
policy_audit_trail_module: Optional[Any] = None

def initialize_rbac_manager(audit_trail_module: Any):
    """Initializes the RBAC manager, ensuring default root admin exists and setting up audit logging."""
    global policy_audit_trail_module
    policy_audit_trail_module = audit_trail_module
    
    os.makedirs(WORKSPACE, exist_ok=True)
    if not os.path.exists(ADMINS_FILE):
        initial_admins = {DEFAULT_ROOT_ADMIN: "root"}
        with open(ADMINS_FILE, "w") as f:
            json.dump(initial_admins, f, indent=2)
        logger.info(f"Initialized RBAC with default root admin: {DEFAULT_ROOT_ADMIN}")
    else:
        # Ensure Samuel Mukandara is always root if file exists but might be modified
        try:
            with open(ADMINS_FILE, "r+") as f:
                admins = json.load(f)
                if admins.get(DEFAULT_ROOT_ADMIN) != "root":
                    admins[DEFAULT_ROOT_ADMIN] = "root"
                    f.seek(0)
                    json.dump(admins, f, indent=2)
                    f.truncate()
                    logger.warning(f"Ensured {DEFAULT_ROOT_ADMIN} is set as 'root' in {ADMINS_FILE}.")
        except (FileNotFoundError, json.JSONDecodeError):
            logger.error(f"Admins file {ADMINS_FILE} corrupted. Recreating with default root.")
            initialize_rbac_manager(audit_trail_module) # Re-initialize if corrupted

async def get_user_role(username: str) -> Tuple[str, Set[str]]:
    """Retrieve a user's role string and a set of their associated permissions."""
    try:
        with open(ADMINS_FILE) as f:
            admins = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error(f"Admins file not found or corrupted: {ADMINS_FILE}. Returning 'user' role.")
        return "user", ROLE_PERMS.get("user", set())

    role_str = admins.get(username, "user")
    perms = ROLE_PERMS.get(role_str, set())
    return role_str, perms

async def add_admin(task_id: str, requester: str, new_user: str, new_role: str) -> Dict:
    """Add or update an admin user's role, with permission checks and immutable root rule."""
    req_role_str, req_perms = await get_user_role(requester)
    
    # Check if requester has permission to manage users
    if "user_admin" not in req_perms and "full_override" not in req_perms:
        logger.warning(f"Access denied: {requester} attempted to add admin without 'user_admin' perm.")
        return {"status": "DENIED", "reason": "Insufficient permissions: 'user_admin' required."}
    
    # Enforce immutable root admin rule
    if new_user == DEFAULT_ROOT_ADMIN and new_role != "root":
        logger.warning(f"Access denied: {requester} attempted to demote immutable root admin {DEFAULT_ROOT_ADMIN}.")
        return {"status": "DENIED", "reason": f"Cannot demote {DEFAULT_ROOT_ADMIN}."}
    
    # Enforce 2-man rule for granting 'root' role: Only the default root can grant 'root'
    if new_role == "root" and requester != DEFAULT_ROOT_ADMIN:
        logger.warning(f"Access denied: {requester} attempted to grant 'root' role but is not {DEFAULT_ROOT_ADMIN}.")
        return {"status": "DENIED", "reason": f"Only {DEFAULT_ROOT_ADMIN} can grant 'root' role."}

    try:
        with open(ADMINS_FILE, "r+") as f:
            admins = json.load(f)
            old_role = admins.get(new_user, "none")
            admins[new_user] = new_role
            f.seek(0) # Rewind to beginning
            json.dump(admins, f, indent=2)
            f.truncate() # Truncate any remaining old content
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Failed to update {ADMINS_FILE}: {e}")
        return {"status": "ERROR", "reason": f"Failed to update admin file: {e}"}
    
    if policy_audit_trail_module:
        await policy_audit_trail_module.log_change(
            task_id=task_id, 
            event_type="rbac_user_role_update", 
            old_value=old_role, 
            new_value=new_role, 
            actor=requester, 
            description=f"Role changed for {new_user} from {old_role} to {new_role}."
        )
    else:
        logger.warning("Policy audit trail module not initialized for RBAC manager. Audit log skipped.")

    logger.info(f"Admin user {new_user} role changed to {new_role} by {requester}.")
    return {"status": "SUCCESS", "user": new_user, "role": new_role, "previous_role": old_role}

async def get_all_admins() -> List[List[str]]:
    """Return a list of all admins and their roles for display (e.g., in UI)."""
    try:
        with open(ADMINS_FILE) as f:
            admins = json.load(f)
        return [[user, role] for user, role in admins.items()]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error reading admins file {ADMINS_FILE}: {e}. Returning empty list.")
        return []


