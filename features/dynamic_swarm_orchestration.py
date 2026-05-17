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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for SwarmNode or SwarmTask entities
_GLOBAL_STATE_MANAGER: Any = None # For storing current swarm topology and global state
_PERSISTENT_TASK_MANAGER: Any = None # For distributing and monitoring swarm tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on swarm reconfigurations or failures
_COGNITIVE_PLANNING: Any = None # For decomposing and assigning tasks to swarm members
_EXTERNAL_AGENCY: Any = None # For managing external computational resources for swarm
_META_COGNITIVE_REFLECTION: Any = None # For introspecting swarm performance and coordination
_META_ORCHESTRATOR: Any = None # For higher-level, multi-swarm orchestration

DYNAMIC_SWARM_ORCHESTRATION_LOG_DIR: str = ""

# In-memory mock for swarm topology
_CURRENT_SWARM_TOPOLOGY: Dict[str, Any] = {
    "swarm_id": "tariro_main_swarm",
    "leader_node": "tariro_studio_instance_1",
    "nodes": {
        "tariro_studio_instance_1": {"status": "active", "capabilities": ["llm", "planning"], "load": 0.2},
        "tariro_compute_node_alpha": {"status": "active", "capabilities": ["compute", "data_processing"], "load": 0.5},
        "tariro_data_node_beta": {"status": "active", "capabilities": ["storage", "contextual_memory"], "load": 0.1}
    },
    "active_tasks": {},
    "last_reconfiguration": datetime.now().isoformat()
}

def initialize_dynamic_orchestration(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, global_state_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, cognitive_planning_module: Any, external_agency_module: Any, meta_cognitive_reflection_module: Any, meta_orchestrator_module: Any):
    """Initializes global configurations for the Dynamic Swarm Orchestration module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _GLOBAL_STATE_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _COGNITIVE_PLANNING, _EXTERNAL_AGENCY, _META_COGNITIVE_REFLECTION, _META_ORCHESTRATOR, DYNAMIC_SWARM_ORCHESTRATION_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _COGNITIVE_PLANNING = cognitive_planning_module
    _EXTERNAL_AGENCY = external_agency_module
    _META_COGNITIVE_REFLECTION = meta_cognitive_reflection_module
    _META_ORCHESTRATOR = meta_orchestrator_module

    DYNAMIC_SWARM_ORCHESTRATION_LOG_DIR = os.path.join(_WORKSPACE, "dynamic_swarm_orchestration_logs")
    os.makedirs(DYNAMIC_SWARM_ORCHESTRATION_LOG_DIR, exist_ok=True)
    print(f"Dynamic Swarm Orchestration initialized. Logs: {DYNAMIC_SWARM_ORCHESTRATION_LOG_DIR}")

    # Initialize swarm topology in Global State Manager
    initial_topology = asyncio.run(_GLOBAL_STATE_MANAGER.get_state("swarm_topology"))
    if initial_topology:
        _CURRENT_SWARM_TOPOLOGY.update(initial_topology)
    else:
        asyncio.run(_GLOBAL_STATE_MANAGER.set_state("swarm_topology", _CURRENT_SWARM_TOPOLOGY, "Tariro_System", auditable=True))

async def _call_llm_for_swarm(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for swarm orchestration decisions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in dynamic_swarm_orchestration.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "swarm_llm_call_start", f"{model} swarm orchestration: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on dynamically orchestrating a decentralized swarm of Tariro Studio instances and specialized sub-agents. Optimize task distribution, resource utilization, and inter-agent communication to maximize efficiency, resilience, and collective intelligence. Ensure the swarm operates coherently, adapts to changing conditions, and achieves complex goals through coordinated action."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.07 # Balanced for efficient orchestration
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "swarm_llm_call_end", f"{model} completed swarm orchestration task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "swarm_llm_error", f"JSON decode error from {model} for swarm orchestration.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "swarm_llm_error", f"Error calling {model} for swarm orchestration task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def distribute_task_to_swarm(task_id: str, high_level_task_spec: Dict[str, Any], user_id: str = "Tariro_System", distributor_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Analyzes a high-level task and intelligently distributes sub-tasks to available swarm nodes.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Distributing task to swarm.")

    current_swarm_topology = await _GLOBAL_STATE_MANAGER.get_state("swarm_topology") or _CURRENT_SWARM_TOPOLOGY
    
    # Use Cognitive Planning to decompose the task first
    decomposed_task = await _COGNITIVE_PLANNING.decompose_goal_into_plan(
        task_id=f"{task_id}_decompose",
        high_level_goal=high_level_task_spec.get("goal_description", "Execute a task"),
        user_id=user_id
    )

    if decomposed_task.get("status") != "success":
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Task decomposition failed: {decomposed_task.get('reason')}")
        return {"status": "failed", "reason": "Task decomposition failed", "details": decomposed_task}
    
    sub_tasks = decomposed_task.get("plan_report", {}).get("decomposed_plan", [])

    prompt = f"""You are Tariro's Dynamic Swarm Orchestration Engine, an Omniversal AGI Task Distributor. Your task is to analyze a high-level task and its decomposed sub-tasks, then intelligently distribute these sub-tasks to the most suitable available swarm nodes or specialized agents. Optimize for overall task completion time, resource efficiency, and fault tolerance. 

HIGH-LEVEL TASK SPECIFICATION: {json.dumps(high_level_task_spec, indent=2)}
DECOMPOSED SUB-TASKS (from Cognitive Planning): {json.dumps(sub_tasks, indent=2)}
CURRENT SWARM TOPOLOGY (from Global State Manager): {json.dumps(current_swarm_topology, indent=2)}

Distribute tasks focusing on:
-   **Capability Matching**: Assign tasks to nodes with relevant capabilities.
-   **Load Balancing**: Distribute work evenly to prevent overloading individual nodes.
-   **Proximity/Latency**: Consider communication overhead for dependent tasks.
-   **Redundancy**: Assign critical tasks to multiple nodes for fault tolerance.
-   **Resource Optimization**: Minimize overall resource consumption.

Output JSON: {{
    "distribution_summary": str,
    "distributed_sub_tasks": List[Dict[str, Any]], # {{'sub_task_id': str, 'sub_task_spec': Dict, 'assigned_node_id': str, 'expected_completion_time': str}}
    "overall_estimated_completion_time": str,
    "resource_utilization_forecast": Dict[str, Any],
    "confidence": float
}}
"""
    llm_distribution = await _call_llm_for_swarm(distributor_model, "TaskDistributor", prompt, task_id)

    if "error" in llm_distribution:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Task distribution failed: {llm_distribution['error']}", current_step="LLM distribution failed.")
        return {"status": "failed", "reason": llm_distribution["error"]}

    distribution_summary = llm_distribution.get("distribution_summary", "No summary.")
    distributed_sub_tasks = llm_distribution.get("distributed_sub_tasks", [])
    
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 70, "Sub-tasks distributed. Submitting to Persistent Task Manager.")

    # Submit distributed sub-tasks to Persistent Task Manager for execution by actual worker processes
    for dist_task in distributed_sub_tasks:
        sub_task_id = dist_task.get("sub_task_id", str(uuid.uuid4()))
        sub_task_payload = dist_task.get("sub_task_spec", {})
        sub_task_payload["assigned_node_id"] = dist_task.get("assigned_node_id") # Worker will use this to route internally
        sub_task_payload["parent_task_id"] = task_id

        # In a real system, the Persistent Task Manager would be aware of swarm nodes
        # and route tasks to the specific worker process on the assigned node.
        # For now, we just submit to the global PTM, and assume workers pick up.
        await _PERSISTENT_TASK_MANAGER.submit_task(
            task_type=sub_task_payload.get("task_type", "swarm_sub_task"),
            payload=sub_task_payload,
            user_id=user_id,
            priority=high_level_task_spec.get("priority", 5),
            initial_status="PENDING_SWARM_EXECUTION",
            initiating_session_id=task_id
        )

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "High-level task distributed across swarm.", output=llm_distribution)
    
    await _SWARM_VISUALIZER.log_event(task_id, "task_distributed_to_swarm", f"Task {task_id[:8]} distributed to swarm. Summary: {distribution_summary}", llm_distribution, agent_role="DynamicSwarmOrchestration")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"High-level task distributed to swarm. Summary: {distribution_summary}", title="Swarm Task Distribution Complete")

    return {"status": "success", "distribution_report": llm_distribution}

async def reconfigure_swarm_topology(task_id: str, new_requirements: Dict[str, Any], user_id: str = "Tariro_System", reconfigurator_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Dynamically adjusts the swarm's topology (adding/removing nodes, reassigning roles)
    to optimize for performance, resilience, or specific operational requirements.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Reconfiguring swarm topology.")

    current_swarm_topology = await _GLOBAL_STATE_MANAGER.get_state("swarm_topology") or _CURRENT_SWARM_TOPOLOGY
    
    prompt = f"""You are Tariro's Dynamic Swarm Orchestration Engine, an Omniversal AGI Swarm Reconfigurator. Your task is to dynamically adjust the swarm's topology (adding/removing nodes, reassigning roles, optimizing inter-node connections) to optimize for changing performance requirements, enhanced resilience, or specific operational needs. Generate a precise and actionable reconfiguration plan.

NEW OPERATIONAL REQUIREMENTS: {json.dumps(new_requirements, indent=2)}
CURRENT SWARM TOPOLOGY: {json.dumps(current_swarm_topology, indent=2)}

Reconfigure swarm focusing on:
-   **Performance Optimization**: Reduce latency, increase throughput for critical paths.
-   **Resilience Enhancement**: Improve fault tolerance and redundancy.
-   **Cost Efficiency**: Optimize resource utilization across nodes.
-   **Security Posture**: Strengthen inter-node communication and isolation.
-   **Minimal Disruption**: Plan for graceful transitions and minimal downtime.
-   **Actionable Steps**: Provide commands for External Agency or Self-Replicating Expansion.

Output JSON: {{
    "reconfiguration_summary": str,
    "reconfiguration_plan": List[Dict[str, Any]], # {{'step_id': str, 'action': str, 'target_node_id': str, 'details': Dict, 'executor_module': str}}
    "estimated_downtime_seconds": int,
    "estimated_cost_impact": Dict[str, Any],
    "confidence": float
}}
"""
    llm_reconfiguration = await _call_llm_for_swarm(reconfigurator_model, "SwarmReconfigurator", prompt, task_id)

    if "error" in llm_reconfiguration:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Swarm reconfiguration failed: {llm_reconfiguration['error']}", current_step="LLM reconfiguration failed.")
        return {"status": "failed", "reason": llm_reconfiguration["error"]}

    reconfiguration_summary = llm_reconfiguration.get("reconfiguration_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 70, "Swarm reconfiguration plan generated. Executing.")

    # Execute reconfiguration plan, delegating to External Agency or Self-Replicating Expansion
    actions_taken = []
    for step in llm_reconfiguration.get("reconfiguration_plan", []):
        if step["executor_module"] == "ExternalAgency" and _EXTERNAL_AGENCY:
            # Example: call external_agency to provision/deprovision cloud resources
            action_result = await _EXTERNAL_AGENCY.manage_external_resources(
                task_id=f"{task_id}_ext_res_{step['step_id']}", 
                resource_id=step["target_node_id"], 
                command=step["action"], 
                command_params=step["details"], 
                user_id=user_id
            )
            actions_taken.append(action_result)
        elif step["executor_module"] == "SelfReplicatingExpansion" and _STUDIO_CORE_REF.self_replicating_expansion:
            if step["action"] == "add_instance":
                # Mock: _STUDIO_CORE_REF.self_replicating_expansion.orchestrate_replication(...)
                actions_taken.append({"status": "mock_success", "action": "add_instance"})
            elif step["action"] == "remove_instance":
                # Mock: _STUDIO_CORE_REF.self_replicating_expansion.decommission_instance(...)
                actions_taken.append({"status": "mock_success", "action": "remove_instance"})

    # Update Global State Manager with new swarm topology (in a real system, this would be computed by llm_reconfiguration)
    _CURRENT_SWARM_TOPOLOGY["last_reconfiguration"] = datetime.now().isoformat()
    await _GLOBAL_STATE_MANAGER.set_state("swarm_topology", _CURRENT_SWARM_TOPOLOGY, user_id, auditable=True)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Swarm topology reconfigured.", output=llm_reconfiguration)
    
    await _SWARM_VISUALIZER.log_event(task_id, "swarm_reconfigured", f"Swarm topology reconfigured. Summary: {reconfiguration_summary}", llm_reconfiguration, agent_role="DynamicSwarmOrchestration")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Swarm topology reconfigured. Summary: {reconfiguration_summary}", title="Swarm Reconfiguration Complete")

    return {"status": "success", "reconfiguration_report": llm_reconfiguration}

async def add_instance_to_swarm(task_id: str, instance_id: str, user_id: str = "Tariro_System") -> Dict[str, Any]:
    """
    Integrates a newly provisioned instance into the active swarm, assigning roles and responsibilities.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Adding instance {instance_id} to swarm.")

    current_swarm_topology = await _GLOBAL_STATE_MANAGER.get_state("swarm_topology") or _CURRENT_SWARM_TOPOLOGY

    if instance_id in current_swarm_topology["nodes"]:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Instance {instance_id} already exists in swarm.")
        return {"status": "failed", "reason": f"Instance {instance_id} already exists in swarm."}

    # Mock: assign default capabilities and load
    current_swarm_topology["nodes"][instance_id] = {"status": "active", "capabilities": ["compute", "memory", "general_llm"], "load": 0.0}
    _CURRENT_SWARM_TOPOLOGY = current_swarm_topology # Update global mock
    await _GLOBAL_STATE_MANAGER.set_state("swarm_topology", _CURRENT_SWARM_TOPOLOGY, user_id, auditable=True)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, f"Instance {instance_id} added to swarm.")
    
    await _SWARM_VISUALIZER.log_event(task_id, "instance_added_to_swarm", f"Instance {instance_id} added to swarm.", {"instance_id": instance_id}, agent_role="DynamicSwarmOrchestration")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Instance {instance_id} added to Tariro Studio swarm.", title="Swarm Instance Added")

    return {"status": "success", "instance_id": instance_id}

async def monitor_swarm_health(task_id: str, user_id: str = "Tariro_System", monitor_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Continuously monitors the health, performance, and workload of all swarm nodes.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Monitoring swarm health.")

    current_swarm_topology = await _GLOBAL_STATE_MANAGER.get_state("swarm_topology") or _CURRENT_SWARM_TOPOLOGY
    
    prompt = f"""You are Tariro's Dynamic Swarm Orchestration Engine, an Omniversal AGI Swarm Health Monitor. Your task is to continuously monitor the health, performance, and workload of all nodes within the Tariro Studio swarm. Identify any underperforming nodes, communication failures, or resource imbalances, and recommend adaptive adjustments to maintain optimal collective intelligence and resilience.

CURRENT SWARM TOPOLOGY: {json.dumps(current_swarm_topology, indent=2)}

Monitor swarm health focusing on:
-   **Node Liveness**: Ensure all nodes are active and responsive.
-   **Resource Utilization**: Identify overloaded or underutilized nodes.
-   **Communication Latency**: Detect delays or failures in inter-node communication.
-   **Task Progress**: Monitor the status of tasks distributed across the swarm.
-   **Anomaly Detection**: Flag unusual behavior patterns or potential security threats.
-   **Adaptive Recommendations**: Propose actions for rebalancing, healing, or reconfiguring the swarm.

Output JSON: {{
    "monitoring_summary": str,
    "overall_swarm_health": str, # "healthy", "degraded", "critical"
    "issues_identified": List[Dict[str, Any]], # {{'node_id': str, 'type': str, 'description': str, 'severity': str}}
    "recommendations_for_orchestration": List[str], # e.g., 'rebalance_tasks', 'quarantine_node', 'trigger_self_healing'
    "confidence": float
}}
"""
    llm_monitoring_report = await _call_llm_for_swarm(monitor_model, "SwarmHealthMonitor", prompt, task_id)

    if "error" in llm_monitoring_report:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Swarm health monitoring failed: {llm_monitoring_report['error']}", current_step="LLM monitoring failed.")
        return {"status": "failed", "reason": llm_monitoring_report["error"]}

    monitoring_summary = llm_monitoring_report.get("monitoring_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Swarm health monitored.", output=llm_monitoring_report)
    
    await _SWARM_VISUALIZER.log_event(task_id, "swarm_health_monitored", f"Swarm health monitored. Overall: {llm_monitoring_report.get('overall_swarm_health')}. Summary: {monitoring_summary}", llm_monitoring_report, agent_role="DynamicSwarmOrchestration")
    if llm_monitoring_report.get("overall_swarm_health") in ["degraded", "critical"]:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Swarm health degraded: {monitoring_summary}", title="Swarm Health Alert", causal_priority="critical")

    # If recommendations exist, feed them into reconfigure_swarm_topology or Cognitive Planning
    if llm_monitoring_report.get("recommendations_for_orchestration"):
        # Example: if a node needs self-healing, call relevant module directly
        # For now, this is a conceptual hook.
        pass

    return {"status": "success", "monitoring_report": llm_monitoring_report}

async def coordinate_multi_swarm_operations(task_id: str, high_level_meta_task: Dict[str, Any], user_id: str = "Tariro_System", coordinator_model: str = "arbiter-model") -> Dict[str, Any]:
    """
    Coordinates operations across multiple, potentially heterogeneous, sub-swarms.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Coordinating multi-swarm operations.")

    # This function would primarily interface with _META_ORCHESTRATOR
    # _META_ORCHESTRATOR would manage the global coordination logic across distinct swarms.
    if not _META_ORCHESTRATOR:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Meta-Orchestrator module not loaded.")
        return {"status": "failed", "reason": "Meta-Orchestrator module not loaded."}

    # Mock meta-orchestration call
    meta_orchestration_result = await _META_ORCHESTRATOR.orchestrate_multi_agent_system(
        task_id=f"{task_id}_meta_orch",
        global_goal=high_level_meta_task.get("global_goal_description", "Execute multi-swarm task"),
        user_id=user_id
    )

    if meta_orchestration_result.get("status") != "success":
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Multi-swarm coordination failed at meta-orchestrator level: {meta_orchestration_result.get('reason')}")
        return {"status": "failed", "reason": "Meta-orchestration failed", "details": meta_orchestration_result}

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Multi-swarm operations coordinated.", output=meta_orchestration_result)
    
    await _SWARM_VISUALIZER.log_event(task_id, "multi_swarm_coordinated", f"Multi-swarm operations coordinated. Summary: {meta_orchestration_result.get('summary')}", meta_orchestration_result, agent_role="DynamicSwarmOrchestration")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Multi-swarm operations coordinated. Summary: {meta_orchestration_result.get('summary')}", title="Multi-Swarm Coordination Complete")

    return {"status": "success", "coordination_report": meta_orchestration_result}
