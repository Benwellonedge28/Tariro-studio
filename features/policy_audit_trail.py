import os
import json
from datetime import datetime
from typing import Dict, Any, List

# --- Configuration & Shared Data ---
_WORKSPACE: str = ""
_SWARM_VISUALIZER: Any = None
_CONTEXTUAL_MEMORY: Any = None

POLICY_AUDIT_LOG_DIR: str = ""

def initialize_policy_audit_trail(workspace_path: str, swarm_visualizer_module: Any, contextual_memory_module: Any):
    """Initializes the Self-Governance Policy Audit Trail module."""
    global _WORKSPACE, _SWARM_VISUALIZER, _CONTEXTUAL_MEMORY, POLICY_AUDIT_LOG_DIR
    _WORKSPACE = workspace_path
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CONTEXTUAL_MEMORY = contextual_memory_module

    POLICY_AUDIT_LOG_DIR = os.path.join(_WORKSPACE, "policy_audit_logs")
    os.makedirs(POLICY_AUDIT_LOG_DIR, exist_ok=True)
    print(f"Policy Audit Trail initialized. Logs stored in: {POLICY_AUDIT_LOG_DIR}")

async def log_policy_change(task_id: str, policy_name: str, old_value: Any, new_value: Any, authorized_by: str, justification: str) -> Dict[str, Any]:
    """
    Records an immutable log of a policy change.
    """
    audit_entry = {
        "timestamp": datetime.now().isoformat(),
        "task_id": task_id,
        "policy_name": policy_name,
        "old_value": old_value,
        "new_value": new_value,
        "authorized_by": authorized_by,
        "justification": justification
    }
    
    log_filename = os.path.join(POLICY_AUDIT_LOG_DIR, f"policy_change_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    try:
        with open(log_filename, "w") as f:
            json.dump(audit_entry, f, indent=2)
            
        await _CONTEXTUAL_MEMORY.store_memory(
            task_id, "system", f"policy_audit_{policy_name}_{uuid.uuid4().hex}", audit_entry, 
            f"Logged policy change for {policy_name} from {old_value} to {new_value}."
        )
        
        await _SWARM_VISUALIZER.log_event(
            task_id, "policy_audit_logged", f"Policy change for {policy_name} logged.",
            audit_entry, model_name="system", agent_role="policy_auditor", level="INFO"
        )
        return {"status": "success", "audit_entry": audit_entry, "message": f"Policy change for '{policy_name}' logged successfully."}
    except Exception as e:
        await _SWARM_VISUALIZER.log_event(task_id, "policy_audit_error", f"Error logging policy change for {policy_name}.", {"error": str(e)}, model_name="system", agent_role="policy_auditor", level="ERROR")
        return {"status": "failed", "error": str(e), "message": f"Failed to log policy change for '{policy_name}'."}

async def get_audit_trail(task_id: str, filter_policy: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Retrieves the audit trail of policy changes, optionally filtered by policy name.
    """
    audit_entries = []
    try:
        for filename in os.listdir(POLICY_AUDIT_LOG_DIR):
            if filename.startswith("policy_change_") and filename.endswith(".json"):
                file_path = os.path.join(POLICY_AUDIT_LOG_DIR, filename)
                with open(file_path, "r") as f:
                    entry = json.load(f)
                    if filter_policy is None or entry.get("policy_name") == filter_policy:
                        audit_entries.append(entry)
        
        audit_entries.sort(key=lambda x: x["timestamp"]) # Sort by timestamp
        
        await _SWARM_VISUALIZER.log_event(
            task_id, "audit_trail_retrieved", f"Retrieved audit trail. Entries: {len(audit_entries)}",
            {"filter": filter_policy}, model_name="system", agent_role="policy_auditor", level="INFO"
        )
        return {"status": "success", "audit_trail": audit_entries, "message": f"Retrieved {len(audit_entries)} audit entries."}
    except Exception as e:
        await _SWARM_VISUALIZER.log_event(task_id, "audit_trail_error", f"Error retrieving audit trail.", {"error": str(e)}, model_name="system", agent_role="policy_auditor", level="ERROR")
        return {"status": "failed", "error": str(e), "message": "Failed to retrieve audit trail."}
