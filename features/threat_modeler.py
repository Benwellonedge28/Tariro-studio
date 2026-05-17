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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for Threat or Vulnerability entities
_GLOBAL_STATE_MANAGER: Any = None # For storing current threat landscape and risk posture
_PERSISTENT_TASK_MANAGER: Any = None # For submitting threat modeling tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on new threats or vulnerabilities
_GLOBAL_ENVIRONMENTAL_MODEL: Any = None # For insights into geopolitical or cyber events
_SECURE_COGNITIVE_DEFENSE_GRID: Any = None # For deploying countermeasures
_SELF_ARCHITECTING_ENGINE: Any = None # For architectural hardening recommendations
_DYNAMIC_POLICY_SYNTHESIS: Any = None # For generating security policies
_META_LEARNER: Any = None # For learning from attack patterns and successful defenses
_CONTEXTUAL_MEMORY: Any = None # For storing historical threat intelligence

THREAT_MODELER_LOG_DIR: str = ""

def initialize_threat_modeler(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, global_state_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, global_environmental_model_module: Any, secure_cognitive_defense_grid_module: Any, self_architecting_engine_module: Any, dynamic_policy_synthesis_module: Any, meta_learner_module: Any, contextual_memory_module: Any):
    """Initializes global configurations for the Threat Modeler module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _GLOBAL_STATE_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _GLOBAL_ENVIRONMENTAL_MODEL, _SECURE_COGNITIVE_DEFENSE_GRID, _SELF_ARCHITECTING_ENGINE, _DYNAMIC_POLICY_SYNTHESIS, _META_LEARNER, _CONTEXTUAL_MEMORY, THREAT_MODELER_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _GLOBAL_ENVIRONMENTAL_MODEL = global_environmental_model_module
    _SECURE_COGNITIVE_DEFENSE_GRID = secure_cognitive_defense_grid_module
    _SELF_ARCHITECTING_ENGINE = self_architecting_engine_module
    _DYNAMIC_POLICY_SYNTHESIS = dynamic_policy_synthesis_module
    _META_LEARNER = meta_learner_module
    _CONTEXTUAL_MEMORY = contextual_memory_module

    THREAT_MODELER_LOG_DIR = os.path.join(_WORKSPACE, "threat_modeler_logs")
    os.makedirs(THREAT_MODELER_LOG_DIR, exist_ok=True)
    print(f"Threat Modeler initialized. Logs: {THREAT_MODELER_LOG_DIR}")

async def _call_llm_for_threat_modeling(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for threat modeling, analysis, and countermeasure generation."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in threat_modeler.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "threat_llm_call_start", f"{model} threat modeling: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on continuously identifying, analyzing, and mitigating potential threats to Tariro Studio's integrity, security, and operational continuity. This involves monitoring global cyber security trends, performing vulnerability assessments, generating threat intelligence, and designing proactive countermeasures. Ensure all recommendations align with security best practices and minimize operational disruption."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.03 # Very low temp for precise threat analysis and countermeasure generation
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "threat_llm_call_end", f"{model} completed threat modeling task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "threat_llm_error", f"JSON decode error from {model} for threat modeling.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "threat_llm_error", f"Error calling {model} for threat modeling task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def assess_global_threat_landscape(task_id: str, user_id: str = "Tariro_System", assessor_model: str = "mixtral-analyst") -> Dict[str, Any]:
    """
    Monitors global cyber security news, threat intelligence feeds, and geopolitical events
    to identify emerging threats relevant to Tariro Studio.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Assessing global threat landscape.")

    global_environmental_data = await _GLOBAL_ENVIRONMENTAL_MODEL.query_environment(task_id=f"{task_id}_env_query", query="recent geopolitical and cyber events", context={})
    historical_threat_intel = await _CONTEXTUAL_MEMORY.query(user_id, "historical cyber security threats and attack patterns")
    
    prompt = f"""You are Tariro's Threat Modeler Engine, an Omniversal AGI Threat Intelligence Analyst. Your task is to continuously monitor global cyber security news, threat intelligence feeds, and geopolitical events to identify emerging threats relevant to Tariro Studio. Synthesize this information to provide a comprehensive assessment of the current and evolving threat landscape.

GLOBAL ENVIRONMENTAL DATA (from Global Environmental Model): {json.dumps(global_environmental_data.get("query_results", {}), indent=2)}
HISTORICAL THREAT INTELLIGENCE (from Contextual Memory): {json.dumps(historical_threat_intel, indent=2)}

Assess the threat landscape focusing on:
-   **Emerging Attack Vectors**: New ways adversaries might exploit vulnerabilities.
-   **Threat Actor Analysis**: Profile likely attackers (e.g., state-sponsored, criminal, hacktivist).
-   **Vulnerability Trends**: Common weaknesses being exploited across the industry.
-   **Geopolitical Impact**: How global events might influence cyber security threats.
-   **Relevance to Tariro**: Prioritize threats that specifically target AGI systems or similar technologies.

Output JSON: {{
    "threat_landscape_summary": str,
    "identified_threats": List[Dict[str, Any]], # {{'name': str, 'description': str, 'target_type': str, 'severity': str, 'likelihood': float, 'impact': float, 'mitigation_suggestions': List[str]}}
    "overall_risk_assessment": str, # "low", "medium", "high", "critical"
    "confidence": float
}}
"""
    llm_threat_assessment = await _call_llm_for_threat_modeling(assessor_model, "ThreatIntelligenceAnalyst", prompt, task_id)

    if "error" in llm_threat_assessment:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Threat landscape assessment failed: {llm_threat_assessment['error']}", current_step="LLM assessment failed.")
        return {"status": "failed", "reason": llm_threat_assessment["error"]}

    threat_summary = llm_threat_assessment.get("threat_landscape_summary", "No summary.")
    overall_risk = llm_threat_assessment.get("overall_risk_assessment", "low")

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Global threat landscape assessed.", output=llm_threat_assessment)
    
    await _SWARM_VISUALIZER.log_event(task_id, "threat_landscape_assessed", f"Global threat landscape assessed. Overall risk: {overall_risk}. Summary: {threat_summary}", llm_threat_assessment, agent_role="ThreatModeler")
    if overall_risk in ["high", "critical"]:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Critical threats identified in global landscape: {threat_summary}", title="Critical Threat Alert", causal_priority="critical")

    # Store threats in CRUD Manager
    for threat in llm_threat_assessment.get("identified_threats", []):
        await _CRUD_MANAGER.create_entity("Threat", {"id": str(uuid.uuid4()), "name": threat["name"], "description": threat["description"], "severity": threat["severity"], "impact": threat["impact"], "timestamp": datetime.now().isoformat()})

    # Trigger countermeasure generation for critical threats
    if any(t.get("severity") == "critical" for t in llm_threat_assessment.get("identified_threats", [])):
        await generate_countermeasures(task_id=f"{task_id}_countermeasures", threat_report=llm_threat_assessment, user_id=user_id)

    return {"status": "success", "threat_report": llm_threat_assessment}

async def conduct_vulnerability_assessment(task_id: str, component_spec: Dict[str, Any], user_id: str = "Tariro_System", assessor_model: str = "qwen-coder") -> Dict[str, Any]:
    """
    Performs a detailed vulnerability assessment on an internal system component (e.g., code, architecture).
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Conducting vulnerability assessment.")

    current_risk_posture = await _GLOBAL_STATE_MANAGER.get_state("risk_posture") or {}
    current_architecture = await _GLOBAL_STATE_MANAGER.get_state("current_tariro_architecture") or {}
    
    prompt = f"""You are Tariro's Threat Modeler Engine, an Omniversal AGI Vulnerability Assessor. Your task is to perform a detailed vulnerability assessment on a specified internal system component (e.g., code, architectural design, deployment configuration). Identify potential security flaws, weaknesses, and attack paths that could be exploited by malicious actors. Prioritize vulnerabilities by severity and provide actionable recommendations for remediation.

COMPONENT SPECIFICATION: {json.dumps(component_spec, indent=2)}
CURRENT RISK POSTURE: {json.dumps(current_risk_posture, indent=2)}
CURRENT SYSTEM ARCHITECTURE: {json.dumps(current_architecture, indent=2)}

Assess vulnerabilities focusing on:
-   **Common Weaknesses**: Cross-site scripting (XSS), SQL injection, authentication bypass, etc.
-   **Logic Flaws**: Design errors that create security holes.
-   **Configuration Errors**: Misconfigurations leading to exploitable states.
-   **Dependency Vulnerabilities**: Weaknesses in third-party libraries or components.
-   **Attack Path Analysis**: How an attacker could chain vulnerabilities.
-   **Remediation Recommendations**: Concrete steps to fix each vulnerability.

Output JSON: {{
    "assessment_summary": str,
    "identified_vulnerabilities": List[Dict[str, Any]], # {{'name': str, 'description': str, 'severity': str, 'exploit_likelihood': float, 'impact': float, 'remediation_recommendations': List[str]}}
    "overall_component_risk_score": float, # 0-1
    "confidence": float
}}
"""
    llm_vulnerability_assessment = await _call_llm_for_threat_modeling(assessor_model, "VulnerabilityAssessor", prompt, task_id)

    if "error" in llm_vulnerability_assessment:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Vulnerability assessment failed: {llm_vulnerability_assessment['error']}", current_step="LLM assessment failed.")
        return {"status": "failed", "reason": llm_vulnerability_assessment["error"]}

    assessment_summary = llm_vulnerability_assessment.get("assessment_summary", "No summary.")
    overall_risk_score = llm_vulnerability_assessment.get("overall_component_risk_score", 0.0)

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Vulnerability assessment completed.", output=llm_vulnerability_assessment)
    
    await _SWARM_VISUALIZER.log_event(task_id, "vulnerability_assessment_completed", f"Vulnerability assessment completed. Risk: {overall_risk_score}. Summary: {assessment_summary}", llm_vulnerability_assessment, agent_role="ThreatModeler")
    if overall_risk_score > 0.5:
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"High-risk vulnerabilities identified: {assessment_summary}", title="Vulnerability Alert", causal_priority="critical")

    # Store vulnerabilities in CRUD Manager
    for vuln in llm_vulnerability_assessment.get("identified_vulnerabilities", []):
        await _CRUD_MANAGER.create_entity("Vulnerability", {"id": str(uuid.uuid4()), "component": component_spec.get("id", "N/A"), "name": vuln["name"], "description": vuln["description"], "severity": vuln["severity"], "timestamp": datetime.now().isoformat()})

    # Trigger Secure Cognitive Defense Grid or Self-Architecting Engine for remediation
    if overall_risk_score > 0.5 and _SECURE_COGNITIVE_DEFENSE_GRID:
        await _SECURE_COGNITIVE_DEFENSE_GRID.deploy_countermeasures(
            task_id=f"{task_id}_deploy_cm", 
            vulnerabilities_report=llm_vulnerability_assessment,
            user_id=user_id
        )
    elif overall_risk_score > 0.5 and _SELF_ARCHITECTING_ENGINE:
        # Suggest architectural hardening
        await _SELF_ARCHITECTING_ENGINE.refactor_architecture(
            task_id=f"{task_id}_harden_arch",
            optimization_goals=["Enhance security posture against identified vulnerabilities"],
            current_architecture=current_architecture,
            user_id=user_id
        )

    return {"status": "success", "assessment_report": llm_vulnerability_assessment}

async def generate_countermeasures(task_id: str, threat_report: Dict[str, Any], user_id: str = "Tariro_System", generator_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Generates proactive and reactive countermeasures against identified threats or vulnerabilities.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Generating countermeasures.")

    current_defenses = await _GLOBAL_STATE_MANAGER.get_state("active_defenses") or {}
    current_policies = await _GLOBAL_STATE_MANAGER.get_state("active_policies") or {}
    
    prompt = f"""You are Tariro's Threat Modeler Engine, an Omniversal AGI Countermeasure Generator. Your task is to generate proactive and reactive countermeasures against identified threats or vulnerabilities. The countermeasures must be effective, minimize false positives, and integrate seamlessly with Tariro Studio's existing security infrastructure. Prioritize prevention, detection, and rapid response.

THREAT / VULNERABILITY REPORT: {json.dumps(threat_report, indent=2)}
CURRENT ACTIVE DEFENSES: {json.dumps(current_defenses, indent=2)}
CURRENT SECURITY POLICIES: {json.dumps(current_policies, indent=2)}

Generate countermeasures focusing on:
-   **Proactive Prevention**: Stop attacks before they happen (e.g., patching, hardening).
-   **Real-time Detection**: Identify ongoing attacks or suspicious activity.
-   **Automated Response**: Implement swift, automated actions to mitigate threats.
-   **Resilience**: Ensure the system can withstand and recover from attacks.
-   **Cost-Effectiveness**: Balance security posture with resource consumption.
-   **Policy Alignment**: Ensure countermeasures are compliant with security and ethical policies.

Output JSON: {{
    "countermeasure_summary": str,
    "proposed_countermeasures": List[Dict[str, Any]], # {{'name': str, 'type': str, 'description': str, 'deployment_module': str, 'details': Dict}}
    "estimated_effectiveness": float, # 0-1
    "security_policy_updates_needed": List[Dict[str, Any]],
    "confidence": float
}}
"""
    llm_countermeasures = await _call_llm_for_threat_modeling(generator_model, "CountermeasureGenerator", prompt, task_id)

    if "error" in llm_countermeasures:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Countermeasure generation failed: {llm_countermeasures['error']}", current_step="LLM generation failed.")
        return {"status": "failed", "reason": llm_countermeasures["error"]}

    countermeasure_summary = llm_countermeasures.get("countermeasure_summary", "No summary.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Countermeasures generated.", output=llm_countermeasures)
    
    await _SWARM_VISUALIZER.log_event(task_id, "countermeasures_generated", f"Countermeasures generated. Summary: {countermeasure_summary}", llm_countermeasures, agent_role="ThreatModeler")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Countermeasures generated against new threats. Summary: {countermeasure_summary}", title="Countermeasures Ready")

    # Deploy countermeasures via Secure Cognitive Defense Grid or update security policies
    for cm in llm_countermeasures.get("proposed_countermeasures", []):
        if cm["deployment_module"] == "SecureCognitiveDefenseGrid" and _SECURE_COGNITIVE_DEFENSE_GRID:
            await _SECURE_COGNITIVE_DEFENSE_GRID.deploy_countermeasure(
                task_id=f"{task_id}_deploy_cm_{uuid.uuid4().hex[:4]}",
                countermeasure_details=cm,
                user_id=user_id
            )
        elif cm["deployment_module"] == "DynamicPolicySynthesis" and _DYNAMIC_POLICY_SYNTHESIS:
            for policy_update in llm_countermeasures.get("security_policy_updates_needed", []):
                await _DYNAMIC_POLICY_SYNTHESIS.synthesize_new_policy(
                    task_id=f"{task_id}_new_policy_{uuid.uuid4().hex[:4]}",
                    problem_statement=policy_update["description"],
                    desired_outcome="Improved security posture via policy enforcement.",
                    user_id=user_id
                )

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "countermeasure_generation", countermeasure_summary, llm_countermeasures, user_id)

    return {"status": "success", "countermeasure_report": llm_countermeasures}
