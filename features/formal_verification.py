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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for VerificationResult or Specification entities
_PERSISTENT_TASK_MANAGER: Any = None # For submitting formal verification tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on verification success/failure
_GLOBAL_STATE_MANAGER: Any = None # For storing current specifications and verified states
_SELF_ARCHITECTING_ENGINE: Any = None # For providing designs to verify
_DYNAMIC_POLICY_SYNTHESIS: Any = None # For providing policies to verify
_SELF_REPAIRING_AUTO_HEALING: Any = None # For verifying repaired components
_AUTONOMY_GOVERNANCE: Any = None # For policy checks on verification actions
_META_LEARNER: Any = None # For learning from verification outcomes
_LLM_COMPILER: Any = None # For generating proof code or verification conditions

FORMAL_VERIFICATION_LOG_DIR: str = ""

def initialize_formal_verification(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, global_state_manager_module: Any, self_architecting_engine_module: Any, dynamic_policy_synthesis_module: Any, self_repairing_auto_healing_module: Any, autonomy_governance_module: Any, meta_learner_module: Any, llm_compiler_module: Any):
    """Initializes global configurations for the Formal Verification module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _GLOBAL_STATE_MANAGER, _SELF_ARCHITECTING_ENGINE, _DYNAMIC_POLICY_SYNTHESIS, _SELF_REPAIRING_AUTO_HEALING, _AUTONOMY_GOVERNANCE, _META_LEARNER, _LLM_COMPILER, FORMAL_VERIFICATION_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _SELF_ARCHITECTING_ENGINE = self_architecting_engine_module
    _DYNAMIC_POLICY_SYNTHESIS = dynamic_policy_synthesis_module
    _SELF_REPAIRING_AUTO_HEALING = self_repairing_auto_healing_module
    _AUTONOMY_GOVERNANCE = autonomy_governance_module
    _META_LEARNER = meta_learner_module
    _LLM_COMPILER = llm_compiler_module

    FORMAL_VERIFICATION_LOG_DIR = os.path.join(_WORKSPACE, "formal_verification_logs")
    os.makedirs(FORMAL_VERIFICATION_LOG_DIR, exist_ok=True)
    print(f"Formal Verification initialized. Logs: {FORMAL_VERIFICATION_LOG_DIR}")

async def _call_llm_for_verification(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for generating verification conditions or interpreting proof results."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in formal_verification.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "fv_llm_call_start", f"{model} formal verification: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on assisting with formal verification tasks. This involves generating formal specifications, translating designs/policies into verifiable conditions, interpreting proof results, and suggesting refinements to designs or proof strategies. Ensure mathematical rigor, logical consistency, and completeness in all verification-related outputs."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.01 # Extremely low temp for precise, deterministic logic
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "fv_llm_call_end", f"{model} completed formal verification task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "fv_llm_error", f"JSON decode error from {model} for formal verification.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "fv_llm_error", f"Error calling {model} for formal verification task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def verify_design(task_id: str, design_spec: Dict[str, Any], user_id: str = "Tariro_System", verifier_model: str = "arbiter-model") -> Dict[str, Any]:
    """
    Performs formal verification on a system design specification (e.g., architectural design, algorithm).
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Performing formal verification on design.")

    # Policy check for formal verification of designs
    policy_check_context = {"design_spec": design_spec}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "design_formal_verification", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Design verification blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's Formal Verification Engine, an Omniversal AGI Formal Design Verifier. Your task is to perform rigorous formal verification on a given system design specification. Translate the design into formal properties, generate proof obligations, and use (conceptual) automated theorem provers or model checkers to mathematically prove its correctness, safety, and adherence to requirements. 

DESIGN SPECIFICATION: {json.dumps(design_spec, indent=2)}

Perform verification focusing on:
-   **Correctness**: Does the design meet its functional requirements?
-   **Safety**: Does the design avoid undesirable states or behaviors?
-   **Liveness**: Does the design guarantee progress and eventual outcomes?
-   **Absence of Deadlock/Livelock**: Are concurrency issues prevented?
-   **Completeness**: Does the design cover all specified scenarios?
-   **Proof Strategy**: Outline the formal methods and tools used (conceptually).

Output JSON: {{
    "verification_summary": str,
    "is_correct": bool,
    "proof_log": str, # Conceptual output from theorem prover/model checker
    "identified_invariants": List[str],
    "counterexamples_found": List[Dict[str, Any]], # If not correct
    "confidence": float
}}
"""
    llm_verification = await _call_llm_for_verification(verifier_model, "FormalDesignVerifier", prompt, task_id)

    if "error" in llm_verification:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Design verification failed: {llm_verification['error']}", current_step="LLM verification failed.")
        return {"status": "failed", "reason": llm_verification["error"]}

    verification_summary = llm_verification.get("verification_summary", "No summary.")
    is_correct = llm_verification.get("is_correct", False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Design formal verification completed.", output=llm_verification)
    
    await _SWARM_VISUALIZER.log_event(task_id, "design_verified", f"Design verification completed. Correctness: {is_correct}. Summary: {verification_summary}", llm_verification, agent_role="FormalVerification")
    if not is_correct:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Design verification failed: {verification_summary}", title="Design Verification Failed", causal_priority="critical")
    else:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Design verification successful: {verification_summary}", title="Design Verified")

    # Store verification result in CRUD Manager
    await _CRUD_MANAGER.create_entity("VerificationResult", {"id": task_id, "verified_item_type": "design", "item_id": design_spec.get("id", "N/A"), "result": llm_verification, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "design_verification", verification_summary, llm_verification, user_id)

    return {"status": "success", "is_correct": is_correct, "verification_report": llm_verification}

async def verify_policy(task_id: str, policy_spec: Dict[str, Any], user_id: str = "Tariro_System", verifier_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Performs formal verification on an operational policy specification (e.g., access control, resource allocation).
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Performing formal verification on policy.")

    # Policy check for formal verification of policies
    policy_check_context = {"policy_spec": policy_spec}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "policy_formal_verification", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Policy verification blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's Formal Verification Engine, an Omniversal AGI Formal Policy Verifier. Your task is to perform rigorous formal verification on an operational policy specification. Translate the policy rules into formal logic, identify potential loopholes, contradictions, or unintended consequences, and mathematically prove its adherence to ethical guidelines and operational objectives. 

POLICY SPECIFICATION: {json.dumps(policy_spec, indent=2)}

Perform verification focusing on:
-   **Consistency**: Is the policy internally consistent? Are there any contradictions?
-   **Completeness**: Does the policy cover all relevant scenarios without ambiguity?
-   **Fairness**: Does the policy treat all relevant entities equitably?
-   **Robustness**: Can the policy be easily circumvented or exploited?
-   **Ethical Alignment**: Does it adhere to EVAS ethical principles (conceptually)?
-   **Proof Strategy**: Outline the formal methods and tools used (conceptually).

Output JSON: {{
    "verification_summary": str,
    "is_correct": bool,
    "proof_log": str, # Conceptual output from theorem prover/model checker
    "identified_loopholes": List[str],
    "contradictions_found": List[Dict[str, Any]], # If contradictions exist
    "confidence": float
}}
"""
    llm_verification = await _call_llm_for_verification(verifier_model, "FormalPolicyVerifier", prompt, task_id)

    if "error" in llm_verification:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Policy verification failed: {llm_verification['error']}", current_step="LLM verification failed.")
        return {"status": "failed", "reason": llm_verification["error"]}

    verification_summary = llm_verification.get("verification_summary", "No summary.")
    is_correct = llm_verification.get("is_correct", False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Policy formal verification completed.", output=llm_verification)
    
    await _SWARM_VISUALIZER.log_event(task_id, "policy_verified", f"Policy verification completed. Correctness: {is_correct}. Summary: {verification_summary}", llm_verification, agent_role="FormalVerification")
    if not is_correct:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Policy verification failed: {verification_summary}", title="Policy Verification Failed", causal_priority="critical")
    else:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Policy verification successful: {verification_summary}", title="Policy Verified")

    # Store verification result in CRUD Manager
    await _CRUD_MANAGER.create_entity("VerificationResult", {"id": task_id, "verified_item_type": "policy", "item_id": policy_spec.get("name", "N/A"), "result": llm_verification, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "policy_verification", verification_summary, llm_verification, user_id)

    return {"status": "success", "is_correct": is_correct, "verification_report": llm_verification}

async def verify_refactoring_plan(task_id: str, plan_spec: Dict[str, Any], user_id: str = "Tariro_System", verifier_model: str = "arbiter-model") -> Dict[str, Any]:
    """
    Performs formal verification on an architectural refactoring plan to ensure it maintains
    correctness and introduces no new bugs or vulnerabilities.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Performing formal verification on refactoring plan.")

    # Policy check for refactoring plan verification
    policy_check_context = {"plan_spec": plan_spec}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "refactoring_formal_verification", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Refactoring verification blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    current_architecture = await _GLOBAL_STATE_MANAGER.get_state("current_tariro_architecture") or {}
    
    prompt = f"""You are Tariro's Formal Verification Engine, an Omniversal AGI Refactoring Verifier. Your task is to perform rigorous formal verification on an architectural refactoring plan. Analyze the proposed changes against the original design specifications and system invariants. Mathematically prove that the refactoring preserves correctness, introduces no new bugs or vulnerabilities, and achieves its intended optimization goals.

REFACTORING PLAN SPECIFICATION: {json.dumps(plan_spec, indent=2)}
CURRENT SYSTEM ARCHITECTURE: {json.dumps(current_architecture, indent=2)}

Perform verification focusing on:
-   **Preservation of Invariants**: Ensure critical system properties remain true.
-   **Functional Equivalence**: Prove that the refactored system behaves identically for unchanged functionality.
-   **Absence of New Bugs**: Detect any unintended errors or side effects.
-   **Security Implications**: Assess for new vulnerabilities introduced by changes.
-   **Optimization Goal Attainment**: Verify that the refactoring achieves its stated performance, scalability, or other goals.
-   **Proof Strategy**: Outline the formal methods and tools used (conceptually).

Output JSON: {{
    "verification_summary": str,
    "is_correct": bool,
    "proof_log": str, # Conceptual output from theorem prover/model checker
    "new_bugs_introduced": List[str],
    "new_vulnerabilities": List[str],
    "confidence": float
}}
"""
    llm_verification = await _call_llm_for_verification(verifier_model, "FormalRefactoringVerifier", prompt, task_id)

    if "error" in llm_verification:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Refactoring verification failed: {llm_verification['error']}", current_step="LLM verification failed.")
        return {"status": "failed", "reason": llm_verification["error"]}

    verification_summary = llm_verification.get("verification_summary", "No summary.")
    is_correct = llm_verification.get("is_correct", False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Refactoring plan formal verification completed.", output=llm_verification)
    
    await _SWARM_VISUALIZER.log_event(task_id, "refactoring_verified", f"Refactoring plan verification completed. Correctness: {is_correct}. Summary: {verification_summary}", llm_verification, agent_role="FormalVerification")
    if not is_correct:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Refactoring plan verification failed: {verification_summary}", title="Refactoring Verification Failed", causal_priority="critical")
    else:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Refactoring plan verification successful: {verification_summary}", title="Refactoring Verified")

    # Store verification result in CRUD Manager
    await _CRUD_MANAGER.create_entity("VerificationResult", {"id": task_id, "verified_item_type": "refactoring_plan", "item_id": plan_spec.get("plan_id", "N/A"), "result": llm_verification, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "refactoring_verification", verification_summary, llm_verification, user_id)

    return {"status": "success", "is_correct": is_correct, "verification_report": llm_verification}

async def verify_repaired_component(task_id: str, component_spec: Dict[str, Any], user_id: str = "Tariro_System", verifier_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Performs formal verification on a repaired system component to ensure the fix is correct
    and introduces no regressions.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Performing formal verification on repaired component.")

    # Policy check for repaired component verification
    policy_check_context = {"component_spec": component_spec}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "repair_formal_verification", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Repaired component verification blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    original_spec = await _GLOBAL_STATE_MANAGER.get_state(f"original_spec_{component_spec.get('id')}") or {}
    
    prompt = f"""You are Tariro's Formal Verification Engine, an Omniversal AGI Repair Verifier. Your task is to perform rigorous formal verification on a repaired system component. Analyze the applied fix against the original specifications and the identified bug, and mathematically prove that the repair is correct, fully resolves the issue, and introduces no regressions or new vulnerabilities.

REPAIRED COMPONENT SPECIFICATION: {json.dumps(component_spec, indent=2)}
ORIGINAL COMPONENT SPECIFICATION: {json.dumps(original_spec, indent=2)}

Perform verification focusing on:
-   **Bug Resolution**: Confirm the original bug is completely fixed.
-   **Regression Absence**: Prove that no existing functionality has been broken.
-   **Side Effects**: Ensure no unintended negative side effects were introduced.
-   **Compliance**: Verify that the component still adheres to design and security policies.
-   **Proof Strategy**: Outline the formal methods and tools used (conceptually).

Output JSON: {{
    "verification_summary": str,
    "is_correct": bool,
    "proof_log": str, # Conceptual output from theorem prover/model checker
    "regressions_found": List[str],
    "new_bugs_introduced": List[str],
    "confidence": float
}}
"""
    llm_verification = await _call_llm_for_verification(verifier_model, "FormalRepairVerifier", prompt, task_id)

    if "error" in llm_verification:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Repaired component verification failed: {llm_verification['error']}", current_step="LLM verification failed.")
        return {"status": "failed", "reason": llm_verification["error"]}

    verification_summary = llm_verification.get("verification_summary", "No summary.")
    is_correct = llm_verification.get("is_correct", False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Repaired component formal verification completed.", output=llm_verification)
    
    await _SWARM_VISUALIZER.log_event(task_id, "repaired_component_verified", f"Repaired component verification completed. Correctness: {is_correct}. Summary: {verification_summary}", llm_verification, agent_role="FormalVerification")
    if not is_correct:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Repaired component verification failed: {verification_summary}", title="Repaired Component Verification Failed", causal_priority="critical")
    else:
        await _ASYCH_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Repaired component verification successful: {verification_summary}", title="Repaired Component Verified")

    # Store verification result in CRUD Manager
    await _CRUD_MANAGER.create_entity("VerificationResult", {"id": task_id, "verified_item_type": "repaired_component", "item_id": component_spec.get("id", "N/A"), "result": llm_verification, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "repair_verification", verification_summary, llm_verification, user_id)

    return {"status": "success", "is_correct": is_correct, "verification_report": llm_verification}

async def verify_system_invariant(task_id: str, invariant_spec: str, current_system_state: Dict[str, Any], user_id: str = "Tariro_System", verifier_model: str = "arbiter-model") -> Dict[str, Any]:
    """
    Verifies a critical system invariant against the current system state or a proposed state.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Verifying system invariant.")

    # Policy check for invariant verification
    policy_check_context = {"invariant_spec": invariant_spec, "current_system_state": current_system_state}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "invariant_formal_verification", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Invariant verification blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's Formal Verification Engine, an Omniversal AGI Invariant Verifier. Your task is to rigorously verify a critical system invariant against a given system state (current or proposed). Translate the invariant into formal logic and mathematically prove whether the system state satisfies this invariant. This ensures foundational properties of the system are always maintained.

INVARIANT SPECIFICATION: {invariant_spec}
SYSTEM STATE TO VERIFY: {json.dumps(current_system_state, indent=2)}

Perform verification focusing on:
-   **Logical Consistency**: Does the state adhere to the invariant?
-   **Counterexample Search**: If not, identify a specific scenario that violates it.
-   **Scope**: Clearly define the scope and assumptions of the invariant.
-   **Impact of Violation**: Explain the consequences if the invariant is violated.
-   **Proof Strategy**: Outline the formal methods and tools used (conceptually).

Output JSON: {{
    "verification_summary": str,
    "invariant_holds": bool,
    "proof_log": str, # Conceptual output from theorem prover/model checker
    "violation_details": Optional[Dict[str, Any]], # If invariant does not hold
    "confidence": float
}}
"""
    llm_verification = await _call_llm_for_verification(verifier_model, "FormalInvariantVerifier", prompt, task_id)

    if "error" in llm_verification:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Invariant verification failed: {llm_verification['error']}", current_step="LLM verification failed.")
        return {"status": "failed", "reason": llm_verification["error"]}

    verification_summary = llm_verification.get("verification_summary", "No summary.")
    invariant_holds = llm_verification.get("invariant_holds", False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "System invariant formal verification completed.", output=llm_verification)
    
    await _SWARM_VISUALIZER.log_event(task_id, "invariant_verified", f"System invariant verification completed. Holds: {invariant_holds}. Summary: {verification_summary}", llm_verification, agent_role="FormalVerification")
    if not invariant_holds:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"System invariant violation detected: {verification_summary}", title="System Invariant Violation", causal_priority="critical")
    else:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"System invariant holds: {verification_summary}", title="System Invariant Verified")

    # Store verification result in CRUD Manager
    await _CRUD_MANAGER.create_entity("VerificationResult", {"id": task_id, "verified_item_type": "system_invariant", "item_id": invariant_spec[:50], "result": llm_verification, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "invariant_verification", verification_summary, llm_verification, user_id)

    return {"status": "success", "invariant_holds": invariant_holds, "verification_report": llm_verification}
