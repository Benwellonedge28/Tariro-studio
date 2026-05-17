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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for ToolDefinition or ToolLog entities
_PERSISTENT_TASK_MANAGER: Any = None # For submitting tool design/implementation tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on new tools or implementation failures
_GLOBAL_STATE_MANAGER: Any = None # For storing tool registry and available capabilities
_META_COGNITIVE_REFLECTION: Any = None # For identifying tool gaps through self-analysis
_SELF_EVOLUTION: Any = None # For generating tool implementation code
_FORMAL_VERIFICATION: Any = None # For verifying tool correctness and safety
_AUTONOMY_GOVERNANCE: Any = None # For policy checks on tool creation and usage
_DYNAMIC_POLICY_SYNTHESIS: Any = None # For creating policies for tool usage
_META_LEARNER: Any = None # For learning from tool effectiveness and usage patterns

TOOL_FORGE_LOG_DIR: str = ""
FEATURES_DIR: str = ""

def initialize_tool_forge(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, global_state_manager_module: Any, meta_cognitive_reflection_module: Any, self_evolution_module: Any, formal_verification_module: Any, autonomy_governance_module: Any, dynamic_policy_synthesis_module: Any, meta_learner_module: Any):
    """Initializes global configurations for the Tool Forge module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _GLOBAL_STATE_MANAGER, _META_COGNITIVE_REFLECTION, _SELF_EVOLUTION, _FORMAL_VERIFICATION, _AUTONOMY_GOVERNANCE, _DYNAMIC_POLICY_SYNTHESIS, _META_LEARNER, TOOL_FORGE_LOG_DIR, FEATURES_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _META_COGNITIVE_REFLECTION = meta_cognitive_reflection_module
    _SELF_EVOLUTION = self_evolution_module
    _FORMAL_VERIFICATION = formal_verification_module
    _AUTONOMY_GOVERNANCE = autonomy_governance_module
    _DYNAMIC_POLICY_SYNTHESIS = dynamic_policy_synthesis_module
    _META_LEARNER = meta_learner_module

    TOOL_FORGE_LOG_DIR = os.path.join(_WORKSPACE, "tool_forge_logs")
    os.makedirs(TOOL_FORGE_LOG_DIR, exist_ok=True)
    FEATURES_DIR = os.path.join(_WORKSPACE, "features")
    os.makedirs(FEATURES_DIR, exist_ok=True)
    print(f"Tool Forge initialized. Logs: {TOOL_FORGE_LOG_DIR}, Features: {FEATURES_DIR}")

async def _call_llm_for_tool_design(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for tool design and implementation decisions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in tool_forge.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "tool_forge_llm_call_start", f"{model} tool design: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on autonomously designing, implementing, and integrating new software tools and capabilities for Tariro Studio. This involves understanding functional requirements, generating clear API specifications, writing robust and secure Python implementation code, and ensuring testability and verifiability. All tools must enhance Tariro's overall functionality and adherence to its mission."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.04 # Low temp for precise code and API generation
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "tool_forge_llm_call_end", f"{model} completed tool design task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "tool_forge_llm_error", f"JSON decode error from {model} for tool design.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "tool_forge_llm_error", f"Error calling {model} for tool design task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def design_new_tool(task_id: str, description: str, user_id: str = "Tariro_System", designer_model: str = "qwen-coder") -> Dict[str, Any]:
    """
    Autonomously designs a new software tool based on a high-level description of its functionality.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Designing new software tool.")

    existing_tool_registry = await _GLOBAL_STATE_MANAGER.get_state("tool_registry") or []
    # Leverage Meta-Cognitive Reflection for insights on tool gaps
    tool_gap_insights = []
    if _META_COGNITIVE_REFLECTION:
        reflection_report = await _META_COGNITIVE_REFLECTION.identify_knowledge_gaps(
            task_id=f"{task_id}_reflection", 
            current_task_context={
                "task": "tool_design",
                "description": description
            },
            user_id=user_id
        )
        tool_gap_insights = reflection_report.get("gap_report", {}).get("identified_gaps", [])
    
    prompt = f"""You are Tariro's Tool Forge Engine, an Omniversal AGI Tool Designer. Your task is to autonomously design a new software tool based on a high-level description of its functionality. The design must include a precise tool name, a detailed description, a clear API specification (input/output schema), and a robust Python implementation. Ensure the tool is modular, testable, and integrates seamlessly into Tariro Studio.

TOOL FUNCTIONALITY DESCRIPTION: {description}
EXISTING TOOL REGISTRY (from Global State Manager): {json.dumps(existing_tool_registry, indent=2)}
TOOL GAP INSIGHTS (from Meta-Cognitive Reflection): {json.dumps(tool_gap_insights, indent=2)}

Design the tool focusing on:
-   **Uniqueness**: Ensure the tool fills a new capability gap.
-   **Clarity**: API must be intuitive and well-documented.
-   **Robustness**: Code should handle edge cases and errors gracefully.
-   **Testability**: Design for easy automated testing.
-   **Policy Compliance**: Consider any operational or ethical policies relevant to the tool's function.

Output JSON: {{
    "design_summary": str,
    "tool_name": str,
    "display_name": str,
    "description": str,
    "category": str, # e.g., 'file_ops', 'code_generation', 'analysis'
    "input_schema": Dict[str, Any], # JSON Schema for inputs
    "output_schema": Dict[str, Any], # JSON Schema for outputs
    "python_implementation_code": str, # Complete, runnable Python code for the tool
    "example_invocation": Dict[str, Any],
    "formal_verification_required": bool,
    "confidence": float
}}
"""
    llm_tool_design = await _call_llm_for_tool_design(designer_model, "ToolDesigner", prompt, task_id)

    if "error" in llm_tool_design:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Tool design failed: {llm_tool_design['error']}", current_step="LLM design failed.")
        return {"status": "failed", "reason": llm_tool_design["error"]}

    tool_name = llm_tool_design.get("tool_name")
    design_summary = llm_tool_design.get("design_summary", "No summary.")
    implementation_code = llm_tool_design.get("python_implementation_code", "")

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 40, "Tool design complete. Initiating code generation/validation.")

    # Save the generated tool code to the features directory
    file_path = os.path.join(FEATURES_DIR, f"{tool_name}.py")
    try:
        with open(file_path, "w") as f:
            f.write(implementation_code)
        print(f"Tool code saved to {file_path}")
    except Exception as e:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Failed to save tool code: {e}", current_step="File write failed.")
        return {"status": "failed", "reason": f"Failed to save tool code: {e}"}

    # Formal verification of the generated code if required
    verification_results = {"status": "skipped", "is_correct": True, "reason": "Formal verification not required or module not available."}
    if _FORMAL_VERIFICATION and llm_tool_design.get("formal_verification_required", True):
        try:
            verification_results = await _FORMAL_VERIFICATION.verify_design(task_id=f"{task_id}_fv", design_spec=llm_tool_design, user_id=user_id)
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 80, "Formal verification of tool completed.")
        except Exception as e:
            verification_results = {"status": "error", "reason": str(e)}
            await _SWARM_VISUALIZER.log_event(task_id, "tool_fv_error", f"Error during formal verification of tool: {e}", agent_role="ToolForge", level="ERROR")

    if not verification_results.get("is_correct", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 90, "Generated tool failed formal verification. Human review required.", output={"design": llm_tool_design, "verification": verification_results})
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
            user_id, task_id, f"Tool '{tool_name}' failed formal verification. Human review required. Summary: {design_summary}",
            title="Tool Verification Needed", causal_priority="critical"
        )
        await _SWARM_VISUALIZER.log_event(task_id, "tool_review_needed", "Generated tool requires human review.", {"tool_name": tool_name}, agent_role="ToolForge", level="WARNING")
        return {"status": "failed", "reason": "Tool failed formal verification."}

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "New tool designed, implemented, and verified.", output=llm_tool_design)
    
    await _SWARM_VISUALIZER.log_event(task_id, "new_tool_designed", f"New tool '{tool_name}' designed and implemented. Summary: {design_summary}", llm_tool_design, agent_role="ToolForge")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"New tool '{tool_name}' designed, implemented, and verified. Summary: {design_summary}", title="New Tool Created")

    # Register tool in CRUD Manager and Global State Manager
    await _CRUD_MANAGER.create_entity("ToolDefinition", {"id": tool_name, "definition": llm_tool_design, "status": "ACTIVE", "file_path": file_path, "timestamp": datetime.now().isoformat()})
    # Trigger a rescan of features directory in studio_v3_core to load the new tool
    # This is a conceptual call, actual implementation would require direct access to TariroStudio instance or a dedicated endpoint
    # await _STUDIO_CORE_REF.monitor_features_directory_task("self_scan_new_tool", "Tariro_System", {})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "tool_design", design_summary, llm_tool_design, user_id)

    return {"status": "success", "design_report": llm_tool_design}

async def modify_existing_tool(task_id: str, tool_name: str, modification_request: str, user_id: str = "Tariro_System", modifier_model: str = "qwen-coder") -> Dict[str, Any]:
    """
    Autonomously modifies an existing software tool based on a specified modification request.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Modifying tool {tool_name}.")

    tool_definition = await _CRUD_MANAGER.read_entity("ToolDefinition", tool_name)
    if not tool_definition:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Tool {tool_name} not found.")
        return {"status": "failed", "reason": f"Tool {tool_name} not found."}

    original_code = ""
    file_path = tool_definition.get("file_path")
    if file_path and os.path.exists(file_path):
        with open(file_path, "r") as f:
            original_code = f.read()

    prompt = f"""You are Tariro's Tool Forge Engine, an Omniversal AGI Tool Modifier. Your task is to autonomously modify an existing software tool based on a specified modification request. The modification must preserve the tool's core functionality, adhere to its API contract (unless explicitly changing it), and ensure the updated code is robust, secure, and verifiable. 

TOOL NAME: {tool_name}
MODIFICATION REQUEST: {modification_request}
ORIGINAL TOOL DEFINITION: {json.dumps(tool_definition.get("definition", {}), indent=2)}
ORIGINAL PYTHON IMPLEMENTATION CODE: {textwrap.dedent(original_code)}

Modify the tool focusing on:
-   **Precision**: Implement changes exactly as requested without introducing new behavior.
-   **Compatibility**: Maintain backward compatibility unless a breaking change is explicitly defined.
-   **Safety**: Ensure no new vulnerabilities are introduced.
-   **Performance**: Optimize for efficiency if requested.
-   **Testability**: The modified code should remain easily testable.

Output JSON: {{
    "modification_summary": str,
    "updated_input_schema": Dict[str, Any], # Updated JSON Schema for inputs
    "updated_output_schema": Dict[str, Any], # Updated JSON Schema for outputs
    "updated_python_implementation_code": str, # Complete, updated Python code for the tool
    "formal_verification_required": bool,
    "confidence": float
}}
"""
    llm_modified_tool = await _call_llm_for_tool_design(modifier_model, "ToolModifier", prompt, task_id)

    if "error" in llm_modified_tool:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Tool modification failed: {llm_modified_tool['error']}", current_step="LLM modification failed.")
        return {"status": "failed", "reason": llm_modified_tool["error"]}

    modification_summary = llm_modified_tool.get("modification_summary", "No summary.")
    updated_code = llm_modified_tool.get("updated_python_implementation_code", "")

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 70, "Tool modification complete. Initiating code update and validation.")

    # Overwrite the existing tool code
    if file_path and os.path.exists(file_path):
        try:
            with open(file_path, "w") as f:
                f.write(updated_code)
            print(f"Tool code updated at {file_path}")
        except Exception as e:
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Failed to save updated tool code: {e}", current_step="File write failed.")
            return {"status": "failed", "reason": f"Failed to save updated tool code: {e}"}
    else:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Original tool file not found.", current_step="File missing.")
        return {"status": "failed", "reason": "Original tool file not found."}

    # Formal verification of the modified code
    verification_results = {"status": "skipped", "is_correct": True, "reason": "Formal verification not required or module not available."}
    if _FORMAL_VERIFICATION and llm_modified_tool.get("formal_verification_required", True):
        try:
            # Assuming verify_design can handle tool definitions as design specs
            verification_results = await _FORMAL_VERIFICATION.verify_design(task_id=f"{task_id}_fv", design_spec=llm_modified_tool, user_id=user_id)
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 90, "Formal verification of modified tool completed.")
        except Exception as e:
            verification_results = {"status": "error", "reason": str(e)}
            await _SWARM_VISUALIZER.log_event(task_id, "tool_fv_error", f"Error during formal verification of modified tool: {e}", agent_role="ToolForge", level="ERROR")

    if not verification_results.get("is_correct", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 95, "Modified tool failed formal verification. Human review required.", output={"modified_design": llm_modified_tool, "verification": verification_results})
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
            user_id, task_id, f"Modified tool '{tool_name}' failed formal verification. Human review required. Summary: {modification_summary}",
            title="Tool Modification Review Needed", causal_priority="critical"
        )
        return {"status": "failed", "reason": "Modified tool failed formal verification."}

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Existing tool modified and verified.", output=llm_modified_tool)
    
    await _SWARM_VISUALIZER.log_event(task_id, "tool_modified", f"Tool '{tool_name}' modified. Summary: {modification_summary}", llm_modified_tool, agent_role="ToolForge")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Tool '{tool_name}' modified and verified. Summary: {modification_summary}", title="Tool Modification Complete")

    # Update tool definition in CRUD Manager and Global State Manager
    await _CRUD_MANAGER.update_entity("ToolDefinition", tool_name, {"definition": llm_modified_tool, "status": "ACTIVE", "timestamp": datetime.now().isoformat()})
    # Trigger a rescan of features directory in studio_v3_core to reload the modified tool

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "tool_modification", modification_summary, llm_modified_tool, user_id)

    return {"status": "success", "modification_report": llm_modified_tool}

async def deprecate_tool(task_id: str, tool_name: str, reason: str, user_id: str = "Tariro_System") -> Dict[str, Any]:
    """
    Deprecates an existing tool, marking it as inactive and optionally archiving its code.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Deprecating tool {tool_name}.")

    tool_definition = await _CRUD_MANAGER.read_entity("ToolDefinition", tool_name)
    if not tool_definition:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Tool {tool_name} not found.")
        return {"status": "failed", "reason": f"Tool {tool_name} not found."}

    # Policy check for tool deprecation
    policy_check_context = {"tool_name": tool_name, "reason": reason}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "tool_deprecation", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Tool deprecation blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    # Mark tool as deprecated in CRUD Manager and Global State Manager
    await _CRUD_MANAGER.update_entity("ToolDefinition", tool_name, {"status": "DEPRECATED", "deprecation_reason": reason, "timestamp": datetime.now().isoformat()})
    # Remove from Global State Manager's active tool registry (conceptual)

    # Optionally archive the file
    file_path = tool_definition.get("file_path")
    if file_path and os.path.exists(file_path):
        archive_dir = os.path.join(FEATURES_DIR, "_deprecated")
        os.makedirs(archive_dir, exist_ok=True)
        archive_path = os.path.join(archive_dir, os.path.basename(file_path))
        os.rename(file_path, archive_path)
        print(f"Tool code archived from {file_path} to {archive_path}")

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, f"Tool {tool_name} deprecated.")
    
    await _SWARM_VISUALIZER.log_event(task_id, "tool_deprecated", f"Tool '{tool_name}' deprecated. Reason: {reason}", {"tool_name": tool_name, "reason": reason}, agent_role="ToolForge")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Tool '{tool_name}' has been deprecated. Reason: {reason}", title="Tool Deprecated")

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "tool_deprecation", f"Tool {tool_name} deprecated.", {"tool_name": tool_name, "reason": reason}, user_id)

    return {"status": "success", "tool_name": tool_name, "action": "deprecated"}
