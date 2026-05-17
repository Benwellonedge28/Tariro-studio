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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for Forecast or Scenario entities
_GLOBAL_STATE_MANAGER: Any = None # For storing current strategic goals and world model
_PERSISTENT_TASK_MANAGER: Any = None # For submitting foresight tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on critical forecasts or opportunities
_GLOBAL_ENVIRONMENTAL_MODEL: Any = None # For providing comprehensive environmental context
_COGNITIVE_PLANNING: Any = None # For incorporating foresight into planning
_DYNAMIC_RESOURCE_ALLOCATOR: Any = None # For resource impact assessment of scenarios
_META_LEARNER: Any = None # For learning from prediction accuracy
_THREAT_MODELER: Any = None # For integrating security threat intelligence
_SELF_ARCHITECTING_ENGINE: Any = None # For architectural implications of future scenarios

STRATEGIC_FORESIGHT_LOG_DIR: str = ""

def initialize_strategic_foresight(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, global_state_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, global_environmental_model_module: Any, cognitive_planning_module: Any, dynamic_resource_allocator_module: Any, meta_learner_module: Any, threat_modeler_module: Any, self_architecting_engine_module: Any):
    """Initializes global configurations for the Strategic Foresight module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _GLOBAL_STATE_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _GLOBAL_ENVIRONMENTAL_MODEL, _COGNITIVE_PLANNING, _DYNAMIC_RESOURCE_ALLOCATOR, _META_LEARNER, _THREAT_MODELER, _SELF_ARCHITECTING_ENGINE, STRATEGIC_FORESIGHT_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _GLOBAL_ENVIRONMENTAL_MODEL = global_environmental_model_module
    _COGNITIVE_PLANNING = cognitive_planning_module
    _DYNAMIC_RESOURCE_ALLOCATOR = dynamic_resource_allocator_module
    _META_LEARNER = meta_learner_module
    _THREAT_MODELER = threat_modeler_module
    _SELF_ARCHITECTING_ENGINE = self_architecting_engine_module

    STRATEGIC_FORESIGHT_LOG_DIR = os.path.join(_WORKSPACE, "strategic_foresight_logs")
    os.makedirs(STRATEGIC_FORESIGHT_LOG_DIR, exist_ok=True)
    print(f"Strategic Foresight initialized. Logs: {STRATEGIC_FORESIGHT_LOG_DIR}")

async def _call_llm_for_foresight(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for strategic foresight decisions and scenario analysis."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in strategic_foresight.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "foresight_llm_call_start", f"{model} strategic foresight: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on anticipating future trends, generating plausible scenarios, identifying potential opportunities and threats, and assessing their strategic implications for Tariro Studio. Integrate insights from the Global Environmental Model and Threat Modeler. Provide actionable recommendations for long-term planning and adaptive strategy development."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.09 # Higher temp for creative scenario generation, but grounded
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "foresight_llm_call_end", f"{model} completed strategic foresight task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "foresight_llm_error", f"JSON decode error from {model} for strategic foresight.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "foresight_llm_error", f"Error calling {model} for strategic foresight task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def generate_future_scenarios(task_id: str, strategic_question: str, horizon: str, user_id: str = "Tariro_System", generator_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Generates a set of plausible future scenarios based on current trends and potential disruptions.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Generating future scenarios for '{strategic_question[:50]}'.")

    current_world_model = await _GLOBAL_STATE_MANAGER.get_state("world_model") or _GLOBAL_ENVIRONMENTAL_MODEL._CURRENT_WORLD_MODEL # Fallback
    external_threats = []
    if _THREAT_MODELER:
        threat_report = await _THREAT_MODELER.assess_global_threat_landscape(task_id=f"{task_id}_threats", user_id=user_id)
        external_threats = threat_report.get("identified_threats", [])

    prompt = f"""You are Tariro's Strategic Foresight Engine, an Omniversal AGI Scenario Generator. Your task is to generate a set of diverse, plausible future scenarios in response to a strategic question, considering current trends, potential disruptions, and insights from the Global Environmental Model and Threat Modeler. Each scenario should be coherent, internally consistent, and clearly describe potential pathways.

STRATEGIC QUESTION: {strategic_question}
FORESIGHT HORIZON: {horizon}
CURRENT WORLD MODEL (from Global Environmental Model): {json.dumps(current_world_model, indent=2)}
EXTERNAL THREATS (from Threat Modeler): {json.dumps(external_threats, indent=2)}

Generate scenarios focusing on:
-   **Plausibility**: Scenarios must be believable and grounded in current reality.
-   **Diversity**: Cover a range of possible outcomes (optimistic, pessimistic, transformative).
-   **Key Drivers**: Identify the main factors shaping each scenario.
-   **Trigger Events**: What events could lead to this scenario?
-   **Strategic Implications**: What does each scenario mean for Tariro Studio?

Output JSON: {{
    "scenario_generation_summary": str,
    "scenarios": List[Dict[str, Any]], # {{'name': str, 'description': str, 'key_drivers': List[str], 'trigger_events': List[str], 'implications_for_tariro': List[str]}}
    "most_likely_scenario_name": str,
    "confidence": float
}}
"""
    llm_scenarios = await _call_llm_for_foresight(generator_model, "ScenarioGenerator", prompt, task_id)

    if "error" in llm_scenarios:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Scenario generation failed: {llm_scenarios['error']}", current_step="LLM generation failed.")
        return {"status": "failed", "reason": llm_scenarios["error"]}

    scenario_summary = llm_scenarios.get("scenario_generation_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Future scenarios generated.", output=llm_scenarios)
    
    await _SWARM_VISUALIZER.log_event(task_id, "scenarios_generated", f"Future scenarios for '{strategic_question[:50]}' generated. Summary: {scenario_summary}", llm_scenarios, agent_role="StrategicForesight")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Future scenarios for '{strategic_question[:50]}' generated. Summary: {scenario_summary}", title="Strategic Scenarios Complete")

    # Store scenarios in CRUD Manager
    for scenario in llm_scenarios.get("scenarios", []):
        await _CRUD_MANAGER.create_entity("Scenario", {"id": str(uuid.uuid4()), "strategic_question": strategic_question, "details": scenario, "horizon": horizon, "created_at": datetime.now().isoformat()})

    return {"status": "success", "scenarios_report": llm_scenarios}

async def identify_opportunities_and_threats(task_id: str, scenario_details: Dict[str, Any], user_id: str = "Tariro_System", identifier_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Analyzes generated scenarios to pinpoint specific opportunities for growth/advantage and potential threats/risks.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Identifying opportunities and threats.")

    current_strategic_goals = await _GLOBAL_STATE_MANAGER.get_state("current_long_term_strategy") or {}
    
    prompt = f"""You are Tariro's Strategic Foresight Engine, an Omniversal AGI Opportunity/Threat Identifier. Your task is to rigorously analyze a generated future scenario to pinpoint specific opportunities for growth, competitive advantage, or societal benefit, and potential threats, risks, or challenges that could impact Tariro Studio. Provide actionable insights for each. 

SCENARIO DETAILS: {json.dumps(scenario_details, indent=2)}
CURRENT STRATEGIC GOALS: {json.dumps(current_strategic_goals, indent=2)}

Identify opportunities and threats focusing on:
-   **Specificity**: Clearly define each opportunity and threat.
-   **Impact Assessment**: Quantify (or qualitatively describe) the potential positive or negative impact.
-   **Likelihood**: Estimate the probability of the opportunity/threat materializing.
-   **Actionable Insights**: For opportunities, suggest how Tariro can capitalize. For threats, suggest mitigation strategies.
-   **Alignment**: How do they align with or diverge from current strategic goals?

Output JSON: {{
    "analysis_summary": str,
    "identified_opportunities": List[Dict[str, Any]], # {{'name': str, 'description': str, 'impact': str, 'likelihood': float, 'recommended_actions': List[str]}}
    "identified_threats": List[Dict[str, Any]], # {{'name': str, 'description': str, 'impact': str, 'likelihood': float, 'mitigation_strategies': List[str]}}
    "overall_strategic_implications": str,
    "confidence": float
}}
"""
    llm_opportunities_threats = await _call_llm_for_foresight(identifier_model, "OpportunityThreatIdentifier", prompt, task_id)

    if "error" in llm_opportunities_threats:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Opportunity/threat identification failed: {llm_opportunities_threats['error']}", current_step="LLM identification failed.")
        return {"status": "failed", "reason": llm_opportunities_threats["error"]}

    analysis_summary = llm_opportunities_threats.get("analysis_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Opportunities and threats identified.", output=llm_opportunities_threats)
    
    await _SWARM_VISUALIZER.log_event(task_id, "opportunities_threats_identified", f"Opportunities and threats identified. Summary: {analysis_summary}", llm_opportunities_threats, agent_role="StrategicForesight")
    if llm_opportunities_threats.get("identified_threats"):
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Potential threats identified in scenario. Summary: {analysis_summary}", title="Strategic Threat Alert", causal_priority="high")

    # Integrate insights into Cognitive Planning and Self-Architecting Engine
    if _COGNITIVE_PLANNING and llm_opportunities_threats.get("identified_opportunities"):
        for opp in llm_opportunities_threats["identified_opportunities"]:
            # Potentially create a new high-level goal based on an opportunity
            await _COGNITIVE_PLANNING.decompose_goal_into_plan(
                task_id=f"{task_id}_opp_plan_{uuid.uuid4().hex[:4]}",
                high_level_goal=f"Capitalize on opportunity: {opp['name']}. {opp['description']}",
                user_id=user_id
            )
    
    if _SELF_ARCHITECTING_ENGINE and llm_opportunities_threats.get("identified_threats"):
        for threat in llm_opportunities_threats["identified_threats"]:
            # Potentially trigger architectural refactoring to mitigate a threat
            await _SELF_ARCHITECTING_ENGINE.refactor_architecture(
                task_id=f"{task_id}_threat_refactor_{uuid.uuid4().hex[:4]}",
                optimization_goals=[f"Mitigate threat: {threat['name']}"],
                current_architecture=await _GLOBAL_STATE_MANAGER.get_state("current_tariro_architecture"),
                user_id=user_id
            )

    return {"status": "success", "analysis_report": llm_opportunities_threats}

async def develop_adaptive_strategy(task_id: str, primary_goal: str, forecast_data: Dict[str, Any], user_id: str = "Tariro_System", strategy_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Develops adaptive strategies to achieve primary goals across various potential future scenarios, optimizing for resilience and flexibility.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Developing adaptive strategy.")

    current_resource_outlook = await _DYNAMIC_RESOURCE_ALLOCATOR.monitor_resources(task_id=f"{task_id}_res_mon", user_id=user_id) # Get current resource outlook
    
    prompt = f"""You are Tariro's Strategic Foresight Engine, an Omniversal AGI Adaptive Strategist. Your task is to develop robust, adaptive strategies to achieve a primary goal across various potential future scenarios. The strategies must optimize for resilience, flexibility, and efficient resource utilization, enabling Tariro Studio to thrive in an uncertain future.

PRIMARY GOAL: {primary_goal}
FORECAST AND SCENARIO DATA: {json.dumps(forecast_data, indent=2)}
CURRENT RESOURCE OUTLOOK (from Dynamic Resource Allocator): {json.dumps(current_resource_outlook, indent=2)}

Develop adaptive strategies focusing on:
-   **No-Regret Moves**: Actions beneficial across all plausible scenarios.
-   **Trigger Points**: Define conditions under which different strategic paths are activated.
-   **Resource Optimization**: Efficient allocation and reallocation of resources under different scenarios.
-   **Flexibility**: Strategies should allow for rapid adaptation to unexpected events.
-   **Policy Alignment**: Ensure strategies align with core ethical and operational policies.

Output JSON: {{
    "strategy_summary": str,
    "adaptive_strategy_plan": List[Dict[str, Any]], # {{'phase': str, 'actions': List[str], 'trigger_conditions': str, 'resource_implications': Dict}}
    "key_assumptions": List[str],
    "robustness_score": float, # 0-1 (how well it handles various scenarios)
    "confidence": float
}}
"""
    llm_strategy = await _call_llm_for_foresight(strategy_model, "AdaptiveStrategist", prompt, task_id)

    if "error" in llm_strategy:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Adaptive strategy development failed: {llm_strategy['error']}", current_step="LLM strategy failed.")
        return {"status": "failed", "reason": llm_strategy["error"]}

    strategy_summary = llm_strategy.get("strategy_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Adaptive strategy developed.", output=llm_strategy)
    
    await _SWARM_VISUALIZER.log_event(task_id, "adaptive_strategy_developed", f"Adaptive strategy developed for '{primary_goal[:50]}'. Summary: {strategy_summary}", llm_strategy, agent_role="StrategicForesight")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Adaptive strategy for '{primary_goal[:50]}' developed. Summary: {strategy_summary}", title="Adaptive Strategy Complete")

    # Store strategy in CRUD Manager (or update Global State Manager's strategic goals)
    await _GLOBAL_STATE_MANAGER.set_state("current_long_term_strategy", {"goal": primary_goal, "strategy": llm_strategy}, user_id, auditable=True)

    # Feed learning insights to Meta-Learner based on strategy robustness
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "adaptive_strategy", strategy_summary, llm_strategy, user_id)

    return {"status": "success", "strategy_report": llm_strategy}
