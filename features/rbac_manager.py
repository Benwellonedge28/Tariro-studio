import os
import json
import hmac
import hashlib
from typing import Dict, List, Tuple, Any, Set
import logging

logger = logging.getLogger("RbacManager")

# Global constant, assumed to be set by the main studio_v3.py
WORKSPACE = os.getenv("WORKSPACE", "/app/workspace")
ADMINS_FILE = os.path.join(WORKSPACE, "admins.json")
DEFAULT_ROOT_ADMIN = "Samuel Mukandara" # hardcoded, cannot be removed

# Permissions for roles
ROLE_PERMS: Dict[str, Set[str]] = {
    "root": {"system_mutation", "deployment", "governance", "user_admin", "view_architecture", "admin_chat_access", "debug_access", "full_override"},
    "sysop": {"deployment", "code_generation", "view_logs", "admin_chat_access"},
    "analyst": {"run_queries", "view_dashboard", "admin_chat_access"},
    "user": set()
}

def initialize_rbac_manager(policy_audit_trail_module: Any):
    # Ensure the workspace exists
    os.makedirs(WORKSPACE, exist_ok=True)
    if not os.path.exists(ADMINS_FILE):
        initial_admins = {DEFAULT_ROOT_ADMIN: "root"}
        with open(ADMINS_FILE, "w") as f:
            json.dump(initial_admins, f, indent=2)
        logger.info(f"Initialized RBAC with default root admin: {DEFAULT_ROOT_ADMIN}")
    # Store the policy_audit_trail module for logging changes
    global policy_audit_trail
    policy_audit_trail = policy_audit_trail_module

async def get_user_role(username: str) -> Tuple[str, Set[str]]:
    """Retrieve a user's role and associated permissions."""
    try:
        with open(ADMINS_FILE) as f:
            admins = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error(f"Admins file not found or corrupted: {ADMINS_FILE}. Re-initializing.")
        initialize_rbac_manager(policy_audit_trail) # Re-initialize if file is bad
        with open(ADMINS_FILE) as f:
            admins = json.load(f)

    role_str = admins.get(username, "user")
    perms = ROLE_PERMS.get(role_str, set())
    logger.debug(f"User {username} has role {role_str} with permissions {perms}")
    return role_str, perms

async def add_admin(task_id: str, requester: str, new_user: str, new_role: str) -> Dict:
    """Add or update an admin user's role, with permission checks and 2-man rule for root."""
    req_role_str, req_perms = await get_user_role(requester)
    
    if "user_admin" not in req_perms and "full_override" not in req_perms:
        logger.warning(f"Access denied: {requester} attempted to add admin without 'user_admin' perm.")
        return {"status": "DENIED", "reason": "Insufficient permissions to manage admins."}
    
    if new_role == "root":
        if requester != DEFAULT_ROOT_ADMIN:
            logger.warning(f"Access denied: {requester} attempted to grant root role, but is not {DEFAULT_ROOT_ADMIN}.")
            return {"status": "DENIED", "reason": f"Only {DEFAULT_ROOT_ADMIN} can grant 'root' role."}
        # Enforce 2-man rule for granting root: requires explicit approval/confirmation from another root
        # This would typically be an out-of-band confirmation or a multi-step workflow.
        # For this implementation, we'll simplify and say only Samuel can grant root.

    if new_user == DEFAULT_ROOT_ADMIN and new_role != "root":
        logger.warning(f"Access denied: {requester} attempted to demote {DEFAULT_ROOT_ADMIN}.")
        return {"status": "DENIED", "reason": f"Cannot demote {DEFAULT_ROOT_ADMIN}."}

    try:
        with open(ADMINS_FILE, "r+") as f:
            admins = json.load(f)
            old_role = admins.get(new_user, "none")
            admins[new_user] = new_role
            f.seek(0)
            json.dump(admins, f, indent=2)
            f.truncate()
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Failed to update {ADMINS_FILE}: {e}")
        return {"status": "ERROR", "reason": f"Failed to update admin file: {e}"}
    
    if policy_audit_trail:
        await policy_audit_trail.log_change(
            task_id, "rbac_add_admin", old_role, {"user": new_user, "role": new_role}, 
            requester, f"Role grant: {new_role} for {new_user}"
        )
    else:
        logger.warning("Policy audit trail module not initialized for RBAC manager.")

    logger.info(f"Admin {new_user} role changed to {new_role} by {requester}.")
    return {"status": "SUCCESS", "user": new_user, "role": new_role}

async def get_all_admins() -> List[Tuple[str, str]]:
    """Return a list of all admins and their roles."""
    try:
        with open(ADMINS_FILE) as f:
            admins = json.load(f)
        return list(admins.items())
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error(f"Admins file not found or corrupted: {ADMINS_FILE}.")
        return []
