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
_CONTEXTUAL_MEMORY: Any = None # Reference to contextual_memory module
_CRUD_MANAGER: Any = None # Reference to crud_manager module

GOAL_RECALIBRATION_LOG_DIR: str = ""

def initialize_goal_recalibrator(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, contextual_memory_module: Any, crud_manager_module: Any):
    """Initializes global configurations for Real-time Dynamic Goal Recalibration."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CONTEXTUAL_MEMORY, _CRUD_MANAGER, GOAL_RECALIBRATION_LOG_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CONTEXTUAL_MEMORY = contextual_memory_module
    _CRUD_MANAGER = crud_manager_module

    GOAL_RECALIBRATION_LOG_DIR = os.path.join(_WORKSPACE, "goal_recalibration_logs")
    os.makedirs(GOAL_RECALIBRATION_LOG_DIR, exist_ok=True)
    print(f"Goal Recalibrator initialized. Logs: {GOAL_RECALIBRATION_LOG_DIR}")

async def _call_llm_for_goal_recal(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for goal recalibration tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in goal_recalibrator.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "goal_recal_llm_call_start", f"{model} evaluating goal recalibration: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    try:
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on strategic re-evaluation and adjustment of goals."},
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
            out = {"content": content}
        out["model"] = model

        await _SWARM_VISUALIZER.log_event(
            task_id, "goal_recal_llm_call_end", f"{model} completed goal recalibration task.",
            {"model": model, "response_summary": content[:100]},
            model_name=model, agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "goal_recal_llm_error", f"JSON decode error from {model} for goal recalibration.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": model}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "goal_recal_llm_error", f"Error calling {model} for goal recalibration.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model}

async def recalibrate_goals(task_id: str, current_goals_str: str, external_factors_prompt: str, scenario_analysis_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates Tariro autonomously re-evaluating and adjusting goals based on evolving factors.
    """
    print(f"AGI ({scenario_analysis_model}) initiating goal recalibration...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "goal_recal_start", f"AGI ({scenario_analysis_model}) starting goal recalibration.",
        {"external_factors": external_factors_prompt[:100]}, model_name=scenario_analysis_model, agent_role=_ALL_MODELS.get(scenario_analysis_model, "Goal Strategist")
    )

    try:
        current_goals = json.loads(current_goals_str)
    except json.JSONDecodeError:
        return {"status": "failed", "reason": "Invalid JSON for current goals."}

    # Simulate RAG: Fetch relevant strategic documents or global data feeds from memory/external sources
    # For now, we simulate this by providing the external_factors_prompt directly to the LLM.
    # In a real system, _CONTEXTUAL_MEMORY.query_memory_rag could fetch this.
    rag_context = await _CONTEXTUAL_MEMORY.query_memory_rag(task_id, f"Retrieve strategic documents and global data feeds relevant to: {external_factors_prompt}", scenario_analysis_model)
    if rag_context.get("response") and rag_context["response"] != "No relevant context found in memory.":
        rag_info = rag_context["response"]
    else:
        rag_info = f"No specific RAG data, relying on general knowledge about: {external_factors_prompt}"
    
    # Simulate SIMD: Rapid scenario analysis. The LLM's thought process will cover this.
    
    prompt = f"""You are a highly advanced AGI strategic planner. Your task is to dynamically recalibrate a set of current goals based on new external factors and a rapid scenario analysis.
    
Current Goals (prioritized):
{json.dumps(current_goals, indent=2)}

New External Factors & Strategic Data (RAG output):
{rag_info}

Perform a rapid scenario analysis (SIMD-like conceptual processing) considering these factors.
Identify which existing goals need adjustment, which new goals should be introduced, or which goals are no longer relevant.
For each proposed change, provide a clear rationale.

Output JSON: {{'recalibrated_goals': list[dict], 'adjustments_made': list[dict], 'rationale': str, 'confidence_score': float}}
Each goal in 'recalibrated_goals' should have 'title', 'description', 'priority', 'status', 'id' (if existing, else new UUID).
Each adjustment dict should have: {{'goal_id': str, 'type': 'new' | 'update' | 'remove', 'details': dict, 'reason': str}}.
"""
    
    result = await _call_llm_for_goal_recal(
        scenario_analysis_model,
        _ALL_MODELS.get(scenario_analysis_model, "Goal Strategist"),
        prompt,
        task_id,
        context=f"Current Goals: {current_goals_str}\nExternal Factors: {external_factors_prompt}\nRAG Context: {rag_info}"
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    # Simulate applying changes to goals via CRUD Manager
    applied_changes = []
    for adjustment in result.get("adjustments_made", []):
        goal_id = adjustment["goal_id"]
        adj_type = adjustment["type"]
        details = adjustment["details"]
        
        if adj_type == "new":
            new_goal_data = {**details, "status": details.get("status", "active"), "priority": details.get("priority", "medium")}
            crud_res = await _CRUD_MANAGER.create_entity(task_id, "Goal", new_goal_data)
            applied_changes.append({"action": "created", "goal_id": crud_res.get("id"), "title": details.get("title")})
        elif adj_type == "update":
            crud_res = await _CRUD_MANAGER.update_entity(task_id, "Goal", goal_id, details)
            if crud_res.get("status") == "success":
                applied_changes.append({"action": "updated", "goal_id": goal_id, "title": details.get("title")})
            else:
                applied_changes.append({"action": "update_failed", "goal_id": goal_id, "reason": crud_res.get("reason")})
        elif adj_type == "remove":
            crud_res = await _CRUD_MANAGER.delete_entity(task_id, "Goal", goal_id)
            if crud_res.get("status") == "success":
                applied_changes.append({"action": "removed", "goal_id": goal_id})
            else:
                applied_changes.append({"action": "remove_failed", "goal_id": goal_id, "reason": crud_res.get("reason")})
    
    log_filename = os.path.join(GOAL_RECALIBRATION_LOG_DIR, f"goal_recal_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    final_output = {
        "timestamp": datetime.now().isoformat(),
        "initial_goals": current_goals,
        "external_factors_prompt": external_factors_prompt,
        "recalibration_decision": result,
        "applied_changes": applied_changes
    }
    with open(log_filename, "w") as f:
        json.dump(final_output, f, indent=2)
    final_output["saved_path"] = log_filename
    final_output["status"] = "success"
    print(f"Goal recalibration analysis saved to {log_filename} and changes applied via CRUD.")

    await _CONTEXTUAL_MEMORY.store_memory(task_id, scenario_analysis_model, "recalibrated_goals_summary", final_output, "Summary of goal recalibration process and outcomes.")
    await _SWARM_VISUALIZER.log_event(
        task_id, "goal_recal_complete", f"Goals successfully recalibrated. Changes: {len(applied_changes)}",
        final_output, model_name=scenario_analysis_model, agent_role=_ALL_MODELS.get(scenario_analysis_model, "Goal Strategist")
    )
    
    return final_output
