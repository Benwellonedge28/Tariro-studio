import os
import json
import asyncio
from typing import Dict, List, Tuple, Any, Set
import hmac
import hashlib
from datetime import datetime
import uuid

# --- Configuration & Shared Data (initialized from studio_v3_core.py) ---
_WORKSPACE: str = ""
_SWARM_VISUALIZER: Any = None
_POLICY_AUDIT_TRAIL: Any = None
_ASYNC_NOTIFICATION_SYSTEM: Any = None
_GLOBAL_STATE_MANAGER: Any = None

ADMINS_FILE: str = ""
DEFAULT_ROOT_ADMIN: str = ""

# Define permissions for each role
ROLE_PERMS: Dict[str, Set[str]] = {
    "root": {"system_mutation", "deployment", "governance", "user_admin", "view_architecture", "view_audit", "security_bypass", "full_access"},
    "sysop": {"deployment", "code_generation", "view_logs", "run_queries", "manage_resources"},
    "analyst": {"run_queries", "view_dashboard", "access_data"},
    "user": {"run_tasks"}
}

def initialize_rbac_manager(workspace_path: str, swarm_visualizer_module: Any, policy_audit_trail_module: Any, async_notification_system_module: Any, global_state_manager_module: Any, default_root_admin_email: str):
    """Initializes global configurations for the RBAC Manager module."""
    global _WORKSPACE, _SWARM_VISUALIZER, _POLICY_AUDIT_TRAIL, _ASYNC_NOTIFICATION_SYSTEM, _GLOBAL_STATE_MANAGER, ADMINS_FILE, DEFAULT_ROOT_ADMIN
    
    _WORKSPACE = workspace_path
    _SWARM_VISUALIZER = swarm_visualizer_module
    _POLICY_AUDIT_TRAIL = policy_audit_trail_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    ADMINS_FILE = os.path.join(_WORKSPACE, "admins.json")
    DEFAULT_ROOT_ADMIN = default_root_admin_email

    if not os.path.exists(ADMINS_FILE):
        with open(ADMINS_FILE, "w") as f:
            json.dump({DEFAULT_ROOT_ADMIN: "root"}, f)
        print(f"Initialized admins.json with default root admin: {DEFAULT_ROOT_ADMIN}")

    print(f"RBAC Manager initialized. Admins file: {ADMINS_FILE}")

async def get_user_role(username: str) -> Tuple[str, Set[str]]:
    """
    Retrieves the role and associated permissions for a given user.
    """
    try:
        with open(ADMINS_FILE, "r") as f:
            admins = json.load(f)
        role = admins.get(username, "user")
        return role, ROLE_PERMS.get(role, set())
    except FileNotFoundError:
        print(f"WARNING: admins.json not found. Defaulting {username} to 'user' role.")
        return "user", ROLE_PERMS.get("user", set())
    except json.JSONDecodeError:
        print(f"ERROR: Invalid JSON in admins.json. Defaulting {username} to 'user' role.")
        return "user", ROLE_PERMS.get("user", set())

async def check_permission(username: str, permission: str) -> bool:
    """
    Checks if a user has a specific permission.
    """
    role, perms = await get_user_role(username)
    return permission in perms

async def add_admin(task_id: str, requester: str, new_user: str, new_role: str) -> Dict:
    """
    Adds or updates an admin user's role.
    Requires 'user_admin' permission. Samuel Mukandara is immutable root.
    """
    req_role, req_perms = await get_user_role(requester)
    
    if "user_admin" not in req_perms:
        await _POLICY_AUDIT_TRAIL.log_event(
            task_id, "rbac_add_admin_denied", f"Unauthorized attempt to add admin by {requester}.",
            {"requester": requester, "new_user": new_user, "new_role": new_role},
            user_id=requester, agent_role="RBACManager", level="CRITICAL"
        )
        return {"status": "DENIED", "reason": "Insufficient permissions"}

    if new_role == "root" and requester != DEFAULT_ROOT_ADMIN:
        await _POLICY_AUDIT_TRAIL.log_event(
            task_id, "rbac_add_root_denied", f"Unauthorized attempt by {requester} to grant root to {new_user}.",
            {"requester": requester, "new_user": new_user},
            user_id=requester, agent_role="RBACManager", level="CRITICAL"
        )
        return {"status": "DENIED", "reason": f"Only {DEFAULT_ROOT_ADMIN} can grant root role"}

    if new_user == DEFAULT_ROOT_ADMIN and new_role != "root":
        await _POLICY_AUDIT_TRAIL.log_event(
            task_id, "rbac_demote_root_denied", f"Unauthorized attempt by {requester} to demote {DEFAULT_ROOT_ADMIN}.",
            {"requester": requester, "new_user": new_user, "new_role": new_role},
            user_id=requester, agent_role="RBACManager", level="CRITICAL"
        )
        return {"status": "DENIED", "reason": "Cannot demote default root admin"}
    
    # Implement 2-Man Rule for root roles if enabling later: Samuel Mukandara + 1 other root approval
    # For now, it's a direct grant by Samuel

    try:
        with open(ADMINS_FILE, "r+") as f:
            admins = json.load(f)
            old_role = admins.get(new_user, "none")
            admins[new_user] = new_role
            f.seek(0); json.dump(admins, f); f.truncate()
        
        await _POLICY_AUDIT_TRAIL.log_event(
            task_id, "rbac_add_admin_success", f"User {requester} added/updated {new_user} with role {new_role}.",
            {"requester": requester, "new_user": new_user, "old_role": old_role, "new_role": new_role},
            user_id=requester, agent_role="RBACManager", level="INFO"
        )
        await _SWARM_VISUALIZER.log_event(
            task_id, "admin_role_updated", f"User {new_user} role set to {new_role}.",
            {"new_user": new_user, "new_role": new_role},
            agent_id=requester, agent_role="RBACManager"
        )
        if _ASYNC_NOTIFICATION_SYSTEM:
            await _ASYNC_NOTIFICATION_SYSTEM.send_notification(new_user, task_id, f"Your role in Tariro Studio has been set to {new_role} by {requester}.", title="Tariro Role Update")
            if new_user != requester:
                await _ASYNC_NOTIFICATION_SYSTEM.send_notification(requester, task_id, f"Successfully set {new_user}'s role to {new_role}.", title="Role Update Confirmation")

        return {"status": "SUCCESS", "user": new_user, "role": new_role}
    except Exception as e:
        await _POLICY_AUDIT_TRAIL.log_event(
            task_id, "rbac_add_admin_error", f"Error adding admin {new_user}: {e}.",
            {"requester": requester, "new_user": new_user, "new_role": new_role, "error": str(e)},
            user_id=requester, agent_role="RBACManager", level="CRITICAL"
        )
        return {"status": "ERROR", "reason": str(e)}

async def get_all_admins() -> List[Dict[str, str]]:
    """
    Retrieves a list of all configured admins and their roles.
    """
    try:
        with open(ADMINS_FILE, "r") as f:
            admins = json.load(f)
        return [{"username": u, "role": r} for u, r in admins.items()]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("ERROR: Invalid JSON in admins.json during get_all_admins.")
        return []
