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

DEPLOYMENT_LOG_DIR: str = ""

def initialize_automated_deployment(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any):
    """Initializes global configurations for Automated Deployment Pipelines."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, DEPLOYMENT_LOG_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module

    DEPLOYMENT_LOG_DIR = os.path.join(_WORKSPACE, "deployment_logs")
    os.makedirs(DEPLOYMENT_LOG_DIR, exist_ok=True)
    print(f"Automated Deployment initialized. Logs: {DEPLOYMENT_LOG_DIR}")

async def _call_llm_for_deployment_decision(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for deployment-related decision tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in automated_deployment.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "deployment_llm_call_start", f"{model} evaluating deployment decision: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    try:
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on safe and efficient deployment decisions."},
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
            task_id, "deployment_llm_call_end", f"{model} completed deployment decision.",
            {"model": model, "response_summary": content[:100]},
            model_name=model, agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "deployment_llm_error", f"JSON decode error from {model} for deployment task.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": model}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "deployment_llm_error", f"Error calling {model} for deployment task.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model}

async def simulate_deploy(task_id: str, target: str, version: str) -> Dict[str, Any]:
    """
    Simulates the deployment of a service to a target environment.
    Can randomly succeed or fail.
    """
    print(f"Simulating deployment of {version} to {target}...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "sim_deploy_start", f"Simulating deployment of {version} to {target}.",
        {"target": target, "version": version}, model_name="system", agent_role="deployment_system"
    )

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "task_id": task_id,
        "target": target,
        "version": version,
        "action": "deploy"
    }

    if random.random() < 0.85: # 85% chance of initial success
        status = "deployed"
        details = {"message": f"Service {version} successfully deployed to {target}."}
        await _SWARM_VISUALIZER.log_event(task_id, "sim_deploy_success", details["message"], details, model_name="system", agent_role="deployment_system")
    else:
        status = "failed"
        error_message = random.choice([
            "Deployment target unresponsive.",
            "Dependency conflict detected during provisioning.",
            "Resource allocation failed.",
            "Version mismatch in environment."
        ])
        details = {"message": f"Deployment of {version} to {target} failed: {error_message}"}
        await _SWARM_VISUALIZER.log_event(task_id, "sim_deploy_fail", details["message"], details, model_name="system", agent_role="deployment_system", level="ERROR")
    
    log_entry["status"] = status
    log_entry["details"] = details
    
    log_filename = os.path.join(DEPLOYMENT_LOG_DIR, f"deploy_{task_id}_{target}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump(log_entry, f, indent=2)

    return {"status": status, "target": target, "version": version, "log_path": log_filename, "details": details}

async def simulate_monitor_health(task_id: str, target: str, deployed_version: str) -> Dict[str, Any]:
    """
    Simulates real-time monitoring of a deployed service.
    Can randomly detect issues after deployment.
    """
    print(f"Simulating monitoring for {deployed_version} on {target}...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "sim_monitor_start", f"Monitoring health of {deployed_version} on {target}.",
        {"target": target, "version": deployed_version}, model_name="system", agent_role="monitoring_system"
    )

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "task_id": task_id,
        "target": target,
        "version": deployed_version,
        "action": "monitor"
    }

    if random.random() < 0.2: # 20% chance of detecting an issue
        status = "degraded"
        issue = random.choice([
            "High latency spikes detected.",
            "Error rate above threshold (5xx errors).",
            "Resource utilization (CPU/Memory) exceeding limits.",
            "Service response time inconsistent."
        ])
        details = {"message": f"Monitoring detected issue on {target} ({deployed_version}): {issue}"}
        await _SWARM_VISUALIZER.log_event(task_id, "sim_monitor_issue", details["message"], details, model_name="system", agent_role="monitoring_system", level="WARNING")
    else:
        status = "healthy"
        details = {"message": f"Service {deployed_version} on {target} is healthy."}
        await _SWARM_VISUALIZER.log_event(task_id, "sim_monitor_healthy", details["message"], details, model_name="system", agent_role="monitoring_system")
    
    log_entry["status"] = status
    log_entry["details"] = details

    log_filename = os.path.join(DEPLOYMENT_LOG_DIR, f"monitor_{task_id}_{target}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump(log_entry, f, indent=2)

    return {"status": status, "target": target, "deployed_version": deployed_version, "log_path": log_filename, "details": details}

async def agi_decide_rollback(task_id: str, target: str, current_version: str, monitoring_report: Dict[str, Any], agi_model: str = "arbiter") -> Dict[str, Any]:
    """
    An AGI (Arbiter) analyzes monitoring data and decides if a rollback is necessary.
    """
    print(f"AGI ({agi_model}) deciding rollback for {target} (version {current_version})...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "agi_rollback_decision_start", f"AGI ({agi_model}) evaluating rollback for {target}.",
        {"target": target, "version": current_version, "monitoring_status": monitoring_report["status"]},
        model_name=agi_model, agent_role=_ALL_MODELS.get(agi_model, "Arbiter")
    )

    prompt = f"""You are an AGI responsible for maintaining system stability.
    A service deployed to target '{target}' with version '{current_version}' is experiencing issues.
    Here is the latest monitoring report:
    {json.dumps(monitoring_report, indent=2)}

    Based on this report, should a rollback be initiated?
    Respond with JSON: {{'decision': 'rollback' | 'monitor_further' | 'ignore', 'reason': 'detailed explanation'}}.
    Prioritize system stability and safety.
    """
    
    result = await _call_llm_for_deployment_decision(
        agi_model,
        _ALL_MODELS.get(agi_model, "Arbiter"),
        prompt,
        task_id,
        context=json.dumps(monitoring_report)
    )

    decision = result.get("decision", "monitor_further")
    reason = result.get("reason", "AGI decision could not be parsed.")

    await _SWARM_VISUALIZER.log_event(
        task_id, "agi_rollback_decision_end", f"AGI decided: {decision} for {target}.",
        {"target": target, "decision": decision, "reason": reason},
        model_name=agi_model, agent_role=_ALL_MODELS.get(agi_model, "Arbiter"),
        level="INFO" if decision == "monitor_further" else ("WARNING" if decision == "rollback" else "INFO")
    )

    print(f"AGI decision for {target}: {decision} - {reason}")
    return {"decision": decision, "reason": reason, "model": agi_model}

async def simulate_rollback(task_id: str, target: str, version_to_rollback: str) -> Dict[str, Any]:
    """
    Simulates rolling back a service to a previous stable version.
    """
    print(f"Simulating rollback for {target} to version {version_to_rollback}...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "sim_rollback_start", f"Simulating rollback for {target} to version {version_to_rollback}.",
        {"target": target, "version": version_to_rollback}, model_name="system", agent_role="deployment_system"
    )

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "task_id": task_id,
        "target": target,
        "version": version_to_rollback,
        "action": "rollback"
    }

    if random.random() < 0.95: # High chance of rollback success
        status = "rolled_back"
        details = {"message": f"Service {target} successfully rolled back to version {version_to_rollback}."}
        await _SWARM_VISUALIZER.log_event(task_id, "sim_rollback_success", details["message"], details, model_name="system", agent_role="deployment_system")
    else:
        status = "rollback_failed"
        details = {"message": f"Rollback for {target} to {version_to_rollback} failed."}
        await _SWARM_VISUALIZER.log_event(task_id, "sim_rollback_fail", details["message"], details, model_name="system", agent_role="deployment_system", level="ERROR")
    
    log_entry["status"] = status
    log_entry["details"] = details

    log_filename = os.path.join(DEPLOYMENT_LOG_DIR, f"rollback_{task_id}_{target}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump(log_entry, f, indent=2)

    return {"status": status, "target": target, "version": version_to_rollback, "log_path": log_filename, "details": details}
