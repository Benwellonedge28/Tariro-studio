import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import random
import uuid

# --- Configuration & Shared Data (initialized from studio_v3.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Base model definitions from studio_v3.py
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module
_CONTEXTUAL_MEMORY: Any = None # Reference to contextual_memory module
_CRUD_MANAGER: Any = None # Reference to crud_manager module

TASK_AUTOMATION_LOG_DIR: str = ""
AUTOMATION_SCRIPTS_DIR: str = ""

def initialize_task_automation(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, contextual_memory_module: Any, crud_manager_module: Any):
    """Initializes global configurations for Autonomous Self-Programming Task Automation."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CONTEXTUAL_MEMORY, _CRUD_MANAGER, TASK_AUTOMATION_LOG_DIR, AUTOMATION_SCRIPTS_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CONTEXTUAL_MEMORY = contextual_memory_module
    _CRUD_MANAGER = crud_manager_module

    TASK_AUTOMATION_LOG_DIR = os.path.join(_WORKSPACE, "task_automation_logs")
    os.makedirs(TASK_AUTOMATION_LOG_DIR, exist_ok=True)
    AUTOMATION_SCRIPTS_DIR = os.path.join(_WORKSPACE, "automation_scripts")
    os.makedirs(AUTOMATION_SCRIPTS_DIR, exist_ok=True)
    print(f"Task Automation initialized. Logs: {TASK_AUTOMATION_LOG_DIR}, Scripts: {AUTOMATION_SCRIPTS_DIR}")

async def _call_llm_for_automation(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for task automation tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in task_automation.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "automation_llm_call_start", f"{model} evaluating automation task: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    try:
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on generating, testing, and deploying internal automation scripts."},
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
            task_id, "automation_llm_call_end", f"{model} completed automation task.",
            {"model": model, "response_summary": content[:100]},
            model_name=model, agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "automation_llm_error", f"JSON decode error from {model} for automation.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": model}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "automation_llm_error", f"Error calling {model} for automation.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model}

async def identify_automation_opportunity(task_id: str, current_operational_summary: str, identifier_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates identifying repetitive or inefficient tasks for automation.
    """
    print(f"AGI ({identifier_model}) identifying automation opportunities...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "automation_identify_start", f"AGI ({identifier_model}) identifying automation opportunities.",
        {"operational_summary": current_operational_summary[:100]}, model_name=identifier_model, agent_role=_ALL_MODELS.get(identifier_model, "Automation Identifier")
    )

    # Simulate RAG: Retrieve PerformanceLogs and LearningInsights for patterns
    performance_logs = await _CRUD_MANAGER.read_entities(task_id, "PerformanceLog")
    learning_insights = await _CRUD_MANAGER.read_entities(task_id, "LearningInsight")

    logs_context = {
        "performance_logs": performance_logs[-5:] if performance_logs else [],
        "learning_insights": learning_insights[-5:] if learning_insights else []
    }
    
    prompt = f"""You are an AGI dedicated to improving system efficiency through automation.
    Analyze the provided operational summary and recent system logs/insights to identify a clear opportunity for automation.
    Focus on repetitive, error-prone, or time-consuming tasks.
    
    Current Operational Summary: "{current_operational_summary}"
    Recent Performance Logs & Learning Insights: {json.dumps(logs_context, indent=2)}

    Output JSON: {{'automation_needed': bool, 'identified_task_description': str, 'reason_for_automation': str, 'estimated_gain': str, 'confidence': float}}
    """
    
    result = await _call_llm_for_automation(
        identifier_model,
        _ALL_MODELS.get(identifier_model, "Automation Identifier"),
        prompt,
        task_id,
        context=json.dumps(logs_context)
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    log_filename = os.path.join(TASK_AUTOMATION_LOG_DIR, f"automation_opportunity_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump(result, f, indent=2)
    result["saved_path"] = log_filename
    result["status"] = "success"
    print(f"Automation opportunity analysis saved to {log_filename}")

    await _CONTEXTUAL_MEMORY.store_memory(task_id, identifier_model, "automation_opportunity", result, "Identified task for automation.")
    await _SWARM_VISUALIZER.log_event(
        task_id, "automation_identify_complete", f"Automation opportunity identified: {result.get('identified_task_description', '')[:50]}",
        result, model_name=identifier_model, agent_role=_ALL_MODELS.get(identifier_model, "Automation Identifier")
    )
    
    return result

async def generate_automation_script(task_id: str, identified_task: str, context_details: str, script_generator_model: str = "qwen-coder") -> Dict[str, Any]:
    """
    Simulates generating a Python automation script for the identified task.
    """
    print(f"AGI ({script_generator_model}) generating automation script for: {identified_task[:50]}...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "script_gen_start", f"AGI ({script_generator_model}) generating automation script.",
        {"identified_task": identified_task[:100]}, model_name=script_generator_model, agent_role=_ALL_MODELS.get(script_generator_model, "Script Generator")
    )

    # Simulate RAG: Retrieve API documentation and code examples from contextual memory or external sources
    api_docs_rag = await _CONTEXTUAL_MEMORY.query_memory_rag(task_id, "Retrieve Python API documentation and code examples for common internal automation tasks and system interactions.", script_generator_model)
    
    rag_context = api_docs_rag.get("response", "No specific API documentation or code examples found.")

    prompt = f"""You are an Autonomous Self-Programming Agent. Your task is to write a robust and efficient Python script to automate the following identified task.
    
    Identified Task to Automate: "{identified_task}"
    Context & Requirements: "{context_details}"
    
    Relevant API Documentation & Code Examples (RAG output):
    ---
    {rag_context}
    ---
    
    The script should be self-contained and perform the task. Include comments to explain logic. Assume necessary libraries are available or can be installed.
    Output ONLY the Python code, wrapped in ```python ... ```, no other text or explanation.
    """
    
    script_result = await _call_llm_for_automation(
        script_generator_model,
        _ALL_MODELS.get(script_generator_model, "Script Generator"),
        prompt,
        task_id,
        context=f"Identified task: {identified_task}, Context: {context_details}, RAG: {rag_context}",
        response_format_type="text" # Expect raw code
    )

    if "error" in script_result:
        return {"status": "failed", "reason": script_result["error"]}
    
    script_code_raw = script_result.get("content", "")
    if "```python" in script_code_raw and "```" in script_code_raw:
        script_code = script_code_raw.split("```python")[1].split("```")[0].strip()
    else:
        script_code = script_code_raw.strip()

    if not script_code:
        return {"status": "failed", "reason": "Failed to generate automation script."}

    script_name = "auto_script_" + str(uuid.uuid4())[:8] + ".py"
    script_path = os.path.join(AUTOMATION_SCRIPTS_DIR, script_name)
    with open(script_path, "w") as f:
        f.write(script_code)
    
    log_filename = os.path.join(TASK_AUTOMATION_LOG_DIR, f"script_gen_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    final_output = {
        "timestamp": datetime.now().isoformat(),
        "identified_task": identified_task,
        "script_path": script_path,
        "script_code_summary": script_code[:500]
    }
    with open(log_filename, "w") as f:
        json.dump(final_output, f, indent=2)
    final_output["saved_path"] = log_filename
    final_output["status"] = "success"
    print(f"Automation script generated and saved to {script_path}")

    await _CONTEXTUAL_MEMORY.store_memory(task_id, script_generator_model, "generated_automation_script", final_output, "Details of the generated automation script.")
    await _SWARM_VISUALIZER.log_event(
        task_id, "script_gen_complete", f"Automation script generated: {script_name}",
        final_output, model_name=script_generator_model, agent_role=_ALL_MODELS.get(script_generator_model, "Script Generator")
    )
    
    return final_output

async def test_automation_script(task_id: str, script_path: str, testing_context: str, tester_model: str = "deepseek-coder") -> Dict[str, Any]:
    """
    Simulates testing the generated automation script for functionality and safety.
    """
    print(f"AGI ({tester_model}) testing automation script: {os.path.basename(script_path)}...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "script_test_start", f"AGI ({tester_model}) testing automation script: {os.path.basename(script_path)}.",
        {"script": os.path.basename(script_path)}, model_name=tester_model, agent_role=_ALL_MODELS.get(tester_model, "Automation Tester")
    )

    # Simulate RAG: Retrieve testing best practices, safety guidelines.
    testing_rag = await _CONTEXTUAL_MEMORY.query_memory_rag(task_id, "Retrieve automation script testing best practices, safety guidelines, and relevant test cases.", tester_model)
    rag_context = testing_rag.get("response", "No specific testing guidelines found.")

    # Simulate SIMD: Conceptual parallel execution of test cases.
    script_content = ""
    try:
        with open(script_path, "r") as f:
            script_content = f.read()
    except FileNotFoundError:
        return {"status": "failed", "reason": "Script file not found."}

    prompt = f"""You are an Autonomous Script Tester, capable of rapid and thorough testing (SIMD-like conceptual processing).
    Evaluate the following Python automation script for functionality, potential side effects, and adherence to safety guidelines.
    
    Script Content:
    ```python
    {script_content}
    ```
    Testing Context: "{testing_context}"
    Testing Best Practices (RAG output):
    ---
    {rag_context}
    ---
    
    Describe the simulated test execution, the results, and provide a clear assessment of whether the script is safe and functional for deployment.
    
    Output JSON: {{'test_passed': bool, 'simulated_test_results': list[str], 'issues_found': list[str], 'recommendation': 'deploy' | 'revise' | 'discard', 'confidence': float}}
    """
    
    result = await _call_llm_for_automation(
        tester_model,
        _ALL_MODELS.get(tester_model, "Automation Tester"),
        prompt,
        task_id,
        context=f"Script: {os.path.basename(script_path)}, Context: {testing_context}, RAG: {rag_context}"
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    log_filename = os.path.join(TASK_AUTOMATION_LOG_DIR, f"script_test_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump(result, f, indent=2)
    result["saved_path"] = log_filename
    result["status"] = "success"
    print(f"Automation script test results saved to {log_filename}")

    await _CONTEXTUAL_MEMORY.store_memory(task_id, tester_model, "automation_script_test_results", result, "Results from testing the automation script.")
    await _SWARM_VISUALIZER.log_event(
        task_id, "script_test_complete", f"Automation script tested. Passed: {result.get('test_passed')}",
        result, model_name=tester_model, agent_role=_ALL_MODELS.get(tester_model, "Automation Tester")
    )
    
    return result

async def deploy_automation_script(task_id: str, script_path: str, deploy_context: str, deployer_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates deploying the automation script internally.
    """
    print(f"AGI ({deployer_model}) deploying automation script: {os.path.basename(script_path)}...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "script_deploy_start", f"AGI ({deployer_model}) deploying automation script: {os.path.basename(script_path)}.",
        {"script": os.path.basename(script_path)}, model_name=deployer_model, agent_role=_ALL_MODELS.get(deployer_model, "Automation Deployer")
    )

    # Simulate actual deployment (e.g., moving to an active directory, registering in a scheduler)
    # For now, this is a conceptual step.
    
    prompt = f"""You are an Autonomous Deployment Agent for internal automation scripts.
    Deploy the following script and confirm its operational readiness.
    
    Script Path: "{script_path}"
    Deployment Context: "{deploy_context}"
    
    Output JSON: {{'deployment_successful': bool, 'deployment_status_message': str, 'confidence': float}}
    """
    
    result = await _call_llm_for_automation(
        deployer_model,
        _ALL_MODELS.get(deployer_model, "Automation Deployer"),
        prompt,
        task_id,
        context=f"Script: {os.path.basename(script_path)}, Context: {deploy_context}"
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    log_filename = os.path.join(TASK_AUTOMATION_LOG_DIR, f"script_deploy_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump(result, f, indent=2)
    result["saved_path"] = log_filename
    result["status"] = "success"
    print(f"Automation script deployment results saved to {log_filename}")

    await _CONTEXTUAL_MEMORY.store_memory(task_id, deployer_model, "automation_script_deployment", result, "Results from deploying the automation script.")
    await _SWARM_VISUALIZER.log_event(
        task_id, "script_deploy_complete", f"Automation script deployed. Success: {result.get('deployment_successful')}",
        result, model_name=deployer_model, agent_role=_ALL_MODELS.get(deployer_model, "Automation Deployer")
    )
    
    return result
