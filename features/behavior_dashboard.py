import os
import json
from datetime import datetime
from typing import Dict, Any, List

# --- Configuration & Shared Data ---
_WORKSPACE: str = ""
_SWARM_VISUALIZER: Any = None
_LEARNING_INSIGHT_MANAGER: Any = None # Reference to learning insights

def initialize_behavior_dashboard(workspace_path: str, swarm_visualizer_module: Any, learning_insight_module: Any):
    global _WORKSPACE, _SWARM_VISUALIZER, _LEARNING_INSIGHT_MANAGER
    _WORKSPACE = workspace_path
    _SWARM_VISUALIZER = swarm_visualizer_module
    _LEARNING_INSIGHT_MANAGER = learning_insight_module
    print("Behavior Dashboard initialized.")

async def get_adaptation_history(task_id: str, context_filter: str = "all") -> List[Dict[str, Any]]:
    """Retrieves and correlates learning insights for behavioral adaptation visualization."""
    # Simulate retrieving learning insights and correlating them with task context
    insights = await _LEARNING_INSIGHT_MANAGER.list_insights(task_id)
    
    # Filter or aggregate based on context
    if context_filter != "all":
        insights = [i for i in insights if context_filter in i.get("context", "")]
        
    await _SWARM_VISUALIZER.log_event(
        task_id, "behavior_dashboard_query", f"Retrieving adaptation history for: {context_filter}",
        {}, model_name="system", agent_role="governance_controller"
    )
    
    return insights