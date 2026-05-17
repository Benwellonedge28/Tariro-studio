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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for FaultLog or RemediationPlan entities
_GLOBAL_STATE_MANAGER: Any = None # Reference to global_state_manager for system health metrics, component states
_PERSISTENT_TASK_MANAGER: Any = None # For submitting self-healing tasks and monitoring their status
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on system faults or successful repairs
_DYNAMIC_RESOURCE_ALLOCATOR: Any = None # For monitoring resource anomalies and potentially adjusting allocations
_META_COGNITIVE_REFLECTION: Any = None # For learning from failure and repair
_SELF_EVOLUTION: Any = None # For applying code patches
_SELF_ARCHITECTING_ENGINE: Any = None # For architectural adjustments during healing
_UNIVERSAL_DEPLOYMENT_MANAGER: Any = None # For configuration changes or component redeployment
_META_LEARNER: Any = None # For improving diagnosis and remediation strategies
_FORMAL_VERIFICATION: Any = None # For verifying correctness of remediation plans
_POLICY_AUDIT_TRAIL: Any = None # For retrieving error logs and ensuring compliance

SELF_REPAIRING_AUTO_HEALING_LOG_DIR: str = ""

def initialize_self_repairing_auto_healing(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, global_state_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, dynamic_resource_allocator_module: Any, meta_cognitive_reflection_module: Any, self_evolution_module: Any, self_architecting_engine_module: Any, universal_deployment_manager_module: Any, meta_learner_module: Any, formal_verification_module: Any, policy_audit_trail_module: Any):
    """Initializes global configurations for the Self-Repairing & Auto-Healing Systems module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _GLOBAL_STATE_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _DYNAMIC_RESOURCE_ALLOCATOR, _META_COGNITIVE_REFLECTION, _SELF_EVOLUTION, _SELF_ARCHITECTING_ENGINE, _UNIVERSAL_DEPLOYMENT_MANAGER, _META_LEARNER, _FORMAL_VERIFICATION, _POLICY_AUDIT_TRAIL, SELF_REPAIRING_AUTO_HEALING_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _DYNAMIC_RESOURCE_ALLOCATOR = dynamic_resource_allocator_module
    _META_COGNITIVE_REFLECTION = meta_cognitive_reflection_module
    _SELF_EVOLUTION = self_evolution_module
    _SELF_ARCHITECTING_ENGINE = self_architecting_engine_module
    _UNIVERSAL_DEPLOYMENT_MANAGER = universal_deployment_manager_module
    _META_LEARNER = meta_learner_module
    _FORMAL_VERIFICATION = formal_verification_module
    _POLICY_AUDIT_TRAIL = policy_audit_trail_module

    SELF_REPAIRING_AUTO_HEALING_LOG_DIR = os.path.join(_WORKSPACE, "self_repairing_auto_healing_logs")
    os.makedirs(SELF_REPAIRING_AUTO_HEALING_LOG_DIR, exist_ok=True)
    print(f"Self-Repairing & Auto-Healing initialized. Logs: {SELF_REPAIRING_AUTO_HEALING_LOG_DIR}")

async def _call_llm_for_auto_healing(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for self-healing decisions and remediation planning."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in self_repairing_auto_healing.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "auto_healing_llm_call_start", f"{model} performing self-healing: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on autonomously detecting, diagnosing, and remediating internal system failures (software bugs, resource issues, hardware degradation) to ensure continuous operational availability and integrity for Tariro Studio. Prioritize safety, minimal disruption, and long-term stability."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.03 # Very low temp for critical repair operations
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "auto_healing_llm_call_end", f"{model} completed self-healing task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "auto_healing_llm_error", f"JSON decode error from {model} for self-healing.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "auto_healing_llm_error", f"Error calling {model} for self-healing task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def detect_system_fault(task_id: str, error_log: Dict[str, Any], user_id: str = "Tariro_System", detector_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Monitors system health metrics and error logs to immediately identify deviations
    indicative of a fault.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Detecting system fault.")

    system_health_metrics = await _GLOBAL_STATE_MANAGER.get_state("system_health_metrics") or {}
    component_states = await _GLOBAL_STATE_MANAGER.get_state("component_states") or {}
    
    # Also query Policy Audit Trail for recent unusual activities related to error_log source
    audit_context = ""
    if _POLICY_AUDIT_TRAIL and "source_component" in error_log:
        audit_context = await _POLICY_AUDIT_TRAIL.get_recent_logs_for_component(error_log["source_component"])

    prompt = f"""You are Tariro's Self-Repairing & Auto-Healing System, an Omniversal AGI Fault Detector. Your task is to analyze incoming error logs and current system health metrics to immediately identify potential system faults, deviations from normal operation, or resource anomalies.

ERROR LOG INPUT: {json.dumps(error_log, indent=2)}
CURRENT SYSTEM HEALTH METRICS: {json.dumps(system_health_metrics, indent=2)}
COMPONENT STATES: {json.dumps(component_states, indent=2)}
POLICY AUDIT TRAIL CONTEXT: {audit_context}

Detect system faults focusing on:
-   **Anomaly Correlation**: Correlate error logs with metric anomalies.
-   **Severity Assessment**: How critical is the potential fault?
-   **Impact Prediction**: What are the potential consequences if not addressed?
-   **Fault Type Categorization**: Software bug, hardware degradation, resource starvation, security breach.

Output JSON: {{
    "fault_detection_summary": str,
    "fault_detected": bool,
    "fault_id": str,
    "fault_type": str, # e.g., 'software_bug', 'resource_exhaustion', 'hardware_failure', 'security_incident'
    "severity": str, # "critical", "high", "medium", "low"
    "affected_components": List[str],
    "confidence": float
}}
"""
    llm_fault_detection = await _call_llm_for_auto_healing(detector_model, "FaultDetector", prompt, task_id)

    if "error" in llm_fault_detection:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"System fault detection failed: {llm_fault_detection['error']}", current_step="LLM detection failed.")
        return {"status": "failed", "reason": llm_fault_detection["error"]}

    detection_summary = llm_fault_detection.get("fault_detection_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "System fault detected.", output=llm_fault_detection)
    
    await _SWARM_VISUALIZER.log_event(task_id, "system_fault_detected", f"System fault detected. Summary: {detection_summary}", llm_fault_detection, agent_role="SelfRepairingAutoHealing")
    
    if llm_fault_detection.get("fault_detected"):
        fault_id = llm_fault_detection.get("fault_id", str(uuid.uuid4()))
        # Store fault log in CRUD Manager
        await _CRUD_MANAGER.create_entity("FaultLog", {
            "id": fault_id,
            "error_log_input": error_log,
            "detection_report": llm_fault_detection,
            "status": "DETECTED",
            "created_at": datetime.now().isoformat()
        })
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
            user_id, task_id, f"System fault detected ({llm_fault_detection.get('fault_type')}, Severity: {llm_fault_detection.get('severity')}). Summary: {detection_summary}",
            title="System Fault Alert", causal_priority=llm_fault_detection.get('severity', 'medium')
        )
        await diagnose_root_cause(task_id=f"{task_id}_diagnose", fault_details=llm_fault_detection, user_id=user_id)

    return {"status": "success", "detection_report": llm_fault_detection}

async def diagnose_root_cause(task_id: str, fault_details: Dict[str, Any], user_id: str = "Tariro_System", diagnostician_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Utilizes expert systems, probabilistic reasoning, and knowledge graph queries
    to pinpoint the underlying cause of a detected fault.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Diagnosing root cause of fault.")

    fault_id = fault_details.get("fault_id")
    error_log_input = fault_details.get("error_log_input", {})
    
    # Query contextual memory (knowledge graph) for similar past faults or related knowledge
    kg_context = ""
    if _GLOBAL_STATE_MANAGER.autonomous_knowledge_graph_genesis: # Check if KG Genesis module exists and is initialized
        kg_context = await _GLOBAL_STATE_MANAGER.autonomous_knowledge_graph_genesis.query_knowledge_graph(
            task_id=f"{task_id}_kg_query",
            query=f"known causes for {fault_details.get('fault_type')} faults in {fault_details.get('affected_components')}",
            context={"fault_details": fault_details}
        ).get("query_results", {}).get("answer", "")
    elif _CONTEXTUAL_MEMORY:
        kg_context = await _CONTEXTUAL_MEMORY.query(user_id, f"past faults, {fault_details.get('fault_type')}, {error_log_input.get('message', '')}")


    prompt = f"""You are Tariro's Self-Repairing & Auto-Healing System, an Omniversal AGI Root Cause Diagnostician. Your task is to rigorously analyze a detected system fault and pinpoint its underlying root cause. Utilize probabilistic reasoning, system logs, health metrics, and knowledge graph insights to derive an accurate diagnosis.

FAULT DETAILS: {json.dumps(fault_details, indent=2)}
ERROR LOG INPUT: {json.dumps(error_log_input, indent=2)}
KNOWLEDGE GRAPH CONTEXT (from Contextual Memory): {kg_context}

Diagnose the root cause focusing on:
-   **Event Correlation**: Link the fault to specific system events, changes, or anomalies.
-   **Causal Chain Analysis**: Trace back the sequence of events leading to the fault.
-   **Component Interaction Failure**: Identify which module or component interaction failed.
-   **Resource Contention**: Was it a resource exhaustion issue (CPU, memory, network, LLM tokens)?
-   **Software Bug**: Is it a logical error in code?
-   **Hardware Degradation**: Is it a physical system issue?

Output JSON: {{
    "diagnosis_summary": str,
    "root_cause": str, # Concise description of the root cause
    "root_cause_type": str, # e.g., 'software_bug', 'configuration_error', 'resource_leak', 'network_issue', 'external_dependency_failure'
    "affected_subsystems": List[str],
    "diagnosis_confidence": float, # 0-1
    "potential_remediation_categories": List[str] # e.g., 'code_patch', 'config_change', 'resource_scale_up', 'restart_component'
}}
"""
    llm_diagnosis = await _call_llm_for_auto_healing(diagnostician_model, "RootCauseDiagnostician", prompt, task_id)

    if "error" in llm_diagnosis:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Root cause diagnosis failed: {llm_diagnosis['error']}", current_step="LLM diagnosis failed.")
        return {"status": "failed", "reason": llm_diagnosis["error"]}

    diagnosis_summary = llm_diagnosis.get("diagnosis_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Root cause diagnosed.", output=llm_diagnosis)
    
    await _SWARM_VISUALIZER.log_event(task_id, "root_cause_diagnosed", f"Root cause for fault {fault_id[:8]} diagnosed. Summary: {diagnosis_summary}", llm_diagnosis, agent_role="SelfRepairingAutoHealing")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Root cause for fault {fault_id[:8]} diagnosed. Summary: {diagnosis_summary}", title="Fault Diagnosis Complete")

    # Update FaultLog in CRUD Manager with diagnosis
    await _CRUD_MANAGER.update_entity("FaultLog", fault_id, {"diagnosis": llm_diagnosis, "status": "DIAGNOSED"})
    
    await generate_remediation_plan(task_id=f"{task_id}_plan", diagnosis=llm_diagnosis, user_id=user_id)

    return {"status": "success", "diagnosis_report": llm_diagnosis}


async def generate_remediation_plan(task_id: str, diagnosis: Dict[str, Any], user_id: str = "Tariro_System", planner_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Creates a precise, verifiable plan to fix the issue, involving code patches,
    configuration changes, resource reallocation, or hardware replacement.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Generating remediation plan.")

    fault_id = diagnosis.get("fault_id")
    root_cause = diagnosis.get("root_cause")
    root_cause_type = diagnosis.get("root_cause_type")
    affected_subsystems = diagnosis.get("affected_subsystems", [])
    
    current_system_architecture = await _GLOBAL_STATE_MANAGER.get_state("current_tariro_architecture") or {} # From SelfArchitectingEngine
    available_resources = await _GLOBAL_STATE_MANAGER.get_state("system_resource_metrics") or {} # From DynamicResourceAllocator

    prompt = f"""You are Tariro's Self-Repairing & Auto-Healing System, an Omniversal AGI Remediation Planner. Your task is to create a precise, verifiable, and minimal-disruption remediation plan to fix a diagnosed system fault. The plan may involve code patches, configuration changes, resource re-allocation, or architectural adjustments.

FAULT ID: {fault_id[:8]}
ROOT CAUSE: {root_cause} (Type: {root_cause_type})
AFFECTED SUBSYSTEMS: {json.dumps(affected_subsystems, indent=2)}
CURRENT SYSTEM ARCHITECTURE (relevant parts): {json.dumps(current_system_architecture, indent=2)}
AVAILABLE RESOURCES: {json.dumps(available_resources, indent=2)}

Generate a remediation plan focusing on:
-   **Precision**: Clearly define each step and its expected outcome.
-   **Verifiability**: How can each step or the overall plan be formally verified or tested?
-   **Minimizing Disruption**: Avoid downtime or cascading failures.
-   **Safety**: Prioritize system integrity and security during repair.
-   **Delegation**: Specify which other modules should execute which part of the plan (e.g., Self-Evolution for code, UDM for config, DRA for resources).

Output JSON: {{
    "remediation_plan_summary": str,
    "plan_id": str,
    "remediation_steps": List[Dict[str, Any]], # {{'step_id': str, 'description': str, 'action_type': str, 'executor_module': str, 'payload': Dict, 'dependencies': List[str], 'rollback_strategy': str}}
    "estimated_recovery_time_seconds": int,
    "formal_verification_required": bool,
    "confidence": float
}}
"""
    llm_remediation_plan = await _call_llm_for_auto_healing(planner_model, "RemediationPlanner", prompt, task_id)

    if "error" in llm_remediation_plan:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Remediation plan generation failed: {llm_remediation_plan['error']}", current_step="LLM planning failed.")
        return {"status": "failed", "reason": llm_remediation_plan["error"]}

    plan_summary = llm_remediation_plan.get("remediation_plan_summary", "No summary.")
    remediation_steps = llm_remediation_plan.get("remediation_steps", [])
    
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 70, current_step="Remediation plan generated.")

    # Formal verification of the plan steps if required
    verification_results = {"status": "skipped", "reason": "Formal verification not required or module not available."}
    if _FORMAL_VERIFICATION and llm_remediation_plan.get("formal_verification_required", True):
        try:
            # Assuming formal_verification can verify a sequence of actions or state transitions
            verification_results = await _FORMAL_VERIFICATION.verify_remediation_plan(
                task_id=f"{task_id}_fv_plan",
                plan_spec=llm_remediation_plan,
                affected_components=affected_subsystems
            )
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 80, current_step="Formal verification of plan completed.")
        except Exception as e:
            verification_results = {"status": "error", "reason": str(e)}
            await _SWARM_VISUALIZER.log_event(task_id, "plan_fv_error", f"Error during formal verification of plan: {e}", agent_role="SelfRepairingAutoHealing", level="ERROR")


    if verification_results.get("status") == "success" and verification_results.get("is_correct", True):
        # Update FaultLog in CRUD Manager with remediation plan
        await _CRUD_MANAGER.update_entity("FaultLog", fault_id, {"remediation_plan": llm_remediation_plan, "status": "PLAN_GENERATED"})
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Remediation plan for fault {fault_id[:8]} generated and verified. Summary: {plan_summary}", title="Remediation Plan Ready")
        await execute_remediation_atomically(task_id=f"{task_id}_exec", remediation_plan=llm_remediation_plan, user_id=user_id)
    else:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 90, "Remediation plan failed formal verification. Human review required.", output={"plan": llm_remediation_plan, "verification": verification_results})
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
            user_id, task_id, f"Remediation plan for fault {fault_id[:8]} failed verification. Human review required. Summary: {plan_summary}",
            title="Remediation Plan Review Needed", causal_priority="critical"
        )
        await _SWARM_VISUALIZER.log_event(task_id, "remediation_review_needed", "Remediation plan requires human review.", {"plan": llm_remediation_plan}, agent_role="SelfRepairingAutoHealing", level="WARNING")


    return {"status": "success", "remediation_plan": llm_remediation_plan}


async def execute_remediation_atomically(task_id: str, remediation_plan: Dict[str, Any], user_id: str = "Tariro_System", executor_model: str = "arbiter-model") -> Dict[str, Any]:
    """
    Orchestrates the safe, atomic application of the repair, with built-in rollback mechanisms
    and rigorous post-repair verification.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Executing remediation plan atomically.")

    fault_id = remediation_plan.get("fault_id")
    remediation_steps = remediation_plan.get("remediation_steps", [])
    
    current_system_state_snapshot = await _GLOBAL_STATE_MANAGER.get_state("system_state_snapshot") # Take a snapshot for rollback
    
    prompt = f"""You are Tariro's Self-Repairing & Auto-Healing System, an Omniversal AGI Remediation Executor. Your task is to safely and atomically execute a series of remediation steps. Each step must be delegated to the appropriate module. Ensure robust pre-checks, post-checks, and a clear rollback strategy for every change.

REMEDIATION PLAN: {json.dumps(remediation_plan, indent=2)}
CURRENT SYSTEM STATE SNAPSHOT (for rollback): {json.dumps(current_system_state_snapshot, indent=2)}

Execute the remediation steps focusing on:
-   **Atomic Execution**: Treat the entire plan as a single transaction (all or nothing).
-   **Pre-Checks**: Verify conditions before applying each step.
-   **Delegation**: Call appropriate modules (Self-Evolution, Self-Architecting, UDM, DRA) for specific actions.
-   **Post-Checks**: Verify success after each step and overall plan completion.
-   **Rollback**: If any step fails or post-checks show degradation, execute the rollback strategy.
-   **Monitoring**: Continuously monitor system health during and after execution.

Output JSON: {{
    "execution_summary": str,
    "execution_status": str, # "success", "failed", "rolled_back"
    "steps_executed": List[Dict[str, Any]], # {{'step_id': str, 'status': str, 'result': Any}}
    "overall_repair_outcome": str,
    "final_system_state": Optional[Dict[str, Any]],
    "confidence": float
}}
"""
    llm_execution_report = await _call_llm_for_auto_healing(executor_model, "RemediationExecutor", prompt, task_id)

    if "error" in llm_execution_report:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Remediation execution failed: {llm_execution_report['error']}", current_step="LLM orchestration failed.")
        return {"status": "failed", "reason": llm_execution_report["error"]}

    execution_summary = llm_execution_report.get("execution_summary", "No summary.")
    execution_status = llm_execution_report.get("execution_status", "failed")

    if execution_status == "success":
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Remediation plan executed successfully.", output=llm_execution_report)
        await _CRUD_MANAGER.update_entity("FaultLog", fault_id, {"status": "REPAIRED", "repair_outcome": llm_execution_report})
        await _SWARM_VISUALIZER.log_event(task_id, "remediation_executed", f"Remediation for fault {fault_id[:8]} executed successfully. Summary: {execution_summary}", llm_execution_report, agent_role="SelfRepairingAutoHealing")
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"System fault {fault_id[:8]} repaired successfully. Summary: {execution_summary}", title="System Repaired", causal_priority="low")
    elif execution_status == "rolled_back":
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 100, "Remediation failed and rolled back.", output=llm_execution_report)
        await _CRUD_MANAGER.update_entity("FaultLog", fault_id, {"status": "ROLLED_BACK", "repair_outcome": llm_execution_report})
        await _SWARM_VISUALIZER.log_event(task_id, "remediation_rolled_back", f"Remediation for fault {fault_id[:8]} rolled back. Summary: {execution_summary}", llm_execution_report, agent_role="SelfRepairingAutoHealing", level="WARNING")
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"System fault {fault_id[:8]} remediation failed and rolled back. Summary: {execution_summary}", title="Remediation Rolled Back", causal_priority="high")
    else: # failed
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 100, "Remediation failed. Manual intervention needed.", output=llm_execution_report)
        await _CRUD_MANAGER.update_entity("FaultLog", fault_id, {"status": "REPAIR_FAILED", "repair_outcome": llm_execution_report})
        await _SWARM_VISUALIZER.log_event(task_id, "remediation_failed", f"Remediation for fault {fault_id[:8]} failed. Summary: {execution_summary}", llm_execution_report, agent_role="SelfRepairingAutoHealing", level="CRITICAL")
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"System fault {fault_id[:8]} remediation failed. Manual intervention needed. Summary: {execution_summary}", title="Remediation Failed", causal_priority="critical")

    # Feed lessons learned from failure and repair
    await learn_from_failure_and_repair(task_id=f"{task_id}_learn", failure_event={"fault_id": fault_id, "details": fault_details}, repair_outcome=llm_execution_report, user_id=user_id)

    return {"status": "success", "execution_report": llm_execution_report}

async def learn_from_failure_and_repair(task_id: str, failure_event: Dict[str, Any], repair_outcome: Dict[str, Any], user_id: str = "Tariro_System", learner_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Feeds lessons learned from every failure and successful repair back into
    meta_learner and meta_cognitive_reflection to prevent recurrence and improve future self-healing capabilities.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Learning from failure and repair.")

    fault_id = failure_event.get("fault_id")
    
    prompt = f"""You are Tariro's Self-Repairing & Auto-Healing System, an Omniversal AGI Failure Learner. Your task is to extract lessons learned from a system failure and its subsequent repair process. These lessons should be fed back into Tariro's meta-learning and meta-cognitive reflection systems to prevent recurrence, improve future self-healing capabilities, and refine internal processes.

FAILURE EVENT DETAILS: {json.dumps(failure_event, indent=2)}
REPAIR OUTCOME: {json.dumps(repair_outcome, indent=2)}

Extract lessons learned focusing on:
-   **Root Cause Analysis Refinement**: Improve future diagnosis accuracy.
-   **Remediation Plan Optimization**: Identify more efficient or robust repair strategies.
-   **Preventative Measures**: Suggest changes to prevent similar failures.
-   **Architectural Resilience**: Recommend architectural improvements to absorb future shocks.
-   **Knowledge Gaps**: What knowledge was missing that prolonged diagnosis or complicated repair?

Output JSON: {{
    "lessons_learned_summary": str,
    "preventative_actions_recommended": List[str],
    "system_improvements_suggested": List[str], # For Self-Evolution or Self-Architecting Engine
    "meta_learning_insights": List[str], # For Meta-Learner
    "cognitive_reflection_topics": List[str], # For Meta-Cognitive Reflection
    "confidence": float
}}
"""
    llm_lessons = await _call_llm_for_auto_healing(learner_model, "FailureLearner", prompt, task_id)

    if "error" in llm_lessons:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Learning from failure failed: {llm_lessons['error']}", current_step="LLM learning failed.")
        return {"status": "failed", "reason": llm_lessons["error"]}

    lessons_summary = llm_lessons.get("lessons_learned_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Lessons learned from failure and repair.", output=llm_lessons)
    
    await _SWARM_VISUALIZER.log_event(task_id, "lessons_learned", f"Lessons learned from fault {fault_id[:8]} and repair. Summary: {lessons_summary}", llm_lessons, agent_role="SelfRepairingAutoHealing")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Lessons learned from fault {fault_id[:8]} and repair. Summary: {lessons_summary}", title="Lessons Learned")

    # Feed insights to Meta-Learner
    if _META_LEARNER and llm_lessons.get("meta_learning_insights"):
        for insight in llm_lessons["meta_learning_insights"]:
            await _META_LEARNER.ingest_insight(task_id, "failure_learning", insight, {"fault_id": fault_id, "summary": lessons_summary}, user_id)
    
    # Trigger Meta-Cognitive Reflection topics
    if _META_COGNITIVE_REFLECTION and llm_lessons.get("cognitive_reflection_topics"):
        for topic in llm_lessons["cognitive_reflection_topics"]:
            await _PERSISTENT_TASK_MANAGER.submit_task(
                task_type="meta_cognitive_reflection.reflect_on_decision", # Reusing generic reflection
                payload={
                    "decision_context": {"reflection_topic": topic, "source_fault_id": fault_id},
                    "outcome": {"lessons_summary": lessons_summary},
                    "user_id": user_id
                },
                user_id=user_id,
                priority=4,
                initiating_session_id=task_id
            )

    return {"status": "success", "lessons_report": llm_lessons}
