import os
import json
from datetime import datetime
from typing import Dict, Any, List

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

async def set_autonomy_level(task_id: str, domain: str, level: str, justification: str) -> Dict[str, Any]:
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
    policy_path = os.path.join(AUTONOMY_POLICIES_DIR, f"policy_{domain}.json")
    with open(policy_path, "w") as f:
        json.dump(policy_data, f, indent=2)
        
    await _CONTEXTUAL_MEMORY.store_memory(
        task_id, "system", f"autonomy_policy_{domain}", policy_data, 
        f"Updated autonomy level to {level} for domain: {domain}."
    )
    
    await _SWARM_VISUALIZER.log_event(
        task_id, "autonomy_level_changed", f"Autonomy level updated.",
        {"domain": domain, "level": level},
        model_name="system", agent_role="governance_controller"
    )
    
    return {"status": "success", "policy": policy_data}