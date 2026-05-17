import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid

# --- Configuration & Shared Data ---
_WORKSPACE: str = ""
_POLICY_AUDIT_TRAIL: Any = None # Reference to Policy Audit Trail module
_CRUD_MANAGER: Any = None # Reference to CRUD Manager for Role/Permission entities
_GLOBAL_STATE_MANAGER: Any = None # For storing/retrieving current RBAC configurations

RBAC_MANAGER_LOG_DIR: str = ""

# Mock RBAC configuration (in a real system, this would be persistent and dynamic)
_MOCKED_ROLES_PERMISSIONS: Dict[str, Dict[str, List[str]]] = {
    "super_admin": {
        "permissions": [
            "*
        ],
        "description": "Full control over all system functions and data."
    },
    "developer": {
        "permissions": [
            "chat",
            "initiate_lang_dev_pipeline",
            "initiate_app_dev_pipeline",
            "read_system_logs",
            "debug_modules",
            "upload_files",
            "access_crud_manager",
            "scan_for_new_modules",
            "learn_new_lang_framework"
        ],
        "description": "Permissions for development activities."
    },
    "security_auditor": {
        "permissions": [
            "read_system_logs",
            "review_policy_violations",
            "audit_security_configs",
            "access_crud_manager"
        ],
        "description": "View system logs and security-related configurations."
    },
    "guest": {
        "permissions": [
            "chat",
            "view_public_info"
        ],
        "description": "Limited view and chat capabilities."
    }
}

_MOCKED_USER_ROLES: Dict[str, List[str]] = {
    "Samuel Mukandara": ["super_admin"],  # Root admin
    "dev_user_1": ["developer"],
    "auditor_1": ["security_auditor"],
    "guest_user": ["guest"]
}

def initialize_rbac_manager(workspace_path: str, policy_audit_trail_module: Any, crud_manager_module: Any, global_state_manager_module: Any):
    """Initializes global RBAC configurations."""
    global _WORKSPACE, _POLICY_AUDIT_TRAIL, _CRUD_MANAGER, _GLOBAL_STATE_MANAGER, RBAC_MANAGER_LOG_DIR
    
    _WORKSPACE = workspace_path
    _POLICY_AUDIT_TRAIL = policy_audit_trail_module
    _CRUD_MANAGER = crud_manager_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module

    RBAC_MANAGER_LOG_DIR = os.path.join(_WORKSPACE, "rbac_manager_logs")
    os.makedirs(RBAC_MANAGER_LOG_DIR, exist_ok=True)
    print(f"RBAC Manager initialized. Logs: {RBAC_MANAGER_LOG_DIR}")

    # Load or initialize roles/permissions in Global State Manager
    initial_roles = asyncio.run(_GLOBAL_STATE_MANAGER.get_state("rbac_roles_permissions"))
    if initial_roles:
        _MOCKED_ROLES_PERMISSIONS.update(initial_roles)
    else:
        asyncio.run(_GLOBAL_STATE_MANAGER.set_state("rbac_roles_permissions", _MOCKED_ROLES_PERMISSIONS, "Tariro_System", auditable=True))

    initial_user_roles = asyncio.run(_GLOBAL_STATE_MANAGER.get_state("rbac_user_roles"))
    if initial_user_roles:
        _MOCKED_USER_ROLES.update(initial_user_roles)
    else:
        asyncio.run(_GLOBAL_STATE_MANAGER.set_state("rbac_user_roles", _MOCKED_USER_ROLES, "Tariro_System", auditable=True))

async def check_permission(user_id: str, permission: str, policy_audit_trail: Any) -> bool:
    """
    Checks if a given user has the specified permission.

    Args:
        user_id (str): The ID of the user.
        permission (str): The permission string to check.
        policy_audit_trail (Any): The policy audit trail module for logging.

    Returns:
        bool: True if the user has the permission, False otherwise.
    """
    user_roles = _MOCKED_USER_ROLES.get(user_id, [])
    roles_permissions = _MOCKED_ROLES_PERMISSIONS # Access directly from global for simplicity

    has_permission = False
    for role_name in user_roles:
        role = roles_permissions.get(role_name)
        if role and ("*" in role["permissions"] or permission in role["permissions"]):
            has_permission = True
            break

    if policy_audit_trail:
        await policy_audit_trail.log_event(
            session_id=str(uuid.uuid4()), # New session for RBAC check
            event_type="rbac_check",
            description=f"Permission check for user {user_id} on {permission}: {has_permission}",
            metadata={
                "user_id": user_id,
                "permission": permission,
                "user_roles": user_roles,
                "result": has_permission
            },
            user_id=user_id,
            agent_role="RBAC_Manager",
            level="INFO"
        )

    return has_permission

async def add_role(role_name: str, permissions: List[str], description: str, user_id: str = "Tariro_System") -> Dict[str, Any]:
    """
    Adds a new role to the RBAC system.
    """
    if role_name in _MOCKED_ROLES_PERMISSIONS:
        return {"status": "failed", "reason": f"Role {role_name} already exists."}
    
    _MOCKED_ROLES_PERMISSIONS[role_name] = {"permissions": permissions, "description": description}
    await _GLOBAL_STATE_MANAGER.set_state("rbac_roles_permissions", _MOCKED_ROLES_PERMISSIONS, user_id, auditable=True)
    if _POLICY_AUDIT_TRAIL:
        await _POLICY_AUDIT_TRAIL.log_event(str(uuid.uuid4()), "rbac_add_role", f"Role {role_name} added.", {"role_name": role_name, "permissions": permissions}, user_id=user_id, agent_role="RBAC_Manager")
    return {"status": "success", "message": f"Role {role_name} added."}

async def assign_role_to_user(user_id_target: str, role_name: str, admin_user_id: str = "Tariro_System") -> Dict[str, Any]:
    """
    Assigns a role to a user.
    """
    if role_name not in _MOCKED_ROLES_PERMISSIONS:
        return {"status": "failed", "reason": f"Role {role_name} does not exist."}

    if user_id_target not in _MOCKED_USER_ROLES:
        _MOCKED_USER_ROLES[user_id_target] = []
    if role_name not in _MOCKED_USER_ROLES[user_id_target]:
        _MOCKED_USER_ROLES[user_id_target].append(role_name)
    
    await _GLOBAL_STATE_MANAGER.set_state("rbac_user_roles", _MOCKED_USER_ROLES, admin_user_id, auditable=True)
    if _POLICY_AUDIT_TRAIL:
        await _POLICY_AUDIT_TRAIL.log_event(str(uuid.uuid4()), "rbac_assign_role", f"Role {role_name} assigned to {user_id_target}.", {"user_id": user_id_target, "role_name": role_name}, user_id=admin_user_id, agent_role="RBAC_Manager")
    return {"status": "success", "message": f"Role {role_name} assigned to {user_id_target}."}

async def remove_role_from_user(user_id_target: str, role_name: str, admin_user_id: str = "Tariro_System") -> Dict[str, Any]:
    """
    Removes a role from a user.
    """
    if user_id_target in _MOCKED_USER_ROLES and role_name in _MOCKED_USER_ROLES[user_id_target]:
        _MOCKED_USER_ROLES[user_id_target].remove(role_name)
        await _GLOBAL_STATE_MANAGER.set_state("rbac_user_roles", _MOCKED_USER_ROLES, admin_user_id, auditable=True)
        if _POLICY_AUDIT_TRAIL:
            await _POLICY_AUDIT_TRAIL.log_event(str(uuid.uuid4()), "rbac_remove_role", f"Role {role_name} removed from {user_id_target}.", {"user_id": user_id_target, "role_name": role_name}, user_id=admin_user_id, agent_role="RBAC_Manager")
        return {"status": "success", "message": f"Role {role_name} removed from {user_id_target}."}
    return {"status": "failed", "reason": f"User {user_id_target} does not have role {role_name}."}

async def get_user_roles(user_id: str) -> List[str]:
    """
    Retrieves all roles assigned to a user.
    """
    return _MOCKED_USER_ROLES.get(user_id, [])

async def get_role_permissions(role_name: str) -> List[str]:
    """
    Retrieves all permissions for a specific role.
    """
    role = _MOCKED_ROLES_PERMISSIONS.get(role_name)
    return role["permissions"] if role else []
