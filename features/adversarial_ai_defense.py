import os
import json
from datetime import datetime
from typing import Dict, Any, List, Literal

# --- Configuration & Shared Data ---
_WORKSPACE: str = ""
_SWARM_VISUALIZER: Any = None
_CONTEXTUAL_MEMORY: Any = None

AGI_PERSONALITY_CONFIG_DIR: str = ""

def initialize_agi_personality_config(workspace_path: str, swarm_visualizer_module: Any, contextual_memory_module: Any):
    """Initializes global configurations for AGI Personality Trait Configuration for Interaction."""
    global _WORKSPACE, _SWARM_VISUALIZER, _CONTEXTUAL_MEMORY, AGI_PERSONALITY_CONFIG_DIR
    _WORKSPACE = workspace_path
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CONTEXTUAL_MEMORY = contextual_memory_module

    AGI_PERSONALITY_CONFIG_DIR = os.path.join(_WORKSPACE, "agi_personality_configs")
    os.makedirs(AGI_PERSONALITY_CONFIG_DIR, exist_ok=True)
    print(f"AGI Personality Config initialized. Configs: {AGI_PERSONALITY_CONFIG_DIR}")

async def set_personality_traits(
    task_id: str,
    target_agent_id: str,
    communication_style: Literal['formal', 'informal', 'concise', 'verbose', 'empathetic', 'authoritative'],
    responsiveness: Literal['instant', 'fast', 'moderate', 'deliberate'],
    proactivity: Literal['reactive', 'proactive', 'highly_proactive'],
    justification: str
) -> Dict[str, Any]:
    """
    Simulates setting personality traits for an AGI agent's interaction style.
    """
    print(f"Setting personality traits for {target_agent_id}...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "agi_personality_config_start", f"Setting personality traits for {target_agent_id}.",
        {"style": communication_style, "responsiveness": responsiveness, "proactivity": proactivity},
        model_name="system", agent_role="governance_controller"
    )

    personality_config = {
        "agent_id": target_agent_id,
        "communication_style": communication_style,
        "responsiveness": responsiveness,
        "proactivity": proactivity,
        "justification": justification,
        "timestamp": datetime.now().isoformat()
    }
    
    config_filename = os.path.join(AGI_PERSONALITY_CONFIG_DIR, f"personality_config_{target_agent_id}.json")
    with open(config_filename, "w") as f:
        json.dump(personality_config, f, indent=2)

    await _CONTEXTUAL_MEMORY.store_memory(
        task_id, "system", f"agi_personality_config_{target_agent_id}", personality_config,
        f"Updated personality configuration for agent {target_agent_id}."
    )
    
    await _SWARM_VISUALIZER.log_event(
        task_id, "agi_personality_config_complete", f"Personality traits set for {target_agent_id}.",
        personality_config, model_name="system", agent_role="governance_controller"
    )
    
    return {"status": "success", "config": personality_config, "saved_path": config_filename}

async def get_personality_traits(task_id: str, target_agent_id: str) -> Dict[str, Any]:
    """
    Retrieves the currently configured personality traits for an AGI agent.
    """
    config_filename = os.path.join(AGI_PERSONALITY_CONFIG_DIR, f"personality_config_{target_agent_id}.json")
    
    if os.path.exists(config_filename):
        with open(config_filename, "r") as f:
            personality_config = json.load(f)
        await _SWARM_VISUALIZER.log_event(
            task_id, "agi_personality_get_complete", f"Retrieved personality traits for {target_agent_id}.",
            personality_config, model_name="system", agent_role="governance_controller"
        )
        return {"status": "success", "config": personality_config}
    else:
        await _SWARM_VISUALIZER.log_event(
            task_id, "agi_personality_get_not_found", f"No personality configuration found for {target_agent_id}.",
            {"agent_id": target_agent_id}, model_name="system", agent_role="governance_controller", level="WARNING"
        )
        return {"status": "not_found", "message": f"No personality configuration found for {target_agent_id}."}