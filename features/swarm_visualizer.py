import os
import json
from datetime import datetime
from typing import Dict, Any, List

# --- Configuration & Shared Data (initialized from studio_v3.py) ---
_WORKSPACE: str = ""
SWARM_EVENT_LOG_DIR: str = ""

def initialize_swarm_visualizer(workspace_path: str):
    """Initializes global configurations for the Swarm Visualizer."""
    global _WORKSPACE, SWARM_EVENT_LOG_DIR
    _WORKSPACE = workspace_path
    SWARM_EVENT_LOG_DIR = os.path.join(_WORKSPACE, "swarm_events")
    os.makedirs(SWARM_EVENT_LOG_DIR, exist_ok=True)
    print(f"Swarm Visualizer initialized. Event logs: {SWARM_EVENT_LOG_DIR}")

async def log_event(
    task_id: str,
    event_type: str, # e.g., "model_call_start", "coder_output", "test_passed", "tool_proposed", "agi_evaluated"
    description: str,
    details: Dict[str, Any],
    model_name: str = "system", # Which model initiated/is associated with the event
    agent_role: str = "system", # Role of the associated model/system component
    level: str = "INFO" # INFO, WARNING, ERROR, DEBUG
):
    """
    Logs a structured event to a task-specific JSONL file.
    Each task gets its own log file for easier retrieval.
    """
    timestamp = datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "event_type": event_type,
        "description": description,
        "details": details,
        "model_name": model_name,
        "agent_role": agent_role,
        "level": level
    }
    
    # Use a task_id specific log file
    log_filename = os.path.join(SWARM_EVENT_LOG_DIR, f"task_{task_id}.jsonl")
    with open(log_filename, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    # print(f"Swarm Event Logged ({task_id}): {event_type} - {description}")

def get_events_for_task(task_id: str) -> List[Dict[str, Any]]:
    """
    Retrieves all logged events for a given task ID.
    """
    log_filename = os.path.join(SWARM_EVENT_LOG_DIR, f"task_{task_id}.jsonl")
    events = []
    if os.path.exists(log_filename):
        with open(log_filename, "r") as f:
            for line in f:
                try:
                    events.append(json.loads(line))
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from event log line: {line.strip()}")
    return events

# You might add more utility functions here for filtering, sorting, or summarizing events.
