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

THREAT_MODEL_LOG_DIR: str = ""

def initialize_threat_modeler(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, contextual_memory_module: Any):
    """Initializes global configurations for Predictive Threat Landscape Modeler."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CONTEXTUAL_MEMORY, THREAT_MODEL_LOG_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CONTEXTUAL_MEMORY = contextual_memory_module

    THREAT_MODEL_LOG_DIR = os.path.join(_WORKSPACE, "threat_model_logs")
    os.makedirs(THREAT_MODEL_LOG_DIR, exist_ok=True)
    print(f"Threat Modeler initialized. Logs: {THREAT_MODEL_LOG_DIR}")

async def _call_llm_for_threat_modeling(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for predictive threat modeling tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in threat_modeler.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "threat_model_llm_call_start", f"{model} evaluating threat modeling task: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    try:
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on generating real-time, evolving threat models based on global cyber activity and geopolitical shifts."},
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
            task_id, "threat_model_llm_call_end", f"{model} completed threat modeling task.",
            {"model": model, "response_summary": content[:100]},
            model_name=model, agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "threat_model_llm_error", f"JSON decode error from {model} for threat modeling.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": model}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "threat_model_llm_error", f"Error calling {model} for threat modeling.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model}

async def generate_threat_model(task_id: str, current_events_summary: str, geopolitical_factors: str, model_agent: str = "llama-architect") -> Dict[str, Any]:
    """
    Generates real-time, evolving threat models based on global cyber activity and geopolitical shifts.
    Conceptualizes RAG for global threat intel/news and SIMD for predictive attack path analysis.
    """
    print(f"AGI ({model_agent}) generating predictive threat model...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "threat_model_gen_start", f"AGI ({model_agent}) generating predictive threat model.",
        {"events": current_events_summary[:100], "geopolitical": geopolitical_factors[:100]},
        model_name=model_agent, agent_role=_ALL_MODELS.get(model_agent, "Threat Modeler")
    )

    # Simulate RAG: Retrieve global threat intelligence, news, security advisories.
    threat_intel_rag = await _CONTEXTUAL_MEMORY.query_memory_rag(task_id, f"Retrieve latest global cyber threat intelligence, security news, geopolitical analyses relevant to: {current_events_summary} and {geopolitical_factors}.", model_agent)
    
    rag_context = threat_intel_rag.get("response", "No specific global threat intelligence found in memory.")

    # Simulate SIMD: The LLM conceptually performs rapid predictive attack path analysis and scenario modeling.
    
    prompt = f"""You are a Predictive Threat Landscape Modeler. Your task is to generate a real-time, evolving threat model based on global cyber activity and geopolitical shifts.
    
    Summary of Current Global Cyber Events: "{current_events_summary}"
    Summary of Relevant Geopolitical Factors: "{geopolitical_factors}"
    
    Global Threat Intelligence & News (RAG output):
    ---
    {rag_context}
    ---

    Perform predictive attack path analysis and scenario modeling (SIMD-like conceptual processing).
    
    Output JSON: {{'threat_model_summary': str, 'identified_threats': list[dict], 'likely_attack_vectors': list[str], 'recommendations': list[str], 'model_confidence': float}}
    Each identified_threat dict should have: {{'threat_name': str, 'description': str, 'severity': 'low' | 'medium' | 'high' | 'critical', 'potential_impact': str}}
    """
    
    result = await _call_llm_for_threat_modeling(
        model_agent,
        _ALL_MODELS.get(model_agent, "Threat Modeler"),
        prompt,
        task_id,
        context=f"Events: {current_events_summary}, Geopolitical: {geopolitical_factors}, RAG: {rag_context}"
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    log_filename = os.path.join(THREAT_MODEL_LOG_DIR, f"threat_model_gen_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    final_output = {
        "timestamp": datetime.now().isoformat(),
        "input_events": current_events_summary,
        "input_geopolitical": geopolitical_factors,
        "threat_model": result
    }
    with open(log_filename, "w") as f:
        json.dump(final_output, f, indent=2)
    final_output["saved_path"] = log_filename
    final_output["status"] = "success"
    print(f"Predictive threat model saved to {log_filename}")

    await _CONTEXTUAL_MEMORY.store_memory(task_id, model_agent, "predictive_threat_model", final_output, "Generated predictive threat model based on global events.")
    await _SWARM_VISUALIZER.log_event(
        task_id, "threat_model_gen_complete", f"Predictive threat model generated. Identified threats: {len(result.get('identified_threats', []))}",
        final_output, model_name=model_agent, agent_role=_ALL_MODELS.get(model_agent, "Threat Modeler")
    )
    
    return final_output
