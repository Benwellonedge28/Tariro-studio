import os
import json
from datetime import datetime
from typing import Dict, Any, List
import importlib.util

# --- Configuration & Shared Data (initialized from studio_v3.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Model names and their base roles
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module

SDK_OUTPUT_DIR: str = ""
_TOOL_FORGE_MODULE: Any = None # Reference to tool_forge module
_MULTIMODAL_MODULE: Any = None # Reference to multimodal_collaboration module

def initialize_sdk_manager(
    workspace_path: str,
    openai_client: Any,
    all_models: Dict[str, str],
    swarm_visualizer_module: Any,
    tool_forge_module: Any,
    multimodal_module: Any
):
    """Initializes global configurations for the SDK Manager."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, SDK_OUTPUT_DIR, _TOOL_FORGE_MODULE, _MULTIMODAL_MODULE
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _TOOL_FORGE_MODULE = tool_forge_module
    _MULTIMODAL_MODULE = multimodal_module

    SDK_OUTPUT_DIR = os.path.join(_WORKSPACE, "sdk_outputs")
    os.makedirs(SDK_OUTPUT_DIR, exist_ok=True)
    print(f"SDK Manager initialized. Outputs: {SDK_OUTPUT_DIR}")


async def _call_model_for_sdk_gen(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "text") -> Dict[str, Any]:
    """Helper to call LLM for SDK generation related tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in sdk_manager.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "sdk_gen_llm_call_start", f"{model} generating SDK part: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    try:
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Generate clean, functional SDK code."},
            {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
        ]
        
        resp = await _CLIENT.chat.completions.create(
            model=model,
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.1
        )
        content = resp.choices[0].message.content
        
        out = {"content": content}
        out["model"] = model

        await _SWARM_VISUALIZER.log_event(
            task_id, "sdk_gen_llm_call_end", f"{model} completed SDK part generation.",
            {"model": model, "response_summary": content[:100]},
            model_name=model, agent_role=role
        )
        return out
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "sdk_gen_llm_error", f"Error calling {model} for SDK generation.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model}


def _get_exposed_capabilities() -> Dict[str, Any]:
    """Collects information on dynamically available tools and multimodal assets."""
    tools = _TOOL_FORGE_MODULE.get_validated_tools() if _TOOL_FORGE_MODULE else []
    multimodal_assets = _MULTIMODAL_MODULE.get_all_validated_assets() if _MULTIMODAL_MODULE else [] # Assuming this function exists or will exist

    return {
        "tools": tools,
        "multimodal_assets": multimodal_assets
    }

async def generate_sdk(task_id: str, app_name: str, language: str, sdk_version: str = "1.0.0", model_caller: str = "llama-architect") -> Dict[str, Any]:
    """
    Generates an SDK in the specified language, exposing dynamically discovered capabilities.
    """
    print(f"Generating {language} SDK for '{app_name}' (version: {sdk_version})...")
    await _SWARM_VISUALIZER.log_event(task_id, "sdk_gen_start", f"Generating {language} SDK for {app_name}.", {"app_name": app_name, "language": language}, model_name="system", agent_role="sdk_manager_orchestrator")

    exposed_capabilities = _get_exposed_capabilities()
    
    sdk_code = ""
    filename = ""
    mime_type = ""

    if language.lower() == "python":
        prompt = f"""Generate a Python SDK client for an application named '{app_name}'.
The SDK should include methods to interact with the following capabilities:
- **Custom Tools:**
{json.dumps([{'name': t['name'], 'description': t['description'], 'cli_template': t['cli_command_template']} for t in exposed_capabilities['tools']], indent=2)}
- **Multi-modal Assets:**
{json.dumps([{'asset_type': a['asset_type'], 'description': a['description'], 'url': a['url']} for a in exposed_capabilities['multimodal_assets']], indent=2)}

For each custom tool, create a Python function that takes arguments corresponding to the CLI template and executes the underlying tool script (assuming it's installed or accessible via PATH).
For multi-modal assets, create methods to retrieve asset metadata (description, URL).
The SDK should be a Python class, with clear docstrings. Include an `__init__` method.
Return ONLY the Python code, wrapped in ```python ... ```, no other text or explanation.
"""
        model_role = _ALL_MODELS.get(model_caller, "SDK architect and code generator.")
        result = await _call_model_for_sdk_gen(model_caller, model_role, prompt, task_id)
        
        sdk_code_raw = result.get("content", "")
        if "```python" in sdk_code_raw and "```" in sdk_code_raw:
            sdk_code = sdk_code_raw.split("```python")[1].split("```")[0].strip()
        else:
            sdk_code = sdk_code_raw.strip()

        filename = f"{app_name.lower().replace(' ', '_')}_sdk_v{sdk_version.replace('.', '_')}.py"
        mime_type = "text/x-python"

    elif language.lower() == "javascript":
        prompt = f"""Generate a JavaScript SDK client for an application named '{app_name}'.
The SDK should include methods to interact with the following capabilities:
- **Custom Tools:**
{json.dumps([{'name': t['name'], 'description': t['description'], 'cli_template': t['cli_command_template']} for t in exposed_capabilities['tools']], indent=2)}
- **Multi-modal Assets:**
{json.dumps([{'asset_type': a['asset_type'], 'description': a['description'], 'url': a['url']} for a in exposed_capabilities['multimodal_assets']], indent=2)}

For custom tools, create asynchronous JavaScript functions that would typically make an API call to a backend that wraps the actual CLI execution. For now, just log the intended CLI command.
For multi-modal assets, create methods to retrieve asset metadata (description, URL).
The SDK should be a JavaScript class. Return ONLY the JavaScript code, wrapped in ```javascript ... ```, no other text or explanation.
"""
        model_role = _ALL_MODELS.get(model_caller, "SDK architect and code generator.")
        result = await _call_model_for_sdk_gen(model_caller, model_role, prompt, task_id)

        sdk_code_raw = result.get("content", "")
        if "```javascript" in sdk_code_raw and "```" in sdk_code_raw:
            sdk_code = sdk_code_raw.split("```javascript")[1].split("```")[0].strip()
        else:
            sdk_code = sdk_code_raw.strip()
            
        filename = f"{app_name.lower().replace(' ', '_')}_sdk_v{sdk_version.replace('.', '_')}.js"
        mime_type = "application/javascript"
    else:
        await _SWARM_VISUALIZER.log_event(task_id, "sdk_gen_fail", f"Unsupported SDK language: {language}.", {"language": language}, model_name="system", agent_role="sdk_manager_orchestrator", level="ERROR")
        return {"status": "failed", "reason": f"Unsupported language: {language}"}

    if not sdk_code:
        await _SWARM_VISUALIZER.log_event(task_id, "sdk_gen_fail", f"Failed to generate SDK code for {language}.", {}, model_name=model_caller, agent_role=_ALL_MODELS[model_caller], level="ERROR")
        return {"status": "failed", "reason": "Failed to generate SDK code."}

    output_path = os.path.join(SDK_OUTPUT_DIR, filename)
    with open(output_path, "w") as f:
        f.write(sdk_code)

    await _SWARM_VISUALIZER.log_event(task_id, "sdk_gen_success", f"Generated {language} SDK for {app_name}.", {"path": output_path, "version": sdk_version}, model_name="system", agent_role="sdk_manager_orchestrator")
    print(f"Generated SDK saved to {output_path}")
    return {"status": "success", "path": output_path, "filename": filename, "language": language, "sdk_version": sdk_version, "mime_type": mime_type}
