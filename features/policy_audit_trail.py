import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid

# --- Configuration & Shared Data (initialized from studio_v3_core.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Base model definitions from studio_v3_core.py
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module
_CRUD_MANAGER: Any = None # Reference to crud_manager module for AuditLog entities

POLICY_AUDIT_TRAIL_LOG_DIR: str = ""

def initialize_policy_audit_trail(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any):
    """Initializes global configurations for the Policy Audit Trail module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, POLICY_AUDIT_TRAIL_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module

    POLICY_AUDIT_TRAIL_LOG_DIR = os.path.join(_WORKSPACE, "policy_audit_trail_logs")
    os.makedirs(POLICY_AUDIT_TRAIL_LOG_DIR, exist_ok=True)
    print(f"Policy Audit Trail initialized. Logs: {POLICY_AUDIT_TRAIL_LOG_DIR}")

async def log_event(session_id: str, event_type: str, description: str, metadata: Dict[str, Any], user_id: str = "Tariro_System", agent_role: str = "System", level: str = "INFO") -> Dict[str, Any]:
    """
    Logs an auditable event to the system. This function is called by other modules
    to record significant actions, decisions, or system states for accountability,
    debugging, and meta-cognitive reflection.

    Args:
        session_id (str): A unique identifier for the current session or task.
        event_type (str): Categorization of the event (e.g., "rbac_check", "firewall_action", "module_load_failure").
        description (str): A concise natural language description of the event.
        metadata (Dict[str, Any]): A dictionary containing relevant structured data about the event.
        user_id (str): The ID of the user or entity that initiated the action (defaults to "Tariro_System").
        agent_role (str): The specific role or module within Tariro that generated the event.
        level (str): Severity level of the log ("INFO", "WARNING", "ERROR", "CRITICAL").

    Returns:
        Dict[str, Any]: A dictionary containing the status of the log operation and the created log entry.
    """
    log_entry = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "session_id": session_id,
        "user_id": user_id,
        "agent_role": agent_role,
        "event_type": event_type,
        "description": description,
        "metadata": metadata,
        "level": level
    }

    # Log to local file for persistence and immediate access
    log_filename = os.path.join(POLICY_AUDIT_TRAIL_LOG_DIR, f"audit_log_{datetime.now().strftime("%Y%m%d")}.jsonl")
    try:
        with open(log_filename, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    except Exception as e:
        print(f"ERROR: Failed to write to audit log file: {e}")
        # Fallback if file logging fails

    # Also store in CRUD Manager for structured querying
    if _CRUD_MANAGER:
        try:
            # The CRUD manager would typically define the schema for 'AuditLog' entities.
            # For now, we pass the dictionary directly.
            await _CRUD_MANAGER.create_entity("AuditLog", log_entry)
        except Exception as e:
            print(f"ERROR: Failed to store audit log in CRUD Manager: {e}")
            # This could be a critical error depending on system design.

    # Log to swarm visualizer (if initialized) for real-time monitoring
    if _SWARM_VISUALIZER:
        try:
            await _SWARM_VISUALIZER.log_event(session_id, event_type, description, metadata, user_id, agent_role, level)
        except Exception as e:
            print(f"ERROR: Failed to log event to Swarm Visualizer: {e}")

    return {"status": "success", "log_entry_id": log_entry["id"], "log_entry": log_entry}

async def get_logs_for_session(session_id: str, limit: int = 100) -> List[Dict[str, Any]]:
    """
    Retrieves a list of audit logs for a given session ID.

    Args:
        session_id (str): The ID of the session to retrieve logs for.
        limit (int): The maximum number of log entries to retrieve.

    Returns:
        List[Dict[str, Any]]: A list of audit log entries.
    """
    if not _CRUD_MANAGER:
        print("WARNING: CRUD Manager not initialized. Cannot retrieve audit logs.")
        return []
    try:
        # Assuming CRUD Manager has a filter method that supports querying by session_id
        logs = await _CRUD_MANAGER.filter_entities("AuditLog", {"session_id": session_id}, limit=limit, sort_by="timestamp")
        return logs
    except Exception as e:
        print(f"ERROR: Failed to retrieve audit logs from CRUD Manager: {e}")
        return []

async def get_recent_logs_for_component(component_name: str, limit: int = 20) -> List[Dict[str, Any]]:
    """
    Retrieves recent audit logs generated by a specific component/agent role.
    """
    if not _CRUD_MANAGER:
        print("WARNING: CRUD Manager not initialized. Cannot retrieve audit logs.")
        return []
    try:
        # Assuming CRUD Manager has a filter method that supports querying by agent_role
        logs = await _CRUD_MANAGER.filter_entities("AuditLog", {"agent_role": component_name}, limit=limit, sort_by="timestamp")
        return logs
    except Exception as e:
        print(f"ERROR: Failed to retrieve audit logs from CRUD Manager for component {component_name}: {e}")
        return []
