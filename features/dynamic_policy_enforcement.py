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
_CONTEXTUAL_MEMORY: Any = None # Reference to contextual_memory module

POLICY_ENFORCEMENT_LOG_DIR: str = ""

def initialize_dynamic_policy_enforcement(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, contextual_memory_module: Any):
    """Initializes global configurations for Dynamic Policy Enforcement Engine."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CONTEXTUAL_MEMORY, POLICY_ENFORCEMENT_LOG_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CONTEXTUAL_MEMORY = contextual_memory_module

    POLICY_ENFORCEMENT_LOG_DIR = os.path.join(_WORKSPACE, "policy_enforcement_logs")
    os.makedirs(POLICY_ENFORCEMENT_LOG_DIR, exist_ok=True)
    print(f"Dynamic Policy Enforcement initialized. Logs: {POLICY_ENFORCEMENT_LOG_DIR}")

async def _call_llm_for_policy_enforcement(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for dynamic policy enforcement tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in dynamic_policy_enforcement.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "policy_enforcement_llm_call_start", f"{model} evaluating policy enforcement: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    try:
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on continuously monitoring system behavior against predefined policies and taking corrective action."},
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
            task_id, "policy_enforcement_llm_call_end", f"{model} completed policy enforcement task.",
            {"model": model, "response_summary": content[:100]},
            model_name=model, agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "policy_enforcement_llm_error", f"JSON decode error from {model} for policy enforcement.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": model}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "policy_enforcement_llm_error", f"Error calling {model} for policy enforcement.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model}

async def monitor_and_evaluate_behavior(task_id: str, observed_behavior_summary: str, system_context: str, enforcer_agent: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates monitoring system behavior and evaluating it against predefined policies.
    Conceptualizes RAG for policy documents and threat intel, and SIMD for real-time behavioral analysis.
    """
    print(f"AGI ({enforcer_agent}) monitoring and evaluating behavior...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "policy_monitor_start", f"AGI ({enforcer_agent}) monitoring system behavior.",
        {"behavior_summary": observed_behavior_summary[:100], "context": system_context[:100]},
        model_name=enforcer_agent, agent_role=_ALL_MODELS.get(enforcer_agent, "Policy Enforcer")
    )

    # Simulate RAG: Retrieve policy documents (security, ethical, operational) and relevant threat intelligence.
    policy_rag = await _CONTEXTUAL_MEMORY.query_memory_rag(task_id, f"Retrieve all relevant security policies, ethical guidelines, operational mandates, and current threat intelligence for evaluating system behavior: {observed_behavior_summary} in context: {system_context}.", enforcer_agent)
    
    rag_context = policy_rag.get("response", "No specific policy documents or threat intelligence found in memory.")

    # Simulate policy violation detection
    violation_detected = random.random() < 0.3 # 30% chance of detecting a violation

    prompt = f"""You are a Dynamic Policy Enforcement Engine. Your task is to continuously monitor system behavior and evaluate it against predefined policies.
    
    Observed System Behavior Summary: "{observed_behavior_summary}"
    Current System Context: "{system_context}"
    
    Predefined Policies & Threat Intelligence (RAG output):
    ---
    {rag_context}
    ---

    Perform real-time behavioral analysis (SIMD-like conceptual processing) to detect any policy violations (security, ethical, operational).
    
    Output JSON: {{'violation_detected': bool, 'violation_details': str, 'policy_violated': str, 'severity': 'low' | 'medium' | 'high' | 'critical', 'recommendation': str, 'confidence': float}}
    The 'recommendation' should suggest a corrective action (e.g., 'isolate_component', 'revert_action', 'alert_human', 'log_and_monitor').
    """
    
    result = await _call_llm_for_policy_enforcement(
        enforcer_agent,
        _ALL_MODELS.get(enforcer_agent, "Policy Enforcer"),
        prompt,
        task_id,
        context=f"Behavior: {observed_behavior_summary}, Context: {system_context}, RAG: {rag_context}"
    )

    # Override LLM's detection with simulated random detection
    if not violation_detected:
        result["violation_detected"] = False
        result["violation_details"] = "No policy violation detected."
        result["policy_violated"] = "N/A"
        result["severity"] = "low"
        result["recommendation"] = "log_and_monitor"
    else:
        result["violation_detected"] = True
        result["violation_details"] = "Simulated unauthorized data access attempt."
        result["policy_violated"] = random.choice(["Data Privacy Policy", "Access Control Policy", "Ethical Use Policy"])
        result["severity"] = random.choice(["medium", "high", "critical"])
        result["recommendation"] = random.choice(["isolate_component", "revert_action", "alert_human"])


    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    log_filename = os.path.join(POLICY_ENFORCEMENT_LOG_DIR, f"policy_evaluation_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    final_output = {
        "timestamp": datetime.now().isoformat(),
        "observed_behavior_summary": observed_behavior_summary,
        "system_context": system_context,
        "evaluation_result": result
    }
    with open(log_filename, "w") as f:
        json.dump(final_output, f, indent=2)
    final_output["saved_path"] = log_filename
    final_output["status"] = "success"
    print(f"Policy evaluation results saved to {log_filename}")

    await _CONTEXTUAL_MEMORY.store_memory(task_id, enforcer_agent, "policy_violation_detection", final_output, "Results of dynamic policy monitoring and evaluation.")
    await _SWARM_VISUALIZER.log_event(
        task_id, "policy_monitor_complete", f"Policy evaluation completed. Violation detected: {final_output['evaluation_result']['violation_detected']}",
        final_output, model_agent=enforcer_agent, agent_role=_ALL_MODELS.get(enforcer_agent, "Policy Enforcer")
    )
    
    return final_output

async def take_corrective_action(task_id: str, evaluation_report: Dict[str, Any], action_agent: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates taking corrective action in real-time based on a policy violation report.
    """
    print(f"AGI ({action_agent}) taking corrective action...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "policy_corrective_action_start", f"AGI ({action_agent}) taking corrective action.",
        {"recommendation": evaluation_report.get('evaluation_result', {}).get('recommendation', 'N/A')},
        model_name=action_agent, agent_role=_ALL_MODELS.get(action_agent, "Policy Actioner")
    )

    if not evaluation_report.get("evaluation_result", {}).get("violation_detected"):
        return {"status": "no_action_needed", "reason": "No policy violation detected for corrective action."}

    # Simulate RAG: Retrieve incident response playbooks and system control interfaces.
    action_rag = await _CONTEXTUAL_MEMORY.query_memory_rag(task_id, "Retrieve relevant incident response playbooks, system control interfaces (e.g., for blocking traffic, reverting changes), and human escalation protocols.", action_agent)
    
    rag_context = action_rag.get("response", "No specific action playbooks found.")

    # Determine simulated action based on recommendation
    recommended_action = evaluation_report.get('evaluation_result', {}).get('recommendation', 'alert_human')
    action_taken_details = ""
    action_successful = True

    if recommended_action == 'isolate_component':
        action_taken_details = f"Simulated isolation of affected component due to {evaluation_report['evaluation_result']['violation_details']}."
    elif recommended_action == 'revert_action':
        action_taken_details = f"Simulated reversion of violating action due to {evaluation_report['evaluation_result']['violation_details']}."
    elif recommended_action == 'alert_human':
        action_taken_details = f"Simulated alerting human operator due to {evaluation_report['evaluation_result']['violation_details']}."
    else:
        action_taken_details = f"Simulated logging and monitoring due to {evaluation_report['evaluation_result']['violation_details']}."
    
    prompt = f"""You are a Dynamic Policy Action Engine. Based on the provided policy violation report and recommended action, simulate taking the appropriate real-time corrective action.
    
    Policy Violation Report:
    {json.dumps(evaluation_report, indent=2)}
    
    Incident Response Playbooks & System Controls (RAG output):
    ---
    {rag_context}
    ---

    Describe the steps taken to implement the recommended corrective action.
    
    Output JSON: {{'action_successful': bool, 'action_taken_details': str, 'result_assessment': str, 'post_action_status': str, 'confidence': float}}
    """
    
    result = await _call_llm_for_policy_enforcement(
        action_agent,
        _ALL_MODELS.get(action_agent, "Policy Actioner"),
        prompt,
        task_id,
        context=json.dumps(evaluation_report)
    )

    # Override LLM's result with simulated action
    result["action_successful"] = action_successful
    result["action_taken_details"] = action_taken_details
    result["post_action_status"] = "policy_restored" if action_successful else "investigation_needed"


    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    log_filename = os.path.join(POLICY_ENFORCEMENT_LOG_DIR, f"corrective_action_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    final_output = {
        "timestamp": datetime.now().isoformat(),
        "evaluation_report": evaluation_report,
        "corrective_action_result": result
    }
    with open(log_filename, "w") as f:
        json.dump(final_output, f, indent=2)
    final_output["saved_path"] = log_filename
    final_output["status"] = "success"
    print(f"Corrective action results saved to {log_filename}")

    await _CONTEXTUAL_MEMORY.store_memory(task_id, action_agent, "policy_corrective_action", final_output, "Results of corrective action taken for policy violation.")
    await _SWARM_VISUALIZER.log_event(
        task_id, "policy_corrective_action_complete", f"Corrective action completed. Success: {result.get('action_successful')}",
        final_output, model_agent=action_agent, agent_role=_ALL_MODELS.get(action_agent, "Policy Actioner")
    )
    
    return final_output
