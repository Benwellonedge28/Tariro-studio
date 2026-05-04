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

ALIGNMENT_LOG_DIR: str = ""

def initialize_human_agi_alignment(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, contextual_memory_module: Any):
    """Initializes global configurations for Human-AGI Intent Alignment."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CONTEXTUAL_MEMORY, ALIGNMENT_LOG_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CONTEXTUAL_MEMORY = contextual_memory_module

    ALIGNMENT_LOG_DIR = os.path.join(_WORKSPACE, "alignment_logs")
    os.makedirs(ALIGNMENT_LOG_DIR, exist_ok=True)
    print(f"Human-AGI Alignment initialized. Logs: {ALIGNMENT_LOG_DIR}")

async def _call_llm_for_alignment(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for intent alignment and refinement tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in human_agi_alignment.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "alignment_llm_call_start", f"{model} evaluating alignment task: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    try:
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on clarifying human intent and refining task specifications."},
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
            task_id, "alignment_llm_call_end", f"{model} completed alignment task.",
            {"model": model, "response_summary": content[:100]},
            model_name=model, agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "alignment_llm_error", f"JSON decode error from {model} for alignment task.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": model}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "alignment_llm_error", f"Error calling {model} for alignment task.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model}


async def clarify_intent(task_id: str, human_intent: str, a_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates an AGI asking clarifying questions about a human's initial, potentially ambiguous, intent.
    """
    print(f"AGI ({a_model}) clarifying intent for: {human_intent[:50]}...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "intent_clarification_start", f"AGI ({a_model}) clarifying human intent.",
        {"human_intent": human_intent}, model_name=a_model, agent_role=_ALL_MODELS.get(a_model, "AGI Aligner")
    )

    prompt = f"""You are an AGI intent clarification agent.
    A human has provided the following initial intent: "{human_intent}".
    Your goal is to ask concise, insightful clarifying questions to remove ambiguity and ensure a precise understanding of their goals.
    Consider potential interpretations, missing details, or conflicting information.
    Output JSON: {{'clarifying_questions': list[str], 'identified_ambiguities': list[str], 'suggested_next_step': str}}
    """
    
    result = await _call_llm_for_alignment(
        a_model,
        _ALL_MODELS.get(a_model, "AGI Aligner"),
        prompt,
        task_id,
        context=f"Human intent: {human_intent}"
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    log_filename = os.path.join(ALIGNMENT_LOG_DIR, f"clarify_intent_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump(result, f, indent=2)
    result["saved_path"] = log_filename
    result["status"] = "success"
    print(f"Intent clarification analysis saved to {log_filename}")

    await _CONTEXTUAL_MEMORY.store_memory(task_id, a_model, "clarified_intent_questions", result.get("clarifying_questions", []), "Clarifying questions generated for human intent.")
    
    return result

async def refine_task_spec(task_id: str, initial_intent: str, clarifying_dialogue: str, a_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates an AGI refining a task specification based on initial intent and a clarifying dialogue.
    """
    print(f"AGI ({a_model}) refining task spec for: {initial_intent[:50]}...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "task_refinement_start", f"AGI ({a_model}) refining task specification.",
        {"initial_intent": initial_intent, "dialogue_summary": clarifying_dialogue[:100]},
        model_name=a_model, agent_role=_ALL_MODELS.get(a_model, "AGI Aligner")
    )

    prompt = f"""You are an AGI task refinement agent.
    Based on the following initial human intent and subsequent clarifying dialogue,
    provide a precise, unambiguous, and executable task specification for an AGI swarm.
    The refined specification should eliminate ambiguities and clearly define objectives and constraints.
    Output JSON: {{'refined_task_spec': str, 'confidence_score': float, 'rationale': str}}
    
    Initial Human Intent: "{initial_intent}"
    Clarifying Dialogue:
    ---
    {clarifying_dialogue}
    ---
    """
    
    result = await _call_llm_for_alignment(
        a_model,
        _ALL_MODELS.get(a_model, "AGI Aligner"),
        prompt,
        task_id,
        context=f"Initial intent: {initial_intent}\nDialogue: {clarifying_dialogue}"
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    log_filename = os.path.join(ALIGNMENT_LOG_DIR, f"refined_task_spec_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump(result, f, indent=2)
    result["saved_path"] = log_filename
    result["status"] = "success"
    print(f"Refined task specification analysis saved to {log_filename}")

    await _CONTEXTUAL_MEMORY.store_memory(task_id, a_model, "refined_task_specification", result.get("refined_task_spec", ""), "Refined task specification after dialogue.")
    
    return result
