import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional

# --- Configuration & Shared Data (initialized from studio_v3.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Base model definitions from studio_v3.py
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module
_CONTEXTUAL_MEMORY: Any = None # Reference to contextual_memory module

SENSORY_LOG_DIR: str = ""

def initialize_sensory_fusion(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, contextual_memory_module: Any):
    """Initializes global configurations for Omni-Sensory Data Fusion Engine."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CONTEXTUAL_MEMORY, SENSORY_LOG_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CONTEXTUAL_MEMORY = contextual_memory_module

    SENSORY_LOG_DIR = os.path.join(_WORKSPACE, "sensory_fusion_logs")
    os.makedirs(SENSORY_LOG_DIR, exist_ok=True)
    print(f"Sensory Fusion Engine initialized. Logs: {SENSORY_LOG_DIR}")

async def _call_llm_for_sensory_fusion(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for sensory fusion tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in sensory_fusion.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "sensory_fusion_llm_call_start", f"{model} evaluating sensory data: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    try:
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on synthesizing cross-modal data into a holistic context."},
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
            task_id, "sensory_fusion_llm_call_end", f"{model} completed sensory fusion task.",
            {"model": model, "response_summary": content[:100]},
            model_name=model, agent_role=role
        )
        return out
    except Exception as e:
        await _SWARM_VISUALIZER.log_event(task_id, "sensory_fusion_llm_error", f"Error calling {model} for sensory fusion.", {"error": str(e)}, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model}

async def fuse_sensory_data(task_id: str, data_streams: Dict[str, Any], fusion_agent: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates correlating and normalizing multi-modal data streams.
    """
    print(f"AGI ({fusion_agent}) fusing multi-modal data streams...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "sensory_fusion_start", f"AGI ({fusion_agent}) fusing data streams.",
        {"streams": list(data_streams.keys())}, model_name=fusion_agent, agent_role=_ALL_MODELS.get(fusion_agent, "Data Fusionist")
    )

    prompt = f"""You are an AGI Omni-Sensory Data Fusion Engine.
    Analyze the following multi-modal data streams and synthesize a unified "situational snapshot".
    Correlate events across modalities to identify underlying causes, current state, and actionable insights.
    
    Data Streams:
    {json.dumps(data_streams, indent=2)}
    
    Output JSON: {{'situational_snapshot': str, 'detected_correlations': list[dict], 'actionable_insights': list[str], 'confidence': float}}
    Each correlation dict should have: {{'modalities_involved': list[str], 'correlation_summary': str}}
    """
    
    result = await _call_llm_for_sensory_fusion(
        fusion_agent,
        _ALL_MODELS.get(fusion_agent, "Data Fusionist"),
        prompt,
        task_id,
        context=f"Data Streams: {list(data_streams.keys())}"
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    log_filename = os.path.join(SENSORY_LOG_DIR, f"fusion_snapshot_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump(result, f, indent=2)
    result["saved_path"] = log_filename
    result["status"] = "success"
    
    await _CONTEXTUAL_MEMORY.store_memory(task_id, fusion_agent, "situational_snapshot", result, "Synthesized situational snapshot from multi-modal data fusion.")
    await _SWARM_VISUALIZER.log_event(
        task_id, "sensory_fusion_complete", f"Data fusion completed.",
        result, model_name=fusion_agent, agent_role=_ALL_MODELS.get(fusion_agent, "Data Fusionist")
    )
    
    return result