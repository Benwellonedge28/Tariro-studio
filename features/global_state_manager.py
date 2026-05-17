import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid

# --- Configuration & Shared Data ---
_WORKSPACE: str = ""
_POLICY_AUDIT_TRAIL: Any = None # Reference to Policy Audit Trail module
_SWARM_VISUALIZER: Any = None # Reference to Swarm Visualizer module
_CRUD_MANAGER: Any = None # Reference to CRUD Manager for StateLog entities
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For critical state change notifications

GLOBAL_STATE_MANAGER_LOG_DIR: str = ""

# In-memory mock for global state. In a real system, this would be a persistent, distributed key-value store.
_GLOBAL_STATE: Dict[str, Any] = {}

def initialize_global_state_manager(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, policy_audit_trail_module: Any, async_notification_system_module: Any):
    """Initializes global state manager configurations."""
    global _WORKSPACE, _POLICY_AUDIT_TRAIL, _SWARM_VISUALIZER, _CRUD_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, GLOBAL_STATE_MANAGER_LOG_DIR
    
    _WORKSPACE = workspace_path
    _POLICY_AUDIT_TRAIL = policy_audit_trail_module
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module

    GLOBAL_STATE_MANAGER_LOG_DIR = os.path.join(_WORKSPACE, "global_state_manager_logs")
    os.makedirs(GLOBAL_STATE_MANAGER_LOG_DIR, exist_ok=True)
    print(f"Global State Manager initialized. Logs: {GLOBAL_STATE_MANAGER_LOG_DIR}")

    # Attempt to load initial state from persistent storage if available
    # In a real system, this would involve loading from a database, not a flat file
    state_filepath = os.path.join(GLOBAL_STATE_MANAGER_LOG_DIR, "initial_state.json")
    if os.path.exists(state_filepath):
        try:
            with open(state_filepath, "r") as f:
                _GLOBAL_STATE.update(json.load(f))
            print("Loaded initial global state from file.")
        except Exception as e:
            print(f"WARNING: Failed to load initial state from file: {e}")

async def get_state(key: str) -> Optional[Any]:
    """
    Retrieves a value from the global state by its key.
    """
    # Optional: Log state access if it's sensitive or critical
    # if _POLICY_AUDIT_TRAIL:
    #     await _POLICY_AUDIT_TRAIL.log_event(
    #         session_id=str(uuid.uuid4()), event_type="state_access",
    #         description=f"Accessed global state key: {key}", metadata={"key": key},
    #         agent_role="GlobalStateManager", level="DEBUG"
    #     )
    return _GLOBAL_STATE.get(key)

async def set_state(key: str, value: Any, user_id: str = "Tariro_System", auditable: bool = True, notify_changes: bool = False, is_critical: bool = False) -> Dict[str, Any]:
    """
    Sets a value in the global state for a given key. Optionally logs and notifies.

    Args:
        key (str): The key for the state variable.
        value (Any): The value to set.
        user_id (str): The ID of the user or entity modifying the state.
        auditable (bool): Whether this state change should be logged in the audit trail.
        notify_changes (bool): Whether to send a notification for this change.
        is_critical (bool): If true, and notify_changes is true, notification priority will be critical.

    Returns:
        Dict[str, Any]: Status of the operation.
    """
    old_value = _GLOBAL_STATE.get(key)
    _GLOBAL_STATE[key] = value

    event_description = f"Global state key '{key}' updated." if old_value != value else f"Global state key '{key}' set (no change)."
    event_metadata = {"key": key, "old_value": old_value, "new_value": value, "user_id": user_id}

    if auditable and _POLICY_AUDIT_TRAIL:
        await _POLICY_AUDIT_TRAIL.log_event(
            session_id=str(uuid.uuid4()), event_type="state_change",
            description=event_description, metadata=event_metadata,
            user_id=user_id, agent_role="GlobalStateManager", level="INFO"
        )
    if _SWARM_VISUALIZER:
        await _SWARM_VISUALIZER.log_event(
            session_id=str(uuid.uuid4()), event_type="state_change",
            message=event_description,
            details=event_metadata,
            agent_id=user_id, agent_role="GlobalStateManager", level="INFO"
        )
    if notify_changes and _ASYNC_NOTIFICATION_SYSTEM:
        priority = "critical" if is_critical else "medium"
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
            user_id,
            str(uuid.uuid4()), # Create a new task_id for the notification itself
            f"Global state '{key}' changed from {old_value} to {value}.",
            title=f"Critical State Change: {key}" if is_critical else f"State Change: {key}",
            category="system_update",
            causal_priority=priority
        )

    return {"status": "success", "key": key, "value": value, "changed": (old_value != value)}

async def delete_state(key: str, user_id: str = "Tariro_System", auditable: bool = True) -> Dict[str, Any]:
    """
    Deletes a key-value pair from the global state.
    """
    if key in _GLOBAL_STATE:
        value = _GLOBAL_STATE.pop(key)
        if auditable and _POLICY_AUDIT_TRAIL:
            await _POLICY_AUDIT_TRAIL.log_event(
                session_id=str(uuid.uuid4()), event_type="state_delete",
                description=f"Global state key '{key}' deleted.", metadata={
                    "key": key,
                    "deleted_value": value
                },
                user_id=user_id, agent_role="GlobalStateManager", level="WARNING"
            )
        return {"status": "success", "key": key, "deleted_value": value}
    return {"status": "failed", "reason": f"Key '{key}' not found in global state."}

async def get_all_state() -> Dict[str, Any]:
    """
    Retrieves a copy of the entire global state.
    """
    return _GLOBAL_STATE.copy()
