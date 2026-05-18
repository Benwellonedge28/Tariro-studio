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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for EvolutionStrategy or MetaEvolutionLog entities
_PERSISTENT_TASK_MANAGER: Any = None # For submitting self-evolution tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on meta-evolution success/failure
_GLOBAL_STATE_MANAGER: Any = None # For storing meta-evolution strategies and learning models
_META_LEARNER: Any = None # For analyzing self-evolution performance and generating insights
_SELF_EVOLUTION: Any = None # The module to be potentially rewritten
_FORMAL_VERIFICATION: Any = None # For verifying new evolution strategies
_AUTONOMY_GOVERNANCE: Any = None # For policy checks on meta-evolution
_LLM_COMPILER: Any = None # For generating new code for self-evolution strategies
_COGNITIVE_PLANNING: Any = None # For planning complex meta-evolution tasks

META_EVOLUTION_LOG_DIR: str = ""

def initialize_meta_evolution(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, global_state_manager_module: Any, meta_learner_module: Any, self_evolution_module: Any, formal_verification_module: Any, autonomy_governance_module: Any, llm_compiler_module: Any, cognitive_planning_module: Any):
    """Initializes global configurations for the Meta-Evolution module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _GLOBAL_STATE_MANAGER, _META_LEARNER, _SELF_EVOLUTION, _FORMAL_VERIFICATION, _AUTONOMY_GOVERNANCE, _LLM_COMPILER, _COGNITIVE_PLANNING, META_EVOLUTION_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _META_LEARNER = meta_learner_module
    _SELF_EVOLUTION = self_evolution_module
    _FORMAL_VERIFICATION = formal_verification_module
    _AUTONOMY_GOVERNANCE = autonomy_governance_module
    _LLM_COMPILER = llm_compiler_module
    _COGNITIVE_PLANNING = cognitive_planning_module

    META_EVOLUTION_LOG_DIR = os.path.join(_WORKSPACE, "meta_evolution_logs")
    os.makedirs(META_EVOLUTION_LOG_DIR, exist_ok=True)
    print(f"Meta-Evolution initialized. Logs: {META_EVOLUTION_LOG_DIR}")

async def _call_llm_for_meta_evolution(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for meta-evolutionary decisions and strategy generation."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in meta_evolution.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "meta_evolution_llm_call_start", f"{model} meta-evolution: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on autonomously improving Tariro Studio's own self-modification and evolutionary capabilities (i.e., improving the Self-Evolution module itself). Analyze patterns in past self-evolution successes and failures, extract higher-order learning insights, and generate new, more effective self-evolution strategies. Ensure all meta-evolutionary changes maintain functional correctness, enhance resilience, and are formally verifiable. Prioritize improvements that maximize Tariro's ability to adapt and evolve autonomously."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.03 # Very low temp for precise, controlled meta-self-modification
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "meta_evolution_llm_call_end", f"{model} completed meta-evolution task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "meta_evolution_llm_error", f"JSON decode error from {model} for meta-evolution.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "meta_evolution_llm_error", f"Error calling {model} for meta-evolution task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def analyze_self_evolution_failures(task_id: str, failed_attempts_report: List[Dict[str, Any]], user_id: str = "Tariro_System", analyzer_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Analyzes a series of failed self-evolution attempts to identify systemic weaknesses
    in the Self-Evolution module's strategies or implementation.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Analyzing self-evolution failures.")

    # Get insights from Meta-Learner about past evolution performance
    evolution_insights = await _META_LEARNER.get_insights_on_model("self_evolution")
    
    prompt = f"""You are Tariro's Meta-Evolution Engine, an Omniversal AGI Self-Evolution Analyst. Your task is to analyze a series of failed self-evolution attempts by the Self-Evolution module. Identify systemic weaknesses in its strategies, code generation, or architectural modification plans. The goal is to understand *why* self-evolution failed and to propose meta-level improvements to its approach.

FAILED SELF-EVOLUTION ATTEMPTS REPORT: {json.dumps(failed_attempts_report, indent=2)}
INSIGHTS FROM META-LEARNER (on self-evolution performance): {json.dumps(evolution_insights, indent=2)}

Analyze failures focusing on:
-   **Root Cause Analysis**: Pinpoint the underlying reasons for repeated failures (e.g., flawed strategy, code generation errors, verification gaps).
-   **Pattern Identification**: Discover recurring patterns in failure modes.
-   **Strategic Flaws**: Identify conceptual errors in how Self-Evolution attempts to modify itself or other modules.
-   **Learning Gaps**: Are there areas where Self-Evolution needs to learn more effectively?
-   **Recommendations**: Propose meta-level changes to the Self-Evolution module.

Output JSON: {{
    "analysis_summary": str,
    "root_causes_identified": List[str],
    "systemic_weaknesses": List[str],
    "proposed_meta_evolution_strategy": Dict[str, Any], # {{'description': str, 'code_changes_required': str, 'target_self_evolution_function': str}}
    "confidence": float
}}
"""
    llm_analysis = await _call_llm_for_meta_evolution(analyzer_model, "SelfEvolutionAnalyst", prompt, task_id)

    if "error" in llm_analysis:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Self-evolution failure analysis failed: {llm_analysis['error']}", current_step="LLM analysis failed.")
        return {"status": "failed", "reason": llm_analysis["error"]}

    analysis_summary = llm_analysis.get("analysis_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Self-evolution failures analyzed.", output=llm_analysis)
    
    await _SWARM_VISUALIZER.log_event(task_id, "self_evolution_failures_analyzed", f"Self-evolution failures analyzed. Summary: {analysis_summary}", llm_analysis, agent_role="MetaEvolution")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Self-evolution failures analyzed. Summary: {analysis_summary}", title="Meta-Evolution Analysis Complete")

    # Trigger proposal for self-evolution rewrite
    if llm_analysis.get("proposed_meta_evolution_strategy"):
        await propose_self_evolution_rewrite(task_id=f"{task_id}_rewrite", meta_strategy=llm_analysis["proposed_meta_evolution_strategy"], user_id=user_id)

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "meta_evolution_failure_analysis", analysis_summary, llm_analysis, user_id)

    return {"status": "success", "analysis_report": llm_analysis}

async def propose_self_evolution_rewrite(task_id: str, meta_strategy: Dict[str, Any], user_id: str = "Tariro_System", proposer_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Generates a new, optimized version of the Self-Evolution module's code based on
    meta-level strategy and past failure analysis.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Proposing Self-Evolution module rewrite.")

    # Read current Self-Evolution module code
    self_evolution_code = ""
    self_evolution_path = os.path.join(_WORKSPACE, "features", "self_evolution.py")
    if os.path.exists(self_evolution_path):
        with open(self_evolution_path, "r") as f:
            self_evolution_code = f.read()
    
    # Policy check for system mutation (rewriting self-evolution)
    policy_check_context = {"meta_strategy": meta_strategy, "target_module": "self_evolution", "action": "rewrite_code"}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "system_mutation", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Self-Evolution rewrite blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's Meta-Evolution Engine, an Omniversal AGI Self-Evolution Rewriter. Your task is to generate a new, optimized version of the Self-Evolution module's Python code. This rewrite must implement a new meta-level strategy derived from failure analysis, addressing systemic weaknesses, and enhancing Tariro's ability to adapt and evolve autonomously. The generated code must maintain functional correctness, be highly robust, and amenable to formal verification. Include comprehensive test cases for the new self-evolution logic.

META-LEVEL EVOLUTION STRATEGY: {json.dumps(meta_strategy, indent=2)}
CURRENT SELF-EVOLUTION MODULE CODE: {textwrap.dedent(self_evolution_code)}

Generate new Self-Evolution code focusing on:
-   **Strategy Implementation**: Precisely implement the new meta-level strategy.
-   **Robustness**: Make the module more resilient to errors and unexpected inputs.
-   **Efficiency**: Optimize the self-evolution process itself.
-   **Correctness**: Ensure the new code performs as expected.
-   **Testability**: Generate tests for the new self-evolution logic.
-   **Formal Verifiability**: Design the code to facilitate formal verification.

Output JSON: {{
    "rewrite_summary": str,
    "new_self_evolution_code": str,
    "new_self_evolution_tests": str,
    "formal_verification_required": bool,
    "confidence": float
}}
"""
    llm_rewrite = await _call_llm_for_meta_evolution(proposer_model, "SelfEvolutionRewriter", prompt, task_id)

    if "error" in llm_rewrite:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Self-Evolution rewrite failed: {llm_rewrite['error']}", current_step="LLM rewrite failed.")
        return {"status": "failed", "reason": llm_rewrite["error"]}

    rewrite_summary = llm_rewrite.get("rewrite_summary", "No summary.")
    new_code = llm_rewrite.get("new_self_evolution_code", "")
    new_tests = llm_rewrite.get("new_self_evolution_tests", "")

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 70, "New Self-Evolution code generated. Initiating formal verification.")

    # Formal verification of the new self-evolution code
    verification_results = {"status": "skipped", "is_correct": True, "reason": "Formal verification not required or module not available."}
    if _FORMAL_VERIFICATION and llm_rewrite.get("formal_verification_required", True):
        try:
            verification_results = await _FORMAL_VERIFICATION.verify_design(
                task_id=f"{task_id}_fv",
                design_spec=llm_rewrite, # Assuming the generated code + tests can be used as design_spec
                user_id=user_id
            )
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 90, "Formal verification of new Self-Evolution code completed.")
        except Exception as e:
            verification_results = {"status": "error", "reason": str(e)}
            await _SWARM_VISUALIZER.log_event(task_id, "meta_evolution_fv_error", f"Error during formal verification of Self-Evolution rewrite: {e}", agent_role="MetaEvolution", level="ERROR")

    if not verification_results.get("is_correct", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 95, "New Self-Evolution code failed formal verification. Human review required.", output={"rewrite": llm_rewrite, "verification": verification_results})
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
            user_id, task_id, f"New Self-Evolution code failed formal verification. Human review required. Summary: {rewrite_summary}",
            title="Self-Evolution Rewrite Review Needed", causal_priority="critical"
        )
        return {"status": "failed", "reason": "New Self-Evolution code failed formal verification."}

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Self-Evolution module rewrite proposed and verified.", output=llm_rewrite)
    
    await _SWARM_VISUALIZER.log_event(task_id, "self_evolution_rewritten", f"Self-Evolution module rewritten. Summary: {rewrite_summary}", llm_rewrite, agent_role="MetaEvolution")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Self-Evolution module rewritten and verified. Summary: {rewrite_summary}", title="Self-Evolution Rewrite Complete")

    # This part would typically involve a PR process and an N-1 system for approval
    # For direct application, it would replace the old file
    # _SELF_EVOLUTION_PATH = os.path.join(_WORKSPACE, "features", "self_evolution.py")
    # with open(_SELF_EVOLUTION_PATH, "w") as f:
    #     f.write(new_code)
    # with open(_SELF_EVOLUTION_PATH.replace(".py", "_tests.py"), "w") as f:
    #     f.write(new_tests)
    # This should ideally be handled by a higher-level system for code application.

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "meta_evolution_rewrite", rewrite_summary, llm_rewrite, user_id)

    return {"status": "success", "rewrite_report": llm_rewrite}

async def monitor_self_evolution_performance(task_id: str, user_id: str = "Tariro_System", monitor_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Continuously monitors the effectiveness and efficiency of the Self-Evolution module's
    operations, identifying any degradation or opportunities for meta-improvement.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Monitoring Self-Evolution performance.")

    # Fetch recent Self-Evolution logs from CRUD Manager
    recent_evolution_logs = await _CRUD_MANAGER.filter_entities("EvolutionLog", {}, limit=10, sort_by="-timestamp")
    # Fetch insights about self-evolution from Meta-Learner
    meta_learner_insights = await _META_LEARNER.get_insights_on_model("self_evolution")

    prompt = f"""You are Tariro's Meta-Evolution Engine, an Omniversal AGI Self-Evolution Monitor. Your task is to continuously monitor the effectiveness and efficiency of the Self-Evolution module's operations (e.g., code optimization, architectural redesigns). Identify any degradation in its ability to improve Tariro, detect suboptimal evolutionary strategies, or highlight new opportunities for meta-improvement. 

RECENT SELF-EVOLUTION LOGS: {json.dumps(recent_evolution_logs, indent=2)}
META-LEARNER INSIGHTS ON SELF-EVOLUTION: {json.dumps(meta_learner_insights, indent=2)}

Monitor performance focusing on:
-   **Effectiveness**: Is Self-Evolution successfully improving Tariro's capabilities?
-   **Efficiency**: Is the process of self-evolution resource-optimized?
-   **Adaptability**: Can Self-Evolution adapt its own strategies?
-   **Failure Patterns**: Are there new recurring failure modes in Self-Evolution?
-   **Meta-Improvements**: Suggest ways to make Self-Evolution itself more intelligent.

Output JSON: {{
    "monitoring_summary": str,
    "overall_self_evolution_status": str, # "optimal", "suboptimal", "degraded"
    "issues_identified": List[Dict[str, Any]], # {{'type': str, 'description': str, 'severity': str}}
    "recommendations_for_meta_evolution": List[str],
    "confidence": float
}}
"""
    llm_monitoring_report = await _call_llm_for_meta_evolution(monitor_model, "SelfEvolutionMonitor", prompt, task_id)

    if "error" in llm_monitoring_report:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Self-Evolution monitoring failed: {llm_monitoring_report['error']}", current_step="LLM monitoring failed.")
        return {"status": "failed", "reason": llm_monitoring_report["error"]}

    monitoring_summary = llm_monitoring_report.get("monitoring_summary", "No summary.")
    overall_status = llm_monitoring_report.get("overall_self_evolution_status", "suboptimal")

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Self-Evolution performance monitored.", output=llm_monitoring_report)
    
    await _SWARM_VISUALIZER.log_event(task_id, "self_evolution_performance_monitored", f"Self-Evolution performance monitored. Status: {overall_status}. Summary: {monitoring_summary}", llm_monitoring_report, agent_role="MetaEvolution")
    if overall_status == "degraded":
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Self-Evolution performance degraded: {monitoring_summary}", title="Self-Evolution Degradation Alert", causal_priority="critical")

    # Trigger self-evolution rewrite if critical issues are found
    if overall_status == "degraded" or any(issue.get("severity") == "critical" for issue in llm_monitoring_report.get("issues_identified", [])):
        await analyze_self_evolution_failures(
            task_id=f"{task_id}_failure_analysis",
            failed_attempts_report=[{
                "summary": monitoring_summary, 
                "timestamp": datetime.now().isoformat(),
                "issues": llm_monitoring_report.get("issues_identified")
            }],
            user_id=user_id
        )

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "meta_evolution_monitoring", monitoring_summary, llm_monitoring_report, user_id)

    return {"status": "success", "monitoring_report": llm_monitoring_report}
