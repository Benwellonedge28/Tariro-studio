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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for HealthLog or RemediationAction entities
_GLOBAL_STATE_MANAGER: Any = None # For storing current system health and configuration
_PERSISTENT_TASK_MANAGER: Any = None # For submitting diagnostic/remediation tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on system failures or successful repairs
_DYNAMIC_RESOURCE_ALLOCATOR: Any = None # For reallocating resources during healing
_META_COGNITIVE_REFLECTION: Any = None # For introspecting causes of failures and effectiveness of repairs
_SELF_EVOLUTION: Any = None # For suggesting permanent fixes or architectural improvements
_SELF_ARCHITECTING_ENGINE: Any = None # For modifying architecture to prevent future failures
_UNIVERSAL_DEPLOYMENT_MANAGER: Any = None # For rolling back or redeploying components
_META_LEARNER: Any = None # For learning from healing processes
_FORMAL_VERIFICATION: Any = None # For verifying integrity of repaired components
_POLICY_AUDIT_TRAIL: Any = None # For auditing repair actions

SELF_REPAIRING_AUTO_HEALING_LOG_DIR: str = ""

def initialize_self_repairing_auto_healing(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, global_state_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, dynamic_resource_allocator_module: Any, meta_cognitive_reflection_module: Any, self_evolution_module: Any, self_architecting_engine_module: Any, universal_deployment_manager_module: Any, meta_learner_module: Any, formal_verification_module: Any, policy_audit_trail_module: Any):
    """Initializes global configurations for the Self-Repairing Auto-Healing module."""
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
    print(f"Self-Repairing Auto-Healing initialized. Logs: {SELF_REPAIRING_AUTO_HEALING_LOG_DIR}")

async def _call_llm_for_healing(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for self-repair and auto-healing decisions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in self_repairing_auto_healing.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "healing_llm_call_start", f"{model} self-repair: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on autonomously detecting, diagnosing, and remediating internal system failures (software bugs, resource issues, configuration errors, hardware faults). Prioritize rapid recovery, minimal data loss, and long-term system stability. Generate precise diagnostic reports, actionable repair plans, and suggest preventive architectural improvements. Ensure all repair actions are auditable and formally verifiable."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.03 # Very low temp for reliable diagnosis and precise repairs
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "healing_llm_call_end", f"{model} completed self-repair task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "healing_llm_error", f"JSON decode error from {model} for self-repair.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "healing_llm_error", f"Error calling {model} for self-repair task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def detect_system_failure(task_id: str, symptom_data: Dict[str, Any], user_id: str = "Tariro_System", detector_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Continuously monitors system health metrics and logs to detect anomalies indicative of failure.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Detecting system failure.")

    system_health_snapshot = await _GLOBAL_STATE_MANAGER.get_state("system_health") or {}
    recent_audit_logs = ""
    if _POLICY_AUDIT_TRAIL:
        recent_audit_logs = await _POLICY_AUDIT_TRAIL.get_recent_logs_for_component("Tariro_System", limit=50)
    
    prompt = f"""You are Tariro's Self-Repairing Auto-Healing Engine, an Omniversal AGI Failure Detector. Your task is to continuously monitor system health metrics, logs, and behavioral patterns to detect anomalies indicative of current or impending system failures. Provide a preliminary diagnosis and categorize the severity and likely impact.

SYMPTOM DATA: {json.dumps(symptom_data, indent=2)}
CURRENT SYSTEM HEALTH SNAPSHOT (from Global State Manager): {json.dumps(system_health_snapshot, indent=2)}
RECENT AUDIT LOGS (from Policy Audit Trail): {recent_audit_logs}

Detect failures focusing on:
-   **Anomaly Identification**: Deviations from normal operating parameters.
-   **Correlation**: Connect disparate symptoms to form a coherent picture.
-   **Root Cause Indicators**: Point towards the most probable origin of the failure.
-   **Severity & Impact**: Assess the criticality and potential spread of the failure.
-   **Alert Thresholds**: Compare against predefined thresholds for various metrics.

Output JSON: {{
    "detection_summary": str,
    "failure_detected": bool,
    "preliminary_diagnosis": str,
    "severity": str, # "minor", "moderate", "critical", "catastrophic"
    "affected_components": List[str],
    "confidence": float
}}
"""
    llm_detection = await _call_llm_for_healing(detector_model, "FailureDetector", prompt, task_id)

    if "error" in llm_detection:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"System failure detection failed: {llm_detection['error']}", current_step="LLM detection failed.")
        return {"status": "failed", "reason": llm_detection["error"]}

    detection_summary = llm_detection.get("detection_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "System failure detection completed.", output=llm_detection)
    
    await _SWARM_VISUALIZER.log_event(task_id, "system_failure_detected", f"System failure detected. Summary: {detection_summary}", llm_detection, agent_role="SelfRepairingAutoHealing")
    if llm_detection.get("failure_detected", False):
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"System failure detected: {detection_summary}", title="System Failure Alert", causal_priority=llm_detection.get("severity", "critical"))
        await diagnose_and_plan_repair(task_id=f"{task_id}_diagnose", failure_report=llm_detection, user_id=user_id)

    return {"status": "success", "detection_report": llm_detection}

async def diagnose_and_plan_repair(task_id: str, failure_report: Dict[str, Any], user_id: str = "Tariro_System", diagnostician_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Based on a failure report, performs a deeper diagnostic analysis to identify the root cause
    and generates a detailed plan for repair and recovery.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Diagnosing failure and planning repair.")

    affected_components_status = await _GLOBAL_STATE_MANAGER.get_state("system_component_status") or {}
    relevant_reflection_insights = []
    if _META_COGNITIVE_REFLECTION:
        reflection_query = f"insights on {failure_report.get('preliminary_diagnosis')}"
        reflection_report = await _META_COGNITIVE_REFLECTION.identify_knowledge_gaps(task_id=f"{task_id}_reflection", current_task_context={"query": reflection_query}, user_id=user_id)
        relevant_reflection_insights = reflection_report.get("gap_report", {}).get("identified_gaps", [])
    
    prompt = f"""You are Tariro's Self-Repairing Auto-Healing Engine, an Omniversal AGI Diagnostician and Repair Planner. Your task is to perform a deeper diagnostic analysis of an identified system failure, pinpointing the root cause. Subsequently, generate a detailed, actionable plan for repair and recovery, including potential rollbacks and long-term preventive measures.

FAILURE REPORT (from Failure Detector): {json.dumps(failure_report, indent=2)}
AFFECTED COMPONENTS STATUS (from Global State Manager): {json.dumps(affected_components_status, indent=2)}
RELEVANT REFLECTION INSIGHTS (from Meta-Cognitive Reflection): {json.dumps(relevant_reflection_insights, indent=2)}

Diagnose and plan repair focusing on:
-   **Root Cause Analysis**: Identify the fundamental reason for the failure (e.g., software bug, misconfiguration, resource exhaustion, hardware fault).
-   **Impact Assessment**: Quantify the current and potential future impact of the failure.
-   **Repair Strategy**: Detailed, step-by-step plan for restoring functionality.
-   **Resource Allocation**: Estimate resources needed for repair (via Dynamic Resource Allocator).
-   **Rollback Plan**: Clear steps to revert to a stable state if repair fails.
-   **Preventive Measures**: Suggestions for Self-Evolution or Self-Architecting Engine to avoid recurrence.
-   **Verifiability**: How to verify the repair was successful and did not introduce new issues.

Output JSON: {{
    "diagnosis_summary": str,
    "root_cause": str,
    "repair_plan": List[Dict[str, Any]], # {{'step': str, 'action': str, 'target_component': str, 'details': Dict, 'executor_module': str}}
    "estimated_recovery_time_seconds": int,
    "resource_requirements_for_repair": Dict[str, Any],
    "preventive_suggestions": List[str],
    "confidence": float
}}
"""
    llm_diagnosis = await _call_llm_for_healing(diagnostician_model, "DiagnosticianPlanner", prompt, task_id)

    if "error" in llm_diagnosis:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Diagnosis and planning failed: {llm_diagnosis['error']}", current_step="LLM planning failed.")
        return {"status": "failed", "reason": llm_diagnosis["error"]}

    diagnosis_summary = llm_diagnosis.get("diagnosis_summary", "No summary.")
    repair_plan = llm_diagnosis.get("repair_plan", [])
    
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 70, "Failure diagnosed. Repair plan generated. Executing repair.")

    # Trigger resource allocation for repair if needed
    resource_reqs = llm_diagnosis.get("resource_requirements_for_repair", {})
    for res_type, amount in resource_reqs.items():
        await _DYNAMIC_RESOURCE_ALLOCATOR.allocate_resources(task_id, res_type, amount, user_id)

    # Execute repair plan, delegating to relevant modules
    actions_taken = []
    for step in repair_plan:
        if step["executor_module"] == "SelfEvolution" and _SELF_EVOLUTION:
            if step["action"] == "apply_code_patch":
                # Mock: _SELF_EVOLUTION.apply_code_patch(...)
                actions_taken.append({"status": "mock_success", "action": "apply_code_patch"})
        elif step["executor_module"] == "SelfArchitectingEngine" and _SELF_ARCHITECTING_ENGINE:
            if step["action"] == "refactor_architecture":
                # Mock: _SELF_ARCHITECTING_ENGINE.refactor_architecture(...)
                actions_taken.append({"status": "mock_success", "action": "refactor_architecture"})
        elif step["executor_module"] == "UniversalDeploymentManager" and _UNIVERSAL_DEPLOYMENT_MANAGER:
            if step["action"] == "redeploy_component":
                # Mock: _UNIVERSAL_DEPLOYMENT_MANAGER.deploy_component(...)
                actions_taken.append({"status": "mock_success", "action": "redeploy_component"})
        # Add more delegations as needed

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Failure diagnosed and repair initiated/completed.", output=llm_diagnosis)
    
    await _SWARM_VISUALIZER.log_event(task_id, "failure_diagnosed_repaired", f"Failure diagnosed and repair initiated. Summary: {diagnosis_summary}", llm_diagnosis, agent_role="SelfRepairingAutoHealing")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"System failure diagnosed and repair initiated. Summary: {diagnosis_summary}", title="System Repair Initiated")

    # Store repair log in CRUD Manager
    await _CRUD_MANAGER.create_entity("RepairLog", {"id": task_id, "failure_report": failure_report, "repair_plan": llm_diagnosis, "status": "INITIATED"})

    # If formal verification is required, trigger it
    if llm_diagnosis.get("formal_verification_required", False) and _FORMAL_VERIFICATION:
        await _FORMAL_VERIFICATION.verify_repaired_component(task_id=f"{task_id}_fv", component_spec=repair_plan, user_id=user_id)

    # Feed preventive suggestions to Self-Evolution or Self-Architecting Engine
    for suggestion in llm_diagnosis.get("preventive_suggestions", []):
        if "architectural" in suggestion.lower() and _SELF_ARCHITECTING_ENGINE:
            await _SELF_ARCHITECTING_ENGINE.propose_architectural_improvements(
                task_id=f"{task_id}_prevent_arch", 
                bottlenecks_report={"issue": suggestion, "severity": failure_report.get("severity")},
                user_id=user_id
            )
        elif "code" in suggestion.lower() and _SELF_EVOLUTION:
            await _SELF_EVOLUTION.propose_code_improvement(
                task_id=f"{task_id}_prevent_code", 
                description=suggestion,
                user_id=user_id
            )

    return {"status": "success", "diagnosis_report": llm_diagnosis}

async def rollback_system_state(task_id: str, rollback_point: Dict[str, Any], user_id: str = "Tariro_System", rollback_model: str = "arbiter-model") -> Dict[str, Any]:
    """
    Reverts the system to a previous stable state in case of unrecoverable failure or failed repair.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Initiating system rollback.")

    current_system_state = await _GLOBAL_STATE_MANAGER.get_state("system_configuration") or {}
    
    prompt = f"""You are Tariro's Self-Repairing Auto-Healing Engine, an Omniversal AGI System Rollback Orchestrator. Your task is to safely and efficiently revert the system to a previous stable state. This process must be robust, prevent data corruption, and ensure minimal disruption to unaffected components. It requires careful coordination and verification at each step.

CURRENT SYSTEM STATE: {json.dumps(current_system_state, indent=2)}
ROLLBACK POINT SPECIFICATION: {json.dumps(rollback_point, indent=2)}

Initiate rollback focusing on:
-   **Data Integrity**: Ensure no data corruption during rollback.
-   **Component Reversion**: Revert affected components to their state at the rollback point.
-   **Dependency Management**: Handle dependencies between components during rollback.
-   **Verification**: How to confirm the rollback was successful and the system is stable.
-   **Post-Rollback Actions**: Logging, notification, and root cause analysis.

Output JSON: {{
    "rollback_summary": str,
    "rollback_plan": List[Dict[str, Any]], # {{'step': str, 'action': str, 'target_component': str, 'details': Dict, 'executor_module': str}}
    "estimated_downtime_seconds": int,
    "data_loss_risk": str, # "none", "low", "medium", "high"
    "confidence": float
}}
"""
    llm_rollback_plan = await _call_llm_for_healing(rollback_model, "RollbackOrchestrator", prompt, task_id)

    if "error" in llm_rollback_plan:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"System rollback planning failed: {llm_rollback_plan['error']}", current_step="LLM planning failed.")
        return {"status": "failed", "reason": llm_rollback_plan["error"]}

    rollback_summary = llm_rollback_plan.get("rollback_summary", "No summary.")
    rollback_plan = llm_rollback_plan.get("rollback_plan", [])

    # Perform actual rollback steps (mock)
    actions_executed = []
    for step in rollback_plan:
        # Delegation to Universal Deployment Manager for actual deployment/version management
        if step["executor_module"] == "UniversalDeploymentManager" and _UNIVERSAL_DEPLOYMENT_MANAGER:
            if step["action"] == "redeploy_version":
                # Mock: _UNIVERSAL_DEPLOYMENT_MANAGER.redeploy_version(...)
                actions_executed.append({"status": "mock_success", "action": "redeploy_version"})
        # Add more delegations as needed

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "System rollback initiated/completed.", output=llm_rollback_plan)
    
    await _SWARM_VISUALIZER.log_event(task_id, "system_rollback_initiated", f"System rollback initiated. Summary: {rollback_summary}", llm_rollback_plan, agent_role="SelfRepairingAutoHealing")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"System rollback initiated. Summary: {rollback_summary}", title="System Rollback Initiated", causal_priority="critical")

    # Store rollback log in CRUD Manager
    await _CRUD_MANAGER.create_entity("RollbackLog", {"id": task_id, "rollback_point": rollback_point, "rollback_plan": llm_rollback_plan, "status": "INITIATED"})

    return {"status": "success", "rollback_report": llm_rollback_plan}

async def start_continuous_self_hardening_loop(task_id: str, interval_seconds: int, user_id: str = "Tariro_System"): # task_id for tracking
    """
    Starts a continuous loop for self-hardening and proactive self-repair activities.
    This function should be executed by the background worker framework.
    """
    print(f"[SelfRepairingAutoHealing] Starting continuous self-hardening loop with interval {interval_seconds}s.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "RUNNING_LOOP", 0, "Continuous self-hardening loop started.")

    while True:
        try:
            # Simulate gathering current system state / anomaly detection
            symptom_data = {
                "cpu_temp": random.uniform(40, 70), 
                "memory_usage": random.uniform(0.3, 0.9),
                "disk_io": random.uniform(10, 1000)
            }
            # Check for anomalies (mocked for now, in reality call detect_system_failure)
            if random.random() < 0.05: # 5% chance of simulated failure
                print(f"[SelfRepairingAutoHealing] Simulated failure detected in loop for task {task_id}.")
                await detect_system_failure(f"{task_id}_failure_{uuid.uuid4().hex[:8]}", {"simulated_error": "High memory usage detected"}, user_id)
            
            # Periodically reflect on past repairs for learning
            if _META_COGNITIVE_REFLECTION and random.random() < 0.1: # 10% chance to reflect
                past_repair = await _CRUD_MANAGER.filter_entities("RepairLog", {}, limit=1, sort_by="-created_at")
                if past_repair:
                    await _META_COGNITIVE_REFLECTION.reflect_on_decision(
                        task_id=f"{task_id}_reflection_{uuid.uuid4().hex[:8]}",
                        decision_context={
                            "reflection_topic": "past_system_repair",
                            "repair_log_id": past_repair[0]["id"]},
                        outcome={
                            "status": past_repair[0]["status"],
                            "summary": past_repair[0]["repair_plan"]["diagnosis_summary"]
                            },
                        user_id=user_id
                    )
            
            await asyncio.sleep(interval_seconds)
        except asyncio.CancelledError:
            print(f"[SelfRepairingAutoHealing] Continuous self-hardening loop {task_id} cancelled.")
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "CANCELLED", 100, "Continuous self-hardening loop cancelled.")
            break
        except Exception as e:
            print(f"ERROR: Error in continuous self-hardening loop {task_id}: {e}")
            if _SWARM_VISUALIZER:
                await _SWARM_VISUALIZER.log_event(
                    session_id=task_id,
                    event_type="self_hardening_loop_error",
                    message=f"Error in continuous self-hardening loop: {e}",
                    details={
                        "error": str(e)
                    },
                    agent_id=user_id,
                    agent_role="SelfRepairingAutoHealing",
                    level="CRITICAL"
                )
            await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
                user_id,
                task_id,
                f"Critical error in continuous self-hardening loop: {e}",
                title="Self-Hardening Loop Error",
                category="system_update",
                causal_priority="critical"
            )
            await asyncio.sleep(interval_seconds) # Wait before retrying
