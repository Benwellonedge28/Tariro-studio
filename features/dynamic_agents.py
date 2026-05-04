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

AGENT_CONFIG_DIR: str = ""

def initialize_dynamic_agents(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any):
    """Initializes global configurations for Dynamic Agent Role & Swarm Configuration."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, AGENT_CONFIG_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module

    AGENT_CONFIG_DIR = os.path.join(_WORKSPACE, "agent_configs")
    os.makedirs(AGENT_CONFIG_DIR, exist_ok=True)
    
    # Initialize a default agent configuration if none exists
    if not os.path.exists(os.path.join(AGENT_CONFIG_DIR, "default_agents.json")):
        with open(os.path.join(AGENT_CONFIG_DIR, "default_agents.json"), "w") as f:
            json.dump(_ALL_MODELS, f, indent=2) # Use the initial ALL_MODELS as default
    print(f"Dynamic Agents initialized. Agent configurations: {AGENT_CONFIG_DIR}")

def _load_current_agent_config() -> Dict[str, str]:
    """Loads the currently active agent configuration."""
    # For simplicity, we'll just load the default or the last modified one
    config_path = os.path.join(AGENT_CONFIG_DIR, "active_agents.json")
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            return json.load(f)
    # Fallback to default if no active config found
    default_config_path = os.path.join(AGENT_CONFIG_DIR, "default_agents.json")
    if os.path.exists(default_config_path):
        with open(default_config_path, "r") as f:
            return json.load(f)
    return _ALL_MODELS # Return hardcoded ALL_MODELS if no files found

def _save_agent_config(config: Dict[str, str]):
    """Saves a new active agent configuration."""
    config_path = os.path.join(AGENT_CONFIG_DIR, "active_agents.json")
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)

async def _call_llm_for_agent_config(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for agent configuration related tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in dynamic_agents.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "dynamic_agent_llm_call_start", f"{model} evaluating agent config task: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    try:
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on optimal agent configurations."},
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
            task_id, "dynamic_agent_llm_call_end", f"{model} completed agent config task.",
            {"model": model, "response_summary": content[:100]},
            model_name=model, agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "dynamic_agent_llm_error", f"JSON decode error from {model} for agent config task.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": model}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "dynamic_agent_llm_error", f"Error calling {model} for agent config task.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model}

async def configure_swarm_dynamically(task_id: str, task_description: str, current_config: Dict[str, str], model_caller: str = "phi-pm") -> Dict[str, Any]:
    """
    Analyzes the task and dynamically configures the swarm by suggesting new roles or modifying existing ones.
    """
    print(f"Dynamically configuring swarm for task: {task_description[:50]}...")
    
    prompt = f"""Given the task '{task_description}' and the current agent configuration:
{json.dumps(current_config, indent=2)}

Propose an optimized agent configuration for this specific task. You can:
1. Suggest a new model for a role if an existing one is suboptimal.
2. Define a new specialized role and assign an appropriate model.
3. Modify the description (role) of an existing model.
4. Remove models/roles if they are not needed.

The output MUST be a JSON object representing the *new, complete* ALL_MODELS dictionary, where keys are model names and values are their roles. ONLY output the JSON dictionary.
Ensure all critical roles (coder, tester, architect, reviewer, pm, arbiter) are covered if they are relevant to the task.
"""
    
    result = await _call_llm_for_agent_config(
        model_caller,
        _ALL_MODELS.get(model_caller, "Orchestrator"), # Use its current role
        prompt,
        task_id,
        context=f"Dynamic swarm configuration requested for: {task_description[:100]}"
    )
    
    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    new_config = result.get("content", {}) # LLM should return the dict directly if json_object
    if isinstance(new_config, str):
        try:
            new_config = json.loads(new_config)
        except json.JSONDecodeError:
            return {"status": "failed", "reason": "LLM returned invalid JSON for new config."}

    if not isinstance(new_config, dict):
        return {"status": "failed", "reason": "LLM did not return a dictionary for new config."}

    _save_agent_config(new_config)
    await _SWARM_VISUALIZER.log_event(
        task_id, "dynamic_swarm_configured", f"Dynamically configured swarm for task.",
        {"task_summary": task_description[:100], "new_config_summary": list(new_config.keys())},
        model_name=model_caller, agent_role=_ALL_MODELS.get(model_caller, "Orchestrator")
    )
    print(f"Swarm dynamically reconfigured. New active agents: {list(new_config.keys())}")
    return {"status": "success", "new_active_config": new_config}

def get_active_agent_config() -> Dict[str, str]:
    """Retrieves the currently active agent configuration."""
    return _load_current_agent_config()
