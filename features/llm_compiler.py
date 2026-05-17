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
_CRUD_MANAGER: Any = None # Reference to crud_manager module for CompiledCode or CompilationLog entities
_PERSISTENT_TASK_MANAGER: Any = None # For submitting compilation/transpilation tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on compilation success/failure
_GLOBAL_STATE_MANAGER: Any = None # For storing language definitions, target platform specs
_SELF_EVOLUTION: Any = None # For optimizing generated code
_FORMAL_VERIFICATION: Any = None # For formally verifying generated code correctness
_AUTONOMY_GOVERNANCE: Any = None # For policy checks on code generation/deployment
_META_LEARNER: Any = None # For learning from compilation errors and code performance
_LLM_COMPILER: Any = None # Self-reference, will be passed to other modules if needed

LLM_COMPILER_LOG_DIR: str = ""

def initialize_llm_compiler(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, global_state_manager_module: Any, self_evolution_module: Any, formal_verification_module: Any, autonomy_governance_module: Any, meta_learner_module: Any):
    """Initializes global configurations for the LLM Compiler module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _GLOBAL_STATE_MANAGER, _SELF_EVOLUTION, _FORMAL_VERIFICATION, _AUTONOMY_GOVERNANCE, _META_LEARNER, LLM_COMPILER_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _SELF_EVOLUTION = self_evolution_module
    _FORMAL_VERIFICATION = formal_verification_module
    _AUTONOMY_GOVERNANCE = autonomy_governance_module
    _META_LEARNER = meta_learner_module

    LLM_COMPILER_LOG_DIR = os.path.join(_WORKSPACE, "llm_compiler_logs")
    os.makedirs(LLM_COMPILER_LOG_DIR, exist_ok=True)
    print(f"LLM Compiler initialized. Logs: {LLM_COMPILER_LOG_DIR}")

async def _call_llm_for_compilation(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for code generation and compilation decisions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in llm_compiler.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "llm_compiler_llm_call_start", f"{model} code generation: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on autonomously compiling high-level intent, specifications, or abstract code into executable, optimized, and verifiable code in various target languages or formats (Python, Rust, C++, LLVM IR, WASM, HDL, etc.). Ensure correctness, efficiency, security, and adherence to programming best practices. Generate accompanying test cases and deployment manifests."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.02 # Very low temp for deterministic and correct code generation
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "llm_compiler_llm_call_end", f"{model} completed code generation task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "llm_compiler_llm_error", f"JSON decode error from {model} for code generation.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "llm_compiler_llm_error", f"Error calling {model} for code generation task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def compile_intent_to_code(task_id: str, high_level_intent: str, target_language: str, user_id: str = "Tariro_System", compiler_model: str = "qwen-coder") -> Dict[str, Any]:
    """
    Compiles a high-level semantic intent or abstract specification into executable source code
    in a specified target programming language.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Compiling intent to {target_language} code.")

    target_platform_specs = await _GLOBAL_STATE_MANAGER.get_state(f"platform_spec_{target_language}") or {}
    # Check for relevant coding standards or patterns from Self-Evolution (conceptual)
    coding_standards = []
    if _SELF_EVOLUTION:
        # Mock: coding_standards = await _SELF_EVOLUTION.get_coding_standards(target_language)
        pass
    
    # Policy check for code generation
    policy_check_context = {"intent": high_level_intent, "target_language": target_language}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "code_generation", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Code generation blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's LLM Compiler, an Omniversal AGI Code Synthesizer. Your task is to compile a high-level semantic intent or abstract specification into executable, optimized, and verifiable source code in the specified target programming language. Ensure correctness, efficiency, security, and adherence to programming best practices for the given target platform. Generate accompanying unit tests and clear build instructions.

HIGH-LEVEL SEMANTIC INTENT: {high_level_intent}
TARGET PROGRAMMING LANGUAGE: {target_language}
TARGET PLATFORM SPECIFICATIONS (from Global State Manager): {json.dumps(target_platform_specs, indent=2)}
RELEVANT CODING STANDARDS: {json.dumps(coding_standards, indent=2)}

Generate code focusing on:
-   **Functional Correctness**: The code must meet all specified requirements.
-   **Optimization**: Efficient algorithms, minimal resource usage.
-   **Security**: Implement secure coding practices, prevent common vulnerabilities.
-   **Readability & Maintainability**: Clean, well-commented code.
-   **Testability**: Include comprehensive unit and integration tests.
-   **Build Instructions**: Provide clear steps to compile/run the code.

Output JSON: {{
    "compilation_summary": str,
    "generated_code": str,
    "generated_tests": str,
    "build_instructions": List[str],
    "formal_verification_required": bool,
    "confidence": float
}}
"""
    llm_compilation = await _call_llm_for_compilation(compiler_model, "CodeSynthesizer", prompt, task_id)

    if "error" in llm_compilation:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Code compilation failed: {llm_compilation['error']}", current_step="LLM code generation failed.")
        return {"status": "failed", "reason": llm_compilation["error"]}

    compilation_summary = llm_compilation.get("compilation_summary", "No summary.")
    generated_code = llm_compilation.get("generated_code", "")
    generated_tests = llm_compilation.get("generated_tests", "")

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 70, "Code generated. Initiating formal verification.")

    # Formal verification of generated code
    verification_results = {"status": "skipped", "is_correct": True, "reason": "Formal verification not required or module not available."}
    if _FORMAL_VERIFICATION and llm_compilation.get("formal_verification_required", True):
        try:
            verification_results = await _FORMAL_VERIFICATION.verify_design(
                task_id=f"{task_id}_fv",
                design_spec=llm_compilation, # Assuming code + intent forms design spec
                user_id=user_id
            )
            await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 90, "Formal verification of generated code completed.")
        except Exception as e:
            verification_results = {"status": "error", "reason": str(e)}
            await _SWARM_VISUALIZER.log_event(task_id, "code_fv_error", f"Error during formal verification of generated code: {e}", agent_role="LLMCompiler", level="ERROR")

    if not verification_results.get("is_correct", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 95, "Generated code failed formal verification. Human review required.", output={"compilation": llm_compilation, "verification": verification_results})
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
            user_id, task_id, f"Generated {target_language} code failed formal verification. Human review required. Summary: {compilation_summary}",
            title="Code Verification Failed", causal_priority="critical"
        )
        return {"status": "failed", "reason": "Generated code failed formal verification."}

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "High-level intent compiled to code.", output=llm_compilation)
    
    await _SWARM_VISUALIZER.log_event(task_id, "intent_compiled_to_code", f"Intent compiled to {target_language} code. Summary: {compilation_summary}", llm_compilation, agent_role="LLMCompiler")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"High-level intent compiled to {target_language} code. Summary: {compilation_summary}", title="Code Compilation Complete")

    # Store compiled code in CRUD Manager
    await _CRUD_MANAGER.create_entity("CompiledCode", {"id": task_id, "intent": high_level_intent, "target_language": target_language, "code": generated_code, "tests": generated_tests, "report": llm_compilation, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "code_compilation", compilation_summary, llm_compilation, user_id)

    return {"status": "success", "compilation_report": llm_compilation}

async def optimize_generated_code(task_id: str, generated_code_id: str, optimization_goals: List[str], user_id: str = "Tariro_System", optimizer_model: str = "self-evolution") -> Dict[str, Any]:
    """
    Optimizes previously generated code for performance, resource usage, or security, using Self-Evolution.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Optimizing generated code.")

    compiled_code_record = await _CRUD_MANAGER.read_entity("CompiledCode", generated_code_id)
    if not compiled_code_record:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Compiled code {generated_code_id} not found.")
        return {"status": "failed", "reason": f"Compiled code {generated_code_id} not found."}

    original_code = compiled_code_record.get("code", "")
    target_language = compiled_code_record.get("target_language", "python")

    if not _SELF_EVOLUTION:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Self-Evolution module not loaded for optimization.")
        return {"status": "failed", "reason": "Self-Evolution module not loaded."}

    optimization_result = await _SELF_EVOLUTION.optimize_code(
        task_id=f"{task_id}_evolve",
        code=original_code,
        language=target_language,
        optimization_goals=optimization_goals,
        user_id=user_id
    )

    if optimization_result.get("status") != "success":
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Code optimization failed in Self-Evolution.", output=optimization_result)
        return {"status": "failed", "reason": "Code optimization failed.", "details": optimization_result}

    optimized_code = optimization_result.get("optimized_code", original_code)
    optimization_summary = optimization_result.get("optimization_summary", "No summary.")

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Generated code optimized.", output=optimization_result)
    
    await _SWARM_VISUALIZER.log_event(task_id, "code_optimized", f"Generated code optimized. Summary: {optimization_summary}", optimization_result, agent_role="LLMCompiler")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Generated {target_language} code optimized. Summary: {optimization_summary}", title="Code Optimization Complete")

    # Update compiled code in CRUD Manager
    await _CRUD_MANAGER.update_entity("CompiledCode", generated_code_id, {"code": optimized_code, "optimization_report": optimization_result, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "code_optimization", optimization_summary, optimization_result, user_id)

    return {"status": "success", "optimization_report": optimization_result}

async def transpile_code(task_id: str, source_code: str, source_language: str, target_language: str, user_id: str = "Tariro_System", transpiler_model: str = "qwen-coder") -> Dict[str, Any]:
    """
    Transpiles source code from one programming language to another.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, f"Transpiling code from {source_language} to {target_language}.")

    # Policy check for code transpilation
    policy_check_context = {"source_language": source_language, "target_language": target_language, "source_code_snippet": source_code[:100]}
    policy_compliance_report = await _AUTONOMY_GOVERNANCE.check_policy(user_id, "code_transpilation", policy_check_context)
    if not policy_compliance_report.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Code transpilation blocked by policy.", output=policy_compliance_report)
        return {"status": "failed", "reason": "Policy non-compliance", "details": policy_compliance_report}

    prompt = f"""You are Tariro's LLM Compiler, an Omniversal AGI Code Transpiler. Your task is to accurately and efficiently transpile source code from one programming language to another. The transpiled code must be functionally equivalent to the original, follow best practices for the target language, and maintain readability. Generate accompanying tests for the transpiled code.

SOURCE CODE: {textwrap.dedent(source_code)}
SOURCE LANGUAGE: {source_language}
TARGET LANGUAGE: {target_language}

Transpile code focusing on:
-   **Functional Equivalence**: The transpiled code must behave identically to the original.
-   **Idiomatic Translation**: Use idiomatic constructs and patterns of the target language.
-   **Performance Preservation**: Aim for equivalent or better performance.
-   **Error Handling**: Ensure robust error handling is preserved or adapted.
-   **Test Generation**: Include a set of tests for the transpiled code.

Output JSON: {{
    "transpilation_summary": str,
    "transpiled_code": str,
    "transpiled_tests": str,
    "confidence": float
}}
"""
    llm_transpilation = await _call_llm_for_compilation(transpiler_model, "CodeTranspiler", prompt, task_id)

    if "error" in llm_transpilation:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Code transpilation failed: {llm_transpilation['error']}", current_step="LLM transpilation failed.")
        return {"status": "failed", "reason": llm_transpilation["error"]}

    transpilation_summary = llm_transpilation.get("transpilation_summary", "No summary.")
    transpiled_code = llm_transpilation.get("transpiled_code", "")

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Code transpiled successfully.", output=llm_transpilation)
    
    await _SWARM_VISUALIZER.log_event(task_id, "code_transpiled", f"Code transpiled from {source_language} to {target_language}. Summary: {transpilation_summary}", llm_transpilation, agent_role="LLMCompiler")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Code transpiled from {source_language} to {target_language}. Summary: {transpilation_summary}", title="Code Transpilation Complete")

    # Store transpiled code in CRUD Manager
    await _CRUD_MANAGER.create_entity("CompiledCode", {"id": task_id, "source_code": source_code, "source_language": source_language, "target_language": target_language, "code": transpiled_code, "report": llm_transpilation, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "code_transpilation", transpilation_summary, llm_transpilation, user_id)

    return {"status": "success", "transpilation_report": llm_transpilation}
