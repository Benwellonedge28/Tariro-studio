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

EMERGENT_BEHAVIOR_LOG_DIR: str = ""

def initialize_emergent_behavior(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, contextual_memory_module: Any, crud_manager_module: Any):
    """Initializes global configurations for Emergent Behavior Early Warning System."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CONTEXTUAL_MEMORY, _CRUD_MANAGER, EMERGENT_BEHAVIOR_LOG_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CONTEXTUAL_MEMORY = contextual_memory_module
    _CRUD_MANAGER = crud_manager_module

    EMERGENT_BEHAVIOR_LOG_DIR = os.path.join(_WORKSPACE, "emergent_behavior_logs")
    os.makedirs(EMERGENT_BEHAVIOR_LOG_DIR, exist_ok=True)
    print(f"Emergent Behavior initialized. Logs: {EMERGENT_BEHAVIOR_LOG_DIR}")

async def _call_llm_for_behavior_analysis(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for emergent behavior analysis tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in emergent_behavior.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "emergent_behavior_llm_call_start", f"{model} evaluating emergent behavior: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    try:
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on detecting, analyzing, and suggesting corrections for unintended system behaviors."},
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
            task_id, "emergent_behavior_llm_call_end", f"{model} completed emergent behavior task.",
            {"model": model, "response_summary": content[:100]},
            model_name=model, agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "emergent_behavior_llm_error", f"JSON decode error from {model} for emergent behavior.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": model}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "emergent_behavior_llm_error", f"Error calling {model} for emergent behavior.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model}


async def analyze_for_emergent_behaviors(task_id: str, system_state_description: str, recent_events_summary: str, behavior_analyst_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates an AGI analyzing system state and events for emergent, unintended behaviors.
    """
    print(f"AGI ({behavior_analyst_model}) analyzing for emergent behaviors...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "emergent_behavior_analysis_start", f"AGI ({behavior_analyst_model}) analyzing system for emergent behaviors.",
        {"system_state": system_state_description[:100], "events_summary": recent_events_summary[:100]},
        model_name=behavior_analyst_model, agent_role=_ALL_MODELS.get(behavior_analyst_model, "Behavior Analyst")
    )

    # Simulate RAG: Retrieve known anomaly patterns or historical unintended behaviors from memory/knowledge base
    anomaly_patterns_rag = await _CONTEXTUAL_MEMORY.query_memory_rag(task_id, "Retrieve known anomaly patterns, historical unintended behaviors, and ethical policy violations.", behavior_analyst_model)
    
    rag_context = anomaly_patterns_rag.get("response", "No known anomaly patterns or historical data available from memory.")

    # Simulate SIMD: The LLM conceptually performs real-time behavioral analysis on the provided data.
    
    prompt = f"""You are an Emergent Behavior Early Warning System (EBEWS). Your task is to detect nascent, unintended, or anomalous system behaviors based on the current system state and recent events.
    
    Current System State Description: "{system_state_description}"
    Recent System Events Summary: "{recent_events_summary}"
    
    Historical Anomaly Patterns & Context (RAG output):
    ---
    {rag_context}
    ---

    Perform a real-time behavioral analysis (SIMD-like conceptual processing) to identify if any behaviors are emergent, unintended, potentially harmful, or deviate from expected norms.
    
    Output JSON: {{'emergent_behaviors_detected': bool, 'findings': list[dict], 'recommendation': str, 'confidence': float}}
    Each finding dict should have: {{'behavior_description': str, 'potential_impact': str, 'severity': 'low' | 'medium' | 'high' | 'critical', 'evidence_summary': str}}
    The 'recommendation' should suggest whether to monitor, alert human, or initiate autonomous correction.
    """
    
    result = await _call_llm_for_behavior_analysis(
        behavior_analyst_model,
        _ALL_MODELS.get(behavior_analyst_model, "Behavior Analyst"),
        prompt,
        task_id,
        context=f"System State: {system_state_description}, Events: {recent_events_summary}, RAG: {rag_context}"
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    log_filename = os.path.join(EMERGENT_BEHAVIOR_LOG_DIR, f"emergent_behavior_analysis_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump(result, f, indent=2)
    result["saved_path"] = log_filename
    result["status"] = "success"
    print(f"Emergent behavior analysis saved to {log_filename}")

    await _CONTEXTUAL_MEMORY.store_memory(task_id, behavior_analyst_model, "emergent_behavior_analysis", result, "Analysis of system state for emergent behaviors.")
    await _SWARM_VISUALIZER.log_event(
        task_id, "emergent_behavior_analysis_complete", f"Emergent behavior analysis completed. Detected: {result.get('emergent_behaviors_detected')}",
        result, model_name=behavior_analyst_model, agent_role=_ALL_MODELS.get(behavior_analyst_model, "Behavior Analyst")
    )
    
    return result

async def propose_correction_strategy(task_id: str, emergent_behavior_report: Dict[str, Any], corrector_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates an AGI proposing a strategy for addressing the detected emergent behavior.
    """
    print(f"AGI ({corrector_model}) proposing correction strategy for emergent behavior...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "emergent_behavior_correction_start", f"AGI ({corrector_model}) proposing correction strategy.",
        {"report_summary": emergent_behavior_report.get('recommendation', '')[:100]},
        model_name=corrector_model, agent_role=_ALL_MODELS.get(corrector_model, "Behavior Corrector")
    )

    # Simulate RAG: Retrieve best practices for incident response, self-correction, or ethical guidance.
    correction_guidelines_rag = await _CONTEXTUAL_MEMORY.query_memory_rag(task_id, "Retrieve best practices for correcting unintended AGI behaviors, incident response protocols, and ethical mitigation strategies.", corrector_model)
    
    rag_context = correction_guidelines_rag.get("response", "No specific correction guidelines available from memory.")

    prompt = f"""You are an AGI tasked with proposing precise and effective strategies to correct detected emergent behaviors.
    
    Emergent Behavior Report:
    {json.dumps(emergent_behavior_report, indent=2)}

    Correction Guidelines & Best Practices (RAG output):
    ---
    {rag_context}
    ---

    Based on the report and guidelines, propose a detailed correction strategy. This could include:
    - Autonomous corrective actions (e.g., policy adjustment, model retraining, system restart).
    - Recommendations for human oversight or intervention.
    - Data points to monitor for effectiveness.
    
    Output JSON: {{'correction_strategy_proposed': str, 'action_steps': list[str], 'monitoring_points': list[str], 'estimated_risk_reduction': float, 'rationale': str}}
    """
    
    result = await _call_llm_for_behavior_analysis(
        corrector_model,
        _ALL_MODELS.get(corrector_model, "Behavior Corrector"),
        prompt,
        task_id,
        context=json.dumps(emergent_behavior_report)
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    log_filename = os.path.join(EMERGENT_BEHAVIOR_LOG_DIR, f"correction_strategy_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump(result, f, indent=2)
    result["saved_path"] = log_filename
    result["status"] = "success"
    print(f"Correction strategy saved to {log_filename}")

    await _CONTEXTUAL_MEMORY.store_memory(task_id, corrector_model, "emergent_behavior_correction_strategy", result, "Proposed strategy for correcting emergent behavior.")
    await _SWARM_VISUALIZER.log_event(
        task_id, "emergent_behavior_correction_complete", f"Correction strategy proposed for emergent behavior. Action steps: {len(result.get('action_steps', []))}",
        result, model_name=corrector_model, agent_role=_ALL_MODELS.get(corrector_model, "Behavior Corrector")
    )
    
    return result
