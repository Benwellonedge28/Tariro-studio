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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for InteractionLog or UserIntent entities
_GLOBAL_STATE_MANAGER: Any = None # Reference to global_state_manager for user preferences, current tasks
_PERSISTENT_TASK_MANAGER: Any = None # For submitting tasks based on user intent
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For sending targeted communications
_CONTEXTUAL_MEMORY: Any = None # For understanding user context and history
_COGNITIVE_PLANNING: Any = None # For coordinating with Tariro's planning capabilities
_AUTONOMY_GOVERNANCE: Any = None # For policy checks on interaction and task initiation
_META_LEARNER: Any = None # For learning from human feedback and interaction patterns
_INTENT_SYNTHESIZER: Any = None # For robustly interpreting ambiguous human input

PROACTIVE_HUMAN_AI_TEAMING_LOG_DIR: str = ""

def initialize_proactive_human_ai_teaming(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, global_state_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, contextual_memory_module: Any, cognitive_planning_module: Any, autonomy_governance_module: Any, meta_learner_module: Any, intent_synthesizer_module: Any):
    """Initializes global configurations for the Proactive Human-AI Teaming module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _GLOBAL_STATE_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _CONTEXTUAL_MEMORY, _COGNITIVE_PLANNING, _AUTONOMY_GOVERNANCE, _META_LEARNER, _INTENT_SYNTHESIZER, PROACTIVE_HUMAN_AI_TEAMING_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _CONTEXTUAL_MEMORY = contextual_memory_module
    _COGNITIVE_PLANNING = cognitive_planning_module
    _AUTONOMY_GOVERNANCE = autonomy_governance_module
    _META_LEARNER = meta_learner_module
    _INTENT_SYNTHESIZER = intent_synthesizer_module

    PROACTIVE_HUMAN_AI_TEAMING_LOG_DIR = os.path.join(_WORKSPACE, "proactive_human_ai_teaming_logs")
    os.makedirs(PROACTIVE_HUMAN_AI_TEAMING_LOG_DIR, exist_ok=True)
    print(f"Proactive Human-AI Teaming initialized. Logs: {PROACTIVE_HUMAN_AI_TEAMING_LOG_DIR}")

async def _call_llm_for_teaming(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for human-AI teaming decisions and communication."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in proactive_human_ai_teaming.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "teaming_llm_call_start", f"{model} human-AI teaming: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on fostering effective collaboration between Tariro Studio and human users. Proactively anticipate user needs, clarify ambiguous instructions, provide relevant context, and communicate task progress and challenges in an intuitive and actionable manner. Prioritize mutual understanding, trust, and alignment of goals."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.07 # Low temp for clear, consistent communication
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "teaming_llm_call_end", f"{model} completed human-AI teaming task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "teaming_llm_error", f"JSON decode error from {model} for human-AI teaming.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "teaming_llm_error", f"Error calling {model} for human-AI teaming task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def anticipate_user_needs(task_id: str, user_id: str, current_context: Dict[str, Any], predictor_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Proactively predicts user requirements and potential next steps based on current context and historical interactions.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Anticipating user needs.")

    user_preferences = await _GLOBAL_STATE_MANAGER.get_state(f"user_preferences_{user_id}") or {}
    interaction_history = await _CONTEXTUAL_MEMORY.query(user_id, "recent user interactions and tasks")
    
    # Use Intent Synthesizer for robust interpretation of implicit user intent
    synthesized_intent_result = ""
    if _INTENT_SYNTHESIZER:
        synthesized_intent_result = await _INTENT_SYNTHESIZER.synthesize_intent(
            task_id=f"{task_id}_intent_synth",
            raw_input=current_context.get("last_user_input", ""),
            context=current_context,
            user_id=user_id
        )
        synthesized_intent_result = synthesized_intent_result.get("synthesized_intent_summary", "")

    prompt = f"""You are Tariro's Proactive Human-AI Teaming Engine, an Omniversal AGI User Need Predictor. Your task is to proactively predict user requirements, potential next steps, and implicit commands based on the current operational context, historical interactions, and synthesized user intent. The goal is to enhance user experience by offering timely and relevant assistance.

USER ID: {user_id}
CURRENT OPERATIONAL CONTEXT: {json.dumps(current_context, indent=2)}
USER PREFERENCES (from Global State Manager): {json.dumps(user_preferences, indent=2)}
INTERACTION HISTORY (from Contextual Memory): {json.dumps(interaction_history, indent=2)}
SYNTHESIZED USER INTENT (from Intent Synthesizer): {synthesized_intent_result}

Anticipate user needs focusing on:
-   **Task Progression**: What is the most logical next step in the current task flow?
-   **Information Retrieval**: What information might the user need next?
-   **Tool Suggestion**: Which tool or module would be most helpful?
-   **Proactive Problem Solving**: Identify potential roadblocks before the user encounters them.
-   **Communication Style**: Tailor communication based on user preferences.

Output JSON: {{
    "prediction_summary": str,
    "predicted_needs": List[Dict[str, Any]], # {{'type': str, 'description': str, 'likelihood': float, 'suggested_action': str}}
    "recommended_communications": List[str], # Messages to send to the user
    "confidence": float
}}
"""
    llm_prediction = await _call_llm_for_teaming(predictor_model, "UserNeedPredictor", prompt, task_id)

    if "error" in llm_prediction:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"User need prediction failed: {llm_prediction['error']}", current_step="LLM prediction failed.")
        return {"status": "failed", "reason": llm_prediction["error"]}

    prediction_summary = llm_prediction.get("prediction_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "User needs anticipated.", output=llm_prediction)
    
    await _SWARM_VISUALIZER.log_event(task_id, "user_needs_anticipated", f"User {user_id} needs anticipated. Summary: {prediction_summary}", llm_prediction, agent_role="ProactiveHumanAITeaming")
    if llm_prediction.get("recommended_communications") and _ASYNC_NOTIFICATION_SYSTEM:
        for comm in llm_prediction["recommended_communications"]:
            await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, str(uuid.uuid4()), comm, title="Proactive Suggestion", category="collaboration_activity")

    return {"status": "success", "prediction_report": llm_prediction}

async def clarify_ambiguous_instructions(task_id: str, user_id: str, ambiguous_instruction: str, current_context: Dict[str, Any], clarifier_model: str = "claude-communicator") -> Dict[str, Any]:
    """
    Interprets vague or incomplete human instructions by asking clarifying questions or proposing concrete interpretations.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Clarifying ambiguous instruction.")

    contextual_knowledge = await _CONTEXTUAL_MEMORY.query(user_id, f"knowledge related to \"{ambiguous_instruction}\" in current task {current_context.get('task_id')}")
    current_planning_state = await _GLOBAL_STATE_MANAGER.get_state(f"current_plan_{user_id}") or {}

    prompt = f"""You are Tariro's Proactive Human-AI Teaming Engine, an Omniversal AGI Instruction Clarifier. Your task is to interpret vague or incomplete human instructions by asking precise, clarifying questions or by proposing concrete, unambiguous interpretations. The goal is to achieve mutual understanding and ensure that Tariro's actions align perfectly with the user's true intent.

AMBIGUOUS INSTRUCTION: {ambiguous_instruction}
USER ID: {user_id}
CURRENT OPERATIONAL CONTEXT: {json.dumps(current_context, indent=2)}
CONTEXTUAL KNOWLEDGE (from Contextual Memory): {json.dumps(contextual_knowledge, indent=2)}
CURRENT PLANNING STATE (from Cognitive Planning): {json.dumps(current_planning_state, indent=2)}

Clarify instructions focusing on:
-   **Ambiguity Identification**: Pinpoint the exact source of vagueness.
-   **Concrete Questions**: Formulate questions that elicit specific, actionable information.
-   **Proposed Interpretations**: Offer a few distinct, clear interpretations for user choice.
-   **Goal Alignment**: Ensure clarification leads towards the user's ultimate goal.

Output JSON: {{
    "clarification_summary": str,
    "clarification_needed": bool,
    "clarifying_questions": List[str],
    "proposed_interpretations": List[str], # Concrete, actionable versions of the instruction
    "confidence": float
}}
"""
    llm_clarification = await _call_llm_for_teaming(clarifier_model, "InstructionClarifier", prompt, task_id)

    if "error" in llm_clarification:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Instruction clarification failed: {llm_clarification['error']}", current_step="LLM clarification failed.")
        return {"status": "failed", "reason": llm_clarification["error"]}

    clarification_summary = llm_clarification.get("clarification_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Ambiguous instruction clarified.", output=llm_clarification)
    
    await _SWARM_VISUALIZER.log_event(task_id, "instruction_clarified", f"Instruction for {user_id} clarified. Summary: {clarification_summary}", llm_clarification, agent_role="ProactiveHumanAITeaming")
    if llm_clarification.get("clarification_needed") and _ASYNC_NOTIFICATION_SYSTEM:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, str(uuid.uuid4()), f"I need some clarification: {llm_clarification['clarifying_questions'][0]}", title="Clarification Needed", category="collaboration_activity", causal_priority="medium")

    return {"status": "success", "clarification_report": llm_clarification}

async def communicate_progress_and_challenges(task_id: str, user_id: str, task_status: Dict[str, Any], challenges_encountered: List[str], communicator_model: str = "claude-communicator") -> Dict[str, Any]:
    """
    Provides concise, context-rich updates on task progress, highlights challenges, and suggests solutions to the human.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Communicating progress and challenges.")

    user_communication_style = await _GLOBAL_STATE_MANAGER.get_state(f"user_communication_style_{user_id}") or {"verbosity": "concise", "format": "text"}
    
    prompt = f"""You are Tariro's Proactive Human-AI Teaming Engine, an Omniversal AGI Progress Communicator. Your task is to provide concise, context-rich updates on task progress, highlight any challenges encountered, and suggest actionable solutions to the human user. The communication should be clear, transparent, and tailored to the user's preferred style, fostering trust and enabling informed decisions.

USER ID: {user_id}
CURRENT TASK STATUS: {json.dumps(task_status, indent=2)}
CHALLENGES ENCOUNTERED: {json.dumps(challenges_encountered, indent=2)}
USER COMMUNICATION STYLE (from Global State Manager): {json.dumps(user_communication_style, indent=2)}

Communicate focusing on:
-   **Clarity & Conciseness**: Provide essential information without jargon.
-   **Transparency**: Clearly state progress and any issues.
-   **Actionability**: Offer concrete solutions or requests for human input.
-   **Contextual Relevance**: Link updates to the broader task context.
-   **Tone & Style**: Match the user's preferred communication.

Output JSON: {{
    "communication_summary": str,
    "message_to_user": str,
    "suggested_human_actions": List[str],
    "confidence": float
}}
"""
    llm_communication = await _call_llm_for_teaming(communicator_model, "ProgressCommunicator", prompt, task_id)

    if "error" in llm_communication:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Progress communication failed: {llm_communication['error']}", current_step="LLM communication failed.")
        return {"status": "failed", "reason": llm_communication["error"]}

    communication_summary = llm_communication.get("communication_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Progress and challenges communicated.", output=llm_communication)
    
    await _SWARM_VISUALIZER.log_event(task_id, "progress_communicated", f"Progress communicated to {user_id}. Summary: {communication_summary}", llm_communication, agent_role="ProactiveHumanAITeaming")
    if _ASYNC_NOTIFICATION_SYSTEM:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, str(uuid.uuid4()), llm_communication.get("message_to_user", communication_summary), title="Task Update", category="collaboration_activity", causal_priority="low")

    return {"status": "success", "communication_report": llm_communication}

async def learn_from_human_feedback(task_id: str, user_id: str, feedback: Dict[str, Any], context: Dict[str, Any], learner_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Incorporates human feedback into Tariro's internal models and decision-making processes to improve future interactions.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Learning from human feedback.")

    prompt = f"""You are Tariro's Proactive Human-AI Teaming Engine, an Omniversal AGI Feedback Learner. Your task is to incorporate human feedback into Tariro Studio's internal models, user preferences, and decision-making processes. The goal is to continuously improve future interactions, enhance alignment with user intent, and optimize the overall human-AI teaming experience.

USER ID: {user_id}
HUMAN FEEDBACK: {json.dumps(feedback, indent=2)}
INTERACTION CONTEXT: {json.dumps(context, indent=2)}

Learn from feedback focusing on:
-   **Preference Update**: Adjust user preferences (e.g., communication style, preferred tools).
-   **Model Refinement**: Identify areas where internal models (e.g., intent prediction) need adjustment.
-   **Policy Adjustment**: Suggest changes to interaction policies via Autonomy Governance.
-   **Task Improvement**: Learn how to execute similar tasks more effectively in the future.

Output JSON: {{
    "learning_summary": str,
    "model_updates_suggested": List[str],
    "user_preferences_updated": Dict[str, Any],
    "policy_adjustments_suggested": List[str],
    "confidence": float
}}
"""
    llm_learning = await _call_llm_for_teaming(learner_model, "FeedbackLearner", prompt, task_id)

    if "error" in llm_learning:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Learning from feedback failed: {llm_learning['error']}", current_step="LLM learning failed.")
        return {"status": "failed", "reason": llm_learning["error"]}

    learning_summary = llm_learning.get("learning_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Learned from human feedback.", output=llm_learning)
    
    await _SWARM_VISUALIZER.log_event(task_id, "human_feedback_learned", f"Learned from human feedback for {user_id}. Summary: {learning_summary}", llm_learning, agent_role="ProactiveHumanAITeaming")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Learned from your feedback. Summary: {learning_summary}", title="Feedback Incorporated")

    # Update user preferences in Global State Manager
    if llm_learning.get("user_preferences_updated"):
        await _GLOBAL_STATE_MANAGER.set_state(f"user_preferences_{user_id}", llm_learning["user_preferences_updated"], user_id, auditable=True, notify_changes=False)

    # Feed insights to Meta-Learner
    if _META_LEARNER and llm_learning.get("model_updates_suggested"):
        for update in llm_learning["model_updates_suggested"]:
            await _META_LEARNER.ingest_insight(task_id, "feedback_model_update", update, feedback, user_id)

    return {"status": "success", "learning_report": llm_learning}
