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

SECURITY_LOG_DIR: str = ""

def initialize_security_auditor(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any):
    """Initializes global configurations for Proactive Security Auditing."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, SECURITY_LOG_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module

    SECURITY_LOG_DIR = os.path.join(_WORKSPACE, "security_audits")
    os.makedirs(SECURITY_LOG_DIR, exist_ok=True)
    print(f"Security Auditor initialized. Logs: {SECURITY_LOG_DIR}")

async def _call_llm_for_security_analysis(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for security analysis and remediation tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in security_auditor.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "security_llm_call_start", f"{model} evaluating security task: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    try:
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on identifying vulnerabilities and proposing secure code/configurations."},
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
            task_id, "security_llm_call_end", f"{model} completed security task.",
            {"model": model, "response_summary": content[:100]},
            model_name=model, agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "security_llm_error", f"JSON decode error from {model} for security task.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": model}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "security_llm_error", f"Error calling {model} for security task.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model}


async def simulate_sast_scan(task_id: str, code_snippet: str, language: str = "TariroLang", security_agent: str = "gemma-reviewer") -> Dict[str, Any]:
    """
    Simulates a Static Application Security Testing (SAST) scan on a code snippet.
    """
    print(f"Simulating SAST scan for code snippet: {code_snippet[:50]}...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "sast_scan_start", f"Simulating SAST scan on {language} code.",
        {"code_summary": code_snippet[:100], "language": language}, model_name=security_agent, agent_role=_ALL_MODELS.get(security_agent, "Security Auditor")
    )

    prompt = f"""You are a static analysis security tool. Analyze the following {language} code snippet for common vulnerabilities (e.g., injection flaws, buffer overflows, insecure deserialization, weak cryptography, access control issues).
    Report any detected vulnerabilities in JSON format, including severity, description, and suggested remediation. If no vulnerabilities are found, report an empty list.
    Output JSON: {{'vulnerabilities_found': bool, 'findings': list[dict]}}
    
    Code Snippet:
    ```
    {code_snippet}
    ```
    """
    
    result = await _call_llm_for_security_analysis(
        security_agent,
        _ALL_MODELS.get(security_agent, "Security Auditor"),
        prompt,
        task_id,
        context=f"SAST scan requested for code in {language}"
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}

    vulnerabilities_found = result.get("vulnerabilities_found", False)
    findings = result.get("findings", [])
    
    status = "vulnerabilities_found" if vulnerabilities_found else "clean"
    
    log_filename = os.path.join(SECURITY_LOG_DIR, f"sast_scan_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump({"status": status, "findings": findings}, f, indent=2)
    result["saved_path"] = log_filename
    result["status"] = status
    print(f"SAST scan analysis saved to {log_filename}")
    return result

async def simulate_dast_scan(task_id: str, deployed_service_description: str, entry_points: List[str], security_agent: str = "gemma-reviewer") -> Dict[str, Any]:
    """
    Simulates a Dynamic Application Security Testing (DAST) scan on a deployed service.
    """
    print(f"Simulating DAST scan for service: {deployed_service_description[:50]}...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "dast_scan_start", f"Simulating DAST scan on deployed service.",
        {"service_description": deployed_service_description[:100], "entry_points": entry_points},
        model_name=security_agent, agent_role=_ALL_MODELS.get(security_agent, "Security Auditor")
    )

    prompt = f"""You are a dynamic analysis security tool. Simulate interacting with a deployed service described as: '{deployed_service_description}'.
    Its primary entry points are: {', '.join(entry_points)}.
    Based on common runtime vulnerabilities (e.g., authentication bypass, session management flaws, exposed APIs, insecure configurations), describe potential runtime vulnerabilities you might find.
    Report any detected vulnerabilities in JSON format, including severity, description, and suggested remediation. If no vulnerabilities are found, report an empty list.
    Output JSON: {{'vulnerabilities_found': bool, 'findings': list[dict]}}
    """
    
    result = await _call_llm_for_security_analysis(
        security_agent,
        _ALL_MODELS.get(security_agent, "Security Auditor"),
        prompt,
        task_id,
        context=f"DAST scan requested for service: {deployed_service_description[:100]}"
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}

    vulnerabilities_found = result.get("vulnerabilities_found", False)
    findings = result.get("findings", [])
    
    status = "vulnerabilities_found" if vulnerabilities_found else "clean"
    
    log_filename = os.path.join(SECURITY_LOG_DIR, f"dast_scan_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump({"status": status, "findings": findings}, f, indent=2)
    result["saved_path"] = log_filename
    result["status"] = status
    print(f"DAST scan analysis saved to {log_filename}")
    return result

async def agi_propose_remediation(task_id: str, vulnerability_report: Dict[str, Any], remediation_agent: str = "llama-architect") -> Dict[str, Any]:
    """
    An AGI analyzes vulnerability findings and proposes auto-remediation steps or hardened code.
    """
    print(f"AGI ({remediation_agent}) proposing remediation for vulnerabilities...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "agi_remediation_start", f"AGI ({remediation_agent}) proposing remediation for vulnerabilities.",
        {"vulnerability_count": len(vulnerability_report.get("findings", []))},
        model_name=remediation_agent, agent_role=_ALL_MODELS.get(remediation_agent, "Security Architect")
    )

    prompt = f"""You are an AGI security architect specializing in auto-remediation.
    Given the following vulnerability report:
    {json.dumps(vulnerability_report, indent=2)}

    Propose concrete remediation steps, code fixes (if applicable, provide Python pseudo-code or configuration changes), or hardening measures.
    For each finding, provide a clear, actionable solution.
    Output JSON: {{'remediation_plan': list[dict], 'summary_of_changes': str, 'confidence': float}}
    """
    
    result = await _call_llm_for_security_analysis(
        remediation_agent,
        _ALL_MODELS.get(remediation_agent, "Security Architect"),
        prompt,
        task_id,
        context=json.dumps(vulnerability_report)
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    remediation_plan = result.get("remediation_plan", [])
    summary_of_changes = result.get("summary_of_changes", "No specific changes proposed.")
    
    status = "remediation_proposed" if remediation_plan else "no_remediation_needed"
    
    log_filename = os.path.join(SECURITY_LOG_DIR, f"remediation_plan_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump(result, f, indent=2)
    result["saved_path"] = log_filename
    result["status"] = status
    print(f"Remediation plan generated and saved to {log_filename}")
    return result
