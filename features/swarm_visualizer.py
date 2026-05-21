import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid

# --- Configuration & Shared Data ---
_WORKSPACE: str = ""
_CRUD_MANAGER: Any = None # Reference to CRUD Manager for EventLog entities

SWARM_VISUALIZER_LOG_DIR: str = ""

def initialize_swarm_visualizer(workspace_path: str, crud_manager_module: Any):
    """Initializes global configurations for the Swarm Visualizer module."""
    global _WORKSPACE, _CRUD_MANAGER, SWARM_VISUALIZER_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CRUD_MANAGER = crud_manager_module

    SWARM_VISUALIZER_LOG_DIR = os.path.join(_WORKSPACE, "swarm_visualizer_logs")
    os.makedirs(SWARM_VISUALIZER_LOG_DIR, exist_ok=True)
    print(f"Swarm Visualizer initialized. Logs: {SWARM_VISUALIZER_LOG_DIR}")

async def log_event(session_id: str, event_type: str, message: str, details: Dict[str, Any], agent_id: str = "Tariro_System", agent_role: str = "System", level: str = "INFO", timestamp: Optional[str] = None):
    """
    Logs a structured event for visualization in the Swarm Monitoring UI.

    Args:
        session_id (str): A unique identifier for the current session or task this event relates to.
        event_type (str): Categorization of the event (e.g., "task_start", "llm_call", "tool_execution").
        message (str): A concise natural language message describing the event.
        details (Dict[str, Any]): A dictionary containing structured data relevant to the event.
        agent_id (str): The ID of the agent or module generating the event (defaults to "Tariro_System").
        agent_role (str): The specific role or function of the agent/module.
        level (str): Severity level of the event ("INFO", "WARNING", "ERROR", "CRITICAL").
        timestamp (Optional[str]): ISO format timestamp. If None, current time is used.
    """
    event_entry = {
        "id": str(uuid.uuid4()),
        "timestamp": timestamp or datetime.now().isoformat(),
        "session_id": session_id,
        "agent_id": agent_id,
        "agent_role": agent_role,
        "event_type": event_type,
        "message": message,
        "details": details,
        "level": level
    }

    # Log to local file for persistence and immediate access
    log_filename = os.path.join(SWARM_VISUALIZER_LOG_DIR, f"swarm_events_{datetime.now().strftime('%Y%m%d')}.jsonl")
    try:
        with open(log_filename, "a") as f:
            f.write(json.dumps(event_entry) + "\n")
    except Exception as e:
        print(f"ERROR: Failed to write to Swarm Visualizer log file: {e}")

    # Also store in CRUD Manager for structured querying for UI/analytics
    if _CRUD_MANAGER:
        try:
            await _CRUD_MANAGER.create_entity("SwarmEvent", event_entry)
        except Exception as e:
            print(f"ERROR: Failed to store Swarm Event in CRUD Manager: {e}")

    # In a full implementation, this might also push to a message queue for real-time UI updates
    # e.g., via websockets or server-sent events.

async def get_events_for_session(session_id: str, limit: int = 100) -> List[Dict[str, Any]]:
    """
    Retrieves a list of swarm events for a given session ID.
    """
    if not _CRUD_MANAGER:
        print("WARNING: CRUD Manager not initialized. Cannot retrieve swarm events.")
        return []
    try:
        logs = await _CRUD_MANAGER.filter_entities("SwarmEvent", {"session_id": session_id}, limit=limit, sort_by="timestamp")
        return logs
    except Exception as e:
        print(f"ERROR: Failed to retrieve swarm events from CRUD Manager: {e}")
        return []

async def get_latest_events(agent_id: Optional[str] = None, event_type: Optional[str] = None, limit: int = 50) -> List[Dict[str, Any]]:
    """
    Retrieves the latest swarm events, optionally filtered by agent_id or event_type.
    """
    if not _CRUD_MANAGER:
        print("WARNING: CRUD Manager not initialized. Cannot retrieve swarm events.")
        return []
    query = {}
    if agent_id: query["agent_id"] = agent_id
    if event_type: query["event_type"] = event_type

    try:
        logs = await _CRUD_MANAGER.filter_entities("SwarmEvent", query, limit=limit, sort_by="-timestamp") # Assuming descending sort
        return logs
    except Exception as e:
        print(f"ERROR: Failed to retrieve latest swarm events from CRUD Manager: {e}")
        return []
