import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid
import random

# --- Configuration & Shared Data (initialized from studio_v3_core.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Base model definitions from studio_v3_core.py
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module
_CRUD_MANAGER: Any = None # Reference to crud_manager module for Plan, Goal, or Task entities
_GLOBAL_STATE_MANAGER: Any = None # Reference to global_state_manager for current goals, world model
_PERSISTENT_TASK_MANAGER: Any = None # For submitting decomposed sub-tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on planning progress or failures
_AUTONOMY_GOVERNANCE: Any = None # For policy checks on planning decisions
_DYNAMIC_RESOURCE_ALLOCATOR: Any = None # For estimating resource needs of plans
_CONTEXTUAL_MEMORY: Any = None # For retrieving relevant past plans, strategies, knowledge
_META_ORCHESTRATOR: Any = None # For higher-level orchestration of multiple cognitive planning instances

COGNITIVE_PLANNING_LOG_DIR: str = ""

def initialize_cognitive_planning(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, global_state_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, autonomy_governance_module: Any, dynamic_resource_allocator_module: Any, contextual_memory_module: Any, meta_orchestrator_module: Any):
    """Initializes global configurations for the Cognitive Planning module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _GLOBAL_STATE_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _AUTONOMY_GOVERNANCE, _DYNAMIC_RESOURCE_ALLOCATOR, _CONTEXTUAL_MEMORY, _META_ORCHESTRATOR, COGNITIVE_PLANNING_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _AUTONOMY_GOVERNANCE = autonomy_governance_module
    _DYNAMIC_RESOURCE_ALLOCATOR = dynamic_resource_allocator_module
    _CONTEXTUAL_MEMORY = contextual_memory_module
    _META_ORCHESTRATOR = meta_orchestrator_module

    COGNITIVE_PLANNING_LOG_DIR = os.path.join(_WORKSPACE, "cognitive_planning_logs")
    os.makedirs(COGNITIVE_PLANNING_LOG_DIR, exist_ok=True)
    print(f"Cognitive Planning initialized. Logs: {COGNITIVE_PLANNING_LOG_DIR}")

async def _call_llm_for_planning(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for planning and task decomposition decisions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in cognitive_planning.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "planning_llm_call_start", f"{model} cognitive planning: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on autonomously decomposing complex goals into actionable plans, generating step-by-step tasks, estimating resource needs, and anticipating potential obstacles. Ensure plans are efficient, resilient, and align with overall system objectives and ethical policies."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.07 # Low temp for precise plan generation
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "planning_llm_call_end", f"{model} completed cognitive planning task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "planning_llm_error", f"JSON decode error from {model} for cognitive planning.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "planning_llm_error", f"Error calling {model} for cognitive planning task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def decompose_goal_into_plan(task_id: str, high_level_goal: str, user_id: str = "Tariro_System", decomposition_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Breaks down a complex, high-level goal into a sequence of actionable, manageable sub-tasks.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Decomposing high-level goal into actionable plan.")

    current_world_model = await _GLOBAL_STATE_MANAGER.get_state("world_model") or {}
    past_strategies = await _CONTEXTUAL_MEMORY.query(user_id, f"past successful strategies for {high_level_goal}")
    
    prompt = f"""You are Tariro's Cognitive Planning Engine, an Omniversal AGI Goal Decomposer. Your task is to break down a complex, high-level goal into a well-structured, actionable plan consisting of a sequence of manageable sub-tasks. The plan should be robust, efficient, and take into account current system capabilities and environmental context.

HIGH-LEVEL GOAL: {high_level_goal}
USER ID: {user_id}
CURRENT WORLD MODEL (from Global State Manager): {json.dumps(current_world_model, indent=2)}
RELEVANT PAST STRATEGIES (from Contextual Memory): {json.dumps(past_strategies, indent=2)}

Decompose the goal focusing on:
-   **Logical Flow**: Ensure sub-tasks are in a logical, sequential, or parallel order.
-   **Granularity**: Sub-tasks should be specific enough to be assigned to modules or agents.
-   **Dependencies**: Clearly define dependencies between sub-tasks.
-   **Resource Estimation**: Estimate the resources (compute, time, modules) required for each sub-task.
-   **Contingencies**: Identify potential failure points and plan for alternatives.
-   **Policy Compliance**: Ensure the overall plan and sub-tasks comply with ethical and operational policies.

Output JSON: {{
    "plan_summary": str,
    "decomposed_plan": List[Dict[str, Any]], # {{'task_name': str, 'description': str, 'dependencies': List[str], 'estimated_resources': Dict, 'assigned_module_or_agent': str, 'task_type': str}}
    "estimated_total_time_seconds": int,
    "estimated_total_cost": Dict[str, Any],
    "confidence": float
}}
"""
    llm_plan = await _call_llm_for_planning(decomposition_model, "GoalDecomposer", prompt, task_id)

    if "error" in llm_plan:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Goal decomposition failed: {llm_plan['error']}", current_step="LLM decomposition failed.")
        return {"status": "failed", "reason": llm_plan["error"]}

    plan_summary = llm_plan.get("plan_summary", "No summary.")
    decomposed_plan = llm_plan.get("decomposed_plan", [])
    
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "High-level goal decomposed into actionable plan.", output=llm_plan)
    
    await _SWARM_VISUALIZER.log_event(task_id, "goal_decomposed", f"Goal '{high_level_goal[:50]}' decomposed. Summary: {plan_summary}", llm_plan, agent_role="CognitivePlanning")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Goal '{high_level_goal[:50]}' decomposed. Summary: {plan_summary}", title="Goal Decomposition Complete")

    # Store the plan in CRUD Manager
    plan_entry = {"id": task_id, "goal": high_level_goal, "plan_details": llm_plan, "status": "DECOMPOSED"}
    await _CRUD_MANAGER.create_entity("Plan", plan_entry)

    # Submit sub-tasks for execution via Persistent Task Manager
    for sub_task_data in decomposed_plan:
        sub_task_payload = sub_task_data.get("payload", {})
        sub_task_payload.update({"parent_task_id": task_id, "high_level_goal": high_level_goal})
        await _PERSISTENT_TASK_MANAGER.submit_task(
            task_type=sub_task_data.get("task_type", "generic_sub_task"), # Need a task_type resolver here
            payload=sub_task_payload,
            user_id=user_id,
            priority=sub_task_data.get("priority", 5),
            initiating_session_id=task_id
        )

    return {"status": "success", "plan_report": llm_plan}

async def optimize_plan_execution(task_id: str, current_plan: Dict[str, Any], system_status: Dict[str, Any], user_id: str = "Tariro_System", optimizer_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Dynamically adjusts the execution order, resource allocation, and agent assignments of an active plan
    to adapt to changing conditions or new information.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Optimizing plan execution.")

    resource_inventory = await _GLOBAL_STATE_MANAGER.get_state("system_resource_inventory") or {}
    current_policies = await _GLOBAL_STATE_MANAGER.get_state("active_policies") or {}
    
    prompt = f"""You are Tariro's Cognitive Planning Engine, an Omniversal AGI Plan Optimizer. Your task is to dynamically adjust the execution order, resource allocation, and agent assignments of an active plan to adapt to changing conditions, system status, or new information. The goal is to ensure optimal efficiency, resilience, and goal attainment.

CURRENT ACTIVE PLAN: {json.dumps(current_plan, indent=2)}
CURRENT SYSTEM STATUS (from Global State Manager): {json.dumps(system_status, indent=2)}
AVAILABLE RESOURCES (from Dynamic Resource Allocator): {json.dumps(resource_inventory, indent=2)}
ACTIVE POLICIES (from Autonomy Governance): {json.dumps(current_policies, indent=2)}

Optimize plan execution focusing on:
-   **Adaptive Sequencing**: Reorder tasks based on real-time data.
-   **Dynamic Resource Allocation**: Adjust resource assignments (e.g., more LLM tokens for critical sub-tasks).
-   **Agent Reassignment**: Reassign sub-tasks to more available or capable agents.
-   **Contingency Activation**: Trigger alternative paths if obstacles are encountered.
-   **Policy Compliance**: Ensure all adjustments remain compliant with current policies.

Output JSON: {{
    "optimization_summary": str,
    "adjusted_plan": List[Dict[str, Any]], # Updated plan with changes
    "recommended_resource_changes": List[Dict[str, Any]], # {{'resource_type': str, 'change_amount': Any}}
    "notifications_to_agents": List[Dict[str, Any]], # Instructions for affected agents
    "confidence": float
}}
"""
    llm_optimization = await _call_llm_for_planning(optimizer_model, "PlanOptimizer", prompt, task_id)

    if "error" in llm_optimization:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Plan optimization failed: {llm_optimization['error']}", current_step="LLM optimization failed.")
        return {"status": "failed", "reason": llm_optimization["error"]}

    optimization_summary = llm_optimization.get("optimization_summary", "No summary.")
    adjusted_plan = llm_optimization.get("adjusted_plan", [])
    
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Plan execution optimized.", output=llm_optimization)
    
    await _SWARM_VISUALIZER.log_event(task_id, "plan_optimized", f"Plan for task {task_id[:8]} optimized. Summary: {optimization_summary}", llm_optimization, agent_role="CognitivePlanning")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Plan for task {task_id[:8]} optimized. Summary: {optimization_summary}", title="Plan Optimization Complete")

    # Update plan in CRUD Manager
    await _CRUD_MANAGER.update_entity("Plan", task_id, {"plan_details": llm_optimization, "status": "OPTIMIZED"})

    # Apply resource changes via Dynamic Resource Allocator
    for resource_change in llm_optimization.get("recommended_resource_changes", []):
        resource_type = resource_change["resource_type"]
        change_amount = resource_change["change_amount"]
        if change_amount > 0:
            await _DYNAMIC_RESOURCE_ALLOCATOR.allocate_resources(task_id, resource_type, change_amount, user_id)
        elif change_amount < 0:
            await _DYNAMIC_RESOURCE_ALLOCATOR.deallocate_resources(task_id, resource_type, abs(change_amount), user_id)

    return {"status": "success", "optimization_report": llm_optimization}

async def anticipate_obstacles(task_id: str, plan_segment: Dict[str, Any], environmental_context: Dict[str, Any], user_id: str = "Tariro_System", obstacle_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Identifies potential obstacles, risks, or unexpected events that could impact plan execution,
    and suggests proactive mitigation strategies.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Anticipating obstacles for plan segment.")

    world_model = await _GLOBAL_STATE_MANAGER.get_state("world_model") or {}
    relevant_knowledge = await _CONTEXTUAL_MEMORY.query(user_id, f"risks and obstacles related to {plan_segment.get('task_name')}")
    
    prompt = f"""You are Tariro's Cognitive Planning Engine, an Omniversal AGI Obstacle Anticipator. Your task is to identify potential obstacles, risks, or unexpected events that could impact the execution of a specific plan segment. For each identified obstacle, suggest proactive mitigation strategies to ensure the plan's success.

PLAN SEGMENT: {json.dumps(plan_segment, indent=2)}
ENVIRONMENTAL CONTEXT (from Global Environmental Model): {json.dumps(environmental_context, indent=2)}
CURRENT WORLD MODEL (from Global State Manager): {json.dumps(world_model, indent=2)}
RELEVANT KNOWLEDGE (from Contextual Memory): {json.dumps(relevant_knowledge, indent=2)}

Anticipate obstacles focusing on:
-   **Technical Challenges**: Software bugs, hardware limitations, integration issues.
-   **Resource Constraints**: Shortages of compute, data, or specialized agents.
-   **External Factors**: Changes in external APIs, unexpected user behavior, environmental shifts.
-   **Ethical/Policy Violations**: Potential for unintended negative consequences or policy breaches.
-   **Mitigation Strategies**: Concrete steps to prevent or overcome each identified obstacle.

Output JSON: {{
    "obstacle_summary": str,
    "identified_obstacles": List[Dict[str, Any]], # {{'obstacle_name': str, 'description': str, 'likelihood': float, 'impact': float, 'mitigation_strategy': str}}
    "overall_risk_assessment": str, # e.g., "low", "medium", "high"
    "confidence": float
}}
"""
    llm_obstacles = await _call_llm_for_planning(obstacle_model, "ObstacleAnticipator", prompt, task_id)

    if "error" in llm_obstacles:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Obstacle anticipation failed: {llm_obstacles['error']}", current_step="LLM anticipation failed.")
        return {"status": "failed", "reason": llm_obstacles["error"]}

    obstacle_summary = llm_obstacles.get("obstacle_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Obstacles anticipated and mitigation strategies suggested.", output=llm_obstacles)
    
    await _SWARM_VISUALIZER.log_event(task_id, "obstacles_anticipated", f"Obstacles for plan segment anticipated. Summary: {obstacle_summary}", llm_obstacles, agent_role="CognitivePlanning")
    if llm_obstacles.get("overall_risk_assessment") in ["high", "critical"]:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"High-risk obstacles identified for plan. Summary: {obstacle_summary}", title="High Risk Plan Obstacles", causal_priority="critical")

    # Integrate mitigation strategies back into the plan via CRUD Manager or re-optimize_plan_execution

    return {"status": "success", "obstacle_report": llm_obstacles}

