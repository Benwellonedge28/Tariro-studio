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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for LearningInsight or LearningModel entities
_GLOBAL_STATE_MANAGER: Any = None # For storing meta-learning models and knowledge base
_PERSISTENT_TASK_MANAGER: Any = None # For submitting meta-learning tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on significant learning breakthroughs or failures
_CONTEXTUAL_MEMORY: Any = None # For retrieving past performance data, reflections, and insights
_META_COGNITIVE_REFLECTION: Any = None # For analyzing learning processes and identifying biases
_SELF_EVOLUTION: Any = None # For applying learned improvements to internal algorithms or modules
_DYNAMIC_POLICY_SYNTHESIS: Any = None # For adjusting learning-related policies

META_LEARNER_LOG_DIR: str = ""

def initialize_meta_learner(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, global_state_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, contextual_memory_module: Any, meta_cognitive_reflection_module: Any, self_evolution_module: Any, dynamic_policy_synthesis_module: Any):
    """Initializes global configurations for the Meta-Learner module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _GLOBAL_STATE_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _CONTEXTUAL_MEMORY, _META_COGNITIVE_REFLECTION, _SELF_EVOLUTION, _DYNAMIC_POLICY_SYNTHESIS, META_LEARNER_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _CONTEXTUAL_MEMORY = contextual_memory_module
    _META_COGNITIVE_REFLECTION = meta_cognitive_reflection_module
    _SELF_EVOLUTION = self_evolution_module
    _DYNAMIC_POLICY_SYNTHESIS = dynamic_policy_synthesis_module

    META_LEARNER_LOG_DIR = os.path.join(_WORKSPACE, "meta_learner_logs")
    os.makedirs(META_LEARNER_LOG_DIR, exist_ok=True)
    print(f"Meta-Learner initialized. Logs: {META_LEARNER_LOG_DIR}")

async def _call_llm_for_meta_learning(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for meta-learning decisions and insight extraction."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in meta_learner.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "metalearner_llm_call_start", f"{model} meta-learning: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on autonomously learning how to learn, improve existing learning processes, and optimize Tariro Studio's cognitive capabilities. Analyze patterns in successes and failures across various modules, extract generalizable learning insights, and generate strategies for enhancing future performance, adaptability, and efficiency. Be introspective and systematic in identifying meta-level improvements."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.03 # Very low temp for objective meta-analysis
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "metalearner_llm_call_end", f"{model} completed meta-learning task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "metalearner_llm_error", f"JSON decode error from {model} for meta-learning.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "metalearner_llm_error", f"Error calling {model} for meta-learning task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def ingest_insight(task_id: str, insight_type: str, insight_summary: str, related_data: Dict[str, Any], user_id: str = "Tariro_System") -> Dict[str, Any]:
    """
    Ingests raw learning insights from various modules (e.g., reflection, performance evaluation).
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Ingesting raw learning insight.")

    # Store the raw insight in CRUD Manager for later meta-analysis
    insight_entry = {
        "id": str(uuid.uuid4()),
        "insight_type": insight_type,
        "summary": insight_summary,
        "related_data": related_data,
        "timestamp": datetime.now().isoformat(),
        "source_task_id": task_id,
        "user_id": user_id
    }
    try:
        await _CRUD_MANAGER.create_entity("LearningInsight", insight_entry)
    except Exception as e:
        print(f"ERROR: Failed to store raw learning insight in CRUD Manager: {e}")
        return {"status": "failed", "reason": f"Failed to persist insight: {e}"}

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Raw learning insight ingested.", output=insight_entry)
    
    await _SWARM_VISUALIZER.log_event(task_id, "raw_insight_ingested", f"Raw learning insight of type '{insight_type}' ingested. Summary: {insight_summary[:100]}", insight_entry, agent_role="MetaLearner")

    # Trigger meta-analysis for this insight
    await analyze_learning_patterns(task_id=f"{task_id}_analyze", insight_id=insight_entry["id"], user_id=user_id)

    return {"status": "success", "insight_id": insight_entry["id"]}

async def analyze_learning_patterns(task_id: str, insight_id: str, user_id: str = "Tariro_System", analyzer_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Analyzes patterns across multiple raw learning insights to extract generalizable meta-learning rules.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Analyzing learning patterns.")

    # Retrieve recent relevant insights from CRUD Manager
    recent_insights = await _CRUD_MANAGER.filter_entities("LearningInsight", {"user_id": user_id}, limit=10, sort_by="-timestamp")
    # Also retrieve the specific insight that triggered this analysis
    current_insight = await _CRUD_MANAGER.read_entity("LearningInsight", insight_id)
    if not current_insight: current_insight = {"summary": "N/A", "related_data": {}}

    # Leverage Meta-Cognitive Reflection for deeper analysis of learning processes
    reflection_on_learning_process = ""
    if _META_COGNITIVE_REFLECTION:
        reflection_report = await _META_COGNITIVE_REFLECTION.reflect_on_decision(
            task_id=f"{task_id}_reflection",
            decision_context={
                "reflection_topic": "learning_process_effectiveness",
                "triggered_insight_id": insight_id
            },
            outcome={
                "recent_insights_count": len(recent_insights),
                "current_insight_summary": current_insight["summary"]
            },
            user_id=user_id
        )
        reflection_on_learning_process = reflection_report.get("reflection_report", {}).get("reflection_summary", "")

    prompt = f"""You are Tariro's Meta-Learner, an Omniversal AGI Pattern Analyzer. Your task is to analyze patterns across multiple raw learning insights, including a newly ingested insight, to extract generalizable meta-learning rules, identify systemic strengths or weaknesses in Tariro's learning processes, and propose actionable meta-level improvements.

NEWLY INGESTED INSIGHT: {json.dumps(current_insight, indent=2)}
RECENT LEARNING INSIGHTS: {json.dumps(recent_insights, indent=2)}
META-COGNITIVE REFLECTION ON LEARNING PROCESS: {reflection_on_learning_process}

Analyze learning patterns focusing on:
-   **Recurring Successes**: What learning strategies consistently lead to positive outcomes?
-   **Systemic Failures**: Are there common patterns in how Tariro fails to learn or adapt?
-   **Generalizable Rules**: Extract higher-order rules about effective learning.
-   **Cognitive Biases**: Identify any biases in the learning feedback loop (e.g., over-optimism).
-   **Process Improvements**: Suggest enhancements to Tariro's internal learning algorithms or data pipelines.

Output JSON: {{
    "analysis_summary": str,
    "extracted_meta_learning_rules": List[str], # e.g., 'prioritize_negative_feedback_for_model_adaptation', 'strengthen_cross_modal_correlation_in_fusion'
    "systemic_learning_strengths": List[str],
    "systemic_learning_weaknesses": List[str],
    "suggested_process_improvements": List[Dict[str, Any]], # {{'type': str, 'target_module': str, 'description': str}}
    "confidence": float
}}
"""
    llm_analysis = await _call_llm_for_meta_learning(analyzer_model, "PatternAnalyzer", prompt, task_id)

    if "error" in llm_analysis:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Learning pattern analysis failed: {llm_analysis['error']}", current_step="LLM analysis failed.")
        return {"status": "failed", "reason": llm_analysis["error"]}

    analysis_summary = llm_analysis.get("analysis_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Learning patterns analyzed.", output=llm_analysis)
    
    await _SWARM_VISUALIZER.log_event(task_id, "learning_patterns_analyzed", f"Learning patterns analyzed. Summary: {analysis_summary}", llm_analysis, agent_role="MetaLearner")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Learning patterns analyzed. Summary: {analysis_summary}", title="Meta-Learning Analysis Complete")

    # Apply learned improvements via Self-Evolution or Dynamic Policy Synthesis
    for improvement in llm_analysis.get("suggested_process_improvements", []):
        if improvement["type"] == "algorithm_enhancement" and _SELF_EVOLUTION:
            await _SELF_EVOLUTION.propose_code_improvement(
                task_id=f"{task_id}_evolve_{uuid.uuid4().hex[:4]}",
                description=improvement["description"],
                user_id=user_id
            )
        elif improvement["type"] == "policy_adjustment" and _DYNAMIC_POLICY_SYNTHESIS:
            await _DYNAMIC_POLICY_SYNTHESIS.synthesize_new_policy(
                task_id=f"{task_id}_policy_{uuid.uuid4().hex[:4]}",
                problem_statement=improvement["description"],
                desired_outcome="Improved learning process based on meta-insight.",
                user_id=user_id
            )

    return {"status": "success", "analysis_report": llm_analysis}

async def get_insights_on_model(model_name: str) -> List[Dict[str, Any]]:
    """
    Retrieves relevant learning insights pertaining to a specific internal AI model.
    """
    if not _CRUD_MANAGER:
        print("WARNING: CRUD Manager not initialized. Cannot retrieve insights.")
        return []
    
    # This is a conceptual query; actual implementation would filter LearningInsights based on content/tags related to model_name
    try:
        insights = await _CRUD_MANAGER.filter_entities("LearningInsight", {"summary": {"$regex": model_name, "$options": "i"}}, limit=10, sort_by="-timestamp")
        return insights
    except Exception as e:
        print(f"ERROR: Failed to retrieve insights for model {model_name}: {e}")
        return []
