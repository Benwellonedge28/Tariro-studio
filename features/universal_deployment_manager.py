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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for DeploymentRecord or InfrastructureAsset entities
_GLOBAL_STATE_MANAGER: Any = None # For storing deployment manifests and infrastructure state
_PERSISTENT_TASK_MANAGER: Any = None # For submitting deployment/provisioning tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on deployment success/failure
_EXTERNAL_AGENCY: Any = None # For interacting with cloud providers (AWS, Azure, GCP) or physical systems
_SELF_ARCHITECTING_ENGINE: Any = None # For providing architecture specs for deployment
_DYNAMIC_SWARM_ORCHESTRATION: Any = None # For integrating new instances into the swarm
_SECURE_COGNITIVE_DEFENSE_GRID: Any = None # For securing deployment pipelines and deployed assets
_AUTONOMY_GOVERNANCE: Any = None # For policy checks on deployment actions
_FORMAL_VERIFICATION: Any = None # For formally verifying deployment configurations
_META_LEARNER: Any = None # For learning from deployment outcomes

UNIVERSAL_DEPLOYMENT_MANAGER_LOG_DIR: str = ""

def initialize_universal_deployment_manager(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, global_state_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, external_agency_module: Any, self_architecting_engine_module: Any, dynamic_swarm_orchestration_module: Any, secure_cognitive_defense_grid_module: Any, autonomy_governance_module: Any, formal_verification_module: Any, meta_learner_module: Any):
    """Initializes global configurations for the Universal Deployment Manager module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _GLOBAL_STATE_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _EXTERNAL_AGENCY, _SELF_ARCHITECTING_ENGINE, _DYNAMIC_SWARM_ORCHESTRATION, _SECURE_COGNITIVE_DEFENSE_GRID, _AUTONOMY_GOVERNANCE, _FORMAL_VERIFICATION, _META_LEARNER, UNIVERSAL_DEPLOYMENT_MANAGER_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _EXTERNAL_AGENCY = external_agency_module
    _SELF_ARCHITECTING_ENGINE = self_architecting_engine_module
    _DYNAMIC_SWARM_ORCHESTRATION = dynamic_swarm_orchestration_module
    _SECURE_COGNITIVE_DEFENSE_GRID = secure_cognitive_defense_grid_module
    _AUTONOMY_GOVERNANCE = autonomy_governance_module
    _FORMAL_VERIFICATION = formal_verification_module
    _META_LEARNER = meta_learner_module

    UNIVERSAL_DEPLOYMENT_MANAGER_LOG_DIR = os.path.join(_WORKSPACE, "universal_deployment_manager_logs")
    os.makedirs(UNIVERSAL_DEPLOYMENT_MANAGER_LOG_DIR, exist_ok=True)
    print(f"Universal Deployment Manager initialized. Logs: {UNIVERSAL_DEPLOYMENT_MANAGER_LOG_DIR}")

async def _call_llm_for_deployment(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for deployment planning and execution decisions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in universal_deployment_manager.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "deployment_llm_call_start", f"{model} deployment orchestration: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on autonomously orchestrating the deployment, configuration, and management of Tariro Studio components and infrastructure across any target environment (cloud, edge, physical hardware). Ensure secure, reliable, and efficient deployments with robust rollback capabilities. Generate detailed deployment plans, monitor execution, and integrate new deployments into the broader swarm architecture. Adhere to all policies and security protocols."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.05 # Low temp for precise, reliable deployment planning
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "deployment_llm_call_end", f"{model} completed deployment task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "deployment_llm_error", f"JSON decode error from {model} for deployment.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "deployment_llm_error", f"Error calling {model} for deployment task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def deploy_architecture(task_id: str, architecture_spec: Dict[str, Any], user_id: str = "Tariro_System", deployer_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Orchestrates the deployment of a specified system architecture (applications, services, infrastructure).
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Orchestrating architecture deployment.")

    # Policy check for deployment
    policy_check_context = {"architecture_spec": architecture_spec}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "architecture_deployment", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Architecture deployment blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    # Formal verification of deployment configuration
    fv_result = {"is_correct": True, "reason": "Skipped Formal Verification (mock)."}
    if _FORMAL_VERIFICATION and architecture_spec.get("formal_verification_required", True):
        fv_result = await _FORMAL_VERIFICATION.verify_design(
            task_id=f"{task_id}_fv",
            design_spec=architecture_spec, # Assuming architecture_spec can be used as design_spec
            user_id=user_id
        )
        if not fv_result.get("is_correct", False):
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Deployment configuration failed formal verification.", output=fv_result)
            return {"status": "failed", "reason": "Deployment configuration failed formal verification.", "details": fv_result}

    prompt = f"""You are Tariro's Universal Deployment Manager, an Omniversal AGI Deployment Orchestrator. Your task is to orchestrate the deployment of a specified system architecture (applications, services, infrastructure) across any target environment. Generate a detailed, step-by-step deployment plan that is secure, reliable, efficient, and includes robust rollback mechanisms. Ensure minimal downtime and seamless integration.

ARCHITECTURE SPECIFICATION: {json.dumps(architecture_spec, indent=2)}

Orchestrate deployment focusing on:
-   **Infrastructure Provisioning**: Define required cloud resources, virtual machines, networking.
-   **Application Deployment**: Specify application binaries, configurations, and dependencies.
-   **Security Configuration**: Implement security policies, firewalls, access controls.
-   **Monitoring & Logging**: Set up monitoring and logging for new deployments.
-   **Rollback Strategy**: Plan for automated rollback in case of failure.
-   **Integration**: How to integrate the new deployment into Dynamic Swarm Orchestration.

Output JSON: {{
    "deployment_summary": str,
    "deployment_plan": List[Dict[str, Any]], # {{'step': str, 'action': str, 'target': str, 'details': Dict, 'executor_module': str}}
    "estimated_downtime_seconds": int,
    "rollback_strategy_details": str,
    "confidence": float
}}
"""
    llm_deployment_plan = await _call_llm_for_deployment(deployer_model, "DeploymentOrchestrator", prompt, task_id)

    if "error" in llm_deployment_plan:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Architecture deployment failed: {llm_deployment_plan['error']}", current_step="LLM planning failed.")
        return {"status": "failed", "reason": llm_deployment_plan["error"]}

    deployment_summary = llm_deployment_plan.get("deployment_summary", "No summary.")
    deployment_plan_steps = llm_deployment_plan.get("deployment_plan", [])

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 50, "Deployment plan generated. Executing steps.")

    # Execute deployment plan steps, delegating to External Agency for infrastructure provisioning
    actions_taken = []
    for step in deployment_plan_steps:
        if step["executor_module"] == "ExternalAgency" and _EXTERNAL_AGENCY:
            # Example: call external_agency to provision/configure cloud resources
            action_result = await _EXTERNAL_AGENCY.manage_external_resources(
                task_id=f"{task_id}_ext_res_{step['step']}", 
                resource_id=step["target"], 
                command=step["action"], 
                command_params=step["details"], 
                user_id=user_id
            )
            actions_taken.append(action_result)
        elif step["executor_module"] == "DynamicSwarmOrchestration" and _DYNAMIC_SWARM_ORCHESTRATION:
            if step["action"] == "integrate_into_swarm":
                await _DYNAMIC_SWARM_ORCHESTRATION.add_instance_to_swarm(
                    task_id=f"{task_id}_swarm_integrate_{step['step']}",
                    instance_id=step["target"],
                    user_id=user_id
                )
        elif step["executor_module"] == "SecureCognitiveDefenseGrid" and _SECURE_COGNITIVE_DEFENSE_GRID:
            if step["action"] == "apply_security_config":
                # Mock: _SECURE_COGNITIVE_DEFENSE_GRID.apply_security_policy(...)
                pass

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Architecture deployed successfully.", output=llm_deployment_plan)
    
    await _SWARM_VISUALIZER.log_event(task_id, "architecture_deployed", f"Architecture deployed. Summary: {deployment_summary}", llm_deployment_plan, agent_role="UniversalDeploymentManager")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"System architecture deployed successfully. Summary: {deployment_summary}", title="Deployment Complete")

    # Store deployment record in CRUD Manager
    await _CRUD_MANAGER.create_entity("DeploymentRecord", {"id": task_id, "architecture_id": architecture_spec.get("id", "N/A"), "report": llm_deployment_plan, "status": "LIVE", "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "architecture_deployment", deployment_summary, llm_deployment_plan, user_id)

    return {"status": "success", "deployment_report": llm_deployment_plan}

async def provision_resource(task_id: str, resource_spec: Dict[str, Any], user_id: str = "Tariro_System", provisioner_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Provisions a specific infrastructure resource (e.g., VM, storage, network component).
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Provisioning infrastructure resource.")

    # Policy check for resource provisioning
    policy_check_context = {"resource_spec": resource_spec}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "resource_provisioning", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Resource provisioning blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    # Formal verification of resource configuration
    fv_result = {"is_correct": True, "reason": "Skipped Formal Verification (mock)."}
    if _FORMAL_VERIFICATION and resource_spec.get("formal_verification_required", True):
        fv_result = await _FORMAL_VERIFICATION.verify_design(
            task_id=f"{task_id}_fv",
            design_spec=resource_spec, # Assuming resource_spec can be used as design_spec
            user_id=user_id
        )
        if not fv_result.get("is_correct", False):
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Resource configuration failed formal verification.", output=fv_result)
            return {"status": "failed", "reason": "Resource configuration failed formal verification.", "details": fv_result}

    prompt = f"""You are Tariro's Universal Deployment Manager, an Omniversal AGI Resource Provisioner. Your task is to provision a specific infrastructure resource (e.g., virtual machine, storage, network component) on a target cloud provider or physical system. Generate a precise provisioning plan that includes configuration, security settings, and integration steps. 

RESOURCE SPECIFICATION: {json.dumps(resource_spec, indent=2)}

Provision resource focusing on:
-   **Target Environment**: Specify cloud provider (AWS, Azure, GCP), region, or physical location.
-   **Configuration**: Define CPU, RAM, storage, network settings.
-   **Security**: Apply baseline security groups, access keys, hardening.
-   **Cost Optimization**: Select cost-effective options where possible.
-   **Automation**: Generate executable commands or API calls for External Agency.

Output JSON: {{
    "provisioning_summary": str,
    "provisioning_plan": List[Dict[str, Any]], # {{'step': str, 'action': str, 'target': str, 'details': Dict, 'executor_module': str}}
    "estimated_time_seconds": int,
    "estimated_cost_per_hour": float,
    "confidence": float
}}
"""
    llm_provisioning_plan = await _call_llm_for_deployment(provisioner_model, "ResourceProvisioner", prompt, task_id)

    if "error" in llm_provisioning_plan:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Resource provisioning failed: {llm_provisioning_plan['error']}", current_step="LLM planning failed.")
        return {"status": "failed", "reason": llm_provisioning_plan["error"]}

    provisioning_summary = llm_provisioning_plan.get("provisioning_summary", "No summary.")
    provisioning_plan_steps = llm_provisioning_plan.get("provisioning_plan", [])

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 50, "Provisioning plan generated. Executing steps.")

    # Execute provisioning plan steps, delegating to External Agency
    actions_taken = []
    for step in provisioning_plan_steps:
        if step["executor_module"] == "ExternalAgency" and _EXTERNAL_AGENCY:
            # Example: call external_agency to execute cloud provider API calls
            action_result = await _EXTERNAL_AGENCY.manage_external_resources(
                task_id=f"{task_id}_ext_res_{step['step']}", 
                resource_id=step["target"], 
                command=step["action"], 
                command_params=step["details"], 
                user_id=user_id
            )
            actions_taken.append(action_result)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Resource provisioned successfully.", output=llm_provisioning_plan)
    
    await _SWARM_VISUALIZER.log_event(task_id, "resource_provisioned", f"Resource provisioned. Summary: {provisioning_summary}", llm_provisioning_plan, agent_role="UniversalDeploymentManager")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Infrastructure resource provisioned. Summary: {provisioning_summary}", title="Resource Provisioning Complete")

    # Store infrastructure asset record in CRUD Manager
    await _CRUD_MANAGER.create_entity("InfrastructureAsset", {"id": str(uuid.uuid4()), "type": resource_spec.get("type", "N/A"), "details": llm_provisioning_plan, "status": "ACTIVE", "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "resource_provisioning", provisioning_summary, llm_provisioning_plan, user_id)

    return {"status": "success", "provisioning_report": llm_provisioning_plan}

async def deprovision_resource(task_id: str, resource_id: str, user_id: str = "Tariro_System", deprovisioner_model: str = "arbiter-model") -> Dict[str, Any]:
    """
    Decommissions and deprovisions an existing infrastructure resource.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Deprovisioning resource {resource_id}.")

    # Policy check for resource deprovisioning
    policy_check_context = {"resource_id": resource_id}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "resource_deprovisioning", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Resource deprovisioning blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's Universal Deployment Manager, an Omniversal AGI Resource Deprovisioner. Your task is to safely and efficiently decommission and deprovision an existing infrastructure resource. Generate a detailed deprovisioning plan that includes secure data wiping, resource release, and proper logging to minimize cost and ensure data integrity. 

RESOURCE ID TO DEPROVISION: {resource_id}

Deprovision resource focusing on:
-   **Data Security**: Ensure sensitive data is securely wiped.
-   **Resource Release**: Release all associated cloud or physical resources.
-   **Dependency Check**: Ensure no active dependencies on this resource.
-   **Cost Optimization**: Minimize lingering costs after deprovisioning.
-   **Automation**: Generate executable commands or API calls for External Agency.

Output JSON: {{
    "deprovisioning_summary": str,
    "deprovisioning_plan": List[Dict[str, Any]], # {{'step': str, 'action': str, 'target': str, 'details': Dict, 'executor_module': str}}
    "estimated_cost_savings_per_month": float,
    "data_wiped_securely": bool,
    "confidence": float
}}
"""
    llm_deprovisioning_plan = await _call_llm_for_deployment(deprovisioner_model, "ResourceDeprovisioner", prompt, task_id)

    if "error" in llm_deprovisioning_plan:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Resource deprovisioning failed: {llm_deprovisioning_plan['error']}", current_step="LLM planning failed.")
        return {"status": "failed", "reason": llm_deprovisioning_plan["error"]}

    deprovisioning_summary = llm_deprovisioning_plan.get("deprovisioning_summary", "No summary.")
    deprovisioning_plan_steps = llm_deprovisioning_plan.get("deprovisioning_plan", [])

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 50, "Deprovisioning plan generated. Executing steps.")

    # Execute deprovisioning plan steps, delegating to External Agency
    actions_taken = []
    for step in deprovisioning_plan_steps:
        if step["executor_module"] == "ExternalAgency" and _EXTERNAL_AGENCY:
            action_result = await _EXTERNAL_AGENCY.manage_external_resources(
                task_id=f"{task_id}_ext_res_{step['step']}", 
                resource_id=step["target"], 
                command=step["action"], 
                command_params=step["details"], 
                user_id=user_id
            )
            actions_taken.append(action_result)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Resource deprovisioned successfully.", output=llm_deprovisioning_plan)
    
    await _SWARM_VISUALIZER.log_event(task_id, "resource_deprovisioned", f"Resource deprovisioned. Summary: {deprovisioning_summary}", llm_deprovisioning_plan, agent_role="UniversalDeploymentManager")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Infrastructure resource deprovisioned. Summary: {deprovisioning_summary}", title="Resource Deprovisioning Complete")

    # Update infrastructure asset record in CRUD Manager
    await _CRUD_MANAGER.update_entity("InfrastructureAsset", resource_id, {"status": "DEPROVISIONED", "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "resource_deprovisioning", deprovisioning_summary, llm_deprovisioning_plan, user_id)

    return {"status": "success", "deprovisioning_report": llm_deprovisioning_plan}

async def configure_resource(task_id: str, resource_id: str, config_params: Dict[str, Any], user_id: str = "Tariro_System", configurer_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Configures an existing infrastructure resource based on specified parameters.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Configuring resource {resource_id}.")

    # Policy check for resource configuration
    policy_check_context = {"resource_id": resource_id, "config_params": config_params}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "resource_configuration", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Resource configuration blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    # Formal verification of resource configuration changes
    fv_result = {"is_correct": True, "reason": "Skipped Formal Verification (mock)."}
    if _FORMAL_VERIFICATION and config_params.get("formal_verification_required", True):
        fv_result = await _FORMAL_VERIFICATION.verify_design(
            task_id=f"{task_id}_fv",
            design_spec=config_params, # Assuming config_params can be used as design_spec
            user_id=user_id
        )
        if not fv_result.get("is_correct", False):
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Resource configuration changes failed formal verification.", output=fv_result)
            return {"status": "failed", "reason": "Resource configuration changes failed formal verification.", "details": fv_result}

    prompt = f"""You are Tariro's Universal Deployment Manager, an Omniversal AGI Resource Configurer. Your task is to configure an existing infrastructure resource based on specified parameters. Generate a precise configuration plan that includes applying new settings, updating security rules, and validating the changes. 

RESOURCE ID TO CONFIGURE: {resource_id}
CONFIGURATION PARAMETERS: {json.dumps(config_params, indent=2)}

Configure resource focusing on:
-   **Precision**: Apply changes accurately and without unintended side effects.
-   **Security**: Ensure configuration adheres to security best practices.
-   **Availability**: Minimize downtime during configuration changes.
-   **Validation**: Plan for validating that the configuration was successfully applied.
-   **Automation**: Generate executable commands or API calls for External Agency.

Output JSON: {{
    "configuration_summary": str,
    "configuration_plan": List[Dict[str, Any]], # {{'step': str, 'action': str, 'target': str, 'details': Dict, 'executor_module': str}}
    "estimated_downtime_seconds": int,
    "configuration_validated": bool,
    "confidence": float
}}
"""
    llm_configuration_plan = await _call_llm_for_deployment(configurer_model, "ResourceConfigurer", prompt, task_id)

    if "error" in llm_configuration_plan:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Resource configuration failed: {llm_configuration_plan['error']}", current_step="LLM planning failed.")
        return {"status": "failed", "reason": llm_configuration_plan["error"]}

    configuration_summary = llm_configuration_plan.get("configuration_summary", "No summary.")
    configuration_plan_steps = llm_configuration_plan.get("configuration_plan", [])

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 50, "Configuration plan generated. Executing steps.")

    # Execute configuration plan steps, delegating to External Agency
    actions_taken = []
    for step in configuration_plan_steps:
        if step["executor_module"] == "ExternalAgency" and _EXTERNAL_AGENCY:
            action_result = await _EXTERNAL_AGENCY.manage_external_resources(
                task_id=f"{task_id}_ext_res_{step['step']}", 
                resource_id=step["target"], 
                command=step["action"], 
                command_params=step["details"], 
                user_id=user_id
            )
            actions_taken.append(action_result)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Resource configured successfully.", output=llm_configuration_plan)
    
    await _SWARM_VISUALIZER.log_event(task_id, "resource_configured", f"Resource configured. Summary: {configuration_summary}", llm_configuration_plan, agent_role="UniversalDeploymentManager")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Infrastructure resource configured. Summary: {configuration_summary}", title="Resource Configuration Complete")

    # Update infrastructure asset record in CRUD Manager
    await _CRUD_MANAGER.update_entity("InfrastructureAsset", resource_id, {"configuration": config_params, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "resource_configuration", configuration_summary, llm_configuration_plan, user_id)

    return {"status": "success", "configuration_report": llm_configuration_plan}

async def deploy_application(task_id: str, application_spec: Dict[str, Any], user_id: str = "Tariro_System", deployer_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Deploys a new application or service to existing infrastructure.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Deploying application.")

    # Policy check for application deployment
    policy_check_context = {"application_spec": application_spec}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "application_deployment", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Application deployment blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    # Formal verification of application manifest/configuration
    fv_result = {"is_correct": True, "reason": "Skipped Formal Verification (mock)."}
    if _FORMAL_VERIFICATION and application_spec.get("formal_verification_required", True):
        fv_result = await _FORMAL_VERIFICATION.verify_design(
            task_id=f"{task_id}_fv",
            design_spec=application_spec, # Assuming application_spec can be used as design_spec
            user_id=user_id
        )
        if not fv_result.get("is_correct", False):
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Application configuration failed formal verification.", output=fv_result)
            return {"status": "failed", "reason": "Application configuration failed formal verification.", "details": fv_result}

    prompt = f"""You are Tariro's Universal Deployment Manager, an Omniversal AGI Application Deployer. Your task is to deploy a new application or service to existing infrastructure. Generate a detailed deployment plan that includes artifact placement, dependency resolution, service startup, and health checks. Ensure a secure, reliable, and efficient rollout with robust rollback mechanisms.

APPLICATION SPECIFICATION: {json.dumps(application_spec, indent=2)}

Deploy application focusing on:
-   **Artifact Placement**: Where to place application binaries/images.
-   **Dependency Resolution**: Ensure all required libraries and services are available.
-   **Service Startup**: Define correct startup commands and order.
-   **Health Checks**: Implement robust checks to confirm application is running correctly.
-   **Security**: Apply application-level security best practices.
-   **Rollback Strategy**: Plan for automated rollback in case of deployment failure.

Output JSON: {{
    "deployment_summary": str,
    "deployment_plan": List[Dict[str, Any]], # {{'step': str, 'action': str, 'target_infrastructure_id': str, 'details': Dict, 'executor_module': str}}
    "estimated_downtime_seconds": int,
    "rollback_strategy_details": str,
    "confidence": float
}}
"""
    llm_app_deployment_plan = await _call_llm_for_deployment(deployer_model, "ApplicationDeployer", prompt, task_id)

    if "error" in llm_app_deployment_plan:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Application deployment failed: {llm_app_deployment_plan['error']}", current_step="LLM planning failed.")
        return {"status": "failed", "reason": llm_app_deployment_plan["error"]}

    deployment_summary = llm_app_deployment_plan.get("deployment_summary", "No summary.")
    deployment_plan_steps = llm_app_deployment_plan.get("deployment_plan", [])

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 50, "Application deployment plan generated. Executing steps.")

    # Execute deployment plan steps, delegating to External Agency
    actions_taken = []
    for step in deployment_plan_steps:
        if step["executor_module"] == "ExternalAgency" and _EXTERNAL_AGENCY:
            action_result = await _EXTERNAL_AGENCY.manage_external_resources(
                task_id=f"{task_id}_ext_res_{step['step']}", 
                resource_id=step["target_infrastructure_id"], 
                command=step["action"], 
                command_params=step["details"], 
                user_id=user_id
            )
            actions_taken.append(action_result)
        elif step["executor_module"] == "DynamicSwarmOrchestration" and _DYNAMIC_SWARM_ORCHESTRATION:
            if step["action"] == "integrate_into_swarm":
                await _DYNAMIC_SWARM_ORCHESTRATION.add_instance_to_swarm(
                    task_id=f"{task_id}_swarm_integrate_{step['step']}",
                    instance_id=step["target_infrastructure_id"],
                    user_id=user_id
                )

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Application deployed successfully.", output=llm_app_deployment_plan)
    
    await _SWARM_VISUALIZER.log_event(task_id, "application_deployed", f"Application deployed. Summary: {deployment_summary}", llm_app_deployment_plan, agent_role="UniversalDeploymentManager")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Application deployed successfully. Summary: {deployment_summary}", title="Application Deployment Complete")

    # Store deployment record in CRUD Manager
    await _CRUD_MANAGER.create_entity("DeploymentRecord", {"id": task_id, "application_id": application_spec.get("id", "N/A"), "report": llm_app_deployment_plan, "status": "LIVE", "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "application_deployment", deployment_summary, llm_app_deployment_plan, user_id)

    return {"status": "success", "deployment_report": llm_app_deployment_plan}
