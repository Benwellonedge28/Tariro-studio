import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid
import httpx # For making actual external API calls

# --- Configuration & Shared Data (initialized from studio_v3_core.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Base model definitions from studio_v3_core.py
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module
_CRUD_MANAGER: Any = None # Reference to crud_manager module for API_Call_Log or ExternalResource entities
_GLOBAL_STATE_MANAGER: Any = None # For storing API keys, external service configurations
_PERSISTENT_TASK_MANAGER: Any = None # For submitting external interaction tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on external system issues or data fetched
_DYNAMIC_POLICY_SYNTHESIS: Any = None # For policy checks on external interactions
_AUTONOMY_GOVERNANCE: Any = None # For enforcing access control to external services
_SECURE_COGNITIVE_DEFENSE_GRID: Any = None # For securing external communications and data
_GLOBAL_ENVIRONMENTAL_MODEL: Any = None # For integrating data fetched from external sources
_UNIVERSAL_DEPLOYMENT_MANAGER: Any = None # For provisioning external resources (e.g., cloud instances)
_EVAS_ETHICAL_ALIGNMENT: Any = None # For ethical vetting of external actions

EXTERNAL_AGENCY_LOG_DIR: str = ""

# In-memory mock for external API specifications and credentials
_MOCKED_EXTERNAL_APIS: Dict[str, Any] = {
    "weather_api": {
        "base_url": "https://api.weatherapi.com/v1",
        "endpoints": {"current": "/current.json", "forecast": "/forecast.json"},
        "api_key_name": "WEATHER_API_KEY",
        "auth_type": "query_param",
        "data_schema": {"current": {"temp_c": float, "condition_text": str}},
        "policies": ["rate_limit_100_per_minute"]
    },
    "news_api": {
        "base_url": "https://newsapi.org/v2",
        "endpoints": {"top_headlines": "/top-headlines", "everything": "/everything"},
        "api_key_name": "NEWS_API_KEY",
        "auth_type": "header",
        "data_schema": {"top_headlines": {"articles": List[Dict]}},
        "policies": ["data_privacy_compliance"]
    }
    # ... more APIs
}

def initialize_external_agency(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, global_state_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, dynamic_policy_synthesis_module: Any, autonomy_governance_module: Any, secure_cognitive_defense_grid_module: Any, global_environmental_model_module: Any, universal_deployment_manager_module: Any, evas_ethical_alignment_module: Any):
    """Initializes global configurations for the External Agency module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _GLOBAL_STATE_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _DYNAMIC_POLICY_SYNTHESIS, _AUTONOMY_GOVERNANCE, _SECURE_COGNITIVE_DEFENSE_GRID, _GLOBAL_ENVIRONMENTAL_MODEL, _UNIVERSAL_DEPLOYMENT_MANAGER, _EVAS_ETHICAL_ALIGNMENT, EXTERNAL_AGENCY_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _DYNAMIC_POLICY_SYNTHESIS = dynamic_policy_synthesis_module
    _AUTONOMY_GOVERNANCE = autonomy_governance_module
    _SECURE_COGNITIVE_DEFENSE_GRID = secure_cognitive_defense_grid_module
    _GLOBAL_ENVIRONMENTAL_MODEL = global_environmental_model_module
    _UNIVERSAL_DEPLOYMENT_MANAGER = universal_deployment_manager_module
    _EVAS_ETHICAL_ALIGNMENT = evas_ethical_alignment_module

    EXTERNAL_AGENCY_LOG_DIR = os.path.join(_WORKSPACE, "external_agency_logs")
    os.makedirs(EXTERNAL_AGENCY_LOG_DIR, exist_ok=True)
    print(f"External Agency initialized. Logs: {EXTERNAL_AGENCY_LOG_DIR}")

    # Load API specs and credentials from Global State Manager
    initial_api_specs = asyncio.run(_GLOBAL_STATE_MANAGER.get_state("external_api_specs"))
    if initial_api_specs:
        _MOCKED_EXTERNAL_APIS.update(initial_api_specs)
    else:
        asyncio.run(_GLOBAL_STATE_MANAGER.set_state("external_api_specs", _MOCKED_EXTERNAL_APIS, "Tariro_System", auditable=True))

async def _call_llm_for_external_agency(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for external interaction decisions and data interpretation."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in external_agency.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "external_agency_llm_call_start", f"{model} external interaction: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on safely and effectively interacting with external systems, APIs, and real-world resources (e.g., cloud providers, web services). Ensure all external actions are policy-compliant, ethically sound, and securely executed. Interpret external data and integrate it into Tariro's internal models."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.07 # Balanced for safe interaction and accurate interpretation
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "external_agency_llm_call_end", f"{model} completed external agency task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "external_agency_llm_error", f"JSON decode error from {model} for external agency.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "external_agency_llm_error", f"Error calling {model} for external agency task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}

async def interact_with_external_api(task_id: str, api_spec: Dict[str, Any], action: str, params: Dict[str, Any], user_id: str = "Tariro_System", interaction_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Interacts with external APIs in a policy-compliant and secure manner.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Interacting with external API: {api_spec.get('name')}/{action}.")

    # Policy check for external API interaction
    policy_check_context = {"api_spec": api_spec, "action": action, "params": params}
    policy_compliance_report = await _DYNAMIC_POLICY_SYNTHESIS.get_autonomy_level(user_id, "external_api_interaction") # Re-using get_autonomy_level
    if policy_compliance_report.get("config", {}).get("level") == "human_required":
        # If human_required, send notification and await approval
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Human approval required for external API interaction: {api_spec.get('name')}/{action}", title="External API Approval Needed", causal_priority="critical")
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PAUSED", 0, "Awaiting human approval for external API interaction.")
        return {"status": "paused", "reason": "Human approval required for external API interaction."}

    # Ethical review via EVAS Ethical Alignment module
    ethical_review_result = {"allowed": True, "score": 1.0, "reasoning": "Skipped EVAS (mock)."}
    if _EVAS_ETHICAL_ALIGNMENT:
        ethical_review_result = await _EVAS_ETHICAL_ALIGNMENT.audit_content(
            task_id=f"{task_id}_evas",
            content=json.dumps(policy_check_context),
            user_id=user_id,
            audit_type="external_api_interaction"
        )
    if not ethical_review_result.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "External API interaction blocked by ethical policy.", output=ethical_review_result)
        return {"status": "failed", "reason": "Ethical review failed", "details": ethical_review_result}

    api_name = api_spec.get("name")
    configured_api = _MOCKED_EXTERNAL_APIS.get(api_name)

    if not configured_api:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"API {api_name} not configured.")
        return {"status": "failed", "reason": f"API {api_name} not configured."}

    endpoint_path = configured_api["endpoints"].get(action)
    if not endpoint_path:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Action {action} not found for API {api_name}.")
        return {"status": "failed", "reason": f"Action {action} not found for API {api_name}."}

    api_key = os.getenv(configured_api["api_key_name"]) # Retrieve API key securely from environment variables
    if not api_key:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"API key not found for {api_name}.")
        return {"status": "failed", "reason": f"API key not found for {api_name}. Ensure {configured_api['api_key_name']} is set."}

    headers = {}
    request_params = params.copy()

    if configured_api["auth_type"] == "query_param":
        request_params["key"] = api_key
    elif configured_api["auth_type"] == "header":
        headers["Authorization"] = f"Bearer {api_key}"

    full_url = f"{configured_api["base_url"]}{endpoint_path}"

    # Simulate external API call (replace with actual httpx.get/post in real implementation)
    try:
        # Ensure communication is secured via Secure Cognitive Defense Grid if necessary
        # (e.g., VPN, encrypted tunnel setup, data scrubbing prior to sending)
        processed_params = await _SECURE_COGNITIVE_DEFENSE_GRID.filter_sensitive_data(
            json.dumps(request_params), context="external_api_request", user_id=user_id
        )
        processed_headers = await _SECURE_COGNITIVE_DEFENSE_GRID.filter_sensitive_data(
            json.dumps(headers), context="external_api_request", user_id=user_id
        )

        async with httpx.AsyncClient() as client:
            if action in ["post", "put", "patch"]:
                response = await client.post(full_url, params=json.loads(processed_params), headers=json.loads(processed_headers), timeout=30.0)
            else:
                response = await client.get(full_url, params=json.loads(processed_params), headers=json.loads(processed_headers), timeout=30.0)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            api_response = response.json()

    except httpx.HTTPStatusError as e:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"External API call failed: HTTP error {e.response.status_code}", output={"error": str(e), "response": e.response.text})
        return {"status": "failed", "reason": f"HTTP error: {e}"}
    except httpx.RequestError as e:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"External API call failed: Request error {e}", output={"error": str(e)})
        return {"status": "failed", "reason": f"Request error: {e}"}
    except Exception as e:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"External API call failed: {e}", output={"error": str(e)})
        return {"status": "failed", "reason": str(e)}

    # Further process and integrate API response into Global Environmental Model
    if _GLOBAL_ENVIRONMENTAL_MODEL:
        await _GLOBAL_ENVIRONMENTAL_MODEL.integrate_data_streams(
            task_id=f"{task_id}_gem_integrate", 
            source_type=api_name, 
            raw_data=api_response, 
            user_id=user_id
        )

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "External API interaction successful.", output=api_response)
    
    await _SWARM_VISUALIZER.log_event(task_id, "external_api_interaction", f"API {api_name}/{action} interaction successful.", {"api_name": api_name, "action": action, "response_preview": str(api_response)[:100]}, agent_role="ExternalAgency")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"External API {api_name}/{action} interaction successful.", title="External Interaction Complete")

    return {"status": "success", "api_response": api_response}

async def manage_external_resources(task_id: str, resource_id: str, command: str, command_params: Dict[str, Any], user_id: str = "Tariro_System", management_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Manages external computational or storage resources (e.g., cloud instances, databases).
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Managing external resource {resource_id}: {command}.")

    # Policy check for resource management
    policy_check_context = {"resource_id": resource_id, "command": command, "params": command_params}
    policy_compliance_report = await _DYNAMIC_POLICY_SYNTHESIS.get_autonomy_level(user_id, "external_resource_management")
    if policy_compliance_report.get("config", {}).get("level") == "human_required":
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Human approval required for external resource management: {resource_id}/{command}", title="External Resource Approval Needed", causal_priority="critical")
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PAUSED", 0, "Awaiting human approval for external resource management.")
        return {"status": "paused", "reason": "Human approval required for external resource management."}

    # Ethical review via EVAS
    ethical_review_result = {"allowed": True, "score": 1.0, "reasoning": "Skipped EVAS (mock)."}
    if _EVAS_ETHICAL_ALIGNMENT:
        ethical_review_result = await _EVAS_ETHICAL_ALIGNMENT.audit_content(
            task_id=f"{task_id}_evas",
            content=json.dumps(policy_check_context),
            user_id=user_id,
            audit_type="external_resource_management"
        )
    if not ethical_review_result.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "External resource management blocked by ethical policy.", output=ethical_review_result)
        return {"status": "failed", "reason": "Ethical review failed", "details": ethical_review_result}

    # Delegate to Universal Deployment Manager for actual provisioning/deprovisioning
    if _UNIVERSAL_DEPLOYMENT_MANAGER:
        if command == "provision":
            result = await _UNIVERSAL_DEPLOYMENT_MANAGER.provision_resource(task_id=f"{task_id}_udm", resource_spec=command_params, user_id=user_id)
        elif command == "deprovision":
            result = await _UNIVERSAL_DEPLOYMENT_MANAGER.deprovision_resource(task_id=f"{task_id}_udm", resource_id=resource_id, user_id=user_id)
        elif command == "configure":
            result = await _UNIVERSAL_DEPLOYMENT_MANAGER.configure_resource(task_id=f"{task_id}_udm", resource_id=resource_id, config_params=command_params, user_id=user_id)
        else:
            result = {"status": "failed", "reason": f"Unknown command {command}."}
    else:
        result = {"status": "failed", "reason": "Universal Deployment Manager not loaded."}

    if result.get("status") == "success":
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, f"External resource {resource_id} {command} successful.", output=result)
        await _SWARM_VISUALIZER.log_event(task_id, "external_resource_managed", f"External resource {resource_id} {command} successful.", result, agent_role="ExternalAgency")
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"External resource {resource_id} {command} successful.", title="Resource Management Complete")
        return {"status": "success", "management_response": result}
    else:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"External resource {resource_id} {command} failed.", output=result)
        await _SWARM_VISUALIZER.log_event(task_id, "external_resource_management_failed", f"External resource {resource_id} {command} failed. Details: {result.get('reason')}", result, agent_role="ExternalAgency", level="ERROR")
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"External resource {resource_id} {command} failed. Reason: {result.get('reason', 'N/A')}", title="External Resource Management Failed", causal_priority="critical")
        return {"status": "failed", "reason": "Resource management failed", "details": result}
