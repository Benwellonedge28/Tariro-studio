import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import random

# --- Configuration & Shared Data (initialized from studio_v3.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Base model definitions from studio_v3.py
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module
_CRUD_MANAGER: Any = None # Reference to crud_manager module for simulated entity data

UI_ADAPTATION_LOG_DIR: str = ""

def initialize_adaptive_ui(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any):
    """Initializes global configurations for Adaptive User Interface."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, UI_ADAPTATION_LOG_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module

    UI_ADAPTATION_LOG_DIR = os.path.join(_WORKSPACE, "ui_adaptation_logs")
    os.makedirs(UI_ADAPTATION_LOG_DIR, exist_ok=True)
    print(f"Adaptive UI initialized. Logs: {UI_ADAPTATION_LOG_DIR}")

async def _call_llm_for_ui_adaptation(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for UI adaptation suggestions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in adaptive_ui.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "ui_adapt_llm_call_start", f"{model} evaluating UI adaptation: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    try:
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on practical UI adaptation suggestions."},
            {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
        ]
        
        resp = await _CLIENT.chat.completions.create(
            model=model,
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.1
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content} # Should not happen with json_object
        out["model"] = model

        await _SWARM_VISUALIZER.log_event(
            task_id, "ui_adapt_llm_call_end", f"{model} completed UI adaptation task.",
            {"model": model, "response_summary": content[:100]},
            model_name=model, agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "ui_adapt_llm_error", f"JSON decode error from {model} for UI adaptation.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": model}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "ui_adapt_llm_error", f"Error calling {model} for UI adaptation.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model}


async def suggest_ui_adaptations(task_id: str, current_user_role: str, current_task_phase: str, user_feedback: str = "", a_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates an AGI analyzing context and suggesting UI adaptations.
    """
    print(f"AGI ({a_model}) suggesting UI adaptations for role '{current_user_role}' and phase '{current_task_phase}'...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "ui_adapt_start", f"AGI ({a_model}) suggesting UI adaptations.",
        {"user_role": current_user_role, "task_phase": current_task_phase, "feedback_summary": user_feedback[:100]},
        model_name=a_model, agent_role=_ALL_MODELS.get(a_model, "UI Adaptor")
    )

    # Simulate gathering data from LearningInsight and WellbeingLog via crud_manager
    user_preferences = await _CRUD_MANAGER.read_entities(task_id, "LearningInsight", {"category": "preference"})
    wellbeing_logs = await _CRUD_MANAGER.read_entities(task_id, "WellbeingLog")

    preferences_summary = json.dumps(user_preferences, indent=2) if user_preferences else "No specific preferences recorded."
    wellbeing_summary = json.dumps(wellbeing_logs[-3:], indent=2) if wellbeing_logs else "No recent wellbeing data." # Last 3 logs

    prompt = f"""You are an AGI dedicated to optimizing user experience through adaptive interfaces.
    The current user has the role: '{current_user_role}'.
    The current task is in the phase: '{current_task_phase}'.
    User feedback: '{user_feedback}' (if provided).

    Relevant user preferences from LearningInsight:
    {preferences_summary}

    Recent wellbeing data (last 3 entries) from WellbeingLog:
    {wellbeing_summary}

    Based on this context, propose specific, actionable UI adaptations.
    Consider:
    - Layout changes (e.g., rearrange panels, show/hide sections).
    - Information density adjustments (e.g., simplify views, expand details).
    - Highlighted actions or guidance.
    - Suggestions for proactive notifications or prompts.

    Output JSON: {{'suggested_adaptations': list[dict], 'rationale': str, 'user_impact_score': float}}
    Each adaptation dict should have: {{'element_id': str, 'action': str, 'details': str}}.
    Example: {{'element_id': 'crud_panel', 'action': 'hide', 'details': 'User is coder, rarely uses CRUD.'}}
    """
    
    result = await _call_llm_for_ui_adaptation(
        a_model,
        _ALL_MODELS.get(a_model, "UI Adaptor"),
        prompt,
        task_id,
        context=f"User role: {current_user_role}, Task phase: {current_task_phase}"
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    log_filename = os.path.join(UI_ADAPTATION_LOG_DIR, f"ui_adapt_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump(result, f, indent=2)
    result["saved_path"] = log_filename
    result["status"] = "success"
    print(f"UI adaptation suggestions saved to {log_filename}")

    await _CONTEXTUAL_MEMORY.store_memory(task_id, a_model, "ui_adaptations_suggested", result.get("suggested_adaptations", []), "Suggested UI adaptations based on context.")
    
    return result
