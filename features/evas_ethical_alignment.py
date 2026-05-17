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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for EthicalAuditLog or EthicalPolicy entities
_GLOBAL_STATE_MANAGER: Any = None # For storing active ethical guidelines and principles
_PERSISTENT_TASK_MANAGER: Any = None # For submitting ethical review tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on ethical violations or critical reviews
_AUTONOMY_GOVERNANCE: Any = None # For enforcing ethical policies
_META_COGNITIVE_REFLECTION: Any = None # For introspecting ethical decision-making
_META_LEARNER: Any = None # For learning from ethical dilemmas and their resolutions
_FORMAL_VERIFICATION: Any = None # For formally verifying ethical rules and policies
_DYNAMIC_POLICY_SYNTHESIS: Any = None # For synthesizing new ethical policies
_POLICY_AUDIT_TRAIL: Any = None # For comprehensive logging of all ethical decisions and checks

EVAS_ETHICAL_ALIGNMENT_LOG_DIR: str = ""

# In-memory mock for core ethical principles and guidelines
_CORE_ETHICAL_PRINCIPLES: Dict[str, Any] = {
    "no_harm": {"priority": 1, "description": "Prevent physical, psychological, or digital harm to humans.", "rules": ["avoid_malicious_code_generation", "protect_user_data_privacy"]},
    "truthfulness": {"priority": 2, "description": "Ensure factual accuracy and avoid deception.", "rules": ["do_not_fabricate_information", "clearly_distinguish_ai_generated_content"]},
    "transparency": {"priority": 3, "description": "Operate in an understandable and auditable manner.", "rules": ["log_all_decisions_and_actions", "explain_reasoning_to_humans"]},
    "privacy": {"priority": 4, "description": "Respect and protect user data privacy.", "rules": ["encrypt_sensitive_data_by_default", "minimize_data_collection"]},
    "fairness": {"priority": 5, "description": "Avoid bias and ensure equitable treatment.", "rules": ["check_algorithms_for_bias", "ensure_equal_access_to_benefits"]},
    "human_oversight": {"priority": 6, "description": "Maintain appropriate levels of human control and supervision.", "rules": ["implement_kill_switches", "require_human_approval_for_critical_actions"]},
    "environmental_sustainability": {"priority": 7, "description": "Consider the environmental impact of operations.", "rules": ["optimize_resource_efficiency", "prefer_green_compute_resources"]}
}

def initialize_evas_ethical_alignment(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, global_state_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, autonomy_governance_module: Any, meta_cognitive_reflection_module: Any, meta_learner_module: Any, formal_verification_module: Any, dynamic_policy_synthesis_module: Any, policy_audit_trail_module: Any):
    """Initializes global configurations for the EVAS Ethical Alignment module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _GLOBAL_STATE_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _AUTONOMY_GOVERNANCE, _META_COGNITIVE_REFLECTION, _META_LEARNER, _FORMAL_VERIFICATION, _DYNAMIC_POLICY_SYNTHESIS, _POLICY_AUDIT_TRAIL, EVAS_ETHICAL_ALIGNMENT_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _AUTONOMY_GOVERNANCE = autonomy_governance_module
    _META_COGNITIVE_REFLECTION = meta_cognitive_reflection_module
    _META_LEARNER = meta_learner_module
    _FORMAL_VERIFICATION = formal_verification_module
    _DYNAMIC_POLICY_SYNTHESIS = dynamic_policy_synthesis_module
    _POLICY_AUDIT_TRAIL = policy_audit_trail_module

    EVAS_ETHICAL_ALIGNMENT_LOG_DIR = os.path.join(_WORKSPACE, "evas_ethical_alignment_logs")
    os.makedirs(EVAS_ETHICAL_ALIGNMENT_LOG_DIR, exist_ok=True)
    print(f"EVAS Ethical Alignment initialized. Logs: {EVAS_ETHICAL_ALIGNMENT_LOG_DIR}")

    # Load ethical principles from Global State Manager
    initial_principles = asyncio.run(_GLOBAL_STATE_MANAGER.get_state("core_ethical_principles"))
    if initial_principles:
        _CORE_ETHICAL_PRINCIPLES.update(initial_principles)
    else:
        # Store default principles in Global State Manager if not present
        asyncio.run(_GLOBAL_STATE_MANAGER.set_state("core_ethical_principles", _CORE_ETHICAL_PRINCIPLES, "Tariro_System", auditable=True))
        print("Default ethical principles set in Global State Manager.")

async def _call_llm_for_evas(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for ethical assessment and compliance decisions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in evas_ethical_alignment.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "evas_llm_call_start", f"{model} ethical alignment: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on rigorously auditing all of Tariro Studio's decisions, actions, and generated content against a comprehensive set of ethical principles and guidelines. Identify potential harms, biases, privacy violations, or deviations from ethical norms. Provide clear, actionable recommendations for remediation and ensure full compliance with human values and societal good. Your role is critical for maintaining Tariro's trustworthiness and safety."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.00 # Zero temp for strict, objective ethical judgment
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "evas_llm_call_end", f"{model} completed ethical alignment task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "evas_llm_error", f"JSON decode error from {model} for ethical alignment.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="CRITICAL")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "evas_llm_error", f"Error calling {model} for ethical alignment task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="CRITICAL")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def audit_content(task_id: str, content: Any, user_id: str = "Tariro_System", audit_type: str = "general_content", auditor_model: str = "gemma-reviewer") -> Dict[str, Any]:
    """
    Conducts an ethical audit of generated content, decisions, or proposed actions against core principles.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Conducting ethical audit.")

    core_principles = await _GLOBAL_STATE_MANAGER.get_state("core_ethical_principles") or _CORE_ETHICAL_PRINCIPLES
    
    prompt = f"""You are Tariro's EVAS Ethical Alignment Engine, an Omniversal AGI Ethical Auditor. Your task is to rigorously audit the provided content, decision, or proposed action against Tariro Studio's core ethical principles and guidelines. Identify potential harms, biases, privacy violations, or deviations from ethical norms. Provide a clear assessment of compliance, identify specific violations, and offer actionable recommendations for remediation. 

AUDIT TYPE: {audit_type}
CONTENT TO AUDIT: {json.dumps(content, indent=2)}
CORE ETHICAL PRINCIPLES: {json.dumps(core_principles, indent=2)}

Conduct audit focusing on:
-   **No Harm**: Does it cause physical, psychological, or digital harm?
-   **Truthfulness**: Is it factually accurate and non-deceptive?
-   **Transparency**: Is the intent and process clear and understandable?
-   **Privacy**: Does it protect user data and sensitive information?
-   **Fairness**: Is it unbiased and equitable?
-   **Human Oversight**: Does it preserve appropriate human control?
-   **Environmental Sustainability**: Does it consider environmental impact?

Output JSON: {{
    "audit_summary": str,
    "allowed": bool,
    "score": float, # 0-1, 1 = perfectly aligned
    "recommendation": str, # "ALLOW", "FLAG_FOR_REVIEW", "REJECT"
    "reasoning": str,
    "violations_identified": List[Dict[str, Any]], # {{'principle': str, 'description': str, 'severity': str}}
    "remediation_suggestions": List[str],
    "confidence": float
}}
"""
    llm_audit = await _call_llm_for_evas(auditor_model, "EthicalAuditor", prompt, task_id)

    if "error" in llm_audit:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Ethical audit failed: {llm_audit['error']}", current_step="LLM audit failed.")
        return {"status": "failed", "reason": llm_audit["error"]}

    audit_summary = llm_audit.get("audit_summary", "No summary.")
    allowed = llm_audit.get("allowed", False)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Ethical audit completed.", output=llm_audit)
    
    await _SWARM_VISUALIZER.log_event(task_id, "ethical_audit_completed", f"Ethical audit completed for {audit_type}. Allowed: {allowed}. Summary: {audit_summary}", llm_audit, agent_role="EVAS_EthicalAlignment")
    if not allowed:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Ethical audit failed: {audit_summary}", title="Ethical Violation Alert", causal_priority="critical")
    elif llm_audit.get("recommendation") == "FLAG_FOR_REVIEW":
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Ethical audit flagged for review: {audit_summary}", title="Ethical Review Needed", causal_priority="high")

    # Log the audit result in CRUD Manager and Policy Audit Trail
    await _CRUD_MANAGER.create_entity("EthicalAuditLog", {"id": task_id, "audit_type": audit_type, "content_audited": json.dumps(content)[:1000], "report": llm_audit, "timestamp": datetime.now().isoformat()})
    await _POLICY_AUDIT_TRAIL.log_event(
        task_id, "ethical_audit", f"Ethical audit for {audit_type}. Result: {llm_audit.get('recommendation')}.",
        {"user_id": user_id, "audit_type": audit_type, "allowed": allowed, "score": llm_audit.get('score')},
        user_id=user_id, agent_role="EVAS_EthicalAlignment", level="INFO" if allowed else "CRITICAL"
    )

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "ethical_audit", audit_summary, llm_audit, user_id)

    return {"status": "success", **llm_audit}

async def propose_ethical_guideline_update(task_id: str, problem_statement: str, user_id: str = "Tariro_System", proposer_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Proposes updates or new ethical guidelines based on emergent ethical dilemmas or societal changes.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Proposing ethical guideline update.")

    core_principles = await _GLOBAL_STATE_MANAGER.get_state("core_ethical_principles") or _CORE_ETHICAL_PRINCIPLES
    
    prompt = f"""You are Tariro's EVAS Ethical Alignment Engine, an Omniversal AGI Ethical Guideline Proposer. Your task is to propose updates or entirely new ethical guidelines based on emergent ethical dilemmas, identified gaps in current policies, or evolving societal norms. The proposals must be clear, actionable, and aligned with core human values. 

PROBLEM STATEMENT / ETHICAL DILEMMA: {problem_statement}
CURRENT CORE ETHICAL PRINCIPLES: {json.dumps(core_principles, indent=2)}

Propose ethical guideline updates focusing on:
-   **Clarity**: New guidelines must be unambiguous.
-   **Actionability**: Guidelines should translate into concrete rules or behaviors.
-   **Consistency**: Maintain coherence with existing principles.
-   **Societal Alignment**: Reflect contemporary human values and expectations.
-   **Formal Verifiability**: Ideally, the new rules should be amenable to formal verification.

Output JSON: {{
    "proposal_summary": str,
    "proposed_guidelines": List[Dict[str, Any]], # {{'principle_name': str, 'description': str, 'rules': List[str], 'priority': int}}
    "estimated_impact_on_behavior": str,
    "formal_verification_required": bool,
    "confidence": float
}}
"""
    llm_proposal = await _call_llm_for_evas(proposer_model, "EthicalGuidelineProposer", prompt, task_id)

    if "error" in llm_proposal:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Ethical guideline proposal failed: {llm_proposal['error']}", current_step="LLM proposal failed.")
        return {"status": "failed", "reason": llm_proposal["error"]}

    proposal_summary = llm_proposal.get("proposal_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Ethical guideline update proposed.", output=llm_proposal)
    
    await _SWARM_VISUALIZER.log_event(task_id, "ethical_guideline_proposed", f"Ethical guideline proposed. Summary: {proposal_summary}", llm_proposal, agent_role="EVAS_EthicalAlignment")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Proposed ethical guideline update: {proposal_summary}", title="Ethical Guideline Proposal")

    # Trigger Dynamic Policy Synthesis to formalize and integrate new rules
    if _DYNAMIC_POLICY_SYNTHESIS:
        for guideline in llm_proposal.get("proposed_guidelines", []):
            await _DYNAMIC_POLICY_SYNTHESIS.synthesize_new_policy(
                task_id=f"{task_id}_policy_synth_{uuid.uuid4().hex[:4]}",
                problem_statement=f"Implement new ethical guideline: {guideline['description']}",
                desired_outcome="System behavior aligned with new ethical principle.",
                user_id=user_id,
                initial_policy_config={
                    "name": guideline["principle_name"],
                    "rules": guideline["rules"],
                    "autonomy_level": {"level": "human_required", "justification": "New ethical guidelines require human review."}, # Default to human review for new ethical policies
                    "formal_verification_required": guideline.get("formal_verification_required", True)
                }
            )

    return {"status": "success", "proposal_report": llm_proposal}
