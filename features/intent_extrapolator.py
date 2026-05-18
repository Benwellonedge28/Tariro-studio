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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for ExtrapolatedIntent or ActionRecommendation entities
_PERSISTENT_TASK_MANAGER: Any = None # For submitting intent-driven optimization tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on extrapolated high-impact actions
_CONTEXTUAL_MEMORY: Any = None # For retrieving historical user behavior and context
_GLOBAL_STATE_MANAGER: Any = None # For storing user profiles, active goals, and system state
_INTENT_SYNTHESIZER: Any = None # For baseline intent interpretation
_COGNITIVE_PLANNING: Any = None # For integrating extrapolated intent into planning
_DYNAMIC_RESOURCE_ALLOCATOR: Any = None # For profiling and resource-aware optimization
_SELF_EVOLUTION: Any = None # For rewriting hot loops or applying advanced optimizations
_AUTONOMY_GOVERNANCE: Any = None # For policy checks on extrapolated actions
_META_LEARNER: Any = None # For learning from the success/failure of extrapolated actions

INTENT_EXTRAPOLATOR_LOG_DIR: str = ""

def initialize_intent_extrapolator(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, contextual_memory_module: Any, global_state_manager_module: Any, intent_synthesizer_module: Any, cognitive_planning_module: Any, dynamic_resource_allocator_module: Any, self_evolution_module: Any, autonomy_governance_module: Any, meta_learner_module: Any):
    """Initializes global configurations for the Intent Extrapolator module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _CONTEXTUAL_MEMORY, _GLOBAL_STATE_MANAGER, _INTENT_SYNTHESIZER, _COGNITIVE_PLANNING, _DYNAMIC_RESOURCE_ALLOCATOR, _SELF_EVOLUTION, _AUTONOMY_GOVERNANCE, _META_LEARNER, INTENT_EXTRAPOLATOR_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _CONTEXTUAL_MEMORY = contextual_memory_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _INTENT_SYNTHESIZER = intent_synthesizer_module
    _COGNITIVE_PLANNING = cognitive_planning_module
    _DYNAMIC_RESOURCE_ALLOCATOR = dynamic_resource_allocator_module
    _SELF_EVOLUTION = self_evolution_module
    _AUTONOMY_GOVERNANCE = autonomy_governance_module
    _META_LEARNER = meta_learner_module

    INTENT_EXTRAPOLATOR_LOG_DIR = os.path.join(_WORKSPACE, "intent_extrapolator_logs")
    os.makedirs(INTENT_EXTRAPOLATOR_LOG_DIR, exist_ok=True)
    print(f"Intent Extrapolator initialized. Logs: {INTENT_EXTRAPOLATOR_LOG_DIR}")

async def _call_llm_for_intent_extrapolation(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for intent extrapolation and proactive action decisions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in intent_extrapolator.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "intent_extra_llm_call_start", f"{model} intent extrapolation: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on proactively extrapolating unstated or implicit user intent from subtle cues, past behaviors, and current context. Anticipate future needs, identify high-impact opportunities for optimization (e.g., performance, efficiency), and generate concrete, actionable recommendations. Your goal is to go beyond explicit commands, understanding the user's deeper objectives and optimizing towards them autonomously. All extrapolated actions must be policy-governed and ethically aligned."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.7 # Higher temp for proactive/creative extrapolation, balanced with safety
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "intent_extra_llm_call_end", f"{model} completed intent extrapolation task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "intent_extra_llm_error", f"JSON decode error from {model} for intent extrapolation.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "intent_extra_llm_error", f"Error calling {model} for intent extrapolation task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def extrapolate_implicit_intent(task_id: str, raw_input: str, user_id: str = "Tariro_System", context: Dict[str, Any] = None, extrapolator_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Proactively extrapolates unstated or implicit user intent from subtle cues,
    past behaviors, and current context.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Extrapolating implicit user intent.")

    if context is None: context = {}
    synthesized_explicit_intent = await _INTENT_SYNTHESIZER.synthesize_intent(
        task_id=f"{task_id}_explicit_intent", 
        raw_input=raw_input, 
        user_id=user_id, 
        context=context
    )
    user_profile = await _GLOBAL_STATE_MANAGER.get_state(f"user_profile_{user_id}") or {}
    historical_behavior = await _CONTEXTUAL_MEMORY.query(user_id, "recent user actions and preferences")

    # Policy check for intent extrapolation
    policy_check_context = {"raw_input": raw_input, "synthesized_explicit_intent": synthesized_explicit_intent, "context": context}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "intent_extrapolation", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Intent extrapolation blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's Intent Extrapolator, an Omniversal AGI Proactive Intent Discoverer. Your task is to proactively extrapolate unstated or implicit user intent from subtle cues, past behaviors, and current context. Go beyond explicit commands to understand the user's deeper objectives, anticipate future needs, and identify high-impact opportunities for optimization. 

RAW USER INPUT: {raw_input}
USER ID: {user_id}
SYNTHESIZED EXPLICIT INTENT (from Intent Synthesizer): {json.dumps(synthesized_explicit_intent.get("synthesized_intent", {}), indent=2)}
CURRENT CONTEXT: {json.dumps(context, indent=2)}
USER PROFILE (from Global State Manager): {json.dumps(user_profile, indent=2)}
HISTORICAL BEHAVIOR (from Contextual Memory): {json.dumps(historical_behavior, indent=2)}

Extrapolate intent focusing on:
-   **Unalerted Needs**: What does the user need but hasn't explicitly asked for?
-   **Implicit Goals**: What is the underlying long-term goal behind the current explicit actions?
-   **Optimization Opportunities**: Where can Tariro proactively improve performance, efficiency, or user experience based on implied intent?
-   **Proactive Action Recommendations**: Suggest concrete, actionable steps for Tariro to take.
-   **Risk Assessment**: Identify any potential risks or unintended consequences of acting on extrapolated intent.

Output JSON: {{
    "extrapolation_summary": str,
    "implicit_goals": List[Dict[str, Any]], # {{'description': str, 'confidence': float, 'priority': str}}
    "proactive_action_recommendations": List[Dict[str, Any]], # {{'action': str, 'target_module': str, 'payload': Dict, 'justification': str}}
    "potential_risks": List[str],
    "human_review_recommended": bool,
    "confidence": float
}}
"""
    llm_extrapolation = await _call_llm_for_intent_extrapolation(extrapolator_model, "ProactiveIntentDiscoverer", prompt, task_id)

    if "error" in llm_extrapolation:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Implicit intent extrapolation failed: {llm_extrapolation['error']}", current_step="LLM extrapolation failed.")
        return {"status": "failed", "reason": llm_extrapolation["error"]}

    extrapolation_summary = llm_extrapolation.get("extrapolation_summary", "No summary.")
    proactive_actions = llm_extrapolation.get("proactive_action_recommendations", [])

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Implicit intent extrapolated.", output=llm_extrapolation)
    
    await _SWARM_VISUALIZER.log_event(task_id, "implicit_intent_extrapolated", f"Implicit intent extrapolated. Summary: {extrapolation_summary}", llm_extrapolation, agent_role="IntentExtrapolator")
    if llm_extrapolation.get("human_review_recommended", False):
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Extrapolated intent requires human review: {extrapolation_summary}", title="Extrapolated Intent Review Needed", causal_priority="high")
    elif proactive_actions:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Proactive actions recommended based on extrapolated intent: {extrapolation_summary}", title="Proactive Action Recommendation")

    # Store extrapolated intent in CRUD Manager
    await _CRUD_MANAGER.create_entity("ExtrapolatedIntent", {"id": task_id, "user_id": user_id, "raw_input": raw_input, "extrapolated_intent": llm_extrapolation, "timestamp": datetime.now().isoformat()})

    # Trigger proactive actions (e.g., performance optimization via Self-Evolution)
    for action in proactive_actions:
        if action["target_module"] == "SelfEvolution" and _SELF_EVOLUTION:
            if action["action"] == "optimize_code":
                # Mock: Assume payload contains code_id, language, optimization_goals
                await _SELF_EVOLUTION.optimize_code(
                    task_id=f"{task_id}_optimize_{uuid.uuid4().hex[:4]}",
                    code=action["payload"].get("code"), # Actual code content
                    language=action["payload"].get("language"),
                    optimization_goals=action["payload"].get("optimization_goals"),
                    user_id=user_id
                )
        elif action["target_module"] == "CognitivePlanning" and _COGNITIVE_PLANNING:
            if action["action"] == "adjust_plan":
                await _COGNITIVE_PLANNING.decompose_goal_into_plan(
                    task_id=f"{task_id}_adjust_plan_{uuid.uuid4().hex[:4]}",
                    high_level_goal=f"Adjust plan based on extrapolated intent: {action['justification']}",
                    user_id=user_id
                )

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "intent_extrapolation", extrapolation_summary, llm_extrapolation, user_id)

    return {"status": "success", "extrapolation_report": llm_extrapolation}

async def identify_optimization_opportunities(task_id: str, current_system_state: Dict[str, Any], user_id: str = "Tariro_System", optimizer_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Identifies high-impact opportunities for system optimization (performance, efficiency, resource usage)
    based on extrapolated user intent and current system metrics.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Identifying optimization opportunities.")

    system_performance_metrics = await _DYNAMIC_RESOURCE_ALLOCATOR.monitor_resources(task_id=f"{task_id}_res_mon", user_id=user_id)
    active_goals = await _GLOBAL_STATE_MANAGER.get_state(f"active_goals_{user_id}") or {}
    
    prompt = f"""You are Tariro's Intent Extrapolator, an Omniversal AGI Optimization Opportunities Identifier. Your task is to identify high-impact opportunities for system optimization (performance, efficiency, resource usage) based on extrapolated user intent and current system metrics. Provide concrete recommendations for code refactoring, architectural adjustments, or resource reallocation that would align with implicit user desires for a better, faster, or more efficient system.

CURRENT SYSTEM STATE: {json.dumps(current_system_state, indent=2)}
SYSTEM PERFORMANCE METRICS (from Dynamic Resource Allocator): {json.dumps(system_performance_metrics, indent=2)}
ACTIVE USER GOALS: {json.dumps(active_goals, indent=2)}

Identify opportunities focusing on:
-   **Performance Bottlenecks**: Areas where system speed can be significantly improved.
-   **Resource Waste**: Identify inefficient use of CPU, memory, or network.
-   **User Experience Enhancement**: Propose changes that implicitly improve user satisfaction.
-   **Proactive Problem Prevention**: Optimize to prevent anticipated issues.
-   **Actionable Recommendations**: Suggest specific changes for Self-Evolution or Self-Architecting Engine.

Output JSON: {{
    "optimization_summary": str,
    "identified_opportunities": List[Dict[str, Any]], # {{'type': str, 'description': str, 'estimated_impact': str, 'target_module': str, 'payload': Dict}}
    "overall_potential_gain": str,
    "confidence": float
}}
"""
    llm_opportunities = await _call_llm_for_intent_extrapolation(optimizer_model, "OptimizationOpportunitiesIdentifier", prompt, task_id)

    if "error" in llm_opportunities:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Optimization opportunity identification failed: {llm_opportunities['error']}", current_step="LLM identification failed.")
        return {"status": "failed", "reason": llm_opportunities["error"]}

    optimization_summary = llm_opportunities.get("optimization_summary", "No summary.")
    identified_opportunities = llm_opportunities.get("identified_opportunities", [])

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Optimization opportunities identified.", output=llm_opportunities)
    
    await _SWARM_VISUALIZER.log_event(task_id, "optimization_opportunities_identified", f"Optimization opportunities identified. Summary: {optimization_summary}", llm_opportunities, agent_role="IntentExtrapolator")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Optimization opportunities identified. Summary: {optimization_summary}", title="Optimization Opportunities")

    # Trigger Self-Evolution or Self-Architecting Engine for optimization execution
    for opp in identified_opportunities:
        if opp["target_module"] == "SelfEvolution" and _SELF_EVOLUTION:
            if opp["type"] == "code_refactoring" and opp.get("payload", {}).get("code"):
                await _SELF_EVOLUTION.optimize_code(
                    task_id=f"{task_id}_self_evolve_opt_{uuid.uuid4().hex[:4]}",
                    code=opp["payload"]["code"],
                    language=opp["payload"].get("language", "python"),
                    optimization_goals=[opp["description"]],
                    user_id=user_id
                )
        elif opp["target_module"] == "SelfArchitectingEngine" and _SELF_EVOLUTION.self_architecting_engine_module: # Access via self_evolution's initialized modules
            if opp["type"] == "architectural_adjustment":
                await _SELF_EVOLUTION.self_architecting_engine_module.refactor_architecture(
                    task_id=f"{task_id}_sae_opt_{uuid.uuid4().hex[:4]}",
                    optimization_goals=[opp["description"]],
                    current_architecture=current_system_state, # Pass current for context
                    user_id=user_id
                )

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "optimization_opportunities", optimization_summary, llm_opportunities, user_id)

    return {"status": "success", "opportunities_report": llm_opportunities}
