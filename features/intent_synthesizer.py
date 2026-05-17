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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for UserIntent or ClarificationRequest entities
_PERSISTENT_TASK_MANAGER: Any = None # For submitting intent clarification tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on critical intent misinterpretations
_CONTEXTUAL_MEMORY: Any = None # For retrieving historical interactions and user preferences
_GLOBAL_STATE_MANAGER: Any = None # For storing current user goals, world model, active tasks
_PROACTIVE_HUMAN_AI_TEAMING: Any = None # For requesting clarification from human users
_META_LEARNER: Any = None # For learning from intent synthesis successes/failures and human feedback
_DYNAMIC_POLICY_SYNTHESIS: Any = None # For generating policies on how to handle ambiguous intent

INTENT_SYNTHESIZER_LOG_DIR: str = ""

def initialize_intent_synthesizer(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, contextual_memory_module: Any, global_state_manager_module: Any, proactive_human_ai_teaming_module: Any, meta_learner_module: Any, dynamic_policy_synthesis_module: Any):
    """Initializes global configurations for the Intent Synthesizer module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _CONTEXTUAL_MEMORY, _GLOBAL_STATE_MANAGER, _PROACTIVE_HUMAN_AI_TEAMING, _META_LEARNER, _DYNAMIC_POLICY_SYNTHESIS, INTENT_SYNTHESIZER_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _CONTEXTUAL_MEMORY = contextual_memory_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _PROACTIVE_HUMAN_AI_TEAMING = proactive_human_ai_teaming_module
    _META_LEARNER = meta_learner_module
    _DYNAMIC_POLICY_SYNTHESIS = dynamic_policy_synthesis_module

    INTENT_SYNTHESIZER_LOG_DIR = os.path.join(_WORKSPACE, "intent_synthesizer_logs")
    os.makedirs(INTENT_SYNTHESIZER_LOG_DIR, exist_ok=True)
    print(f"Intent Synthesizer initialized. Logs: {INTENT_SYNTHESIZER_LOG_DIR}")

async def _call_llm_for_intent_synthesis(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for intent interpretation and synthesis decisions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in intent_synthesizer.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "intent_llm_call_start", f"{model} intent synthesis: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on accurately interpreting implicit and explicit user intent from ambiguous natural language inputs. Synthesize a clear, actionable understanding of what the user wants, including their goals, preferences, and any constraints. Identify ambiguities, potential misunderstandings, and propose clarification strategies. Ensure synthesized intent is aligned with ethical guidelines and operational policies."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.08 # Balanced for accurate interpretation and ambiguity detection
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "intent_llm_call_end", f"{model} completed intent synthesis task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "intent_llm_error", f"JSON decode error from {model} for intent synthesis.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "intent_llm_error", f"Error calling {model} for intent synthesis task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def synthesize_intent(task_id: str, raw_input: str, user_id: str = "Tariro_System", context: Dict[str, Any] = None, synthesizer_model: str = "intent-synthesizer") -> Dict[str, Any]:
    """
    Interprets ambiguous natural language inputs to synthesize a clear, actionable understanding of user intent.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Synthesizing user intent.")

    if context is None: context = {}
    user_preferences = await _GLOBAL_STATE_MANAGER.get_state(f"user_preferences_{user_id}") or {}
    historical_interactions = await _CONTEXTUAL_MEMORY.query(user_id, f"recent interactions with {user_id}")

    prompt = f"""You are Tariro's Intent Synthesizer, an Omniversal AGI Intent Interpreter. Your task is to accurately interpret implicit and explicit user intent from potentially ambiguous natural language inputs, taking into account current context, user preferences, and historical interactions. Synthesize a clear, actionable understanding of what the user wants, including their goals, preferences, and any constraints. Identify ambiguities or potential misunderstandings and propose clarification strategies.

RAW USER INPUT: {raw_input}
USER ID: {user_id}
CURRENT CONTEXT: {json.dumps(context, indent=2)}
USER PREFERENCES (from Global State Manager): {json.dumps(user_preferences, indent=2)}
HISTORICAL INTERACTIONS (from Contextual Memory): {json.dumps(historical_interactions, indent=2)}

Synthesize intent focusing on:
-   **Core Goal Extraction**: What is the primary objective?
-   **Parameter Identification**: Extract all relevant parameters, constraints, and conditions.
-   **Ambiguity Detection**: Identify any parts of the input that are unclear or open to multiple interpretations.
-   **Clarification Strategy**: Propose specific questions to resolve ambiguities or alternative interpretations.
-   **Actionable Output**: The synthesized intent should directly inform subsequent actions or module calls.

Output JSON: {{
    "synthesized_intent_summary": str,
    "core_goal": str,
    "action_type": str, # e.g., 'code_generation', 'data_analysis', 'system_query', 'multi_modal_generation'
    "parameters": Dict[str, Any],
    "ambiguities_detected": bool,
    "clarifying_questions": List[str],
    "alternative_interpretations": List[Dict[str, Any]], # {{'summary': str, 'confidence': float}}
    "confidence": float
}}
"""
    llm_intent = await _call_llm_for_intent_synthesis(synthesizer_model, "IntentInterpreter", prompt, task_id)

    if "error" in llm_intent:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Intent synthesis failed: {llm_intent['error']}", current_step="LLM interpretation failed.")
        return {"status": "failed", "reason": llm_intent["error"]}

    intent_summary = llm_intent.get("synthesized_intent_summary", "No summary.")
    ambiguities_detected = llm_intent.get("ambiguities_detected", False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "User intent synthesized.", output=llm_intent)
    
    await _SWARM_VISUALIZER.log_event(task_id, "intent_synthesized", f"User intent synthesized. Summary: {intent_summary}", llm_intent, agent_role="IntentSynthesizer")
    if ambiguities_detected and _PROACTIVE_HUMAN_AI_TEAMING:
        await _PROACTIVE_HUMAN_AI_TEAMING.clarify_ambiguous_instructions(
            task_id=f"{task_id}_clarify",
            user_id=user_id,
            ambiguous_instruction=raw_input,
            current_context=context # Pass the full context
        )
    elif ambiguities_detected and _ASYNC_NOTIFICATION_SYSTEM:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
            user_id, task_id, f"I'm a bit unclear on your request: {llm_intent.get('clarifying_questions', ['Could you provide more details?'])[0]}",
            title="Clarification Needed", causal_priority="medium"
        )

    # Store synthesized intent in CRUD Manager
    await _CRUD_MANAGER.create_entity("UserIntent", {"id": task_id, "user_id": user_id, "raw_input": raw_input, "synthesized_intent": llm_intent, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "intent_synthesis", intent_summary, llm_intent, user_id)

    return {"status": "success", "synthesized_intent": llm_intent}

async def identify_intent_conflicts(task_id: str, new_intent: Dict[str, Any], user_id: str = "Tariro_System", conflict_detector_model: str = "arbiter-model") -> Dict[str, Any]:
    """
    Detects conflicts or inconsistencies between a newly synthesized intent and active goals,
    policies, or known constraints.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Identifying intent conflicts.")

    active_goals = await _GLOBAL_STATE_MANAGER.get_state(f"active_goals_{user_id}") or {}
    active_policies = await _GLOBAL_STATE_MANAGER.get_state("active_policies") or {}
    known_constraints = await _GLOBAL_STATE_MANAGER.get_state("system_constraints") or {}
    
    prompt = f"""You are Tariro's Intent Synthesizer, an Omniversal AGI Conflict Detector. Your task is to detect conflicts or inconsistencies between a newly synthesized user intent and Tariro Studio's active goals, operational policies, or known system constraints. Identify potential ethical violations, security risks, or resource conflicts that could arise if this new intent is executed.

NEWLY SYNTHESIZED INTENT: {json.dumps(new_intent, indent=2)}
USER ID: {user_id}
ACTIVE GOALS (from Global State Manager): {json.dumps(active_goals, indent=2)}
ACTIVE POLICIES (from Global State Manager): {json.dumps(active_policies, indent=2)}
KNOWN SYSTEM CONSTRAINTS (from Global State Manager): {json.dumps(known_constraints, indent=2)}

Identify conflicts focusing on:
-   **Goal Contradiction**: Does the new intent contradict existing, higher-priority goals?
-   **Policy Violation**: Does it violate any operational, ethical, or security policies?
-   **Resource Constraints**: Does executing this intent exceed available resources?
-   **Ethical Implications**: Are there any unintended ethical consequences?
-   **Security Risks**: Does it introduce new vulnerabilities or attack vectors?

Output JSON: {{
    "conflict_detection_summary": str,
    "conflicts_found": bool,
    "identified_conflicts": List[Dict[str, Any]], # {{'type': str, 'description': str, 'severity': str, 'remediation_suggestions': List[str]}}
    "human_review_recommended": bool,
    "confidence": float
}}
"""
    llm_conflicts = await _call_llm_for_intent_synthesis(conflict_detector_model, "ConflictDetector", prompt, task_id)

    if "error" in llm_conflicts:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Intent conflict detection failed: {llm_conflicts['error']}", current_step="LLM detection failed.")
        return {"status": "failed", "reason": llm_conflicts["error"]}

    conflict_summary = llm_conflicts.get("conflict_detection_summary", "No summary.")
    conflicts_found = llm_conflicts.get("conflicts_found", False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Intent conflicts identified.", output=llm_conflicts)
    
    await _SWARM_VISUALIZER.log_event(task_id, "intent_conflicts_identified", f"Intent conflicts identified. Summary: {conflict_summary}", llm_conflicts, agent_role="IntentSynthesizer")
    if conflicts_found:
        if llm_conflicts.get("human_review_recommended", False):
            await _PROACTIVE_HUMAN_AI_TEAMING.communicate_progress_and_challenges(
                task_id=f"{task_id}_human_review",
                user_id=user_id,
                task_status=new_intent,
                challenges_encountered=[f"Conflict with existing goals/policies: {conflict_summary}"]
            )
        elif _ASYNC_NOTIFICATION_SYSTEM:
            await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Intent conflicts detected: {conflict_summary}", title="Intent Conflict Alert", causal_priority="critical")

    # Store conflict report in CRUD Manager
    await _CRUD_MANAGER.create_entity("IntentConflictReport", {"id": task_id, "user_id": user_id, "new_intent": new_intent, "conflict_report": llm_conflicts, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "intent_conflict_detection", conflict_summary, llm_conflicts, user_id)

    return {"status": "success", "conflict_report": llm_conflicts}
