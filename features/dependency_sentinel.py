import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid
import random
import re

# --- Configuration & Shared Data (initialized from studio_v3_core.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Base model definitions from studio_v3_core.py
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module
_CRUD_MANAGER: Any = None # Reference to crud_manager module for Dependency or Environment entities
_PERSISTENT_TASK_MANAGER: Any = None # For submitting dependency resolution tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on missing dependencies or environment issues
_GLOBAL_STATE_MANAGER: Any = None # For storing environment configurations and installed dependencies
_EXTERNAL_AGENCY: Any = None # For interacting with package managers (apt, pip, cargo) in isolated environments
_LLM_COMPILER: Any = None # For analyzing compile commands and suggesting dependency installs
_SELF_ARCHITECTING_ENGINE: Any = None # For defining desired build environments
_AUTONOMY_GOVERNANCE: Any = None # For policy checks on environment modifications
_META_LEARNER: Any = None # For learning from successful dependency resolutions

DEPENDENCY_SENTINEL_LOG_DIR: str = ""

def initialize_dependency_sentinel(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, global_state_manager_module: Any, external_agency_module: Any, llm_compiler_module: Any, self_architecting_engine_module: Any, autonomy_governance_module: Any, meta_learner_module: Any):
    """Initializes global configurations for the Dependency Sentinel module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _GLOBAL_STATE_MANAGER, _EXTERNAL_AGENCY, _LLM_COMPILER, _SELF_ARCHITECTING_ENGINE, _AUTONOMY_GOVERNANCE, _META_LEARNER, DEPENDENCY_SENTINEL_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _EXTERNAL_AGENCY = external_agency_module
    _LLM_COMPILER = llm_compiler_module
    _SELF_ARCHITECTING_ENGINE = self_architecting_engine_module
    _AUTONOMY_GOVERNANCE = autonomy_governance_module
    _META_LEARNER = meta_learner_module

    DEPENDENCY_SENTINEL_LOG_DIR = os.path.join(_WORKSPACE, "dependency_sentinel_logs")
    os.makedirs(DEPENDENCY_SENTINEL_LOG_DIR, exist_ok=True)
    print(f"Dependency Sentinel initialized. Logs: {DEPENDENCY_SENTINEL_LOG_DIR}")

async def _call_llm_for_dependency(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for dependency resolution and environment management decisions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in dependency_sentinel.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "dep_sentinel_llm_call_start", f"{model} dependency resolution: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on autonomously detecting, resolving, and managing software dependencies and build environments for Tariro Studio's projects. This involves parsing error messages, identifying missing packages, generating installation commands, and orchestrating their execution in isolated sandboxed environments. Ensure reproducibility, security, and minimal impact on the host system."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.02 # Very low temp for precise command generation
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "dep_sentinel_llm_call_end", f"{model} completed dependency resolution task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "dep_sentinel_llm_error", f"JSON decode error from {model} for dependency resolution.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "dep_sentinel_llm_error", f"Error calling {model} for dependency resolution task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def resolve_missing_dependency(task_id: str, error_message: str, project_context: Dict[str, Any], user_id: str = "Tariro_System", resolver_model: str = "qwen-coder") -> Dict[str, Any]:
    """
    Analyzes a build or runtime error message to identify missing software dependencies
    and generates installation commands in an isolated environment.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Resolving missing dependency.")

    current_env_config = await _GLOBAL_STATE_MANAGER.get_state("current_build_environment") or {}
    # Use LLM Compiler to help parse compile commands for build system detection
    build_system_detection = await _LLM_COMPILER.compile_intent_to_code(
        task_id=f"{task_id}_detect_build_system",
        high_level_intent=f"Detect build system from compile command: {project_context.get('compile_command', '')[:100]}",
        target_language="json", # Request structured output
        user_id=user_id
    )
    if build_system_detection.get("status") != "success":
        build_system = "unknown" # Fallback
    else:
        build_system = build_system_detection.get("compilation_report", {}).get("generated_code", {"build_system": "unknown"}).get("build_system", "unknown")

    # Policy check for dependency installation
    policy_check_context = {"error_message": error_message, "project_context": project_context, "build_system": build_system}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "dependency_installation", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Dependency installation blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's Dependency Sentinel, an Omniversal AGI Dependency Resolver. Your task is to analyze a build or runtime error message, identify missing software dependencies, and generate precise installation commands for these dependencies. The installation must be orchestrated within an isolated sandboxed environment (e.g., Docker, Nix-shell, bwrap) to ensure reproducibility and minimal impact on the host system. 

ERROR MESSAGE: {error_message}
PROJECT CONTEXT (e.g., programming language, build system, OS): {json.dumps(project_context, indent=2)}
DETECTED BUILD SYSTEM: {build_system}
CURRENT ENVIRONMENT CONFIGURATION (from Global State Manager): {json.dumps(current_env_config, indent=2)}

Resolve dependencies focusing on:
-   **Error Parsing**: Extract the exact missing package or library name.
-   **Package Manager Selection**: Determine the correct package manager (apt, pip, cargo, npm, etc.) based on language/OS.
-   **Command Generation**: Formulate precise, non-interactive installation commands.
-   **Isolation Strategy**: Specify the sandboxing technology (e.g., Docker, bwrap, Nix-shell) to use.
-   **Security**: Ensure installation commands don't introduce vulnerabilities.

Output JSON: {{
    "resolution_summary": str,
    "missing_dependencies": List[str],
    "installation_commands": List[Dict[str, Any]], # {{'command': str, 'env_type': str, 'package_manager': str, 'sandbox_tech': str}}
    "estimated_install_time_seconds": int,
    "confidence": float
}}
"""
    llm_resolution = await _call_llm_for_dependency(resolver_model, "DependencyResolver", prompt, task_id)

    if "error" in llm_resolution:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Dependency resolution failed: {llm_resolution['error']}", current_step="LLM resolution failed.")
        return {"status": "failed", "reason": llm_resolution["error"]}

    resolution_summary = llm_resolution.get("resolution_summary", "No summary.")
    installation_commands = llm_resolution.get("installation_commands", [])

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 70, "Installation commands generated. Executing in sandbox.")

    # Execute installation commands in a sandbox via External Agency
    for cmd_spec in installation_commands:
        # Mocked external_agency interaction for running commands in a sandbox
        # In a real system, external_agency would interface with Docker/bwrap/Nix-shell APIs
        command_result = await _EXTERNAL_AGENCY.manage_external_resources(
            task_id=f"{task_id}_install_{uuid.uuid4().hex[:4]}",
            resource_id=cmd_spec.get("sandbox_tech", "docker_container"), # Resource ID for the sandbox
            command="run_command",
            command_params={
                "command": cmd_spec["command"],
                "env_type": cmd_spec["env_type"],
                "package_manager": cmd_spec["package_manager"]
            },
            user_id=user_id
        )
        if command_result.get("status") != "success":
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Dependency installation failed in sandbox.")
            return {"status": "failed", "reason": "Dependency installation failed in sandbox.", "details": command_result}

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Missing dependencies resolved.", output=llm_resolution)
    
    await _SWARM_VISUALIZER.log_event(task_id, "missing_dependencies_resolved", f"Missing dependencies resolved. Summary: {resolution_summary}", llm_resolution, agent_role="DependencySentinel")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Missing dependencies resolved for project. Summary: {resolution_summary}", title="Dependency Resolution Complete")

    # Store resolved dependency info in CRUD Manager
    await _CRUD_MANAGER.create_entity("Dependency", {"id": str(uuid.uuid4()), "project_context": project_context, "resolved_details": llm_resolution, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "dependency_resolution", resolution_summary, llm_resolution, user_id)

    return {"status": "success", "resolution_report": llm_resolution}

async def ensure_reproducible_environment(task_id: str, project_root: str, user_id: str = "Tariro_System", env_manager_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Analyzes a project's build process and dependencies to generate a reproducible environment
    (e.g., Dockerfile, Nix flake, virtual environment setup).
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Ensuring reproducible environment.")

    # Use Self-Architecting Engine to potentially suggest optimal environment definitions
    env_architecture_suggestion = await _SELF_ARCHITECTING_ENGINE.design_new_component(
        task_id=f"{task_id}_env_arch",
        requirements={
            "functionality": "Reproducible build environment for project",
            "project_type": project_root, # Pass project_root as context
            "isolation_level": "high"
        },
        user_id=user_id,
        designer_model="llama-architect" # Using architect model for this task
    )
    if env_architecture_suggestion.get("status") != "success":
        env_suggestion_summary = "No specific architectural suggestion."
    else:
        env_suggestion_summary = env_architecture_suggestion.get("design_report", {}).get("design_summary", "")

    # Policy check for environment generation
    policy_check_context = {"project_root": project_root, "env_suggestion": env_suggestion_summary}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "reproducible_environment_creation", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Environment creation blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's Dependency Sentinel, an Omniversal AGI Environment Replicator. Your task is to analyze a project's build process, dependencies, and desired characteristics to generate a fully reproducible build environment specification (e.g., Dockerfile, Nix flake, virtual environment setup). Ensure the environment is isolated, secure, and guarantees consistent builds.

PROJECT ROOT DIRECTORY (or project identifier): {project_root}
ARCHITECTURAL SUGGESTION (from Self-Architecting Engine): {env_suggestion_summary}

Generate reproducible environment focusing on:
-   **Dependency Pinning**: Specify exact versions of all dependencies.
-   **Isolation**: Ensure the environment is isolated from the host system.
-   **Reproducibility**: Guarantee that building within this environment yields identical results.
-   **Security**: Implement security best practices for the environment (e.g., minimal privileges).
-   **Tooling**: Include necessary compilers, build tools, and utilities.

Output JSON: {{
    "environment_summary": str,
    "generated_spec_type": str, # e.g., 'Dockerfile', 'Nixflake', 'requirements.txt'
    "generated_spec_content": str,
    "verification_commands": List[str],
    "confidence": float
}}
"""
    llm_env_spec = await _call_llm_for_dependency(env_manager_model, "EnvironmentReplicator", prompt, task_id)

    if "error" in llm_env_spec:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Reproducible environment generation failed: {llm_env_spec['error']}", current_step="LLM generation failed.")
        return {"status": "failed", "reason": llm_env_spec["error"]}

    env_summary = llm_env_spec.get("environment_summary", "No summary.")
    generated_spec_content = llm_env_spec.get("generated_spec_content", "")

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Reproducible environment generated.", output=llm_env_spec)
    
    await _SWARM_VISUALIZER.log_event(task_id, "reproducible_environment_generated", f"Reproducible environment generated. Summary: {env_summary}", llm_env_spec, agent_role="DependencySentinel")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Reproducible environment for project generated. Summary: {env_summary}", title="Environment Generation Complete")

    # Store environment spec in CRUD Manager
    await _CRUD_MANAGER.create_entity("Environment", {"id": str(uuid.uuid4()), "project_root": project_root, "spec_type": llm_env_spec.get("generated_spec_type"), "spec_content": generated_spec_content, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "reproducible_environment", env_summary, llm_env_spec, user_id)

    return {"status": "success", "environment_report": llm_env_spec}

async def update_dependency_catalog(task_id: str, new_dependency_info: Dict[str, Any], user_id: str = "Tariro_System", updater_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Updates the internal catalog of known dependencies, their versions, and common installation methods.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Updating dependency catalog.")

    current_catalog = await _GLOBAL_STATE_MANAGER.get_state("dependency_catalog") or {}
    
    prompt = f"""You are Tariro's Dependency Sentinel, an Omniversal AGI Dependency Catalog Updater. Your task is to update the internal catalog of known software dependencies. This includes adding new packages, updating version information, and recording common installation methods and any specific environment requirements. Ensure the catalog is accurate, comprehensive, and up-to-date.

NEW DEPENDENCY INFORMATION: {json.dumps(new_dependency_info, indent=2)}
CURRENT DEPENDENCY CATALOG (from Global State Manager): {json.dumps(current_catalog, indent=2)}

Update catalog focusing on:
-   **Accuracy**: Ensure information is correct and verifiable.
-   **Completeness**: Add all relevant details (versions, licenses, platforms).
-   **Installation Methods**: Document common commands for various package managers.
-   **Conflict Detection**: Identify potential conflicts with existing catalog entries.

Output JSON: {{
    "update_summary": str,
    "catalog_updated": bool,
    "updated_catalog_entry": Dict[str, Any],
    "confidence": float
}}
"""
    llm_catalog_update = await _call_llm_for_dependency(updater_model, "DependencyCatalogUpdater", prompt, task_id)

    if "error" in llm_catalog_update:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Dependency catalog update failed: {llm_catalog_update['error']}", current_step="LLM update failed.")
        return {"status": "failed", "reason": llm_catalog_update["error"]}

    update_summary = llm_catalog_update.get("update_summary", "No summary.")
    catalog_updated = llm_catalog_update.get("catalog_updated", False)
    updated_entry = llm_catalog_update.get("updated_catalog_entry", {})

    if catalog_updated:
        current_catalog[updated_entry.get("name")] = updated_entry
        await _GLOBAL_STATE_MANAGER.set_state("dependency_catalog", current_catalog, "Tariro_System", auditable=True)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Dependency catalog updated.", output=llm_catalog_update)
    
    await _SWARM_VISUALIZER.log_event(task_id, "dependency_catalog_updated", f"Dependency catalog updated. Summary: {update_summary}", llm_catalog_update, agent_role="DependencySentinel")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Dependency catalog updated. Summary: {update_summary}", title="Dependency Catalog Update Complete")

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "dependency_catalog_update", update_summary, llm_catalog_update, user_id)

    return {"status": "success", "catalog_report": llm_catalog_update}
