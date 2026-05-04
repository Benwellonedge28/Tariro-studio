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

COGNITIVE_ALLOCATION_LOG_DIR: str = ""

def initialize_cognitive_allocator(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, contextual_memory_module: Any, crud_manager_module: Any):
    """Initializes global configurations for Dynamic Cognitive Resource Allocation Orchestrator."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CONTEXTUAL_MEMORY, _CRUD_MANAGER, COGNITIVE_ALLOCATION_LOG_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CONTEXTUAL_MEMORY = contextual_memory_module
    _CRUD_MANAGER = crud_manager_module

    COGNITIVE_ALLOCATION_LOG_DIR = os.path.join(_WORKSPACE, "cognitive_allocation_logs")
    os.makedirs(COGNITIVE_ALLOCATION_LOG_DIR, exist_ok=True)
    print(f"Cognitive Allocator initialized. Logs: {COGNITIVE_ALLOCATION_LOG_DIR}")

async def _call_llm_for_cognitive_allocation(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for cognitive resource allocation tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in cognitive_allocator.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "cognitive_llm_call_start", f"{model} evaluating cognitive allocation: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    try:
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on intelligent allocation of processing power, memory, and attention."},
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
            task_id, "cognitive_llm_call_end", f"{model} completed cognitive allocation task.",
            {"model": model, "response_summary": content[:100]},
            model_name=model, agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "cognitive_llm_error", f"JSON decode error from {model} for cognitive allocation.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": model}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "cognitive_llm_error", f"Error calling {model} for cognitive allocation.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model}

async def analyze_task_cognitive_load(task_id: str, task_description: str, current_priority: str, current_context: str, allocator_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates assessing the cognitive load (processing, memory, attention) required for a given task.
    """
    print(f"AGI ({allocator_model}) analyzing cognitive load for task: {task_description[:50]}...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "cognitive_load_analysis_start", f"AGI ({allocator_model}) analyzing cognitive load.",
        {"task_summary": task_description[:100], "priority": current_priority}, model_name=allocator_model, agent_role=_ALL_MODELS.get(allocator_model, "Cognitive Orchestrator")
    )

    prompt = f"""You are an AGI responsible for self-management of cognitive resources.
    Analyze the following task description and its priority to estimate the required cognitive load.
    
    Task Description: "{task_description}"
    Current Priority: "{current_priority}"
    Current Operational Context: "{current_context}"
    
    Estimate the following:
    - **Processing Power Needed:** (e.g., "high", "medium", "low", "minimal")
    - **Memory Footprint:** (e.g., "extensive_context_retrieval", "moderate_working_memory", "minimal_transient_data")
    - **Attention Span/Focus:** (e.g., "continuous_monitoring", "periodic_checks", "background_processing")
    - **Suggested Models/Specialists:** Which models/roles are best suited given the task type.
    
    Output JSON: {{'processing_power': str, 'memory_footprint': str, 'attention_span': str, 'suggested_models': list[str], 'rationale': str}}
    """
    
    result = await _call_llm_for_cognitive_allocation(
        allocator_model,
        _ALL_MODELS.get(allocator_model, "Cognitive Orchestrator"),
        prompt,
        task_id,
        context=f"Task: {task_description}, Priority: {current_priority}, Context: {current_context}"
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    log_filename = os.path.join(COGNITIVE_ALLOCATION_LOG_DIR, f"cognitive_load_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump(result, f, indent=2)
    result["saved_path"] = log_filename
    result["status"] = "success"
    print(f"Cognitive load analysis saved to {log_filename}")

    await _CONTEXTUAL_MEMORY.store_memory(task_id, allocator_model, "cognitive_load_analysis", result, "Analysis of cognitive load for the task.")
    await _SWARM_VISUALIZER.log_event(
        task_id, "cognitive_load_analysis_complete", f"Cognitive load analyzed for: {task_description[:50]}",
        result, model_name=allocator_model, agent_role=_ALL_MODELS.get(allocator_model, "Cognitive Orchestrator")
    )
    
    return result

async def allocate_cognitive_resources(task_id: str, task_description: str, cognitive_load_analysis: Dict[str, Any], current_system_load: str, allocator_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates dynamic allocation of processing power, memory, and attention based on load analysis.
    """
    print(f"AGI ({allocator_model}) allocating cognitive resources for task: {task_description[:50]}...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "cognitive_allocation_start", f"AGI ({allocator_model}) allocating cognitive resources.",
        {"task_summary": task_description[:100], "current_load": current_system_load}, model_name=allocator_model, agent_role=_ALL_MODELS.get(allocator_model, "Cognitive Orchestrator")
    )

    prompt = f"""You are a dynamic cognitive resource allocation orchestrator. Based on the task description, the cognitive load analysis, and the current system load, propose an optimal allocation strategy for:
    - **Models to engage**: Which specific AGI models should actively work on this task.
    - **Parallelism/Concurrency**: How many sub-tasks can run in parallel (SIMD-like).
    - **Contextual Memory Depth**: How much historical/external context should be loaded into active working memory.
    - **Monitoring Intensity**: How frequently should this task's progress and resource usage be monitored.
    - **Dynamic Configuration Adjustments**: Any adjustments to `ALL_MODELS` roles if a specialist model is needed.
    
    Task Description: "{task_description}"
    Cognitive Load Analysis:
    {json.dumps(cognitive_load_analysis, indent=2)}
    Current System Load: "{current_system_load}"
    
    Output JSON: {{'models_engaged': list[str], 'parallelism_level': str, 'memory_depth': str, 'monitoring_intensity': str, 'suggested_config_changes': dict, 'rationale': str}}
    'suggested_config_changes' should be a dictionary of model:role pairs if new specialists are needed or roles redefined.
    """
    
    result = await _call_llm_for_cognitive_allocation(
        allocator_model,
        _ALL_MODELS.get(allocator_model, "Cognitive Orchestrator"),
        prompt,
        task_id,
        context=f"Task: {task_description}, Load Analysis: {cognitive_load_analysis}, System Load: {current_system_load}"
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    log_filename = os.path.join(COGNITIVE_ALLOCATION_LOG_DIR, f"cognitive_allocation_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump(result, f, indent=2)
    result["saved_path"] = log_filename
    result["status"] = "success"
    print(f"Cognitive resource allocation saved to {log_filename}")

    await _CONTEXTUAL_MEMORY.store_memory(task_id, allocator_model, "cognitive_resource_allocation", result, "Dynamic allocation plan for cognitive resources.")
    await _SWARM_VISUALIZER.log_event(
        task_id, "cognitive_allocation_complete", f"Cognitive resources allocated for: {task_description[:50]}",
        result, model_name=allocator_model, agent_role=_ALL_MODELS.get(allocator_model, "Cognitive Orchestrator")
    )
    
    return result
