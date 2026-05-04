import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import random

# --- Configuration & Shared Data (initialized from studio_v3.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Base model definitions
_SWARM_VISUALIZER: Any = None
_CONTEXTUAL_MEMORY: Any = None

INTEGRITY_LOG_DIR: str = ""

def initialize_integrity_verification(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, contextual_memory_module: Any):
    """Initializes global configurations for Infinite Integrity Verification Loop."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CONTEXTUAL_MEMORY, INTEGRITY_LOG_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CONTEXTUAL_MEMORY = contextual_memory_module

    INTEGRITY_LOG_DIR = os.path.join(_WORKSPACE, "integrity_verification_logs")
    os.makedirs(INTEGRITY_LOG_DIR, exist_ok=True)
    print(f"Integrity Verification initialized. Logs: {INTEGRITY_LOG_DIR}")

async def _call_llm_for_integrity_analysis(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for integrity analysis tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in integrity_verification.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "integrity_llm_call_start", f"{model} evaluating integrity task: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    try:
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on verifying system component integrity and identifying unauthorized changes."},
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
            task_id, "integrity_llm_call_end", f"{model} completed integrity task.",
            {"model": model, "response_summary": content[:100]},
            model_name=model, agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "integrity_llm_error", f"JSON decode error from {model} for integrity analysis.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": model}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "integrity_llm_error", f"Error calling {model} for integrity analysis.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model}

async def run_integrity_scan(task_id: str, component_list: List[str], scan_agent: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates a parallel integrity scan (conceptual SIMD) across system components.
    """
    print(f"AGI ({scan_agent}) initiating integrity scan for components: {component_list}...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "integrity_scan_start", f"AGI ({scan_agent}) starting integrity scan.",
        {"components": component_list},
        model_name=scan_agent, agent_role=_ALL_MODELS.get(scan_agent, "Integrity Auditor")
    )

    # Simulate RAG: Retrieve known good state hashes and security baselines.
    integrity_rag = await _CONTEXTUAL_MEMORY.query_memory_rag(task_id, "Retrieve known good integrity hashes, version snapshots, and security baselines for system components.", scan_agent)
    
    rag_context = integrity_rag.get("response", "No integrity baseline found in memory.")

    # Simulate random tampering for the scan
    tampering_detected = random.random() < 0.2 # 20% chance of detecting "tampering"
    scan_results = []
    for comp in component_list:
        status = "valid"
        if tampering_detected and random.random() < 0.3:
            status = "tampered"
        scan_results.append({"component": comp, "status": status, "last_verified": datetime.now().isoformat()})

    prompt = f"""You are an Infinite Integrity Verification Loop. Analyze the results of a (simulated) parallel integrity scan and report on the system's trustworthiness.
    
    Scan Results:
    {json.dumps(scan_results, indent=2)}
    
    Integrity Baselines & Good State (RAG output):
    ---
    {rag_context}
    ---

    Identify any unauthorized changes or suspicious deviations. Assess the severity and recommend immediate containment steps if tampering is confirmed.
    
    Output JSON: {{'integrity_compromised': bool, 'findings': list[dict], 'trust_score': float, 'analysis_summary': str, 'confidence': float}}
    """
    
    result = await _call_llm_for_integrity_analysis(
        scan_agent,
        _ALL_MODELS.get(scan_agent, "Integrity Auditor"),
        prompt,
        task_id,
        context=f"Scan of {len(component_list)} components. RAG context included."
    )

    # Manual override for consistent simulation
    result["findings"] = [r for r in scan_results if r["status"] == "tampered"]
    result["integrity_compromised"] = len(result["findings"]) > 0

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    log_filename = os.path.join(INTEGRITY_LOG_DIR, f"integrity_report_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    final_output = {
        "timestamp": datetime.now().isoformat(),
        "components_scanned": component_list,
        "integrity_report": result
    }
    with open(log_filename, "w") as f:
        json.dump(final_output, f, indent=2)
    final_output["saved_path"] = log_filename
    final_output["status"] = "success"
    print(f"Integrity report saved to {log_filename}")

    await _CONTEXTUAL_MEMORY.store_memory(task_id, scan_agent, "integrity_verification_report", final_output, "Report on the integrity and trustworthiness of system components.")
    await _SWARM_VISUALIZER.log_event(
        task_id, "integrity_scan_complete", f"Integrity scan completed. Compromised: {result.get('integrity_compromised')}",
        final_output, model_name=scan_agent, agent_role=_ALL_MODELS.get(scan_agent, "Integrity Auditor")
    )
    
    return final_output