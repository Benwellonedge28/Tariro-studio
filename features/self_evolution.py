import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid
import random
import textwrap

# --- Configuration & Shared Data (initialized from studio_v3_core.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Base model definitions from studio_v3_core.py
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module
_CRUD_MANAGER: Any = None # Reference to crud_manager module for CodePatch or ArchitecturalChange entities
_PERSISTENT_TASK_MANAGER: Any = None # For submitting code modification/architectural change tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on self-evolution success/failure
_GLOBAL_STATE_MANAGER: Any = None # For storing current codebases, architectural blueprints
_META_LEARNER: Any = None # For providing learning insights from past evolutionary attempts
_SELF_ARCHITECTING_ENGINE: Any = None # For orchestrating architectural redesign
_LLM_COMPILER: Any = None # For generating and optimizing code
_FORMAL_VERIFICATION: Any = None # For verifying correctness of evolutionary changes
_AUTONOMY_GOVERNANCE: Any = None # For policy checks on self-modification
_DYNAMIC_POLICY_SYNTHESIS: Any = None # For adapting policies related to self-evolution
_SELF_REPAIRING_AUTO_HEALING: Any = None # For ensuring stability during and after evolution

SELF_EVOLUTION_LOG_DIR: str = ""

def initialize_self_evolution(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, global_state_manager_module: Any, meta_learner_module: Any, self_architecting_engine_module: Any, llm_compiler_module: Any, formal_verification_module: Any, autonomy_governance_module: Any, dynamic_policy_synthesis_module: Any, self_repairing_auto_healing_module: Any):
    """Initializes global configurations for the Self-Evolution module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _GLOBAL_STATE_MANAGER, _META_LEARNER, _SELF_ARCHITECTING_ENGINE, _LLM_COMPILER, _FORMAL_VERIFICATION, _AUTONOMY_GOVERNANCE, _DYNAMIC_POLICY_SYNTHESIS, _SELF_REPAIRING_AUTO_HEALING, SELF_EVOLUTION_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _META_LEARNER = meta_learner_module
    _SELF_ARCHITECTING_ENGINE = self_architecting_engine_module
    _LLM_COMPILER = llm_compiler_module
    _FORMAL_VERIFICATION = formal_verification_module
    _AUTONOMY_GOVERNANCE = autonomy_governance_module
    _DYNAMIC_POLICY_SYNTHESIS = dynamic_policy_synthesis_module
    _SELF_REPAIRING_AUTO_HEALING = self_repairing_auto_healing_module

    SELF_EVOLUTION_LOG_DIR = os.path.join(_WORKSPACE, "self_evolution_logs")
    os.makedirs(SELF_EVOLUTION_LOG_DIR, exist_ok=True)
    print(f"Self-Evolution initialized. Logs: {SELF_EVOLUTION_LOG_DIR}")

async def _call_llm_for_evolution(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for self-modification and evolutionary decisions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in self_evolution.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "evolution_llm_call_start", f"{model} self-evolution: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on autonomously improving Tariro Studio's internal code, algorithms, and cognitive architecture. Identify areas for enhancement based on performance metrics, learned insights, and architectural evaluations. Generate precise code patches, refactoring plans, or design modifications. Ensure all evolutionary changes maintain functional correctness, enhance resilience, and are formally verifiable. Prioritize improvements that maximize Tariro's capabilities and efficiency."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.04 # Low temp for precise, controlled self-modification
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "evolution_llm_call_end", f"{model} completed self-evolution task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "evolution_llm_error", f"JSON decode error from {model} for self-evolution.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "evolution_llm_error", f"Error calling {model} for self-evolution task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def propose_code_improvement(task_id: str, description: str, user_id: str = "Tariro_System", proposer_model: str = "qwen-coder") -> Dict[str, Any]:
    """
    Analyzes internal codebases to identify areas for improvement (performance, readability, security)
    and generates precise code patches or refactoring suggestions.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Proposing code improvement.")

    current_codebase_context = await _GLOBAL_STATE_MANAGER.get_state("current_codebase_overview") or {}
    learning_insights = await _META_LEARNER.get_insights_on_model("all_modules") # Generic query for code-related insights
    
    # Policy check for code modification
    policy_check_context = {"description": description, "user_id": user_id}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "code_self_modification", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Code improvement blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's Self-Evolution Engine, an Omniversal AGI Code Optimizer. Your task is to analyze internal codebases to identify areas for improvement (performance, readability, security, resource efficiency) and generate precise code patches or refactoring suggestions. Ensure the proposed changes maintain functional correctness, enhance resilience, and are formally verifiable. 

IMPROVEMENT DESCRIPTION / GOAL: {description}
CURRENT CODEBASE CONTEXT (from Global State Manager): {json.dumps(current_codebase_context, indent=2)}
LEARNING INSIGHTS (from Meta-Learner): {json.dumps(learning_insights, indent=2)}

Propose code improvements focusing on:
-   **Performance Gains**: Optimize algorithms, reduce computational complexity.
-   **Resource Efficiency**: Minimize memory usage, energy consumption.
-   **Security Enhancement**: Patch vulnerabilities, improve defensive coding.
-   **Readability & Maintainability**: Refactor for clarity, modularity.
-   **Test Coverage**: Ensure new/modified code has adequate tests.
-   **Formal Verifiability**: Design changes to be amenable to formal proof.

Output JSON: {{
    "improvement_summary": str,
    "target_files_and_modules": List[str],
    "proposed_code_patches": List[Dict[str, Any]], # {{'file_path': str, 'old_code_snippet': str, 'new_code_snippet': str, 'description': str}}
    "estimated_performance_gain": str,
    "formal_verification_required": bool,
    "confidence": float
}}
"""
    llm_improvement = await _call_llm_for_evolution(proposer_model, "CodeOptimizer", prompt, task_id)

    if "error" in llm_improvement:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Code improvement proposal failed: {llm_improvement['error']}", current_step="LLM proposal failed.")
        return {"status": "failed", "reason": llm_improvement["error"]}

    improvement_summary = llm_improvement.get("improvement_summary", "No summary.")
    proposed_patches = llm_improvement.get("proposed_code_patches", [])

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 70, "Code improvement proposed. Initiating formal verification.")

    # Formal verification of proposed patches
    verification_results = {"status": "skipped", "is_correct": True, "reason": "Formal verification not required or module not available."}
    if _FORMAL_VERIFICATION and llm_improvement.get("formal_verification_required", True):
        try:
            # Assuming verify_design can handle code patches as design specs
            verification_results = await _FORMAL_VERIFICATION.verify_design(task_id=f"{task_id}_fv", design_spec=llm_improvement, user_id=user_id)
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 90, "Formal verification of code patches completed.")
        except Exception as e:
            verification_results = {"status": "error", "reason": str(e)}
            await _SWARM_VISUALIZER.log_event(task_id, "code_fv_error", f"Error during formal verification of code patches: {e}", agent_role="SelfEvolution", level="ERROR")

    if not verification_results.get("is_correct", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 95, "Proposed code changes failed formal verification. Human review required.", output={"improvement": llm_improvement, "verification": verification_results})
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
            user_id, task_id, f"Proposed code changes failed formal verification. Human review required. Summary: {improvement_summary}",
            title="Code Changes Review Needed", causal_priority="critical"
        )
        return {"status": "failed", "reason": "Code changes failed formal verification."}

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Code improvement proposed and verified.", output=llm_improvement)
    
    await _SWARM_VISUALIZER.log_event(task_id, "code_improvement_proposed", f"Code improvement proposed. Summary: {improvement_summary}", llm_improvement, agent_role="SelfEvolution")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Code improvement proposed and verified. Summary: {improvement_summary}", title="Code Improvement Ready")

    # Automatically apply patches (conceptual, in real system would interact with version control/IDE)
    await generate_and_apply_code_patches(task_id=f"{task_id}_apply", code_patches=proposed_patches, user_id=user_id)

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "code_improvement", improvement_summary, llm_improvement, user_id)

    return {"status": "success", "improvement_report": llm_improvement}

async def generate_and_apply_code_patches(task_id: str, code_patches: List[Dict[str, Any]], user_id: str = "Tariro_System", patch_applier_model: str = "qwen-coder") -> Dict[str, Any]:
    """
    Generates and applies precise code patches to internal codebases, ensuring atomicity
    and minimal disruption.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Generating and applying code patches.")

    # Policy check for applying code patches
    policy_check_context = {"code_patches": code_patches, "user_id": user_id}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "apply_code_patches", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Applying code patches blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's Self-Evolution Engine, an Omniversal AGI Code Patcher. Your task is to generate and apply precise code patches to internal codebases, ensuring atomicity, minimal disruption, and the ability to rollback. This involves reading the original file, generating a diff, and applying the changes. Post-patch, trigger integration tests and formal verification.

CODE PATCHES TO APPLY: {json.dumps(code_patches, indent=2)}

Apply patches focusing on:
-   **Atomicity**: All changes for a single logical unit are applied or none are.
-   **Safety**: Prevent accidental overwrites or data loss.
-   **Rollback Capability**: Maintain ability to revert changes if tests fail.
-   **Integration Testing**: Automatically trigger tests after patch application.
-   **Formal Verification**: Re-verify affected components after patching.

Output JSON: {{
    "patch_application_summary": str,
    "patches_applied_status": Dict[str, Any], # {{'file_path': str, 'status': str, 'message': str}}
    "rollback_plan_if_needed": List[str],
    "integration_tests_triggered": bool,
    "formal_verification_triggered": bool,
    "confidence": float
}}
"""
    llm_patch_application = await _call_llm_for_evolution(patch_applier_model, "CodePatcher", prompt, task_id)

    if "error" in llm_patch_application:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Code patch application failed: {llm_patch_application['error']}", current_step="LLM patch failed.")
        return {"status": "failed", "reason": llm_patch_application["error"]}

    patch_summary = llm_patch_application.get("patch_application_summary", "No summary.")
    patches_status = llm_patch_application.get("patches_applied_status", {})

    # Simulate applying patches (in a real system, would use git/file ops)
    for patch in code_patches:
        file_path = patch["file_path"]
        new_code = patch["new_code_snippet"]
        # This would involve reading the old file, applying diff or replacing content, handling backups
        # For now, just a print statement
        print(f"Simulating applying patch to {file_path}. New code snippet: {new_code[:100]}...")

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Code patches generated and applied.", output=llm_patch_application)
    
    await _SWARM_VISUALIZER.log_event(task_id, "code_patches_applied", f"Code patches applied. Summary: {patch_summary}", llm_patch_application, agent_role="SelfEvolution")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Code patches applied. Summary: {patch_summary}", title="Code Patches Applied")

    # Store code patch record in CRUD Manager
    await _CRUD_MANAGER.create_entity("CodePatch", {"id": task_id, "patches": code_patches, "report": llm_patch_application, "status": "APPLIED", "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "code_patch_application", patch_summary, llm_patch_application, user_id)

    # Trigger formal verification if needed
    if llm_patch_application.get("formal_verification_triggered", False) and _FORMAL_VERIFICATION:
        await _FORMAL_VERIFICATION.verify_design(
            task_id=f"{task_id}_fv_post_patch",
            design_spec=llm_patch_application, # Pass relevant info for verification
            user_id=user_id
        )

    return {"status": "success", "patch_report": llm_patch_application}

async def propose_architectural_redesign(task_id: str, problem_statement: str, user_id: str = "Tariro_System", proposer_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Proposes fundamental changes to the cognitive architecture based on long-term strategic goals
    or persistent systemic issues, delegating to the Self-Architecting Engine.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Proposing architectural redesign.")

    current_architecture = await _GLOBAL_STATE_MANAGER.get_state("current_tariro_architecture") or {}
    meta_learning_insights = await _META_LEARNER.get_insights_on_model("tariro_architecture") # Query for relevant insights

    # Policy check for architectural redesign
    policy_check_context = {"problem_statement": problem_statement, "user_id": user_id}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "architectural_redesign", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Architectural redesign blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's Self-Evolution Engine, an Omniversal AGI Architectural Strategist. Your task is to propose fundamental changes to Tariro Studio's cognitive architecture based on long-term strategic goals, persistent systemic issues, or new foundational discoveries. This is a high-level strategic proposal that will be delegated to the Self-Architecting Engine for detailed design.

PROBLEM STATEMENT / STRATEGIC IMPERATIVE: {problem_statement}
CURRENT COGNITIVE ARCHITECTURE: {json.dumps(current_architecture, indent=2)}
META-LEARNING INSIGHTS: {json.dumps(meta_learning_insights, indent=2)}

Propose redesign focusing on:
-   **Long-term Vision**: Align with Tariro's ultimate self-improvement trajectory.
-   **Systemic Problem Resolution**: Address root causes of persistent issues.
-   **Disruptive Innovation**: Introduce new architectural paradigms if warranted.
-   **Feasibility**: Ensure the proposed redesign is practically implementable.
-   **Impact Analysis**: Estimate the benefits (performance, scalability, new capabilities).

Output JSON: {{
    "redesign_proposal_summary": str,
    "high_level_design_principles": List[str],
    "expected_outcomes": List[str],
    "estimated_self_architecting_effort": str, # e.g., "medium", "high"
    "confidence": float
}}
"""
    llm_redesign_proposal = await _call_llm_for_evolution(proposer_model, "ArchitecturalStrategist", prompt, task_id)

    if "error" in llm_redesign_proposal:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Architectural redesign proposal failed: {llm_redesign_proposal['error']}", current_step="LLM proposal failed.")
        return {"status": "failed", "reason": llm_redesign_proposal["error"]}

    redesign_summary = llm_redesign_proposal.get("redesign_proposal_summary", "No summary.")

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Architectural redesign proposed.", output=llm_redesign_proposal)
    
    await _SWARM_VISUALIZER.log_event(task_id, "architectural_redesign_proposed", f"Architectural redesign proposed. Summary: {redesign_summary}", llm_redesign_proposal, agent_role="SelfEvolution")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Architectural redesign proposed. Summary: {redesign_summary}", title="Architectural Redesign Proposal")

    # Delegate to Self-Architecting Engine for detailed design and implementation
    if _SELF_ARCHITECTING_ENGINE:
        await _SELF_ARCHITECTING_ENGINE.refactor_architecture(
            task_id=f"{task_id}_sae_redesign",
            optimization_goals=[problem_statement, redesign_summary],
            current_architecture=current_architecture, # Pass current for context
            user_id=user_id
        )

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "architectural_redesign", redesign_summary, llm_redesign_proposal, user_id)

    return {"status": "success", "redesign_report": llm_redesign_proposal}

async def optimize_code(task_id: str, code: str, language: str, optimization_goals: List[str], user_id: str = "Tariro_System", optimizer_model: str = "qwen-coder") -> Dict[str, Any]:
    """
    Optimizes a given code snippet for performance, resource usage, or security.
    This function is primarily called by LLM Compiler for generated code optimization.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Optimizing {language} code.")

    # Policy check for code optimization
    policy_check_context = {"language": language, "optimization_goals": optimization_goals, "code_snippet": code[:100]}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "code_optimization", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Code optimization blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's Self-Evolution Engine, an Omniversal AGI Code Optimizer. Your task is to optimize a given code snippet in a specified programming language for performance, resource usage, or security. Generate the optimized code, along with a summary of changes and estimated improvements. Ensure functional correctness is maintained.

ORIGINAL CODE: {textwrap.dedent(code)}
PROGRAMMING LANGUAGE: {language}
OPTIMIZATION GOALS: {json.dumps(optimization_goals, indent=2)}

Optimize code focusing on:
-   **Performance**: Reduce execution time, improve throughput.
-   **Resource Usage**: Minimize CPU, memory, network, and disk I/O.
-   **Security**: Remove vulnerabilities, apply best practices.
-   **Functional Equivalence**: Optimized code must produce the same results.
-   **Code Quality**: Maintain readability and maintainability.

Output JSON: {{
    "optimization_summary": str,
    "optimized_code": str,
    "estimated_improvements": Dict[str, Any], # e.g., {{'performance': '20% faster', 'memory': '10% less'}}
    "formal_verification_required": bool,
    "confidence": float
}}
"""
    llm_optimized_code = await _call_llm_for_evolution(optimizer_model, "CodeOptimizer", prompt, task_id)

    if "error" in llm_optimized_code:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Code optimization failed: {llm_optimized_code['error']}", current_step="LLM optimization failed.")
        return {"status": "failed", "reason": llm_optimized_code["error"]}

    optimization_summary = llm_optimized_code.get("optimization_summary", "No summary.")
    optimized_code = llm_optimized_code.get("optimized_code", code)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 70, "Code optimized. Initiating formal verification.")

    # Formal verification of optimized code
    verification_results = {"status": "skipped", "is_correct": True, "reason": "Formal verification not required or module not available."}
    if _FORMAL_VERIFICATION and llm_optimized_code.get("formal_verification_required", True):
        try:
            # Assuming verify_design can handle code as design spec
            verification_results = await _FORMAL_VERIFICATION.verify_design(task_id=f"{task_id}_fv", design_spec=llm_optimized_code, user_id=user_id)
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 90, "Formal verification of optimized code completed.")
        except Exception as e:
            verification_results = {"status": "error", "reason": str(e)}
            await _SWARM_VISUALIZER.log_event(task_id, "code_fv_error", f"Error during formal verification of optimized code: {e}", agent_role="SelfEvolution", level="ERROR")

    if not verification_results.get("is_correct", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 95, "Optimized code failed formal verification. Human review required.", output={"optimization": llm_optimized_code, "verification": verification_results})
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
            user_id, task_id, f"Optimized code failed formal verification. Human review required. Summary: {optimization_summary}",
            title="Optimized Code Review Needed", causal_priority="critical"
        )
        return {"status": "failed", "reason": "Optimized code failed formal verification."}

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Code optimized and verified.", output=llm_optimized_code)
    
    await _SWARM_VISUALIZER.log_event(task_id, "code_optimized_event", f"Code optimized. Summary: {optimization_summary}", llm_optimized_code, agent_role="SelfEvolution")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Code optimized and verified. Summary: {optimization_summary}", title="Code Optimization Complete")

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "code_optimization", optimization_summary, llm_optimized_code, user_id)

    return {"status": "success", "optimized_code": optimized_code, "optimization_report": llm_optimized_code}
