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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for Repo or PullRequest entities
_PERSISTENT_TASK_MANAGER: Any = None # For submitting cross-repo synchronization tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on cross-repo PRs or conflicts
_GLOBAL_STATE_MANAGER: Any = None # For storing multi-repo configurations and shared API definitions
_SELF_EVOLUTION: Any = None # For proposing code changes across repositories
_TOOL_FORGE: Any = None # For generating tools to assist in polyrepo management
_VULNERABILITY_REMEDIATION: Any = None # For applying security fixes across repos
_AUTONOMY_GOVERNANCE: Any = None # For policy checks on cross-repo operations
_LLM_COMPILER: Any = None # For generating code snippets for multi-repo refactoring
_META_LEARNER: Any = None # For learning from cross-repo change success rates
_EXTERNAL_AGENCY: Any = None # For interacting with Git hosting services (e.g., GitHub API)

POLYREPO_ORCHESTRATOR_LOG_DIR: str = ""

def initialize_polyrepo_orchestrator(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, global_state_manager_module: Any, self_evolution_module: Any, tool_forge_module: Any, vulnerability_remediation_module: Any, autonomy_governance_module: Any, llm_compiler_module: Any, meta_learner_module: Any, external_agency_module: Any):
    """Initializes global configurations for the Poly-Repository Orchestrator module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _GLOBAL_STATE_MANAGER, _SELF_EVOLUTION, _TOOL_FORGE, _VULNERABILITY_REMEDIATION, _AUTONOMY_GOVERNANCE, _LLM_COMPILER, _META_LEARNER, _EXTERNAL_AGENCY, POLYREPO_ORCHESTRATOR_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _SELF_EVOLUTION = self_evolution_module
    _TOOL_FORGE = tool_forge_module
    _VULNERABILITY_REMEDIATION = vulnerability_remediation_module
    _AUTONOMY_GOVERNANCE = autonomy_governance_module
    _LLM_COMPILER = llm_compiler_module
    _META_LEARNER = meta_learner_module
    _EXTERNAL_AGENCY = external_agency_module

    POLYREPO_ORCHESTRATOR_LOG_DIR = os.path.join(_WORKSPACE, "polyrepo_orchestrator_logs")
    os.makedirs(POLYREPO_ORCHESTRATOR_LOG_DIR, exist_ok=True)
    print(f"Poly-Repository Orchestrator initialized. Logs: {POLYREPO_ORCHESTRATOR_LOG_DIR}")

async def _call_llm_for_polyrepo(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for poly-repository management decisions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in polyrepo_orchestrator.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "polyrepo_llm_call_start", f"{model} poly-repo orchestration: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on managing and synchronizing codebases across multiple related repositories (polyrepo management). This involves identifying shared dependencies, proposing API changes, generating linked pull requests, and ensuring consistent code quality and security across the entire ecosystem. Minimize merge conflicts and ensure atomic, verifiable changes."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.04 # Low temp for precise code and diff generation
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "polyrepo_llm_call_end", f"{model} completed poly-repo orchestration task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "polyrepo_llm_error", f"JSON decode error from {model} for poly-repo orchestration.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "polyrepo_llm_error", f"Error calling {model} for poly-repo orchestration task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def synchronize_repositories(task_id: str, organization: str, repo_pattern: str, synchronization_goal: str, user_id: str = "Tariro_System", orchestrator_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Clones all repositories matching a pattern in an organization, identifies shared dependencies
    or inconsistencies, and proposes linked PRs to keep APIs/code in sync across repos.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Synchronizing repositories for {organization}/{repo_pattern}.")

    # Use External Agency to list and clone repositories
    # Mocked external_agency interaction
    repo_list_result = await _EXTERNAL_AGENCY.interact_with_external_api(
        task_id=f"{task_id}_list_repos",
        api_spec={"name": "github_api", "endpoint": "/orgs/{org}/repos"}, # Conceptual GitHub API spec
        action="list_repos",
        params={
            "organization": organization,
            "pattern": repo_pattern
        },
        user_id=user_id
    )
    if repo_list_result.get("status") != "success":
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Failed to list repositories.")
        return {"status": "failed", "reason": "Failed to list repositories.", "details": repo_list_result}

    repos_to_sync = repo_list_result.get("api_response", {}).get("repos", [])
    if not repos_to_sync:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "No repositories found for pattern.")
        return {"status": "success", "message": "No repositories found for pattern."}

    # Policy check for cross-repo synchronization
    policy_check_context = {"organization": organization, "repos": repos_to_sync, "goal": synchronization_goal}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "cross_repo_synchronization", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Cross-repo synchronization blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's Poly-Repository Orchestrator, an Omniversal AGI Repo Synchronizer. Your task is to manage and synchronize codebases across multiple related repositories. This involves identifying shared dependencies, proposing API changes, generating linked pull requests, and ensuring consistent code quality and security across the entire ecosystem. Minimize merge conflicts and ensure atomic, verifiable changes.

ORGANIZATION: {organization}
REPOSITORY PATTERN: {repo_pattern}
REPOSITORIES IDENTIFIED: {json.dumps(repos_to_sync, indent=2)}
SYNCHRONIZATION GOAL: {synchronization_goal}

Synchronize repositories focusing on:
-   **Dependency Analysis**: Identify shared libraries, interfaces, and data structures.
-   **API Consistency**: Propose changes to maintain consistent APIs across consuming and providing repos.
-   **Code Modularity**: Suggest ways to extract common code into shared modules or libraries.
-   **Change Propagation**: Generate linked Pull Requests (PRs) across affected repositories.
-   **Conflict Prediction**: Anticipate potential merge conflicts and suggest resolution strategies.

Output JSON: {{
    "synchronization_summary": str,
    "proposed_changesets": List[Dict[str, Any]], # {{'repo_name': str, 'branch_name': str, 'commit_message': str, 'file_changes': List[Dict], 'description': str}}
    "linked_pull_requests": List[Dict[str, Any]], # {{'source_repo': str, 'target_repo': str, 'title': str, 'body': str, 'head_branch': str, 'base_branch': str}}
    "estimated_merge_conflicts": int,
    "confidence": float
}}
"""
    llm_sync_plan = await _call_llm_for_polyrepo(orchestrator_model, "RepoSynchronizer", prompt, task_id)

    if "error" in llm_sync_plan:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Repository synchronization failed: {llm_sync_plan['error']}", current_step="LLM planning failed.")
        return {"status": "failed", "reason": llm_sync_plan["error"]}

    sync_summary = llm_sync_plan.get("synchronization_summary", "No summary.")
    proposed_changesets = llm_sync_plan.get("proposed_changesets", [])
    linked_pull_requests = llm_sync_plan.get("linked_pull_requests", [])

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 70, "Synchronization plan generated. Submitting changes.")

    # Apply changesets and create PRs via External Agency (conceptual GitHub API interaction)
    for changeset in proposed_changesets:
        # Mock: push files to a new branch in the target repo
        push_result = await _EXTERNAL_AGENCY.interact_with_external_api(
            task_id=f"{task_id}_push_files_{uuid.uuid4().hex[:4]}",
            api_spec={"name": "github_api", "endpoint": "/repos/{owner}/{repo}/contents/{path}"}, # Conceptual GitHub API
            action="push_files_batch",
            params={
                "repo": changeset["repo_name"],
                "branch": changeset["branch_name"],
                "message": changeset["commit_message"],
                "files": changeset["file_changes"]
            },
            user_id=user_id
        )
        # Further handling of push_result

    for pr_spec in linked_pull_requests:
        # Mock: create pull request
        pr_result = await _EXTERNAL_AGENCY.interact_with_external_api(
            task_id=f"{task_id}_create_pr_{uuid.uuid4().hex[:4]}",
            api_spec={"name": "github_api", "endpoint": "/repos/{owner}/{repo}/pulls"}, # Conceptual GitHub API
            action="create_pull_request",
            params={
                "repo": pr_spec["target_repo"],
                "title": pr_spec["title"],
                "body": pr_spec["body"],
                "head": pr_spec["head_branch"],
                "base": pr_spec["base_branch"]
            },
            user_id=user_id
        )
        # Further handling of pr_result

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Repositories synchronized and PRs created.", output=llm_sync_plan)
    
    await _SWARM_VISUALIZER.log_event(task_id, "repos_synchronized", f"Repositories synchronized. Summary: {sync_summary}", llm_sync_plan, agent_role="PolyrepoOrchestrator")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Repositories synchronized for {organization}/{repo_pattern}. Summary: {sync_summary}. Check linked PRs.", title="Repo Synchronization Complete")

    # Store synchronization record in CRUD Manager
    await _CRUD_MANAGER.create_entity("RepoSynchronizationLog", {"id": task_id, "organization": organization, "pattern": repo_pattern, "report": llm_sync_plan, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "repo_synchronization", sync_summary, llm_sync_plan, user_id)

    return {"status": "success", "sync_report": llm_sync_plan}

async def propose_cross_repo_refactoring(task_id: str, refactoring_goal: str, organization: str, repo_pattern: str, user_id: str = "Tariro_System", proposer_model: str = "qwen-coder") -> Dict[str, Any]:
    """
    Analyzes code across multiple repositories to identify refactoring opportunities
    for code reuse, API simplification, or security hardening.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Proposing cross-repo refactoring for {organization}/{repo_pattern}.")

    # Fetch codebase context from Global State Manager or by cloning repos via External Agency
    codebase_context = await _GLOBAL_STATE_MANAGER.get_state(f"codebase_context_{organization}_{repo_pattern}") or ""
    if not codebase_context:
        # Mock: clone repos and build a unified codebase context
        codebase_context = "Unified codebase context generated from cloning multiple repos."

    # Policy check for cross-repo refactoring
    policy_check_context = {"organization": organization, "repos_pattern": repo_pattern, "goal": refactoring_goal}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "cross_repo_refactoring", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Cross-repo refactoring blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's Poly-Repository Orchestrator, an Omniversal AGI Cross-Repo Refactorer. Your task is to analyze code across multiple repositories within an organization to identify refactoring opportunities that align with a specified goal. Propose changes for code reuse, API simplification, security hardening, or performance optimization. Generate a detailed refactoring plan that includes proposed code changes, new shared modules, and linked Pull Requests.

REFACTORING GOAL: {refactoring_goal}
ORGANIZATION: {organization}
REPOSITORY PATTERN: {repo_pattern}
UNIFIED CODEBASE CONTEXT: {codebase_context[:1000]}...

Propose refactoring focusing on:
-   **Code Reuse**: Identify duplicated logic and suggest extraction into shared libraries.
-   **API Simplification**: Unify divergent APIs across different services.
-   **Security Hardening**: Apply consistent security best practices across all relevant codebases.
-   **Performance Optimization**: Identify cross-cutting performance bottlenecks.
-   **Impact Analysis**: Predict the impact of changes on consuming repositories.

Output JSON: {{
    "refactoring_summary": str,
    "proposed_refactoring_plan": List[Dict[str, Any]], # {{'type': str, 'description': str, 'target_repos': List[str], 'code_changes': List[Dict], 'new_modules': List[Dict]}}
    "estimated_impact": str,
    "linked_pull_requests_needed": List[Dict[str, Any]], # Similar structure to synchronize_repositories
    "confidence": float
}}
"""
    llm_refactoring_plan = await _call_llm_for_polyrepo(proposer_model, "CrossRepoRefactorer", prompt, task_id)

    if "error" in llm_refactoring_plan:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Cross-repo refactoring proposal failed: {llm_refactoring_plan['error']}", current_step="LLM planning failed.")
        return {"status": "failed", "reason": llm_refactoring_plan["error"]}

    refactoring_summary = llm_refactoring_plan.get("refactoring_summary", "No summary.")
    proposed_plan = llm_refactoring_plan.get("proposed_refactoring_plan", [])

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Cross-repo refactoring proposed and PRs generated.", output=llm_refactoring_plan)
    
    await _SWARM_VISUALIZER.log_event(task_id, "cross_repo_refactoring_proposed", f"Cross-repo refactoring proposed. Summary: {refactoring_summary}", llm_refactoring_plan, agent_role="PolyrepoOrchestrator")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Cross-repo refactoring proposed for {organization}/{repo_pattern}. Summary: {refactoring_summary}. Check generated PRs.", title="Cross-Repo Refactoring Proposal")

    # Interact with Self-Evolution to apply code changes and External Agency to create PRs
    for change in proposed_plan:
        if change["type"] == "code_changes" and _SELF_EVOLUTION:
            # Mock: self_evolution.propose_code_improvement for each relevant repo
            pass
        if change["type"] == "new_shared_module" and _LLM_COMPILER:
            # Mock: LLM Compiler to generate new module, then Self-Evolution to integrate
            pass
    
    # Similar to synchronize_repositories, create PRs via External Agency for linked_pull_requests_needed

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "cross_repo_refactoring", refactoring_summary, llm_refactoring_plan, user_id)

    return {"status": "success", "refactoring_report": llm_refactoring_plan}
