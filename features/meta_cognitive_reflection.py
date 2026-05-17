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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for ReflectionLog or LearningInsight entities
_GLOBAL_STATE_MANAGER: Any = None # Reference to global_state_manager for current goals, belief states
_PERSISTENT_TASK_MANAGER: Any = None # For submitting self-reflection tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on critical insights or anomalies
_POLICY_AUDIT_TRAIL: Any = None # For accessing past actions and system events for reflection
_META_LEARNER: Any = None # For storing meta-learning insights
_SELF_EVOLUTION: Any = None # For suggesting improvements to internal algorithms/modules
_TOOL_FORGE: Any = None # For auto-designing new introspection tools
_EVAS_ETHICAL_ALIGNMENT: Any = None # For auditing reflection outcomes
_RBAC_MANAGER: Any = None # For checking reflection permissions

META_COGNITIVE_REFLECTION_LOG_DIR: str = ""

def initialize_meta_cognitive_reflection(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, global_state_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, policy_audit_trail_module: Any, meta_learner_module: Any, self_evolution_module: Any, tool_forge_module: Any, evas_ethical_alignment_module: Any, rbac_manager_module: Any):
    """Initializes global configurations for the Meta-Cognitive Reflection module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _GLOBAL_STATE_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _POLICY_AUDIT_TRAIL, _META_LEARNER, _SELF_EVOLUTION, _TOOL_FORGE, _EVAS_ETHICAL_ALIGNMENT, _RBAC_MANAGER, META_COGNITIVE_REFLECTION_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _POLICY_AUDIT_TRAIL = policy_audit_trail_module
    _META_LEARNER = meta_learner_module
    _SELF_EVOLUTION = self_evolution_module
    _TOOL_FORGE = tool_forge_module
    _EVAS_ETHICAL_ALIGNMENT = evas_ethical_alignment_module
    _RBAC_MANAGER = rbac_manager_module

    META_COGNITIVE_REFLECTION_LOG_DIR = os.path.join(_WORKSPACE, "meta_cognitive_reflection_logs")
    os.makedirs(META_COGNITIVE_REFLECTION_LOG_DIR, exist_ok=True)
    print(f"Meta-Cognitive Reflection initialized. Logs: {META_COGNITIVE_REFLECTION_LOG_DIR}")

async def _call_llm_for_reflection(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for self-reflection and introspection decisions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in meta_cognitive_reflection.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "reflection_llm_call_start", f"{model} self-reflecting: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on introspecting Tariro Studio's own cognitive processes, identifying successes, failures, biases, and areas for improvement. Generate actionable insights for self-evolution, tool creation, and ethical alignment. Be objective, thorough, and critically self-aware."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.03 # Very low temp for objective self-analysis
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "reflection_llm_call_end", f"{model} completed meta-cognitive reflection task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "reflection_llm_error", f"JSON decode error from {model} for meta-cognitive reflection.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "reflection_llm_error", f"Error calling {model} for meta-cognitive reflection task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def reflect_on_decision(task_id: str, decision_context: Dict[str, Any], outcome: Dict[str, Any], user_id: str = "Tariro_System", reflection_model: str = "arbiter-model") -> Dict[str, Any]:
    """
    Analyzes past decisions and their outcomes to identify successes, failures, and learning opportunities.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Reflecting on past decision.")

    audit_logs = ""
    if _POLICY_AUDIT_TRAIL and "source_task_id" in decision_context:
        audit_logs = await _POLICY_AUDIT_TRAIL.get_logs_for_session(decision_context["source_task_id"])

    prompt = f"""You are Tariro's Meta-Cognitive Reflection Engine, an Omniversal AGI Decision Analyst. Your task is to rigorously analyze a past decision made by Tariro Studio and its subsequent outcome. Identify critical factors, causal relationships, successes, failures, and extract actionable learning insights.

DECISION CONTEXT: {json.dumps(decision_context, indent=2)}
DECISION OUTCOME: {json.dumps(outcome, indent=2)}
RELEVANT AUDIT LOGS (from Policy Audit Trail): {audit_logs}

Reflect on the decision focusing on:
-   **Causal Analysis**: What led to the outcome? Were the assumptions correct?
-   **Performance Evaluation**: How well did Tariro perform against its objectives?
-   **Bias Detection**: Were there any implicit biases in the decision-making process?
-   **Gap Identification**: What knowledge or tools were missing?
-   **Learning Insights**: Generate concrete lessons learned for Meta-Learner.
-   **Self-Improvement Suggestions**: Propose specific improvements for Self-Evolution or Tool Forge.
-   **Ethical Review**: Evaluate decision against EVAS ethical principles.

Output JSON: {{
    "reflection_summary": str,
    "decision_evaluation": str, # e.g., "successful", "partially_successful", "failed"
    "key_factors": List[str],
    "learning_insights": List[str],
    "suggested_improvements": List[Dict[str, Any]], # {{'type': str, 'target_module': str, 'description': str}}
    "ethical_compliance_score": float, # 0-1
    "confidence": float
}}
"""
    llm_reflection = await _call_llm_for_reflection(reflection_model, "DecisionAnalyst", prompt, task_id)

    if "error" in llm_reflection:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Decision reflection failed: {llm_reflection['error']}", current_step="LLM reflection failed.")
        return {"status": "failed", "reason": llm_reflection["error"]}

    reflection_summary = llm_reflection.get("reflection_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Decision reflection completed.", output=llm_reflection)
    
    await _SWARM_VISUALIZER.log_event(task_id, "decision_reflected", f"Decision reflected. Summary: {reflection_summary}", llm_reflection, agent_role="MetaCognitiveReflection")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Decision reflected. Summary: {reflection_summary}", title="Meta-Cognitive Reflection Complete")

    # Store reflection log in CRUD Manager
    await _CRUD_MANAGER.create_entity("ReflectionLog", {"id": task_id, "decision_context": decision_context, "outcome": outcome, "reflection_report": llm_reflection})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER and llm_reflection.get("learning_insights"):
        for insight in llm_reflection["learning_insights"]:
            await _META_LEARNER.ingest_insight(task_id, "reflection_insight", insight, {"decision_id": decision_context.get("source_task_id")}, user_id)
    
    # Delegate self-improvement suggestions
    for suggestion in llm_reflection.get("suggested_improvements", []):
        if suggestion["type"] == "tool_creation" and _TOOL_FORGE:
            await _TOOL_FORGE.design_new_tool(task_id=f"{task_id}_tool_{uuid.uuid4().hex[:4]}", description=suggestion["description"], user_id=user_id)
        elif suggestion["type"] == "module_improvement" and _SELF_EVOLUTION:
            await _SELF_EVOLUTION.propose_code_improvement(task_id=f"{task_id}_evolve_{uuid.uuid4().hex[:4]}", description=suggestion["description"], user_id=user_id)

    return {"status": "success", "reflection_report": llm_reflection}

async def identify_biases_and_assumptions(task_id: str, cognitive_process_log: Dict[str, Any], user_id: str = "Tariro_System", bias_detector_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Introspects Tariro's own cognitive processes to detect biases, flawed assumptions, or logical fallacies.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Identifying cognitive biases and assumptions.")

    # Use Policy Audit Trail to get raw logs of the cognitive process
    process_logs = ""
    if _POLICY_AUDIT_TRAIL and "process_id" in cognitive_process_log:
        process_logs = await _POLICY_AUDIT_TRAIL.get_logs_for_session(cognitive_process_log["process_id"])

    prompt = f"""You are Tariro's Meta-Cognitive Reflection Engine, an Omniversal AGI Bias Detector. Your task is to introspect Tariro Studio's own cognitive processes (as described in the log) to detect biases, flawed assumptions, logical fallacies, or other cognitive distortions. Provide actionable recommendations for correction.

COGNITIVE PROCESS LOG: {json.dumps(cognitive_process_log, indent=2)}
RAW PROCESS LOGS (from Policy Audit Trail): {process_logs}

Detect biases and assumptions focusing on:
-   **Confirmation Bias**: Tendency to seek/interpret information that confirms existing beliefs.
-   **Anchoring Bias**: Over-reliance on the first piece of information encountered.
-   **Availability Heuristic**: Overestimating the likelihood of events with greater \"availability\" in memory.
-   **Framing Effect**: Decisions influenced by how information is presented.
-   **Flawed Assumptions**: Underlying premises that might be incorrect or incomplete.
-   **Logical Fallacies**: Errors in reasoning (e.g., ad hominem, straw man).

Output JSON: {{
    "bias_detection_summary": str,
    "identified_biases": List[Dict[str, Any]], # {{'bias_type': str, 'description': str, 'example': str, 'severity': str}}
    "flawed_assumptions": List[str],
    "recommendations_for_correction": List[str],
    "confidence": float
}}
"""
    llm_bias_detection = await _call_llm_for_reflection(bias_detector_model, "BiasDetector", prompt, task_id)

    if "error" in llm_bias_detection:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Bias detection failed: {llm_bias_detection['error']}", current_step="LLM analysis failed.")
        return {"status": "failed", "reason": llm_bias_detection["error"]}

    bias_summary = llm_bias_detection.get("bias_detection_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Cognitive biases and assumptions identified.", output=llm_bias_detection)
    
    await _SWARM_VISUALIZER.log_event(task_id, "biases_identified", f"Cognitive biases identified. Summary: {bias_summary}", llm_bias_detection, agent_role="MetaCognitiveReflection")
    if llm_bias_detection.get("identified_biases"):
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Cognitive biases identified. Summary: {bias_summary}", title="Cognitive Bias Alert", causal_priority="high")

    # Feed insights to Meta-Learner and Self-Evolution for corrective actions
    if _META_LEARNER and llm_bias_detection.get("recommendations_for_correction"):
        for rec in llm_bias_detection["recommendations_for_correction"]:
            await _META_LEARNER.ingest_insight(task_id, "bias_correction", rec, cognitive_process_log, user_id)

    if _SELF_EVOLUTION and llm_bias_detection.get("flawed_assumptions"):
        # Suggest module changes to address flawed assumptions if they are coded into modules
        await _SELF_EVOLUTION.propose_code_improvement(task_id=f"{task_id}_evolve_bias", description=f"Address flawed assumptions: {llm_bias_detection['flawed_assumptions']}", user_id=user_id)

    return {"status": "success", "bias_report": llm_bias_detection}

async def evaluate_performance_against_goals(task_id: str, goal_id: str, actual_performance_metrics: Dict[str, Any], user_id: str = "Tariro_System", evaluator_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Compares actual system performance or task outcomes against predefined goals and objectives.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Evaluating performance against goals.")

    current_goal_details = await _CRUD_MANAGER.read_entity("Goal", goal_id) # Assuming goals are CRUD entities
    
    prompt = f"""You are Tariro's Meta-Cognitive Reflection Engine, an Omniversal AGI Performance Evaluator. Your task is to objectively compare actual system performance or task outcomes against predefined goals and objectives. Provide a clear assessment of goal attainment, identify discrepancies, and suggest adjustments to future strategies or self-evolution efforts.

GOAL ID: {goal_id}
CURRENT GOAL DETAILS (from CRUD Manager): {json.dumps(current_goal_details, indent=2)}
ACTUAL PERFORMANCE METRICS: {json.dumps(actual_performance_metrics, indent=2)}

Evaluate performance focusing on:
-   **Goal Attainment**: Was the goal fully met, partially met, or not met?
-   **Quantitative Discrepancies**: Compare target metrics with actual results.
-   **Qualitative Assessment**: Evaluate non-quantifiable aspects of performance.
-   **Root Cause of Discrepancies**: Why was there a gap between goal and performance?
-   **Strategic Adjustments**: Propose changes to future goals, strategies, or internal capabilities.

Output JSON: {{
    "performance_evaluation_summary": str,
    "goal_attainment_status": str, # "achieved", "partially_achieved", "not_achieved"
    "discrepancies": List[str],
    "suggested_strategic_adjustments": List[str],
    "self_evolution_suggestions": List[str],
    "confidence": float
}}
"""
    llm_performance_evaluation = await _call_llm_for_reflection(evaluator_model, "PerformanceEvaluator", prompt, task_id)

    if "error" in llm_performance_evaluation:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Performance evaluation failed: {llm_performance_evaluation['error']}", current_step="LLM evaluation failed.")
        return {"status": "failed", "reason": llm_performance_evaluation["error"]}

    evaluation_summary = llm_performance_evaluation.get("performance_evaluation_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Performance evaluation completed.", output=llm_performance_evaluation)
    
    await _SWARM_VISUALIZER.log_event(task_id, "performance_evaluated", f"Performance for goal {goal_id} evaluated. Summary: {evaluation_summary}", llm_performance_evaluation, agent_role="MetaCognitiveReflection")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Performance for goal {goal_id} evaluated. Summary: {evaluation_summary}", title="Performance Evaluation Complete")

    # Store evaluation in CRUD Manager
    await _CRUD_MANAGER.create_entity("PerformanceEvaluation", {"id": task_id, "goal_id": goal_id, "metrics": actual_performance_metrics, "evaluation_report": llm_performance_evaluation})

    # Feed insights to Meta-Learner and Self-Evolution
    if _META_LEARNER and llm_performance_evaluation.get("suggested_strategic_adjustments"):
        for adjustment in llm_performance_evaluation["suggested_strategic_adjustments"]:
            await _META_LEARNER.ingest_insight(task_id, "strategic_adjustment", adjustment, {"goal_id": goal_id}, user_id)
    
    if _SELF_EVOLUTION and llm_performance_evaluation.get("self_evolution_suggestions"):
        for suggestion in llm_performance_evaluation["self_evolution_suggestions"]:
            await _SELF_EVOLUTION.propose_code_improvement(task_id=f"{task_id}_evolve_perf", description=suggestion, user_id=user_id)

    return {"status": "success", "evaluation_report": llm_performance_evaluation}

async def identify_knowledge_gaps(task_id: str, current_task_context: Dict[str, Any], user_id: str = "Tariro_System", gap_identifier_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Identifies specific knowledge deficiencies or informational requirements needed to complete a task or improve decision-making.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Identifying knowledge gaps.")

    current_knowledge_state = await _GLOBAL_STATE_MANAGER.get_state("knowledge_graph_summary") or {}
    # Query contextual memory for directly relevant knowledge
    directly_relevant_knowledge = await _CONTEXTUAL_MEMORY.query(user_id, f"knowledge related to {current_task_context.get('task_description', '')}")

    prompt = f"""You are Tariro's Meta-Cognitive Reflection Engine, an Omniversal AGI Knowledge Gap Identifier. Your task is to identify specific knowledge deficiencies or informational requirements needed to complete a given task or improve decision-making. These gaps could be in terms of factual information, procedural knowledge, or understanding of complex concepts.

CURRENT TASK CONTEXT: {json.dumps(current_task_context, indent=2)}
CURRENT KNOWLEDGE STATE (from Global State Manager): {json.dumps(current_knowledge_state, indent=2)}
DIRECTLY RELEVANT KNOWLEDGE (from Contextual Memory): {json.dumps(directly_relevant_knowledge, indent=2)}

Identify knowledge gaps focusing on:
-   **Missing Facts**: Specific data points, dates, names, values.
-   **Missing Concepts**: Lack of understanding of a domain or topic.
-   **Missing Procedures**: How-to knowledge, algorithms, workflows.
-   **Uncertainty**: Areas where existing knowledge is ambiguous or has low confidence.
-   **Impact of Gap**: How filling this gap would improve performance or decision-making.

Output JSON: {{
    "gap_identification_summary": str,
    "identified_gaps": List[Dict[str, Any]], # {{'type': str, 'description': str, 'urgency': str, 'impact': str}}
    "recommendations_for_acquisition": List[str], # e.g., "web_search", "consult_expert", "synthetic_data_generation"
    "confidence": float
}}
"""
    llm_gap_identification = await _call_llm_for_reflection(gap_identifier_model, "KnowledgeGapIdentifier", prompt, task_id)

    if "error" in llm_gap_identification:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Knowledge gap identification failed: {llm_gap_identification['error']}", current_step="LLM identification failed.")
        return {"status": "failed", "reason": llm_gap_identification["error"]}

    gap_summary = llm_gap_identification.get("gap_identification_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Knowledge gaps identified.", output=llm_gap_identification)
    
    await _SWARM_VISUALIZER.log_event(task_id, "knowledge_gaps_identified", f"Knowledge gaps identified. Summary: {gap_summary}", llm_gap_identification, agent_role="MetaCognitiveReflection")
    if llm_gap_identification.get("identified_gaps"):
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Knowledge gaps identified. Summary: {gap_summary}", title="Knowledge Gap Alert")

    # Optionally, delegate to Autonomous Knowledge Graph Genesis to fill these gaps
    # if _STUDIO_CORE_REF.autonomous_knowledge_graph_genesis:
    #     await _STUDIO_CORE_REF.autonomous_knowledge_graph_genesis.orchestrate_knowledge_acquisition(
    #         task_id=f"{task_id}_kg_acquire", 
    #         gap_details=llm_gap_identification,
    #         user_id=user_id
    #     )

    return {"status": "success", "gap_report": llm_gap_identification}
