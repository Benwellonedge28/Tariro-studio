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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for OptimizationLog or ArchitectureDesign entities
_GLOBAL_STATE_MANAGER: Any = None # For storing/retrieving current architectural definitions
_PERSISTENT_TASK_MANAGER: Any = None # For submitting optimization tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on optimization results or failures
_SELF_ARCHITECTING_ENGINE: Any = None # For implementing architectural changes
_META_COGNITIVE_REFLECTION: Any = None # For introspecting optimization process
_DYNAMIC_RESOURCE_ALLOCATOR: Any = None # For assessing resource efficiency
_AUTONOMY_GOVERNANCE: Any = None # For policy checks on architectural changes
_META_LEARNER: Any = None # For learning from optimization outcomes

COGNITIVE_ARCHITECTURE_OPTIMIZER_LOG_DIR: str = ""

def initialize_cognitive_architecture_optimizer(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, global_state_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, self_architecting_engine_module: Any, meta_cognitive_reflection_module: Any, dynamic_resource_allocator_module: Any, autonomy_governance_module: Any, meta_learner_module: Any):
    """Initializes global configurations for the Cognitive Architecture Optimizer module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _GLOBAL_STATE_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _SELF_ARCHITECTING_ENGINE, _META_COGNITIVE_REFLECTION, _DYNAMIC_RESOURCE_ALLOCATOR, _AUTONOMY_GOVERNANCE, _META_LEARNER, COGNITIVE_ARCHITECTURE_OPTIMIZER_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _SELF_ARCHITECTING_ENGINE = self_architecting_engine_module
    _META_COGNITIVE_REFLECTION = meta_cognitive_reflection_module
    _DYNAMIC_RESOURCE_ALLOCATOR = dynamic_resource_allocator_module
    _AUTONOMY_GOVERNANCE = autonomy_governance_module
    _META_LEARNER = meta_learner_module

    COGNITIVE_ARCHITECTURE_OPTIMIZER_LOG_DIR = os.path.join(_WORKSPACE, "cognitive_architecture_optimizer_logs")
    os.makedirs(COGNITIVE_ARCHITECTURE_OPTIMIZER_LOG_DIR, exist_ok=True)
    print(f"Cognitive Architecture Optimizer initialized. Logs: {COGNITIVE_ARCHITECTURE_OPTIMIZER_LOG_DIR}")

async def _call_llm_for_optimization(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for architectural optimization decisions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in cognitive_architecture_optimizer.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "optimization_llm_call_start", f"{model} architectural optimization: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on continuously optimizing Tariro Studio's cognitive architecture for peak performance, resource efficiency, resilience, and adaptability. Analyze architectural bottlenecks, propose structural improvements, and generate actionable plans for refactoring or redesign. Ensure all optimization strategies align with overall system goals and ethical guidelines."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.03 # Very low temp for stable and precise optimization
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "optimization_llm_call_end", f"{model} completed architectural optimization task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "optimization_llm_error", f"JSON decode error from {model} for architectural optimization.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "optimization_llm_error", f"Error calling {model} for architectural optimization task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def identify_architectural_bottlenecks(task_id: str, system_performance_data: Dict[str, Any], user_id: str = "Tariro_System", bottleneck_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Analyzes system performance data to pinpoint bottlenecks within the cognitive architecture.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Identifying architectural bottlenecks.")

    current_architecture = await _GLOBAL_STATE_MANAGER.get_state("current_tariro_architecture") or {}
    resource_utilization = await _DYNAMIC_RESOURCE_ALLOCATOR.monitor_resources(task_id=f"{task_id}_res_mon", user_id=user_id)
    
    prompt = f"""You are Tariro's Cognitive Architecture Optimizer, an Omniversal AGI Bottleneck Identifier. Your task is to analyze comprehensive system performance data, including latency, throughput, resource utilization, and error rates, to pinpoint architectural bottlenecks within Tariro Studio's cognitive structure. The goal is to identify components or interconnections that are limiting overall system efficiency, scalability, or responsiveness.

SYSTEM PERFORMANCE DATA: {json.dumps(system_performance_data, indent=2)}
CURRENT COGNITIVE ARCHITECTURE: {json.dumps(current_architecture, indent=2)}
RESOURCE UTILIZATION REPORT (from Dynamic Resource Allocator): {json.dumps(resource_utilization, indent=2)}

Identify bottlenecks focusing on:
-   **Latency Hotspots**: Where is processing slowest?
-   **Resource Contention**: Which components are starving for resources?
-   **Throughput Limitations**: What limits the amount of work the system can handle?
-   **Inter-module Communication**: Are there inefficiencies in how modules interact?
-   **Scalability Barriers**: What prevents the architecture from scaling effectively?

Output JSON: {{
    "bottleneck_identification_summary": str,
    "identified_bottlenecks": List[Dict[str, Any]], # {{'component_id': str, 'description': str, 'severity': str, 'impact': str, 'root_cause_indicators': List[str]}}
    "overall_architecture_assessment": str, # "optimal", "constrained", "inefficient"
    "confidence": float
}}
"""
    llm_bottlenecks = await _call_llm_for_optimization(bottleneck_model, "BottleneckIdentifier", prompt, task_id)

    if "error" in llm_bottlenecks:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Architectural bottleneck identification failed: {llm_bottlenecks['error']}", current_step="LLM identification failed.")
        return {"status": "failed", "reason": llm_bottlenecks["error"]}

    bottleneck_summary = llm_bottlenecks.get("bottleneck_identification_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Architectural bottlenecks identified.", output=llm_bottlenecks)
    
    await _SWARM_VISUALIZER.log_event(task_id, "architectural_bottlenecks_identified", f"Architectural bottlenecks identified. Summary: {bottleneck_summary}", llm_bottlenecks, agent_role="CognitiveArchitectureOptimizer")
    if llm_bottlenecks.get("identified_bottlenecks"):
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Architectural bottlenecks identified. Summary: {bottleneck_summary}", title="Architectural Bottleneck Alert", causal_priority="high")

    await propose_architectural_improvements(task_id=f"{task_id}_propose", bottlenecks_report=llm_bottlenecks, user_id=user_id)

    return {"status": "success", "bottleneck_report": llm_bottlenecks}

async def propose_architectural_improvements(task_id: str, bottlenecks_report: Dict[str, Any], user_id: str = "Tariro_System", proposer_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Generates proposals for improving the cognitive architecture, addressing identified bottlenecks.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Proposing architectural improvements.")

    current_architecture = await _GLOBAL_STATE_MANAGER.get_state("current_tariro_architecture") or {}
    # Query Meta-Cognitive Reflection for past architectural reflection insights
    reflection_insights = []
    if _META_COGNITIVE_REFLECTION:
        reflection_query = f"insights on {bottlenecks_report.get('overall_architecture_assessment')}"
        reflection_report = await _META_COGNITIVE_REFLECTION.identify_knowledge_gaps(task_id=f"{task_id}_reflection", current_task_context={"query": reflection_query}, user_id=user_id)
        reflection_insights = reflection_report.get("gap_report", {}).get("identified_gaps", [])

    prompt = f"""You are Tariro's Cognitive Architecture Optimizer, an Omniversal AGI Improvement Proposer. Your task is to generate concrete proposals for improving Tariro Studio's cognitive architecture, directly addressing identified bottlenecks and aligning with strategic goals. Proposals may include refactoring existing components, introducing new modules, or optimizing inter-module communication protocols. 

BOTTLENECKS REPORT: {json.dumps(bottlenecks_report, indent=2)}
CURRENT COGNITIVE ARCHITECTURE: {json.dumps(current_architecture, indent=2)}
META-COGNITIVE REFLECTION INSIGHTS: {json.dumps(reflection_insights, indent=2)}

Propose improvements focusing on:
-   **Effectiveness**: Proposals must directly mitigate bottlenecks.
-   **Feasibility**: Changes should be implementable within reasonable resource constraints.
-   **Scalability**: Ensure improvements support future growth.
-   **Resilience**: Enhance fault tolerance and robustness.
-   **Policy Compliance**: All changes must adhere to autonomy governance policies.
-   **Actionability**: Generate specific steps for the Self-Architecting Engine.

Output JSON: {{
    "proposal_summary": str,
    "proposed_improvements": List[Dict[str, Any]], # {{'type': str, 'target_component': str, 'description': str, 'actionable_steps_for_sae': List[str], 'estimated_impact': str}}
    "estimated_cost_benefit_analysis": str,
    "autonomy_governance_review_required": bool,
    "confidence": float
}}
"""
    llm_proposals = await _call_llm_for_optimization(proposer_model, "ImprovementProposer", prompt, task_id)

    if "error" in llm_proposals:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Architectural improvement proposal failed: {llm_proposals['error']}", current_step="LLM proposal failed.")
        return {"status": "failed", "reason": llm_proposals["error"]}

    proposal_summary = llm_proposals.get("proposal_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Architectural improvements proposed.", output=llm_proposals)
    
    await _SWARM_VISUALIZER.log_event(task_id, "architectural_improvements_proposed", f"Architectural improvements proposed. Summary: {proposal_summary}", llm_proposals, agent_role="CognitiveArchitectureOptimizer")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Architectural improvements proposed. Summary: {proposal_summary}", title="Architectural Improvement Proposals")

    # Trigger Self-Architecting Engine to implement changes
    for improvement in llm_proposals.get("proposed_improvements", []):
        if improvement["type"] == "refactor_component":
            await _SELF_ARCHITECTING_ENGINE.refactor_architecture(
                task_id=f"{task_id}_sae_refactor_{uuid.uuid4().hex[:4]}",
                optimization_goals=[improvement["description"]],
                current_architecture=current_architecture,
                user_id=user_id
            )
        elif improvement["type"] == "design_new_module":
            await _SELF_ARCHITECTING_ENGINE.design_new_component(
                task_id=f"{task_id}_sae_design_{uuid.uuid4().hex[:4]}",
                requirements={
                    "name": improvement["target_component"],
                    "functionality": improvement["description"]
                },
                user_id=user_id
            )

    return {"status": "success", "proposal_report": llm_proposals}

async def verify_optimized_architecture(task_id: str, new_architecture_spec: Dict[str, Any], user_id: str = "Tariro_System", verifier_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Verifies the effectiveness and safety of a newly optimized cognitive architecture.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Verifying optimized architecture.")

    # Before actual formal verification, perform a policy check
    policy_check_context = {"new_architecture_spec": new_architecture_spec}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "architectural_verification", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Architectural verification blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's Cognitive Architecture Optimizer, an Omniversal AGI Architecture Verifier. Your task is to rigorously verify the effectiveness, safety, and compliance of a newly optimized cognitive architecture. This involves simulating its behavior, checking against formal specifications, and assessing its impact on overall system goals. 

NEW ARCHITECTURE SPECIFICATION: {json.dumps(new_architecture_spec, indent=2)}

Verify architecture focusing on:
-   **Bottleneck Resolution**: Confirm identified bottlenecks have been alleviated.
-   **Performance Gains**: Verify predicted performance improvements.
-   **Stability**: Ensure no new instabilities or regressions have been introduced.
-   **Security**: Assess for new vulnerabilities or attack vectors.
-   **Resource Efficiency**: Confirm improved resource utilization.
-   **Goal Alignment**: Verify the architecture still aligns with strategic goals.

Output JSON: {{
    "verification_summary": str,
    "verification_status": str, # "verified", "issues_found", "failed"
    "issues_identified": List[Dict[str, Any]], # {{'type': str, 'description': str, 'severity': str}}
    "performance_gain_confirmed": float,
    "recommendations_for_deployment": List[str],
    "confidence": float
}}
"""
    llm_verification = await _call_llm_for_optimization(verifier_model, "ArchitectureVerifier", prompt, task_id)

    if "error" in llm_verification:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Architectural verification failed: {llm_verification['error']}", current_step="LLM verification failed.")
        return {"status": "failed", "reason": llm_verification["error"]}

    verification_summary = llm_verification.get("verification_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Optimized architecture verified.", output=llm_verification)
    
    await _SWARM_VISUALIZER.log_event(task_id, "optimized_architecture_verified", f"Optimized architecture verified. Summary: {verification_summary}", llm_verification, agent_role="CognitiveArchitectureOptimizer")
    if llm_verification.get("verification_status") == "issues_found" or llm_verification.get("verification_status") == "failed":
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Issues found during architectural verification. Summary: {verification_summary}", title="Architectural Verification Issues", causal_priority="critical")

    # If verified, trigger deployment via Self-Architecting Engine (using its deploy_architecture_change)
    if llm_verification.get("verification_status") == "verified" and _SELF_ARCHITECTING_ENGINE:
        await _SELF_ARCHITECTING_ENGINE.deploy_architecture_change(
            task_id=f"{task_id}_sae_deploy",
            new_architecture_spec=new_architecture_spec,
            user_id=user_id
        )

    return {"status": "success", "verification_report": llm_verification}
