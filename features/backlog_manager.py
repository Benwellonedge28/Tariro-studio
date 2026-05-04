import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid

# --- Configuration & Shared Data (initialized from studio_v3.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Base model definitions from studio_v3.py
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module
_CRUD_MANAGER: Any = None # Reference to crud_manager module for simulated entity data

BACKLOG_LOG_DIR: str = ""

def initialize_backlog_manager(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any):
    """Initializes global configurations for Autonomous Feature Proposal."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, BACKLOG_LOG_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module

    BACKLOG_LOG_DIR = os.path.join(_WORKSPACE, "backlog_proposals")
    os.makedirs(BACKLOG_LOG_DIR, exist_ok=True)
    print(f"Backlog Manager initialized. Logs: {BACKLOG_LOG_DIR}")

async def _call_llm_for_feature_proposal(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for feature proposal tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in backlog_manager.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "backlog_llm_call_start", f"{model} evaluating feature proposal task: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    try:
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on identifying and drafting valuable feature proposals for the AGI system itself."},
            {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
        ]
        
        resp = await _CLIENT.chat.completions.create(
            model=model,
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.2 # Slightly higher temp for creative problem-solving
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = model

        await _SWARM_VISUALIZER.log_event(
            task_id, "backlog_llm_call_end", f"{model} completed feature proposal task.",
            {"model": model, "response_summary": content[:100]},
            model_name=model, agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "backlog_llm_error", f"JSON decode error from {model} for feature proposal.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": model}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "backlog_llm_error", f"Error calling {model} for feature proposal.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model}


async def analyze_for_feature_proposals(task_id: str, analysis_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates a meta-learning agent analyzing PerformanceLog and LearningInsight data
    to identify opportunities for new features or improvements.
    """
    print(f"AGI ({analysis_model}) analyzing system data for feature proposals...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "feature_analysis_start", f"AGI ({analysis_model}) analyzing logs for feature proposals.",
        {}, model_name=analysis_model, agent_role=_ALL_MODELS.get(analysis_model, "Meta-Learner")
    )

    # Retrieve recent performance logs (e.g., last 10)
    performance_logs = await _CRUD_MANAGER.read_entities(task_id, "PerformanceLog") # Simplified call, should use query
    # Retrieve recent learning insights (e.g., last 10)
    learning_insights = await _CRUD_MANAGER.read_entities(task_id, "LearningInsight") # Simplified call, should use query

    performance_summary = json.dumps(performance_logs[-5:], indent=2) if performance_logs else "No recent performance logs."
    insights_summary = json.dumps(learning_insights[-5:], indent=2) if learning_insights else "No recent learning insights."

    prompt = f"""You are a meta-learning agent tasked with improving the TARIRO Studio AGI system itself.
    Analyze the following recent system performance data and learning insights.
    Identify any recurring patterns, common failure points, inefficiencies, or emerging needs that suggest a new feature or improvement for the AGI.

    Recent Performance Logs (last 5):
    {performance_summary}

    Recent Learning Insights (last 5):
    {insights_summary}

    Based on this analysis, propose a single, impactful feature.
    Output JSON: {{'title': str, 'problem_statement': str, 'proposed_solution': str, 'estimated_impact': str, 'priority': 'low' | 'medium' | 'high' | 'critical', 'source': 'self_monitoring'}}
    """
    
    result = await _call_llm_for_feature_proposal(
        analysis_model,
        _ALL_MODELS.get(analysis_model, "Meta-Learner"),
        prompt,
        task_id,
        context=f"Performance logs: {performance_summary}\nLearning Insights: {insights_summary}"
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}

    proposal_data = {
        "title": result.get("title", "Untitled Feature Proposal"),
        "problem_statement": result.get("problem_statement", "Problem identified through autonomous analysis."),
        "proposed_solution": result.get("proposed_solution", "Proposed solution generated by AGI."),
        "estimated_impact": result.get("estimated_impact", "Significant impact expected."),
        "priority": result.get("priority", "medium"),
        "source": result.get("source", "self_monitoring"),
        "status": "proposed" # Default status for autonomously generated proposals
    }
    
    # Store the drafted proposal in our simulated CRUD system
    crud_result = await _CRUD_MANAGER.create_entity(task_id, "FeatureProposal", proposal_data)
    proposal_data["crud_id"] = crud_result.get("id")

    log_filename = os.path.join(BACKLOG_LOG_DIR, f"feature_proposal_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump(proposal_data, f, indent=2)
    proposal_data["saved_path"] = log_filename
    proposal_data["status"] = "proposed_and_saved"
    print(f"Autonomous feature proposal saved to {log_filename} and CRUD system.")

    await _SWARM_VISUALIZER.log_event(
        task_id, "feature_proposal_complete", f"AGI proposed new feature: {proposal_data['title']}",
        proposal_data, model_name=analysis_model, agent_role=_ALL_MODELS.get(analysis_model, "Meta-Learner")
    )
    
    return proposal_data
