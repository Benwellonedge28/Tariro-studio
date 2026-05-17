import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid
import random

# --- Configuration & Shared Data ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Base model definitions from studio_v3_core.py
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module
_CRUD_MANAGER: Any = None # Reference to CRUD Manager for ResourceLog entities
_GLOBAL_STATE_MANAGER: Any = None # For storing/retrieving current resource states
_PERSISTENT_TASK_MANAGER: Any = None # For scheduling resource management tasks
_BACKGROUND_WORKER_FRAMEWORK: Any = None # For dynamic worker pool adjustments
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on resource issues
_AUTONOMY_GOVERNANCE: Any = None # For policy checks on resource allocation
_META_LEARNER: Any = None # For learning from allocation optimizations
_SELF_EVOLUTION: Any = None # For suggesting hardware/software upgrades

DYNAMIC_RESOURCE_ALLOCATOR_LOG_DIR: str = ""

# In-memory mock for resource inventory and allocation policies
_MOCKED_RESOURCE_INVENTORY: Dict[str, Dict[str, Any]] = {
    "CPU_CORES": {"total": 16, "allocated": 4, "unit": "cores"},
    "GPU_UNITS": {"total": 2, "allocated": 0, "unit": "units"},
    "RAM_GB": {"total": 64, "allocated": 16, "unit": "GB"},
    "LLM_TOKENS_PER_MIN": {"total": 1000000, "allocated": 200000, "unit": "tokens/min"},
    "QDRANT_VECTOR_STORAGE_GB": {"total": 100, "allocated": 10, "unit": "GB"},
    "REDIS_CONNECTIONS": {"total": 100, "allocated": 10, "unit": "connections"},
}

_MOCKED_ALLOCATION_POLICIES: Dict[str, Any] = {
    "default_task_priority_multiplier": 1.0,
    "critical_task_min_cpu": 2,
    "llm_burst_capacity_factor": 1.5,
    "low_resource_alert_threshold": 0.85 # 85% utilization
}

def initialize_dynamic_resource_allocator(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, global_state_manager_module: Any, persistent_task_manager_module: Any, background_worker_framework_module: Any, async_notification_system_module: Any, autonomy_governance_module: Any, meta_learner_module: Any, self_evolution_module: Any):
    """Initializes global configurations for the Dynamic Resource Allocator module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _GLOBAL_STATE_MANAGER, _PERSISTENT_TASK_MANAGER, _BACKGROUND_WORKER_FRAMEWORK, _ASYNC_NOTIFICATION_SYSTEM, _AUTONOMY_GOVERNANCE, _META_LEARNER, _SELF_EVOLUTION, DYNAMIC_RESOURCE_ALLOCATOR_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _BACKGROUND_WORKER_FRAMEWORK = background_worker_framework_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _AUTONOMY_GOVERNANCE = autonomy_governance_module
    _META_LEARNER = meta_learner_module
    _SELF_EVOLUTION = self_evolution_module

    DYNAMIC_RESOURCE_ALLOCATOR_LOG_DIR = os.path.join(_WORKSPACE, "dynamic_resource_allocator_logs")
    os.makedirs(DYNAMIC_RESOURCE_ALLOCATOR_LOG_DIR, exist_ok=True)
    print(f"Dynamic Resource Allocator initialized. Logs: {DYNAMIC_RESOURCE_ALLOCATOR_LOG_DIR}")

    # Initialize resource inventory and policies in Global State Manager
    initial_inventory = asyncio.run(_GLOBAL_STATE_MANAGER.get_state("system_resource_inventory"))
    if initial_inventory:
        _MOCKED_RESOURCE_INVENTORY.update(initial_inventory)
    else:
        asyncio.run(_GLOBAL_STATE_MANAGER.set_state("system_resource_inventory", _MOCKED_RESOURCE_INVENTORY, "Tariro_System", auditable=True))

    initial_policies = asyncio.run(_GLOBAL_STATE_MANAGER.get_state("resource_allocation_policies"))
    if initial_policies:
        _MOCKED_ALLOCATION_POLICIES.update(initial_policies)
    else:
        asyncio.run(_GLOBAL_STATE_MANAGER.set_state("resource_allocation_policies", _MOCKED_ALLOCATION_POLICIES, "Tariro_System", auditable=True))

async def allocate_resources(task_id: str, resource_type: str, amount: Any, user_id: str = "Tariro_System") -> Dict[str, Any]:
    """
    Allocates a specified amount of a resource type to a task.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Attempting to allocate {amount} of {resource_type}.")

    resource_inventory = await _GLOBAL_STATE_MANAGER.get_state("system_resource_inventory") or _MOCKED_RESOURCE_INVENTORY
    resource_info = resource_inventory.get(resource_type)

    if not resource_info:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Resource type {resource_type} not found.")
        return {"status": "failed", "reason": f"Resource type {resource_type} not found."}

    if resource_info["allocated"] + amount > resource_info["total"]:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Insufficient {resource_type} available. Total: {resource_info["total"], resource_info["unit"]}, Allocated: {resource_info["allocated"], resource_info["unit"]}")
        # Trigger scale-up suggestion via Self-Evolution or notification
        if _ASYNC_NOTIFICATION_SYSTEM:
            await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
                user_id, task_id, 
                f"Resource warning: Insufficient {resource_type} for task {task_id}. Current usage {resource_info["allocated"]}/{resource_info["total"]}.",
                title="Resource Allocation Warning", causal_priority="high"
            )
        return {"status": "failed", "reason": f"Insufficient {resource_type} available."}
    
    # Check policy for allocation if _AUTONOMY_GOVERNANCE is available
    if _AUTONOMY_GOVERNANCE:
        policy_check = await _AUTONOMY_GOVERNANCE.check_policy(
            user_id, 
            "resource_allocation", 
            {"resource_type": resource_type, "amount": amount, "task_id": task_id, "priority": (await _PERSISTENT_TASK_MANAGER.get_task_status(task_id)).get('task', {}).get('priority', 5)}
        )
        if not policy_check.get("allowed", False):
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Resource allocation of {resource_type} blocked by policy.")
            return {"status": "failed", "reason": "Resource allocation blocked by policy.", "policy_reason": policy_check.get("reason")}

    resource_info["allocated"] += amount
    await _GLOBAL_STATE_MANAGER.set_state("system_resource_inventory", resource_inventory, user_id, auditable=True, notify_changes=True, is_critical=True if resource_info["allocated"] / resource_info["total"] > _MOCKED_ALLOCATION_POLICIES["low_resource_alert_threshold"] else False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 100, f"Allocated {amount} of {resource_type}.")
    if _SWARM_VISUALIZER:
        await _SWARM_VISUALIZER.log_event(
            session_id=task_id,
            event_type="resource_allocated",
            message=f"Allocated {amount} {resource_info['unit']} of {resource_type} for task {task_id}.",
            details={
                "resource_type": resource_type,
                "amount": amount,
                "current_allocated": resource_info["allocated"]
            },
            agent_id=user_id,
            agent_role="DynamicResourceAllocator",
            level="INFO"
        )
    print(f"[DynamicResourceAllocator] Allocated {amount} {resource_info['unit']} of {resource_type} for task {task_id}.")
    return {"status": "success", "resource_type": resource_type, "amount": amount}

async def deallocate_resources(task_id: str, resource_type: str, amount: Any, user_id: str = "Tariro_System") -> Dict[str, Any]:
    """
    Deallocates a specified amount of a resource type from a task.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Attempting to deallocate {amount} of {resource_type}.")

    resource_inventory = await _GLOBAL_STATE_MANAGER.get_state("system_resource_inventory") or _MOCKED_RESOURCE_INVENTORY
    resource_info = resource_inventory.get(resource_type)

    if not resource_info:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Resource type {resource_type} not found.")
        return {"status": "failed", "reason": f"Resource type {resource_type} not found."}

    if resource_info["allocated"] - amount < 0:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Cannot deallocate more than allocated for {resource_type}.")
        return {"status": "failed", "reason": f"Cannot deallocate more than allocated for {resource_type}."}

    resource_info["allocated"] -= amount
    await _GLOBAL_STATE_MANAGER.set_state("system_resource_inventory", resource_inventory, user_id, auditable=True, notify_changes=True)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 100, f"Deallocated {amount} of {resource_type}.")
    if _SWARM_VISUALIZER:
        await _SWARM_VISUALIZER.log_event(
            session_id=task_id,
            event_type="resource_deallocated",
            message=f"Deallocated {amount} {resource_info['unit']} of {resource_type} for task {task_id}.",
            details={
                "resource_type": resource_type,
                "amount": amount,
                "current_allocated": resource_info["allocated"]
            },
            agent_id=user_id,
            agent_role="DynamicResourceAllocator",
            level="INFO"
        )
    print(f"[DynamicResourceAllocator] Deallocated {amount} {resource_info['unit']} of {resource_type} for task {task_id}.")
    return {"status": "success", "resource_type": resource_type, "amount": amount}

async def monitor_resources(task_id: str, user_id: str = "Tariro_System") -> Dict[str, Any]:
    """
    Monitors current resource utilization and identifies potential bottlenecks or underutilization.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Monitoring resources.")

    resource_inventory = await _GLOBAL_STATE_MANAGER.get_state("system_resource_inventory") or _MOCKED_RESOURCE_INVENTORY
    allocation_policies = await _GLOBAL_STATE_MANAGER.get_state("resource_allocation_policies") or _MOCKED_ALLOCATION_POLICIES

    # Simulate gathering real-time data
    real_time_metrics = {k: {"usage": v["allocated"], "total": v["total"], "utilization": v["allocated"] / v["total"]} for k, v in resource_inventory.items()}

    prompt = f"""You are Tariro's Dynamic Resource Allocator, an Omniversal AGI Resource Monitor. Your task is to monitor current resource utilization, identify potential bottlenecks, underutilization, or impending resource shortages, and suggest optimal adjustments. 

CURRENT RESOURCE METRICS: {json.dumps(real_time_metrics, indent=2)}
ALLOCATION POLICIES: {json.dumps(allocation_policies, indent=2)}

Monitor focusing on:
-   **Bottleneck Detection**: Identify resources nearing full capacity.
-   **Underutilization**: Detect idle or underused resources.
-   **Trend Analysis**: Forecast future resource needs based on current trends (conceptual).
-   **Policy Compliance**: Ensure allocations align with defined policies.

Output JSON: {{
    "monitoring_summary": str,
    "resource_status": str, # "optimal", "constrained", "overloaded", "underutilized"
    "issues_identified": List[Dict[str, Any]], # {{'type': str, 'resource': str, 'description': str, 'severity': str}}
    "recommendations": List[str], # e.g., 'scale_up_cpu', 'reallocate_llm_tokens', 'adjust_worker_pool'
    "confidence": float
}}
"""
    llm_monitoring_report = await _CLIENT.chat.completions.create(
        model=_ALL_MODELS["mixtral-analyst"], # Using a dedicated analyst model
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": "Please provide a resource monitoring report based on the provided data."}
        ],
        response_format={"type": "json_object"},
        temperature=0.1
    )
    report_content = json.loads(llm_monitoring_report.choices[0].message.content)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Resource monitoring completed.", output=report_content)
    if _SWARM_VISUALIZER:
        await _SWARM_VISUALIZER.log_event(
            session_id=task_id,
            event_type="resource_monitoring",
            message="System resources monitored.",
            details=report_content,
            agent_id=user_id,
            agent_role="DynamicResourceAllocator",
            level="INFO"
        )
    print(f"[DynamicResourceAllocator] Resource monitoring completed. Status: {report_content.get('resource_status')}")

    if report_content.get("issues_identified") and _ASYNC_NOTIFICATION_SYSTEM:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
            user_id, task_id, 
            f"Resource issues detected: {report_content['monitoring_summary'][:100]}...",
            title="Resource Alert", causal_priority="high"
        )

    if report_content.get("recommendations"):
        await apply_resource_adjustments(task_id=f"{task_id}_adjust", recommendations=report_content["recommendations"], user_id=user_id)

    return {"status": "success", "report": report_content}

async def apply_resource_adjustments(task_id: str, recommendations: List[str], user_id: str = "Tariro_System") -> Dict[str, Any]:
    """
    Applies recommended adjustments to resource allocations or scaling parameters.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Applying resource adjustments.")

    resource_inventory = await _GLOBAL_STATE_MANAGER.get_state("system_resource_inventory") or _MOCKED_RESOURCE_INVENTORY
    
    prompt = f"""You are Tariro's Dynamic Resource Allocator, an Omniversal AGI Resource Adjuster. Your task is to apply recommended adjustments to resource allocations, scaling parameters, or even trigger hardware/software upgrades based on monitoring reports. Ensure changes are policy-compliant and minimize disruption.

RESOURCE ADJUSTMENT RECOMMENDATIONS: {json.dumps(recommendations, indent=2)}
CURRENT RESOURCE INVENTORY: {json.dumps(resource_inventory, indent=2)}

Apply adjustments focusing on:
-   **Prioritization**: Implement critical adjustments first.
-   **Module Interaction**: Direct commands to relevant modules (Background Worker Framework, Self-Evolution).
-   **Verification**: How to confirm the adjustments had the desired effect.
-   **Rollback**: Plan for reverting changes if they cause instability.

Output JSON: {{
    "adjustment_summary": str,
    "actions_taken": List[Dict[str, Any]], # {{'action_type': str, 'target': str, 'value': Any, 'executor_module': str}}
    "estimated_impact": str,
    "confidence": float
}}
"""
    llm_adjustment_plan = await _CLIENT.chat.completions.create(
        model=_ALL_MODELS["llama-architect"], # Using architect for strategic adjustments
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": "Please generate a plan for applying these resource adjustments."}
        ],
        response_format={"type": "json_object"},
        temperature=0.1
    )
    adjustment_plan_content = json.loads(llm_adjustment_plan.choices[0].message.content)

    actions_taken = []
    for action in adjustment_plan_content.get("actions_taken", []):
        # Delegate actions to relevant modules
        if action.get("executor_module") == "BackgroundWorkerFramework" and _BACKGROUND_WORKER_FRAMEWORK:
            if action.get("action_type") == "adjust_worker_pool":
                # Mock: _BACKGROUND_WORKER_FRAMEWORK.adjust_worker_pool_size(action["value"])
                actions_taken.append(f"Adjusted worker pool size to {action['value']}.")
        elif action.get("executor_module") == "SelfEvolution" and _SELF_EVOLUTION:
            if action.get("action_type") == "suggest_upgrade":
                # Mock: _SELF_EVOLUTION.propose_upgrade(action["target"], action["value"])
                actions_taken.append(f"Suggested upgrade for {action['target']} to {action['value']}.")
        elif action.get("action_type") == "reallocate_llm_tokens":
            # This would directly update the _MOCKED_RESOURCE_INVENTORY for LLM_TOKENS_PER_MIN
            resource_inventory["LLM_TOKENS_PER_MIN"]["allocated"] = action["value"]
            await _GLOBAL_STATE_MANAGER.set_state("system_resource_inventory", resource_inventory, user_id, auditable=True)
            actions_taken.append(f"Reallocated LLM tokens to {action['value']}.")
        # Add more delegations for other resource types or actions

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Resource adjustments applied.", output=adjustment_plan_content)
    if _SWARM_VISUALIZER:
        await _SWARM_VISUALIZER.log_event(
            session_id=task_id,
            event_type="resource_adjustments_applied",
            message="System resource adjustments applied.",
            details=adjustment_plan_content,
            agent_id=user_id,
            agent_role="DynamicResourceAllocator",
            level="INFO"
        )
    print(f"[DynamicResourceAllocator] Resource adjustments applied. Summary: {adjustment_plan_content.get('adjustment_summary')}")

    return {"status": "success", "actions_taken": actions_taken, "report": adjustment_plan_content}

async def start_continuous_resource_management_loop(task_id: str, interval_seconds: int, user_id: str = "Tariro_System"): # task_id for tracking
    """
    Starts a continuous loop to monitor and manage resources autonomously.
    This function should be executed by the background worker framework.
    """
    print(f"[DynamicResourceAllocator] Starting continuous resource management loop with interval {interval_seconds}s.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "RUNNING_LOOP", 0, "Continuous resource management loop started.")

    while True:
        try:
            monitor_task_id = f"{task_id}_monitor_{uuid.uuid4().hex[:8]}"
            monitor_report = await monitor_resources(monitor_task_id, user_id)
            
            if monitor_report.get("report", {}).get("issues_identified"):
                adjust_task_id = f"{task_id}_adjust_{uuid.uuid4().hex[:8]}"
                await apply_resource_adjustments(adjust_task_id, monitor_report["report"]["recommendations"], user_id)
            
            await asyncio.sleep(interval_seconds)
        except asyncio.CancelledError:
            print(f"[DynamicResourceAllocator] Continuous resource management loop {task_id} cancelled.")
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "CANCELLED", 100, "Continuous resource management loop cancelled.")
            break
        except Exception as e:
            print(f"ERROR: Error in continuous resource management loop {task_id}: {e}")
            if _SWARM_VISUALIZER:
                await _SWARM_VISUALIZER.log_event(
                    session_id=task_id,
                    event_type="resource_loop_error",
                    message=f"Error in continuous resource management loop: {e}",
                    details={
                        "error": str(e)
                    },
                    agent_id=user_id,
                    agent_role="DynamicResourceAllocator",
                    level="CRITICAL"
                )
            await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
                user_id,
                task_id,
                f"Critical error in continuous resource management loop: {e}",
                title="Resource Management Loop Error",
                category="system_update",
                causal_priority="critical"
            )
            await asyncio.sleep(interval_seconds) # Wait before retrying

