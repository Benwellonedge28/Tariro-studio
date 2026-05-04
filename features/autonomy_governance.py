import os
import json
from datetime import datetime
from typing import Dict, Any, List, Literal
import uuid

# --- Configuration & Shared Data ---
_WORKSPACE: str = ""
_SWARM_VISUALIZER: Any = None
_CONTEXTUAL_MEMORY: Any = None

AUTONOMY_POLICIES_DIR: str = ""

def initialize_autonomy_governance(workspace_path: str, swarm_visualizer_module: Any, contextual_memory_module: Any):
    """Initializes the Autonomy Governance module."""
    global _WORKSPACE, _SWARM_VISUALIZER, _CONTEXTUAL_MEMORY, AUTONOMY_POLICIES_DIR
    _WORKSPACE = workspace_path
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CONTEXTUAL_MEMORY = contextual_memory_module
    
    AUTONOMY_POLICIES_DIR = os.path.join(_WORKSPACE, "autonomy_policies")
    os.makedirs(AUTONOMY_POLICIES_DIR, exist_ok=True)
    print(f"Autonomy Governance initialized. Policies stored in: {AUTONOMY_POLICIES_DIR}")

async def set_autonomy_level(task_id: str, domain: str, level: Literal['full_auto', 'suggest_only', 'human_required'], justification: str) -> Dict[str, Any]:
    """
    Sets the autonomy level for a specific domain.
    Levels: 'full_auto', 'suggest_only', 'human_required'
    """
    policy_data = {
        "domain": domain,
        "level": level,
        "justification": justification,
        "timestamp": datetime.now().isoformat()
    }
    
    # Save the policy to disk and contextual memory
    policy_path = os.path.join(AUTONOMY_POLICIES_DIR, f"policy_{domain.replace(' ', '_').lower()}.json")
    try:
        with open(policy_path, "w") as f:
            json.dump(policy_data, f, indent=2)
            
        await _CONTEXTUAL_MEMORY.store_memory(
            task_id, "system", f"autonomy_policy_{domain}", policy_data, 
            f"Updated autonomy level to {level} for domain: {domain}."
        )
        
        await _SWARM_VISUALIZER.log_event(
            task_id, "autonomy_level_changed", f"Autonomy level updated.",
            {"domain": domain, "level": level},
            model_name="system", agent_role="governance_controller", level="INFO"
        )
        return {"status": "success", "policy": policy_data, "message": f"Autonomy level for '{domain}' set to '{level}'."}
    except Exception as e:
        await _SWARM_VISUALIZER.log_event(task_id, "autonomy_level_error", f"Error setting autonomy level for {domain}.", {"error": str(e)}, model_name="system", agent_role="governance_controller", level="ERROR")
        return {"status": "failed", "error": str(e), "message": f"Failed to set autonomy level for '{domain}'."}

async def get_autonomy_level(task_id: str, domain: str) -> Dict[str, Any]:
    """
    Retrieves the currently configured autonomy level for a specific domain.
    """
    policy_path = os.path.join(AUTONOMY_POLICIES_DIR, f"policy_{domain.replace(' ', '_').lower()}.json")
    
    if os.path.exists(policy_path):
        try:
            with open(policy_path, "r") as f:
                policy_config = json.load(f)
            await _SWARM_VISUALIZER.log_event(
                task_id, "autonomy_level_get_complete", f"Retrieved autonomy level for {domain}.",
                policy_config, model_name="system", agent_role="governance_controller", level="INFO"
            )
            return {"status": "success", "config": policy_config}
        except Exception as e:
            await _SWARM_VISUALIZER.log_event(task_id, "autonomy_level_get_error", f"Error retrieving autonomy level for {domain}.", {"error": str(e)}, model_name="system", agent_role="governance_controller", level="ERROR")
            return {"status": "failed", "error": str(e), "message": f"Failed to retrieve autonomy level for '{domain}'."}
    else:
        await _SWARM_VISUALIZER.log_event(
            task_id, "autonomy_level_get_not_found", f"No autonomy configuration found for {domain}.",
            {"domain": domain}, model_name="system", agent_role="governance_controller", level="WARNING"
        )
        return {"status": "not_found", "message": f"No autonomy configuration found for {domain}. Defaulting to 'suggest_only'."}
