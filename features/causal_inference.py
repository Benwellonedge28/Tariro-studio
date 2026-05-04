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

CAUSAL_INFERENCE_LOG_DIR: str = ""

def initialize_causal_inference(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, contextual_memory_module: Any, crud_manager_module: Any):
    """Initializes global configurations for Causal Inference Engine."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CONTEXTUAL_MEMORY, _CRUD_MANAGER, CAUSAL_INFERENCE_LOG_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CONTEXTUAL_MEMORY = contextual_memory_module
    _CRUD_MANAGER = crud_manager_module

    CAUSAL_INFERENCE_LOG_DIR = os.path.join(_WORKSPACE, "causal_inference_logs")
    os.makedirs(CAUSAL_INFERENCE_LOG_DIR, exist_ok=True)
    print(f"Causal Inference initialized. Logs: {CAUSAL_INFERENCE_LOG_DIR}")

async def _call_llm_for_causal_analysis(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for causal inference tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in causal_inference.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "causal_llm_call_start", f"{model} evaluating causal analysis: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    try:
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on generating a clear, structured causal explanation or graph."},
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
            task_id, "causal_llm_call_end", f"{model} completed causal analysis task.",
            {"model": model, "response_summary": content[:100]},
            model_name=model, agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "causal_llm_error", f"JSON decode error from {model} for causal analysis.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": model}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "causal_llm_error", f"Error calling {model} for causal analysis.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model}

async def perform_causal_analysis(task_id: str, action_or_state_description: str, additional_context: str = "", analyzer_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates Tariro performing causal inference to explain an autonomous action or system state.
    """
    print(f"AGI ({analyzer_model}) performing causal analysis for: {action_or_state_description[:50]}...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "causal_analysis_start", f"AGI ({analyzer_model}) starting causal analysis.",
        {"action_or_state": action_or_state_description}, model_name=analyzer_model, agent_role=_ALL_MODELS.get(analyzer_model, "Causal Analyzer")
    )

    # Simulate RAG: Retrieve relevant logs (Performance, Explainability, SystemHealth) and contextual memories.
    # In a real system, we'd query for logs that chronologically precede the action_or_state.
    recent_performance_logs = await _CRUD_MANAGER.read_entities(task_id, "PerformanceLog")
    recent_explainability_logs = await _CRUD_MANAGER.read_entities(task_id, "ExplainabilityLog")
    recent_system_health_logs = await _CRUD_MANAGER.read_entities(task_id, "SystemHealthLog")
    
    # Consolidate relevant information for the RAG step
    logs_context = {
        "performance_logs": recent_performance_logs[-3:] if recent_performance_logs else [],
        "explainability_logs": recent_explainability_logs[-3:] if recent_explainability_logs else [],
        "system_health_logs": recent_system_health_logs[-3:] if recent_system_health_logs else []
    }
    
    # Query contextual memory for any other relevant task-specific memories
    task_memories = await _CONTEXTUAL_MEMORY.query_memory_rag(task_id, f"What information is relevant to understanding the causes of '{action_or_state_description}'?", analyzer_model)
    
    rag_context_full = f"""
System Logs & Contextual Memories:
---
Performance Logs: {json.dumps(logs_context['performance_logs'], indent=2)}
Explainability Logs: {json.dumps(logs_context['explainability_logs'], indent=2)}
System Health Logs: {json.dumps(logs_context['system_health_logs'], indent=2)}
Task-Specific Memories: {task_memories.get('response', 'None.')}
Additional Provided Context: {additional_context}
---
"""
    
    # Simulate SIMD: The LLM's complex reasoning about causes and effects from diverse data points.
    
    prompt = f"""You are a sophisticated Causal Inference Engine with an Explainability Graph Generator.
    Analyze the following event/state and all provided context (logs, memories).
    
Event/State to Explain: "{action_or_state_description}"

Based on the context, identify the specific causes and effects that led to this event/state.
Construct a conceptual causal graph in JSON format. The graph should be simple but informative, focusing on the main causal relationships.

Output JSON: {{'explanation_summary': str, 'causal_graph': {{'nodes': list[dict], 'edges': list[dict]}}, 'confidence_score': float, 'key_evidence_sources': list[str]}}
Nodes should have 'id', 'label' (e.g., "High CPU", "AGI Decision", "Human Input"), 'type' (e.g., "event", "state", "decision", "input").
Edges should have 'source' (node id), 'target' (node id), 'relation' (e.g., "caused_by", "led_to", "influenced_by").
"""
    
    result = await _call_llm_for_causal_analysis(
        analyzer_model,
        _ALL_MODELS.get(analyzer_model, "Causal Analyzer"),
        prompt,
        task_id,
        context=rag_context_full
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    log_filename = os.path.join(CAUSAL_INFERENCE_LOG_DIR, f"causal_analysis_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    final_output = {
        "timestamp": datetime.now().isoformat(),
        "action_or_state_description": action_or_state_description,
        "additional_context_provided": additional_context,
        "causal_analysis_result": result
    }
    with open(log_filename, "w") as f:
        json.dump(final_output, f, indent=2)
    final_output["saved_path"] = log_filename
    final_output["status"] = "success"
    print(f"Causal inference analysis saved to {log_filename}")

    await _CONTEXTUAL_MEMORY.store_memory(task_id, analyzer_model, "causal_analysis_result", final_output, "Result of causal inference and explainability graph generation.")
    await _SWARM_VISUALIZER.log_event(
        task_id, "causal_analysis_complete", f"Causal analysis completed for: {action_or_state_description[:50]}",
        final_output, model_name=analyzer_model, agent_role=_ALL_MODELS.get(analyzer_model, "Causal Analyzer")
    )
    
    return final_output
