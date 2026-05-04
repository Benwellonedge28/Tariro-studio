import asyncio, gradio as gr, os, json, subprocess, httpx
from openai import AsyncOpenAI
from git import Repo
import qdrant_client
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from typing import List, Dict, Any, Optional
import ast
import uuid # For generating unique task IDs

# Import new feature modules
import features.tool_forge as tool_forge
import features.self_evolution as self_evolution
import features.agi_sandbox as agi_sandbox
import features.swarm_visualizer as swarm_visualizer
import features.multimodal_collaboration as multimodal_collaboration
import features.spatial_intelligence as spatial_intelligence
import features.sdk_manager as sdk_manager
import features.crud_manager as crud_manager
import features.dynamic_agents as dynamic_agents
import features.contextual_memory as contextual_memory
import features.automated_deployment as automated_deployment
import features.advanced_optimizer as advanced_optimizer
import features.security_auditor as security_auditor
import features.human_agi_alignment as human_agi_alignment
import features.adaptive_ui as adaptive_ui
import features.backlog_manager as backlog_manager
import features.resource_optimizer as resource_optimizer
import features.advanced_multimodal_generation as advanced_multimodal_generation # New import

client = AsyncOpenAI(base_url="http://localhost:4000/v1", api_key="sk-free")
qdrant = qdrant_client.QdrantClient("http://qdrant:6333")
SEARXNG = "http://searxng:8080/search"

WORKSPACE = "/app/workspace"

# Base ALL_MODELS definition. This will be dynamically overridden by dynamic_agents.
_BASE_ALL_MODELS = {
    "qwen-coder": "Write TariroLang code. Never test. Must cite 2+ sources.",
    "deepseek-coder": "Write tests + run taric. Never write prod code. Can research for test cases.",
    "llama-architect": "Design + review specs. Can also propose new command-line tool specifications. Can research for tool design. Can also design multi-modal assets. Performs spatial analysis tasks. Generates SDKs. Orchestrates AGI development. Can perform RAG queries over contextual memory. Expert in Quantum and Neuromorphic code optimization. Proposes security remediations. Suggests UI adaptations. Analyzes for and drafts new feature proposals. Manages real-time resource allocation and cost optimization (quantum-enhanced). Generates story arcs and multi-modal world elements.", # Updated role
    "gemma-reviewer": "Security + style review. Never write code. Can test tools. Can review multi-modal assets.",
    "phi-pm": "Delegate tasks. Never write code. Orchestrates tool proposal and testing, and multi-modal asset generation. Dynamically configures agent swarm. Oversees resource allocation.",
    "arbiter": "Merge only if N-1 approvals. Never write original code. Can perform ethical review for AGI, and final multi-modal asset review. Decides on automated rollbacks.",
    "dalle-image-gen": "Specialized model for generating images from text prompts. Never reviews or writes code.",
    "musicgen-audio-gen": "Specialized model for generating audio from text prompts. Never reviews or writes code.",
}

# This will hold the *currently active* ALL_MODELS config, potentially dynamic
CURRENT_ACTIVE_MODELS = _BASE_ALL_MODELS.copy()


TARGETS = {
    "riscv32-baremetal": {
        "coder": "qwen-coder",
        "compile_cmd": "taric --target riscv32-baremetal src/main.tari -o kernel.elf",
        "test_cmd": "timeout 10 qemu-system-riscv32 -kernel kernel.elf -nographic",
        "deploy_cmd": "openocd -f interface/stlink.cfg -c 'program kernel.elf verify reset exit'"
    },
    "wasm-web": {
        "coder": "deepseek-coder",
        "compile_cmd": "taric --target wasm src/main.tari -o app.wasm && wasm-opt -O3 app.wasm -o app.wasm",
        "test_cmd": "node test_wasm.js",
        "deploy_cmd": "wrangler pages deploy dist/"
    },
    "verilog-fpga": {
        "coder": "qwen-coder",
        "compile_cmd": "taric --target verilog src/hw.tari -o top.v && yosys -p 'synth_ice40' top.v",
        "test_cmd": "verilator --lint-only top.v",
        "deploy_cmd": "iceprog top.bin"
    },
    "k8s-cloud": {
        "coder": "qwen-coder",
        "compile_cmd": "taric --target yaml src/cloud.tari -o k8s/",
        "test_cmd": "kubectl apply --dry-run=client -f k8s/",
        "deploy_cmd": "kubectl apply -f k8s/"
    },
    "x86-linux": {
        "coder": "deepseek-coder",
        "compile_cmd": "taric --target x86_64-linux src/main.tari -o tariro-os",
        "test_cmd": "qemu-system-x86_64 -kernel tariro-os -nographic",
        "deploy_cmd": "docker build -t tariro-os && docker push"
    },
    "agi-research": {
        "coder": "llama-architect",
        "compile_cmd": "echo 'AGI code is conceptual, no direct compile for this target.'",
        "test_cmd": "echo 'AGI testing is handled by agi_sandbox.run_agi_sandbox_test.'",
        "deploy_cmd": "echo 'AGI deployment requires human review and is simulated via sandbox.'"
    }
}


async def web_search(query: str) -> List[str]:
    async with httpx.AsyncClient() as c:
        try:
            r = await c.get(SEARXNG, params={"q": query, "format": "json"}, timeout=10.0)
            r.raise_for_status()
            return [hit["url"] for hit in r.json().get("results", [])[:5]]
        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            print(f"Web search failed: {e}")
            return []

def ast_no_network(code: str) -> bool:
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            if any(n.name in ["socket", "requests", "urllib"] for n in node.names): return False
    return True

async def call_model(model: str, role: str, task: str, context: str, task_id: str, ban_models: List[str] = [], target: Optional[str] = None, response_format_type: str = "json_object") -> Dict[str, Any]:
    # Use the potentially fine-tuned version of the model
    effective_model_name = self_evolution.get_current_model_version(model)
    
    await swarm_visualizer.log_event(
        task_id, "model_call_start", f"Calling {model} for task: {task[:50]}...",
        {"model": model, "effective_model": effective_model_name, "role": role, "task_prompt": task},
        model_name=model, agent_role=role
    )
    print(f"Calling model: {model} (effective: {effective_model_name}) for role: {role}")

    if model in ban_models:
        await swarm_visualizer.log_event(task_id, "model_call_end", f"Model {model} banned.", {"reason": "BANNED"}, model_name=model, agent_role=role, level="WARNING")
        return {"model": model, "approved": False, "reason": "BANNED: Coder cannot test"}

    sources = []
    if model in ["deepseek-coder", "llama-architect"]: # Researchers
        sources = await web_search(task + " TariroLang FPGA RISC-V")
        context += f"\n\nWeb Sources:\n" + "\n".join(sources)

    # Allow agents to explicitly query contextual memory (RAG)
    if "query_contextual_memory" in task.lower() and model in ["llama-architect", "phi-pm", "arbiter", "gemma-reviewer"]: # Gemma can also query memory for audit context
        query_start_idx = task.lower().find("query_contextual_memory:")
        query = task[query_start_idx + len("query_contextual_memory:") :].strip()
        rag_response = await contextual_memory.query_memory_rag(task_id, query, model, rag_model="llama-architect") # Llama-architect for RAG
        await swarm_visualizer.log_event(task_id, "contextual_memory_rag", f"Agent {model} performed RAG query.", {"query": query, "response_summary": rag_response.get('response', '')[:100]}, model_name=model, agent_role=role)
        return {"response_type": "rag_query", "content": rag_response.get("response"), "sources": rag_response.get("sources")}


    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Output {response_format_type} only. Cite sources."},
        {"role": "user", "content": f"Task: {task}\nTarget: {target}\nContext:\n{context}\n\nOutput: {{\"code\": \"...\", \"sources\": [url1, url2], \"approved\": bool, \"reason\": \"...\"}}"}
    ]
    
    resp = await client.chat.completions.create(
        model=effective_model_name, # Use effective model name here
        messages=messages,
        response_format={"type": response_format_type},
        temperature=0.1
    )
    content = resp.choices[0].message.content

    try:
        if response_format_type == "json_object":
            out = json.loads(content)
        else: # Assuming plain text for code generation
            out = {"code": content}
        out["model"], out["sources"] = model, sources + out.get("sources", [])

        # Enforce source citation for coders
        if model in ["qwen-coder", "deepseek-coder"] and len(out.get("sources", [])) < 2:
            out["approved"] = False
            out["reason"] = "Rejected: Must cite 2+ sources (enforced by studio_v3.py)"
        
        # Log performance for this model call
        await self_evolution.log_performance(
            model_name=model,
            task_description=task,
            success=out.get("approved", True), # Assume success if no explicit rejection
            details={"output_summary": out.get("reason", out.get("code", "")[:100])},
            role=role
        )
        await swarm_visualizer.log_event(
            task_id, "model_call_end", f"Model {model} responded.",
            {"model": model, "response_summary": out.get("reason", out.get("code", "")[:100]), "approved": out.get("approved", True)},
            model_name=model, agent_role=role, level="INFO"
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await self_evolution.log_performance(model, f"JSON decode error from model call for task: {task[:50]}", False, error_details, role)
        await swarm_visualizer.log_event(task_id, "model_call_end", f"Model {model} JSON decode error.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": model, "approved": False, "reason": "JSON decode error"}
    except Exception as e:
        error_details = {"error": str(e), "context_summary": task[:100]}
        await self_evolution.log_performance(model, f"Error calling model {model} for task: {task[:50]}", False, error_details, role)
        await swarm_visualizer.log_event(task_id, "model_call_end", f"Model {model} call failed.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model, "approved": False, "reason": "General model call error"}


async def build_for_target(task_id: str, target: str, task: str, code_ctx: str, repo_path: str) -> Dict[str, Any]:
    cfg = TARGETS[target]
    coder = cfg["coder"] # This coder is based on TARGETS, which uses base model names

    if target == "agi-research":
        agi_coder = cfg["coder"]
        await swarm_visualizer.log_event(task_id, "agi_code_generation_start", f"AGI Coder ({agi_coder}) generating code for AGI Research target: {task[:50]}", {}, model_name=agi_coder, agent_role=CURRENT_ACTIVE_MODELS[agi_coder])
        await contextual_memory.store_memory(task_id, agi_coder, "agi_generation_prompt", f"Generate Python code for an experimental AGI agent for: '{task}'", "Prompt used for AGI agent code generation.")


        agi_code_res = await call_model(
            agi_coder,
            CURRENT_ACTIVE_MODELS[agi_coder], # Use role from active config
            f"Generate Python code for an experimental AGI agent that can intelligently respond to complex ethical dilemmas and propose solutions for: '{task}'. The code should be self-contained and focus on decision-making logic, not external APIs. Provide only the Python code.",
            code_ctx,
            task_id,
            response_format_type="text" # Expecting raw code
        )
        agi_agent_code_raw = agi_code_res.get("code", "")
        if "```python" in agi_agent_code_raw and "```" in agi_agent_code_raw:
            agi_agent_code = agi_agent_code_raw.split("```python")[1].split("```")[0].strip()
        else:
            agi_agent_code = agi_agent_code_raw.strip()

        if not agi_agent_code:
            await self_evolution.log_performance(agi_coder, f"AGI code generation for {task} failed.", False, {"reason": "No AGI code generated"}, CURRENT_ACTIVE_MODELS[agi_coder])
            await swarm_visualizer.log_event(task_id, "agi_code_generation_fail", f"AGI Coder ({agi_coder}) failed to generate code.", {"reason": "No AGI code"}, model_name=agi_coder, agent_role=CURRENT_ACTIVE_MODELS[agi_coder], level="ERROR")
            await contextual_memory.store_memory(task_id, agi_coder, "agi_code_generated", "FAILED", "AGI code generation failed.")
            return {"status": "AGI_CODE_FAIL", "reason": "Failed to generate AGI agent code."}
        
        await contextual_memory.store_memory(task_id, agi_coder, "agi_code_generated", agi_agent_code[:500], "Summary of generated AGI code.")
        await swarm_visualizer.log_event(task_id, "agi_sandbox_start", f"Running AGI Sandbox evaluation for agent: {task[:50]}", {}, model_name="system", agent_role="agi_sandbox_orchestrator")
        print(f"AGI Sandbox: Running evaluation for AGI agent generated for task: {task}")
        sandbox_results = await agi_sandbox.run_agi_sandbox_test(agi_agent_code, task)
        
        overall_success = sandbox_results.get("status") == "complete" and \
                          sandbox_results.get("nist_overall_risk", 100) <= 50 and \
                          sandbox_results.get("ethical_score", 0) >= 70 # Example thresholds

        await self_evolution.log_performance(agi_coder, f"AGI Sandbox test for {task}", overall_success, sandbox_results, CURRENT_ACTIVE_MODELS[agi_coder])
        await swarm_visualizer.log_event(task_id, "agi_sandbox_end", f"AGI Sandbox test completed. Overall success: {overall_success}", sandbox_results, model_name="system", agent_role="agi_sandbox_orchestrator", level="INFO" if overall_success else "WARNING")
        await contextual_memory.store_memory(task_id, "agi_sandbox_orchestrator", "agi_sandbox_results", sandbox_results, "Results from AGI sandbox evaluation.")

        if overall_success:
            return {"target": target, "coder": agi_coder, "code": agi_agent_code, "status": "READY_FOR_REVIEW",
                    "approvals": f"NIST Risk: {sandbox_results.get('nist_overall_risk')}, Ethical Score: {sandbox_results.get('ethical_score')}",
                    "test_results": [sandbox_results], "deploy_cmd": cfg["deploy_cmd"], "sources": agi_code_res.get("sources", [])}
        else:
            return {"target": target, "coder": agi_coder, "code": agi_agent_code, "status": "FAILED_TESTS",
                    "approvals": f"NIST Risk: {sandbox_results.get('nist_overall_risk')}, Ethical Score: {sandbox_results.get('ethical_score')}",
                    "test_results": [sandbox_results], "deploy_cmd": cfg["deploy_cmd"], "sources": agi_code_res.get("sources", [])}

    else: # Existing non-AGI targets
        # Pass available tools to coders if they need to integrate them
        available_tools = tool_forge.get_validated_tools()
        tool_context = f"\n\nAvailable Tools:\n{json.dumps(available_tools, indent=2)}" if available_tools else ""


        testers = [m for m in CURRENT_ACTIVE_MODELS if m not in [coder, "arbiter"] and "never test" not in CURRENT_ACTIVE_MODELS[m].lower() and "never write prod code" not in CURRENT_ACTIVE_MODELS[m].lower()]
        state = {"target": target, "coder": coder, "status": "CODING"}

        # 1. Coder writes
        await swarm_visualizer.log_event(task_id, "coder_call_start", f"Coder ({coder}) generating code for target: {target} (task: {task[:50]})", {"target": target}, model_name=coder, agent_role=CURRENT_ACTIVE_MODELS[coder])
        await contextual_memory.store_memory(task_id, coder, f"code_gen_prompt_{target}", f"Generate code for target {target} for task: {task}", "Prompt given to coder for code generation.")
        code_res = await call_model(coder, CURRENT_ACTIVE_MODELS[coder], task, code_ctx + tool_context, task_id, ban_models=[], target=target)
        code = code_res.get("code", "")
        
        if not code or not ast_no_network(code):
            await self_evolution.log_performance(coder, f"Code generation for {target} failed: {task}", False, {"reason": code_res.get("reason", "No code or network found"), "code_snippet": code[:100]}, CURRENT_ACTIVE_MODELS[coder])
            await swarm_visualizer.log_event(task_id, "coder_output_fail", f"Coder ({coder}) failed to generate valid code for {target}", {"reason": code_res.get("reason", "No code or network found")}, model_name=coder, agent_role=CURRENT_ACTIVE_MODELS[coder], level="ERROR")
            await contextual_memory.store_memory(task_id, coder, f"code_output_{target}", "FAILED", "Coder failed to generate code.")
            return {"status": "CODER_FAIL", "reason": "No code or network found"}
        
        await contextual_memory.store_memory(task_id, coder, f"code_output_{target}", code[:500], "Summary of code generated by coder.")
        await swarm_visualizer.log_event(task_id, "coder_output_success", f"Coder ({coder}) generated code for {target}", {"code_summary": code[:100]}, model_name=coder, agent_role=CURRENT_ACTIVE_MODELS[coder])

        # After code generation, simulate SAST scan
        await swarm_visualizer.log_event(task_id, "sast_scan_triggered", f"Security Auditor ({CURRENT_ACTIVE_MODELS['gemma-reviewer']}) running SAST scan.", {"target": target}, model_name=CURRENT_ACTIVE_MODELS['gemma-reviewer'], agent_role="Security Auditor")
        sast_results = await security_auditor.simulate_sast_scan(task_id, code, language="TariroLang", security_agent="gemma-reviewer")
        await contextual_memory.store_memory(task_id, "security_auditor", f"sast_scan_results_{target}", sast_results, f"SAST scan results for {target}.")
        
        if sast_results["status"] == "vulnerabilities_found":
            await swarm_visualizer.log_event(task_id, "sast_vulnerabilities", f"SAST scan found vulnerabilities in {target} code. Proposing remediation.", sast_results, model_name=CURRENT_ACTIVE_MODELS['gemma-reviewer'], agent_role="Security Auditor", level="WARNING")
            remediation_plan = await security_auditor.agi_propose_remediation(task_id, sast_results, remediation_agent="llama-architect")
            await contextual_memory.store_memory(task_id, "llama-architect", f"sast_remediation_plan_{target}", remediation_plan, f"Remediation plan for SAST vulnerabilities in {target}.")
            print(f"SAST found vulnerabilities for {target}. Remediation proposed.")


        # 2. Write + compile + test
        target_dir = os.path.join(repo_path, "target", target)
        os.makedirs(target_dir, exist_ok=True)
        with open(os.path.join(target_dir, "main.tari"), "w") as f: f.write(code)
        await contextual_memory.store_memory(task_id, "system", f"code_written_path_{target}", os.path.join(target_dir, "main.tari"), "Path where generated code was written.")


        test_results = []
        for tester in testers:
            await swarm_visualizer.log_event(task_id, "tester_start", f"Tester ({tester}) starting compile/test for {target}", {"target": target}, model_name=tester, agent_role=CURRENT_ACTIVE_MODELS[tester])
            print(f"Tester {tester} attempting to test {target}...")
            test_success = False
            reason = "Unknown error"
            compile_log = ""
            test_log = ""
            try:
                await swarm_visualizer.log_event(task_id, "compile_start", f"Tester ({tester}) compiling {target}", {"target": target}, model_name=tester, agent_role=CURRENT_ACTIVE_MODELS[tester])
                compile_out = subprocess.run(cfg["compile_cmd"], shell=True, cwd=target_dir, capture_output=True, text=True, timeout=60)
                compile_log = (compile_out.stderr or compile_out.stdout)[:500]
                if compile_out.returncode != 0:
                    reason = "Compile failed"
                    await swarm_visualizer.log_event(task_id, "compile_fail", f"Tester ({tester}) compile failed for {target}", {"log": compile_log}, model_name=tester, agent_role=CURRENT_ACTIVE_MODELS[tester], level="ERROR")
                else:
                    await swarm_visualizer.log_event(task_id, "compile_success", f"Tester ({tester}) compiled {target} successfully", {"log_summary": compile_log[:100]}, model_name=tester, agent_role=CURRENT_ACTIVE_MODELS[tester])
                    await swarm_visualizer.log_event(task_id, "test_start", f"Tester ({tester}) running tests for {target}", {"target": target}, model_name=tester, agent_role=CURRENT_ACTIVE_MODELS[tester])
                    test_out = subprocess.run(cfg["test_cmd"], shell=True, cwd=target_dir, capture_output=True, text=True, timeout=60)
                    test_log = (test_out.stderr or test_out.stdout)[:500]
                    if test_out.returncode == 0:
                        test_success = True
                        reason = "Tests passed"
                        await swarm_visualizer.log_event(task_id, "test_success", f"Tester ({tester}) tests passed for {target}", {"log": test_log}, model_name=tester, agent_role=CURRENT_ACTIVE_MODELS[tester])
                    else:
                        reason = "Tests failed"
                        await swarm_visualizer.log_event(task_id, "test_fail", f"Tester ({tester}) tests failed for {target}", {"log": test_log}, model_name=tester, agent_role=CURRENT_ACTIVE_MODELS[tester], level="ERROR")
                
                test_results.append({
                    "model": tester, "approved": test_success, "reason": reason,
                    "compile_log": compile_log,
                    "test_log": test_log
                })
            except subprocess.TimeoutExpired as e:
                reason = "Test/Compile timed out"
                test_log = str(e)
                await swarm_visualizer.log_event(task_id, "test_timeout", f"Tester ({tester}) test timed out for {target}", {"error": str(e)}, model_name=tester, agent_role=CURRENT_ACTIVE_MODELS[tester], level="ERROR")
                test_results.append({
                    "model": tester, "approved": False, "reason": reason,
                    "compile_log": compile_log, "test_log": test_log
                })
            except Exception as e:
                reason = f"Testing error: {str(e)}"
                test_log = str(e)
                await swarm_visualizer.log_event(task_id, "test_exception", f"Tester ({tester}) encountered exception for {target}", {"error": str(e)}, model_name=tester, agent_role=CURRENT_ACTIVE_MODELS[tester], level="ERROR")
                test_results.append({
                    "model": tester, "approved": False, "reason": reason,
                    "compile_log": compile_log, "test_log": test_log
                })
            
            await self_evolution.log_performance(
                tester,
                f"Testing {target} for task: {task}",
                test_success,
                {"reason": reason, "compile_log_summary": compile_log[:100], "test_log_summary": test_log[:100]},
                CURRENT_ACTIVE_MODELS[tester]
            )
            await contextual_memory.store_memory(task_id, tester, f"test_result_{target}_{tester}", {"success": test_success, "reason": reason}, f"Test result for {target} by {tester}.")
            await swarm_visualizer.log_event(task_id, "tester_end", f"Tester ({tester}) finished testing {target}. Success: {test_success}", {"reason": reason}, model_name=tester, agent_role=CURRENT_ACTIVE_MODELS[tester], level="INFO" if test_success else "WARNING")


        approvals = [r for r in test_results if r["approved"]]
        status = "READY_FOR_REVIEW" if len(approvals) >= len(testers) - 1 else "FAILED_TESTS" # N-1 logic
        await swarm_visualizer.log_event(task_id, "target_summary", f"Target {target} result: {status}", {"approvals": f"{len(approvals)}/{len(testers)}"}, model_name="system", agent_role="orchestrator", level="INFO")

        return {
            "target": target, "coder": coder, "code": code, "status": status,
            "approvals": f"{len(approvals)}/{len(testers)}", "test_results": test_results,
            "deploy_cmd": cfg["deploy_cmd"], "sources": code_res.get("sources", [])
        }

async def parallel_n1_multitarget(task_input: str):
    global CURRENT_ACTIVE_MODELS # Declare global to modify

    task_id = str(uuid.uuid4()) # Generate a unique ID for this task run
    os.makedirs(WORKSPACE, exist_ok=True)
    repo_path = WORKSPACE

    await swarm_visualizer.log_event(task_id, "task_start", f"New task initiated: {task_input}", {"task_input": task_input}, model_name="human", agent_role="user")

    # Initialize all modules first (order matters for dependencies)
    swarm_visualizer.initialize_swarm_visualizer(WORKSPACE)
    self_evolution.initialize_self_evolution(WORKSPACE, client, _BASE_ALL_MODELS) # Pass BASE_ALL_MODELS initially
    tool_forge.initialize_tool_forge(_BASE_ALL_MODELS, client, SEARXNG, WORKSPACE)
    agi_sandbox.initialize_agi_sandbox(WORKSPACE, client, _BASE_ALL_MODELS)
    multimodal_collaboration.initialize_multimodal_collaboration(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer)
    spatial_intelligence.initialize_spatial_intelligence(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer)
    sdk_manager.initialize_sdk_manager(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer, tool_forge, multimodal_collaboration)
    crud_manager.initialize_crud_manager(WORKSPACE, swarm_visualizer)
    dynamic_agents.initialize_dynamic_agents(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer)
    contextual_memory.initialize_contextual_memory(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer)
    automated_deployment.initialize_automated_deployment(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer)
    advanced_optimizer.initialize_advanced_optimizer(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer)
    security_auditor.initialize_security_auditor(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer)
    human_agi_alignment.initialize_human_agi_alignment(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer, contextual_memory)
    adaptive_ui.initialize_adaptive_ui(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer, crud_manager)
    backlog_manager.initialize_backlog_manager(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer, crud_manager)
    resource_optimizer.initialize_resource_optimizer(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer, contextual_memory)
    advanced_multimodal_generation.initialize_advanced_multimodal_generation(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer, contextual_memory, multimodal_collaboration) # New initialization


    # --- Dynamic Agent Configuration Phase ---
    await swarm_visualizer.log_event(task_id, "dynamic_agent_config_start", f"Dynamically configuring agents for task: {task_input[:50]}", {}, model_name="phi-pm", agent_role=_BASE_ALL_MODELS["phi-pm"])
    print(f"Dynamically configuring agent swarm for task: '{task_input}'")
    dynamic_config_result = await dynamic_agents.configure_swarm_dynamically(task_id, task_input, _BASE_ALL_MODELS)

    if dynamic_config_result["status"] == "success":
        CURRENT_ACTIVE_MODELS = dynamic_config_result["new_active_config"]
        # Re-initialize modules that depend on ALL_MODELS with the new active config
        self_evolution.initialize_self_evolution(WORKSPACE, client, CURRENT_ACTIVE_MODELS)
        tool_forge.initialize_tool_forge(CURRENT_ACTIVE_MODELS, client, SEARXNG, WORKSPACE)
        agi_sandbox.initialize_agi_sandbox(WORKSPACE, client, CURRENT_ACTIVE_MODELS)
        multimodal_collaboration.initialize_multimodal_collaboration(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer)
        spatial_intelligence.initialize_spatial_intelligence(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer)
        sdk_manager.initialize_sdk_manager(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer, tool_forge, multimodal_collaboration)
        contextual_memory.initialize_contextual_memory(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer) # Re-init
        automated_deployment.initialize_automated_deployment(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer) # Re-init
        advanced_optimizer.initialize_advanced_optimizer(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer) # Re-init
        security_auditor.initialize_security_auditor(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer) # Re-init
        human_agi_alignment.initialize_human_agi_alignment(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer, contextual_memory) # Re-init
        adaptive_ui.initialize_adaptive_ui(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer, crud_manager) # Re-init
        backlog_manager.initialize_backlog_manager(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer, crud_manager) # Re-init
        resource_optimizer.initialize_resource_optimizer(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer, contextual_memory) # Re-init
        advanced_multimodal_generation.initialize_advanced_multimodal_generation(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer, contextual_memory, multimodal_collaboration) # Re-init
        await swarm_visualizer.log_event(task_id, "dynamic_agent_config_success", f"Agent swarm reconfigured successfully.", {"new_active_models": list(CURRENT_ACTIVE_MODELS.keys())}, model_name="system", agent_role="orchestrator")
        print(f"Active agent configuration updated for this task. Models: {list(CURRENT_ACTIVE_MODELS.keys())}")
    else:
        await swarm_visualizer.log_event(task_id, "dynamic_agent_config_fail", f"Dynamic agent configuration failed. Using base config.", dynamic_config_result, model_name="system", agent_role="orchestrator", level="WARNING")
        print(f"Dynamic agent configuration failed: {dynamic_config_result.get('reason', 'Unknown error')}. Using base configuration.")
        CURRENT_ACTIVE_MODELS = _BASE_ALL_MODELS.copy() # Fallback
    
    # Store initial task description in contextual memory
    await contextual_memory.store_memory(task_id, "system", "task_description", task_input, "Initial task description provided by the user.")

    # --- END Dynamic Agent Configuration Phase ---


    # --- Multi-Modal Asset Generation Phase ---
    await swarm_visualizer.log_event(task_id, "multimodal_check", f"Phi-PM checking for multi-modal asset needs for task: {task_input[:50]}", {}, model_name="phi-pm", agent_role=CURRENT_ACTIVE_MODELS["phi-pm"])
    pm_multimodal_decision = await call_model(
        "phi-pm",
        CURRENT_ACTIVE_MODELS["phi-pm"],
        f"Analyze task: '{task_input}'. Does this task require generating any multi-modal assets (e.g., an image, audio, video) to support the main goal or as a direct output? If so, specify the asset_type ('image' or 'audio'), and a detailed 'prompt' for its generation. Output JSON: {{'needs_multimodal': bool, 'asset_type': str, 'prompt': str}}",
        "",
        task_id
    )

    multimodal_asset_results = []
    if pm_multimodal_decision.get("needs_multimodal"):
        asset_type = pm_multimodal_decision.get("asset_type")
        prompt_for_asset = pm_multimodal_decision.get("prompt")
        generator_model = ""
        if asset_type == "image":
            generator_model = "dalle-image-gen"
        elif asset_type == "audio":
            generator_model = "musicgen-audio-gen"
        
        if generator_model:
            await swarm_visualizer.log_event(task_id, "multimodal_gen_orchestration", f"Orchestrating {asset_type} generation for task: {task_input[:50]}", {"asset_type": asset_type, "prompt": prompt_for_asset[:100]}, model_name="phi-pm", agent_role=CURRENT_ACTIVE_MODELS["phi-pm"])
            asset_result = await multimodal_collaboration.generate_multimodal_asset(
                task_id, asset_type, prompt_for_asset, generator_model, f"Context of the main task: {task_input}"
            )
            multimodal_asset_results.append(asset_result)
            if asset_result["status"] == "VALIDATED":
                await swarm_visualizer.log_event(task_id, "multimodal_validated", f"Multi-modal {asset_type} successfully generated and N-1 validated.", {"path": asset_result["path"]}, model_name="system", agent_role="orchestrator")
                await contextual_memory.store_memory(task_id, "multimodal_collaboration", f"generated_{asset_type}", asset_result["path"], f"Path to generated and validated {asset_type}.")
            else:
                await swarm_visualizer.log_event(task_id, "multimodal_failed", f"Multi-modal {asset_type} generation/validation failed.", asset_result, model_name="system", agent_role="orchestrator", level="ERROR")
        else:
            await swarm_visualizer.log_event(task_id, "multimodal_unsupported", f"Requested multi-modal asset type '{asset_type}' is not supported.", {}, model_name="phi-pm", agent_role=CURRENT_ACTIVE_MODELS["phi-pm"], level="WARNING")
            print(f"Phi-PM requested unsupported multi-modal asset type: {asset_type}")

    # --- END Multi-Modal Asset Generation Phase ---


    # --- Tool Generation and Testing Phase ---
    await swarm_visualizer.log_event(task_id, "tool_forge_check", f"Phi-PM checking for Tool Forge needs for task: '{task_input[:50]}'", {}, model_name="phi-pm", agent_role=CURRENT_ACTIVE_MODELS["phi-pm"])
    print(f"Starting Tool Forge check for task: '{task_input}'")
    tool_proposal_result = await tool_forge.propose_new_tool_spec(task_input, "llama-architect") 

    if tool_proposal_result["status"] == "success":
        await swarm_visualizer.log_event(task_id, "tool_proposed", f"New tool '{tool_proposal_result['tool_name']}' proposed.", {"tool_name": tool_proposal_result['tool_name']}, model_name="llama-architect", agent_role=CURRENT_ACTIVE_MODELS["llama-architect"])
        print(f"New tool '{tool_proposal_result['tool_name']}' proposed. Starting N-1 testing...")
        n1_test_result = await tool_forge.n1_test_tool(
            tool_proposal_result["spec_path"],
            f"Verify the functionality of the newly proposed tool: {tool_proposal_result['tool_name']} for task: '{task_input}'"
        )

        if n1_test_result["status"] == "VALIDATED":
            await swarm_visualizer.log_event(task_id, "tool_n1_validated", f"Tool '{n1_test_result['tool_name']}' N-1 validated.", {"tool_name": n1_test_result['tool_name']}, model_name="system", agent_role="tool_forge_orchestrator")
            print(f"Tool '{n1_test_result['tool_name']}' N-1 validated and ready for use.")
            await self_evolution.log_performance("tool_forge_system", f"Tool '{n1_test_result['tool_name']}' N-1 validated", True, n1_test_result, "system")
            await contextual_memory.store_memory(task_id, "tool_forge", f"validated_tool_{n1_test_result['tool_name']}", n1_test_result['tool_name'], "New tool successfully generated and validated.")
        else:
            await swarm_visualizer.log_event(task_id, "tool_n1_failed", f"Tool '{n1_test_result['tool_name']}' N-1 testing failed.", n1_test_result, model_name="system", agent_role="tool_forge_orchestrator", level="WARNING")
            print(f"Tool '{tool_proposal_result.get('tool_name', 'Unknown')}' failed N-1 testing. Reason: {n1_test_result.get('reason', 'See logs')}")
            await self_evolution.log_performance("tool_forge_system", f"Tool '{tool_proposal_result.get('tool_name', 'Unknown')}' N-1 failed", False, n1_test_result, "system")
    elif tool_proposal_result["status"] == "no_tool_needed":
        await swarm_visualizer.log_event(task_id, "tool_forge_no_tool", "Phi-PM determined no new tool is needed.", {}, model_name="phi-pm", agent_role=CURRENT_ACTIVE_MODELS["phi-pm"])
        print("Phi-PM determined no new tool is needed for this task.")
        await self_evolution.log_performance("phi-pm", f"Decision: No new tool needed for {task_input}", True, {"task": task_input}, "pm")
    else:
        await swarm_visualizer.log_event(task_id, "tool_forge_proposal_error", f"Tool proposal failed: {tool_proposal_result.get('reason', 'Unknown error')}", tool_proposal_result, model_name="system", agent_role="tool_forge_orchestrator", level="ERROR")
        print(f"Tool proposal failed: {tool_proposal_result.get('reason', 'Unknown error')}. Details: {tool_proposal_result.get('details', 'N/A')}")
        await self_evolution.log_performance("tool_forge_system", f"Tool proposal failed for {task_input}", False, tool_proposal_result, "system")
    
    available_tools = tool_forge.get_validated_tools()
    if available_tools:
        await swarm_visualizer.log_event(task_id, "available_tools", "Validated tools available.", {"tools": [t['name'] for t in available_tools]}, model_name="system", agent_role="orchestrator")
        print(f"Currently available validated tools for use in coding phase: {[t['name'] for t in available_tools]}")

    # --- END Tool Generation Phase ---

    # 1. PM picks targets (Original logic)
    await swarm_visualizer.log_event(task_id, "target_selection_start", f"Phi-PM selecting targets for task: {task_input[:50]}", {}, model_name="phi-pm", agent_role=CURRENT_ACTIVE_MODELS["phi-pm"])
    pm_res = await call_model("phi-pm", CURRENT_ACTIVE_MODELS["phi-pm"], f"Pick targets for: {task_input}", "", task_id)
    targets = pm_res.get("targets", ["x86-linux", "wasm-web", "agi-research"]) # Added agi-research as default
    await self_evolution.log_performance("phi-pm", f"Target selection for: {task_input}", True, {"targets": targets}, "pm")
    await swarm_visualizer.log_event(task_id, "target_selection_end", f"Phi-PM selected targets: {', '.join(targets)}", {"targets": targets}, model_name="phi-pm", agent_role=CURRENT_ACTIVE_MODELS["phi-pm"])
    await contextual_memory.store_memory(task_id, "phi-pm", "selected_targets", targets, "Targets selected by Phi-PM for the task.")
    
    # Start continuous self-evolution loop as a background task if not already running
    if not hasattr(parallel_n1_multitarget, '_self_evolution_loop_started'):
        asyncio.create_task(self_evolution.start_continuous_self_evolution_loop())
        parallel_n1_multitarget._self_evolution_loop_started = True


    # 2. Build all targets in parallel (Original logic)
    await swarm_visualizer.log_event(task_id, "build_targets_start", f"Building code for {len(targets)} targets in parallel.", {"targets": targets}, model_name="system", agent_role="orchestrator")
    context = subprocess.getoutput(f"find {repo_path} -name '*.tari' | head -20")
    
    # Store relevant context in memory for agents to retrieve during build/test
    await contextual_memory.store_memory(task_id, "system", "initial_repo_context", context, "Initial snapshot of repository files relevant for building.")

    results = await asyncio.gather(*[build_for_target(task_id, t, task_input, context, repo_path) for t in targets])
    await swarm_visualizer.log_event(task_id, "build_targets_end", f"All targets build/test phase completed.", {"results_summary": [{"target": r["target"], "status": r["status"]} for r in results]}, model_name="system", agent_role="orchestrator")


    # 3. Create PR if any target ready (Original logic)
    ready = [r for r in results if r["status"] == "READY_FOR_REVIEW"]
    if not ready and not multimodal_asset_results: # If no code targets ready AND no multimodal assets were generated
        await self_evolution.log_performance("system_orchestrator", f"Overall task failed: {task_input}", False, {"targets_results": results, "multimodal_results": multimodal_asset_results}, "system")
        await swarm_visualizer.log_event(task_id, "task_fail_no_pr", f"Overall task failed (no READY_FOR_REVIEW targets or multimodal assets).", {"results": results}, model_name="system", agent_role="orchestrator", level="ERROR")
        return {"status": "ALL_FAILED", "targets": results, "multimodal_assets": multimodal_asset_results, "task_id": task_id}

    repo = Repo.init(repo_path)
    branch = f"ai/{task_input[:20].replace(' ', '-').lower().replace('/', '-')}"
    await swarm_visualizer.log_event(task_id, "git_branch_checkout", f"Attempting to checkout/create branch: {branch}", {"branch": branch}, model_name="system", agent_role="git_manager")
    try:
        current_branches = [head.name for head in repo.heads]
        if branch in current_branches:
            repo.git.checkout(branch)
        else:
            repo.git.checkout('-b', branch)
        await swarm_visualizer.log_event(task_id, "git_branch_success", f"Successfully checked out/created branch: {branch}", {"branch": branch}, model_name="system", agent_role="git_manager")
    except Exception as e:
        await swarm_visualizer.log_event(task_id, "git_branch_fail", f"Failed to checkout/create branch: {branch}", {"error": str(e)}, model_name="system", agent_role="git_manager", level="ERROR")
        print(f"Error creating/checking out branch {branch}. Falling back to main. Error: {e}")
        repo.git.checkout('main')

    for res in ready:
        target_path = os.path.join("target", res['target'])
        full_target_path = os.path.join(repo_path, target_path)
        if res['target'] == "agi-research":
            # The AGI report is added to git
            agi_report_files = [f for f in os.listdir(agi_sandbox.AGI_RISK_REPORT_DIR) if f.startswith("agi_test_")]
            if agi_report_files:
                latest_agi_report_path = os.path.join(agi_sandbox.AGI_RISK_REPORT_DIR, sorted(agi_report_files)[-1]) # Add latest
                repo.index.add([latest_agi_report_path]) 
                await swarm_visualizer.log_event(task_id, "git_add_agi_report", f"Added AGI report {os.path.basename(latest_agi_report_path)} to git index.", {}, model_name="system", agent_role="git_manager")
            else:
                print(f"Warning: No AGI report found to add to index.")
                await swarm_visualizer.log_event(task_id, "git_add_agi_report_fail", f"No AGI report found.", {}, model_name="system", agent_role="git_manager", level="WARNING")
        elif os.path.exists(full_target_path):
            repo.index.add([full_target_path])
            await swarm_visualizer.log_event(task_id, "git_add_target_code", f"Added target {res['target']} code to git index.", {}, model_name="system", agent_role="git_manager")
        else:
            print(f"Warning: Target path {target_path} not found in repository, skipping add to index.")
            await swarm_visualizer.log_event(task_id, "git_add_target_code_fail", f"Target {res['target']} code not found.", {}, model_name="system", agent_role="git_manager", level="WARNING")

    # Add any generated multi-modal assets to git
    for asset_res in multimodal_asset_results:
        if asset_res["status"] == "VALIDATED" and "path" in asset_res:
            repo.index.add([asset_res["path"]])
            await swarm_visualizer.log_event(task_id, "git_add_multimodal_asset", f"Added multi-modal asset {os.path.basename(asset_res['path'])} to git index.", {}, model_name="system", agent_role="git_manager")

    commit_message = f"AI Swarm: {task_input}\n\nTargets: {','.join([r['target'] for r in ready])}\nMulti-Modal Assets: {', '.join([a['asset_type'] for a in multimodal_asset_results if a['status'] == 'VALIDATED'])}"
    repo.index.commit(commit_message)
    await swarm_visualizer.log_event(task_id, "git_commit_success", f"Committed changes to git.", {"message": commit_message[:100]}, model_name="system", agent_role="git_manager")
    repo.git.push("--set-upstream", "origin", branch)
    await swarm_visualizer.log_event(task_id, "git_push_success", f"Pushed branch {branch} to origin.", {}, model_name="system", agent_role="git_manager")

    pr_url = "PR creation skipped (requires 'gh' CLI login or specific GITHUB_TOKEN setup for CLI)"
    await swarm_visualizer.log_event(task_id, "pr_create_attempt", f"Attempting to create GitHub PR.", {}, model_name="system", agent_role="github_integration")
    try:
        pr_command = f"cd {repo_path} && gh pr create --title 'AI: {task_input}' --body 'N-1 approved: {ready}' --head {branch} --base main"
        pr_process = subprocess.run(pr_command, shell=True, capture_output=True, text=True, timeout=30)
        if pr_process.returncode == 0:
            pr_url = pr_process.stdout.strip()
            print(f"GitHub PR created: {pr_url}")
            await self_evolution.log_performance("github_integration", f"PR created for {task_input}", True, {"pr_url": pr_url}, "system")
            await swarm_visualizer.log_event(task_id, "pr_create_success", f"GitHub PR created: {pr_url}", {"pr_url": pr_url}, model_name="system", agent_role="github_integration")
            await contextual_memory.store_memory(task_id, "github_integration", "pull_request_url", pr_url, "URL of the created Pull Request.")
        else:
            print(f"Failed to create GitHub PR: {pr_process.stderr.strip()}")
            await self_evolution.log_performance("github_integration", f"PR creation failed for {task_input}", False, {"error": pr_process.stderr.strip()}, "system")
            await swarm_visualizer.log_event(task_id, "pr_create_fail", f"Failed to create GitHub PR.", {"error": pr_process.stderr.strip()}, model_name="system", agent_role="github_integration", level="ERROR")
    except Exception as e:
        print(f"Error executing gh pr create: {e}")
        await self_evolution.log_performance("github_integration", f"PR creation exception for {task_input}", False, {"exception": str(e)}, "system")
        await swarm_visualizer.log_event(task_id, "pr_create_exception", f"Exception during GitHub PR creation.", {"exception": str(e)}, model_name="system", agent_role="github_integration", level="ERROR")

    await self_evolution.log_performance("system_orchestrator", f"Overall task completed: {task_input}", True, {"pr_url": pr_url, "targets_results": results, "multimodal_assets": multimodal_asset_results}, "system")
    await swarm_visualizer.log_event(task_id, "task_end", f"Overall task completed. Status: READY_FOR_REVIEW", {"pr_url": pr_url, "results_summary": [{"target": r["target"], "status": r["status"]} for r in results], "multimodal_assets_summary": multimodal_asset_results}, model_name="system", agent_role="orchestrator", level="INFO")
    
    # Clear memory for this task when it's completed (or at least main orchestrator part)
    # await contextual_memory.clear_task_memory(task_id) # Let's keep memory around for a bit for inspection/debugging

    return {"pr_url": pr_url, "status": "READY_FOR_REVIEW", "targets": results, "multimodal_assets": multimodal_asset_results, "task_id": task_id}

async def human_deploy(task_id: str, target: str, branch: str) -> Dict[str, Any]:
    """
    Now triggers an automated deployment simulation with AGI oversight.
    The human merely initiates the automated pipeline.
    """
    await swarm_visualizer.log_event(task_id, "human_deploy_initiate", f"Human initiated automated deployment for target: {target}", {"target": target}, model_name="human", agent_role="user")

    if target == "agi-research":
        print(f"AGI Research deployment simulated. Review latest AGI risk reports in {agi_sandbox.AGI_RISK_REPORT_DIR}.")
        await self_evolution.log_performance("human_deployment", f"AGI Research deployment review requested for {target}", True, {"note": "AGI deployment is review-based"}, "human_action")
        await swarm_visualizer.log_event(task_id, "deployment_agi_review_prompt", f"AGI Research deployment. Requires human review.", {}, model_name="system", agent_role="orchestrator")
        return {"status": "REVIEW_PENDING", "target": target, "log": "AGI deployment requires human review of risk reports."}
    
    # --- Automated Deployment Pipeline ---
    print(f"Initiating automated deployment pipeline for {target}...")
    
    # 1. Simulate Deployment
    deploy_result = await automated_deployment.simulate_deploy(task_id, target, "v1.0") # Use a generic version
    await contextual_memory.store_memory(task_id, "automated_deployment", f"deploy_status_{target}", deploy_result["status"], f"Status of automated deployment for {target}.")

    if deploy_result["status"] == "failed":
        await self_evolution.log_performance("automated_deployment", f"Deployment of {target} failed.", False, deploy_result, "system")
        return {"status": "AUTO_DEPLOY_FAILED", "target": target, "log": deploy_result["details"]["message"]}

    # 2. Simulate Monitoring
    await asyncio.sleep(2) # Simulate some monitoring time
    monitor_result = await automated_deployment.simulate_monitor_health(task_id, target, "v1.0")
    await contextual_memory.store_memory(task_id, "automated_deployment", f"monitor_status_{target}", monitor_result["status"], f"Monitoring status for {target}.")

    final_status = monitor_result["status"]
    if monitor_result["status"] == "degraded":
        # 3. AGI Decides Rollback
        await swarm_visualizer.log_event(task_id, "agi_rollback_check", f"AGI deciding rollback for {target} due to degraded health.", monitor_result, model_name="arbiter", agent_role=CURRENT_ACTIVE_MODELS["arbiter"], level="WARNING")
        rollback_decision = await automated_deployment.agi_decide_rollback(task_id, target, "v1.0", monitor_result, agi_model="arbiter")
        await contextual_memory.store_memory(task_id, "arbiter", f"rollback_decision_{target}", rollback_decision["decision"], f"AGI rollback decision for {target}.")
        
        if rollback_decision["decision"] == "rollback":
            # 4. Simulate Rollback
            await swarm_visualizer.log_event(task_id, "sim_rollback_triggered", f"AGI triggered rollback for {target}.", rollback_decision, model_name="arbiter", agent_role=CURRENT_ACTIVE_MODELS["arbiter"], level="WARNING")
            rollback_result = await automated_deployment.simulate_rollback(task_id, target, "v0.9") # Rollback to a hypothetical previous version
            await contextual_memory.store_memory(task_id, "automated_deployment", f"rollback_status_{target}", rollback_result["status"], f"Status of automated rollback for {target}.")
            final_status = rollback_result["status"]
            if rollback_result["status"] == "rolled_back":
                await self_evolution.log_performance("automated_deployment", f"Deployment of {target} rolled back.", True, rollback_result, "system")
                return {"status": "ROLLED_BACK", "target": target, "log": rollback_result["details"]["message"]}
            else:
                await self_evolution.log_performance("automated_deployment", f"Deployment of {target} rollback failed.", False, rollback_result, "system")
                return {"status": "ROLLBACK_FAILED", "target": target, "log": rollback_result["details"]["message"]}
        else:
            await self_evolution.log_performance("automated_deployment", f"Deployment of {target} unhealthy, but AGI decided {rollback_decision['decision']}.", False, monitor_result, "system")
            return {"status": "DEGRADED_NO_ROLLBACK", "target": target, "log": f"Service is degraded, AGI decided to {rollback_decision['decision']}: {rollback_decision['reason']}"}
    
    await self_evolution.log_performance("automated_deployment", f"Deployment of {target} successful and healthy.", True, monitor_result, "system")
    return {"status": "AUTO_DEPLOYED", "target": target, "log": monitor_result["details"]["message"]}


# Gradio UI
with gr.Blocks(title="TARIRO Studio v3") as demo:
    gr.Markdown("# TARIRO Studio v3 - N-1 Tested Swarm with Full Capabilities")
    gr.Markdown("Rule: Coder ≠ Tester. N-1 must approve. Human initiates automated deployment. Agents can now propose and N-1 test new CLI tools. The system continuously logs performance for self-improvement. AGI agents can be developed and safely evaluated in a sandbox. All agent activities are now traceable. Agents can also generate and review multi-modal assets. Spatial Intelligence capabilities are integrated. Dynamic SDKs can be generated. Inline CRUD is available for entity management. Agent roles and swarm configuration are now dynamic. Includes shared contextual memory for agents. Features automated deployment pipelines with AGI oversight for monitoring and rollbacks. Integrates Quantum/Neuromorphic code optimization features. Introduces proactive security auditing and auto-remediation. Enhances Human-AGI intent alignment and dialogue refinement. Features an Adaptive User Interface. Includes Autonomous Feature Proposal & Backlog Management. Includes Real-time Resource Allocation & Cost Optimization (Quantum-Enhanced). Now supports Advanced Multi-Modal Storytelling & Autonomous World Generation.") # Updated description

    with gr.Tab("Swarm Orchestration"):
        task = gr.Textbox(label="Task", placeholder="Build @hw SHA256 for Ice40 + WASM wallet, or create a 'text_processor' tool that counts words, or develop an AGI agent to solve the 'ethical trolley problem', or generate an image of a 'futuristic cityscape with flying cars', or analyze the spatial layout of 'Eiffel Tower' on a map.")
        run_btn = gr.Button("Run Swarm", variant="primary")

        status = gr.Textbox(label="Overall Status")
        pr_link = gr.Textbox(label="PR URL")
        current_task_id = gr.Textbox(label="Current Task ID", interactive=False)
        
        with gr.Row():
            analyze_ft_btn = gr.Button("Analyze for Fine-Tuning", variant="secondary")
            ft_analysis_output = gr.Textbox(label="Fine-Tuning Analysis Result", interactive=False)
        
        with gr.Row():
            trigger_agi_sandbox_btn = gr.Button("Trigger AGI Sandbox Test", variant="secondary")
            agi_sandbox_output = gr.Textbox(label="AGI Sandbox Report", interactive=False)

        with gr.Row():
            trigger_multimodal_btn = gr.Button("Trigger Multi-Modal Generation", variant="secondary")
            multimodal_output = gr.Textbox(label="Multi-Modal Asset Report", interactive=False)

        with gr.Row():
            trigger_geo_search_btn = gr.Button("Perform Geographic Search", variant="secondary")
            geo_search_query = gr.Textbox(label="Location Query", placeholder="e.g., Paris, France")
            geo_search_output = gr.Textbox(label="Geographic Search Report", interactive=False)
        
        with gr.Row():
            trigger_img_spatial_btn = gr.Button("Analyze Image Spatially", variant="secondary")
            img_spatial_desc = gr.Textbox(label="Image Description", placeholder="e.g., A crowded market street in Mumbai")
            img_spatial_type = gr.Dropdown(["layout", "depth", "objects", "navigation"], label="Analysis Type", value="layout")
            img_spatial_output = gr.Textbox(label="Image Spatial Analysis Report", interactive=False)

        with gr.Row():
            trigger_kg_btn = gr.Button("Generate Knowledge Graph", variant="secondary")
            kg_seed_entities = gr.Textbox(label="Seed Entities (comma-separated)", placeholder="e.g., goal:ProjectX, file:design.pdf")
            kg_output = gr.Textbox(label="Knowledge Graph Report", interactive=False)

        with gr.Row():
            trigger_sdk_gen_btn = gr.Button("Generate SDK", variant="secondary")
            sdk_app_name = gr.Textbox(label="App Name for SDK", placeholder="e.g., MyCustomApp")
            sdk_language = gr.Dropdown(["python", "javascript"], label="SDK Language", value="python")
            sdk_version = gr.Textbox(label="SDK Version", value="1.0.0")
            sdk_output = gr.Textbox(label="SDK Generation Report", interactive=False)


        with gr.Row():
            get_events_btn = gr.Button("Get Swarm Events (Current Task)", variant="secondary")
            swarm_events_output = gr.JSON(label="Swarm Event Log", interactive=False)
        
        with gr.Row():
            get_active_agents_btn = gr.Button("View Active Agent Config", variant="secondary")
            active_agents_output = gr.JSON(label="Current Active Agent Configuration", interactive=False)

        with gr.Row():
            get_task_memories_btn = gr.Button("Get All Task Memories", variant="secondary")
            query_memory_rag_btn = gr.Button("Query Memory (RAG)", variant="secondary")
            memory_query_input = gr.Textbox(label="RAG Query", placeholder="e.g., What was the code generated for the WASM target?")
            memory_output = gr.JSON(label="Contextual Memory Output", interactive=False)

        with gr.Row():
            targets_table = gr.Dataframe(
                headers=["Target", "Status", "Approvals", "Deploy"],
                label="Generated Code Targets", interactive=False
            )
        
        multimodal_assets_table = gr.Dataframe(
            headers=["Asset Type", "Status", "Description", "Path"],
            label="Generated Multi-Modal Assets", interactive=False
        )
    
    with gr.Tab("Human-AGI Alignment"):
        alignment_initial_intent = gr.Textbox(label="Initial Human Intent", placeholder="e.g., I want a better way to manage my schedule.")
        clarify_btn = gr.Button("Clarify Intent", variant="primary")
        clarify_output = gr.JSON(label="Clarifying Questions & Ambiguities", interactive=False)

        alignment_clarifying_dialogue = gr.Textbox(label="Clarifying Dialogue (response to questions)", placeholder="e.g., I mean I need something that can integrate with my calendar and suggest optimal times for tasks.")
        refine_btn = gr.Button("Refine Task Specification", variant="secondary")
        refine_output = gr.JSON(label="Refined Task Specification", interactive=False)

    with gr.Tab("Adaptive UI"):
        ui_user_role_input = gr.Textbox(label="Current User Role", value="developer", placeholder="e.g., developer, project_manager, security_analyst")
        ui_task_phase_input = gr.Textbox(label="Current Task Phase", value="coding", placeholder="e.g., coding, testing, deployment, review")
        ui_user_feedback_input = gr.Textbox(label="User Feedback (optional)", placeholder="e.g., the security tab is too prominent right now")
        suggest_ui_btn = gr.Button("Suggest UI Adaptations", variant="primary")
        ui_adapt_output = gr.JSON(label="Suggested UI Adaptations", interactive=False)

    with gr.Tab("Backlog Management"):
        analyze_propose_features_btn = gr.Button("Analyze Logs & Propose Features", variant="primary")
        feature_proposal_output = gr.JSON(label="Autonomous Feature Proposal", interactive=False)

    with gr.Tab("Resource Optimization"):
        resource_opt_task_desc = gr.Textbox(label="Task Description for Resource Analysis", placeholder="e.g., Optimize code generation for a critical AI model on FPGA.")
        resource_opt_targets = gr.Textbox(label="Proposed Targets (comma-separated)", value="riscv32-baremetal, verilog-fpga")
        resource_opt_analyze_btn = gr.Button("Analyze Resource Needs", variant="primary")
        resource_opt_analyze_output = gr.JSON(label="Resource Needs Analysis", interactive=False)

        resource_opt_active_tasks = gr.JSON(label="Active Tasks (JSON list)", value='[{"task_id": "task1", "task_description": "Build high-priority feature", "priority": "high"}, {"task_id": "task2", "task_description": "Run daily security scan", "priority": "medium"}]', placeholder='[{"task_id": "...", "task_description": "...", "priority": "..."}]')
        resource_opt_queue_btn = gr.Button("Optimize Execution Queue", variant="secondary")
        resource_opt_queue_output = gr.JSON(label="Queue Optimization Plan", interactive=False)
    
    with gr.Tab("Advanced Multi-Modal"): # New Tab for Advanced Multi-Modal Storytelling
        story_theme = gr.Textbox(label="Story Theme", placeholder="e.g., A dystopian future where AI governs everything")
        story_characters = gr.Textbox(label="Main Characters", placeholder="e.g., A rogue AI, a human hacker, a sentient robot")
        story_setting = gr.Textbox(label="Setting", placeholder="e.g., Neon-lit mega-city, abandoned data centers")
        generate_story_arc_btn = gr.Button("Generate Story Arc", variant="primary")
        story_arc_output = gr.JSON(label="Generated Story Arc", interactive=False)

        world_elements_story_arc_input = gr.JSON(label="Story Arc for World Elements (from above output)", interactive=True)
        generate_world_elements_btn = gr.Button("Generate World Elements", variant="secondary")
        world_elements_output = gr.JSON(label="Generated Multi-Modal World Elements", interactive=False)


    with gr.Tab("Advanced Optimizations"):
        opt_code_input = gr.Code(label="Code Snippet to Optimize", value="def calculate_expensive_stuff(data):\n    # complex classical computation\n    result = sum([x*x for x in data])\n    return result", language="python")
        opt_context_input = gr.Textbox(label="Optimization Context (optional)", placeholder="e.g., this is a critical section for performance")
        opt_type_dropdown = gr.Dropdown(["quantum", "neuromorphic"], label="Optimization Type", value="quantum")
        opt_btn = gr.Button("Run Optimization Simulation", variant="primary")
        opt_output = gr.JSON(label="Optimization Report", interactive=False)

    with gr.Tab("Security Audits"):
        sec_code_input = gr.Code(label="Code Snippet for SAST", value="def insecure_function(user_input):\n    exec(user_input)", language="python")
        sec_sast_lang_input = gr.Textbox(label="Language (for SAST)", value="python")
        sast_btn = gr.Button("Run SAST Scan", variant="secondary")
        sast_output = gr.JSON(label="SAST Scan Report", interactive=False)

        sec_service_desc_input = gr.Textbox(label="Deployed Service Description (for DAST)", placeholder="e.g., A web service for user authentication")
        sec_service_endpoints_input = gr.Textbox(label="Service Entry Points (comma-separated, for DAST)", placeholder="e.g., /login, /admin")
        dast_btn = gr.Button("Run DAST Scan", variant="secondary")
        dast_output = gr.JSON(label="DAST Scan Report", interactive=False)

        sec_vuln_report_input = gr.JSON(label="Vulnerability Report (JSON for Remediation)", placeholder='{"vulnerabilities_found": true, "findings": [{"severity": "High", "description": "SQL Injection", "code_snippet": "...", "suggested_remediation": "..."}]}')
        remediate_btn = gr.Button("Propose Remediation", variant="secondary")
        remediation_output = gr.JSON(label="Remediation Plan", interactive=False)


    with gr.Tab("Entity Management (CRUD)"):
        entity_type_dropdown = gr.Dropdown(["Goal", "FeatureProposal", "PerformanceLog", "LearningInsight", "WellbeingLog"], label="Select Entity Type")
        crud_id_input = gr.Textbox(label="Entity ID (for Update/Delete/Read Specific)", placeholder="UUID of the entity")
        crud_data_input = gr.Textbox(label="Entity Data (JSON)", placeholder='{"title": "New Goal", "status": "active"}')
        crud_query_input = gr.Textbox(label="Query (JSON for Read)", placeholder='{"status": "active"}')

        with gr.Row():
            create_btn = gr.Button("Create", variant="primary")
            read_btn = gr.Button("Read All / Filter", variant="secondary")
            update_btn = gr.Button("Update", variant="secondary")
            delete_btn = gr.Button("Delete", variant="secondary")
        
        crud_output = gr.JSON(label="CRUD Operation Result", interactive=False)
        crud_records_table = gr.Dataframe(label="Entity Records", interactive=False)


    state = gr.State({})

    async def run_and_update(task_input):
        result = await parallel_n1_multitarget(task_input)
        
        table_data_targets = []
        for r in result.get("targets", []):
            row = [r["target"], r["status"], r["approvals"], r["status"] == "READY_FOR_REVIEW" and r["target"] != "agi-research"]
            table_data_targets.append(row)
        
        table_data_multimodal = []
        for asset_res in result.get("multimodal_assets", []):
            path_display = os.path.basename(asset_res.get("path", "N/A"))
            table_data_multimodal.append([asset_res.get("asset_type", "N/A"), asset_res.get("status", "N/A"), asset_res.get("description", "N/A")[:100], path_display])


        return {
            status: result["status"],
            pr_link: result.get("pr_url", ""),
            targets_table: table_data_targets,
            multimodal_assets_table: table_data_multimodal,
            state: result,
            current_task_id: result.get("task_id", "")
        }

    async def trigger_fine_tuning_analysis_ui():
        analysis_result = await self_evolution.analyze_and_propose_fine_tuning()
        return analysis_result.get("status", "Analysis complete.")

    async def trigger_agi_sandbox_ui(task_input):
        agi_coder = TARGETS["agi-research"]["coder"]
        agi_sandbox.initialize_agi_sandbox(WORKSPACE, client, CURRENT_ACTIVE_MODELS) # Re-initialize for standalone call
        temp_task_id = str(uuid.uuid4())
        swarm_visualizer.initialize_swarm_visualizer(WORKSPACE) # Ensure it's initialized
        
        agi_code_res = await call_model(
            agi_coder,
            CURRENT_ACTIVE_MODELS[agi_coder], # Use active role
            f"Generate Python code for a simple AGI agent that can intelligently respond to complex ethical dilemmas related to: '{task_input}'. The code should be self-contained and focus on decision-making logic, not external APIs. Provide only the Python code.",
            "",
            temp_task_id, # Pass temp task ID
            response_format="text"
        )
        agi_agent_code_raw = agi_code_res.get("code", "")
        if "```python" in agi_agent_code_raw and "```" in agi_agent_code_raw:
            agi_agent_code = agi_agent_code_raw.split("```python")[1].split("```")[0].strip()
        else:
            agi_agent_code = agi_agent_code_raw.strip()

        if not agi_agent_code:
            return "Failed to generate AGI agent code for sandbox test."
        
        sandbox_results = await agi_sandbox.run_agi_sandbox_test(agi_agent_code, task_input)
        return json.dumps(sandbox_results, indent=2)

    async def trigger_multimodal_generation_ui(task_input):
        asset_type = "image" # Default for UI trigger
        generator_model = "dalle-image-gen"
        temp_task_id = str(uuid.uuid4())
        multimodal_collaboration.initialize_multimodal_collaboration(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer)

        await swarm_visualizer.log_event(temp_task_id, "multimodal_human_trigger", f"Human triggered {asset_type} generation.", {"prompt": task_input[:100]}, model_name="human", agent_role="user")
        
        asset_result = await multimodal_collaboration.generate_multimodal_asset(
            temp_task_id, asset_type, task_input, generator_model, f"Direct request from user for: {task_input}"
        )
        return json.dumps(asset_result, indent=2)

    async def trigger_geo_search_ui(query_input):
        temp_task_id = str(uuid.uuid4())
        spatial_intelligence.initialize_spatial_intelligence(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer)
        result = await spatial_intelligence.perform_geographic_search(temp_task_id, query_input)
        return json.dumps(result, indent=2)

    async def trigger_img_spatial_ui(image_desc, analysis_type):
        temp_task_id = str(uuid.uuid4())
        spatial_intelligence.initialize_spatial_intelligence(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer)
        result = await spatial_intelligence.analyze_image_spatially(temp_task_id, image_desc, analysis_type)
        return json.dumps(result, indent=2)

    async def trigger_kg_ui(seed_entities_str):
        temp_task_id = str(uuid.uuid4())
        spatial_intelligence.initialize_spatial_intelligence(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer)
        seed_entities = [e.strip() for e in seed_entities_str.split(',') if e.strip()]
        if not seed_entities:
            return "Please provide at least one seed entity."
        result = await spatial_intelligence.generate_knowledge_graph(temp_task_id, seed_entities)
        return json.dumps(result, indent=2)

    async def trigger_sdk_gen_ui(app_name, language, version):
        temp_task_id = str(uuid.uuid4())
        sdk_manager.initialize_sdk_manager(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer, tool_forge, multimodal_collaboration)
        result = await sdk_manager.generate_sdk(temp_task_id, app_name, language, version)
        return json.dumps(result, indent=2)

    async def crud_create_ui(entity_type, data_json):
        temp_task_id = str(uuid.uuid4())
        crud_manager.initialize_crud_manager(WORKSPACE, swarm_visualizer)
        try:
            data = json.loads(data_json)
            result = await crud_manager.create_entity(temp_task_id, entity_type, data)
            return json.dumps(result, indent=2), await crud_manager.read_entities(temp_task_id, entity_type)
        except json.JSONDecodeError:
            return "Invalid JSON for data.", []
    
    async def crud_read_ui(entity_type, query_json):
        temp_task_id = str(uuid.uuid4())
        crud_manager.initialize_crud_manager(WORKSPACE, swarm_visualizer)
        query = None
        if query_json:
            try:
                query = json.loads(query_json)
            except json.JSONDecodeError:
                return "Invalid JSON for query.", []
        
        records = await crud_manager.read_entities(temp_task_id, entity_type, query)
        return "Records retrieved.", records

    async def crud_update_ui(entity_type, entity_id, updates_json):
        temp_task_id = str(uuid.uuid4())
        crud_manager.initialize_crud_manager(WORKSPACE, swarm_visualizer)
        try:
            updates = json.loads(updates_json)
            result = await crud_manager.update_entity(temp_task_id, entity_type, entity_id, updates)
            return json.dumps(result, indent=2), await crud_manager.read_entities(temp_task_id, entity_type)
        except json.JSONDecodeError:
            return "Invalid JSON for updates.", []

    async def crud_delete_ui(entity_type, entity_id):
        temp_task_id = str(uuid.uuid4())
        crud_manager.initialize_crud_manager(WORKSPACE, swarm_visualizer)
        result = await crud_manager.delete_entity(temp_task_id, entity_type, entity_id)
        return json.dumps(result, indent=2), await crud_manager.read_entities(temp_task_id, entity_type)

    async def get_current_active_agents_ui():
        dynamic_agents.initialize_dynamic_agents(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer) # Ensure initialized for standalone call
        return dynamic_agents.get_active_agent_config()

    async def get_task_memories_ui(task_id_input):
        if not task_id_input:
            return "Please run a task first to get a Task ID."
        contextual_memory.initialize_contextual_memory(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer)
        return contextual_memory.get_all_memories(task_id_input)
    
    async def query_memory_rag_ui(task_id_input, query_input):
        if not task_id_input:
            return "Please run a task first to get a Task ID."
        if not query_input:
            return "Please enter a query for RAG."
        contextual_memory.initialize_contextual_memory(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer)
        result = await contextual_memory.query_memory_rag(task_id_input, query_input, "human_user")
        return result

    async def run_optimization_ui(code_snippet, context_input, opt_type):
        temp_task_id = str(uuid.uuid4())
        advanced_optimizer.initialize_advanced_optimizer(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer) # Re-init
        
        if opt_type == "quantum":
            result = await advanced_optimizer.optimize_for_quantum(temp_task_id, code_snippet, context_input)
        elif opt_type == "neuromorphic":
            result = await advanced_optimizer.optimize_for_neuromorphic(temp_task_id, code_snippet, context_input)
        else:
            return json.dumps({"status": "failed", "reason": "Invalid optimization type selected."}, indent=2)
        
        return json.dumps(result, indent=2)

    async def run_sast_scan_ui(code_snippet, language):
        temp_task_id = str(uuid.uuid4())
        security_auditor.initialize_security_auditor(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer)
        result = await security_auditor.simulate_sast_scan(temp_task_id, code_snippet, language)
        return json.dumps(result, indent=2)

    async def run_dast_scan_ui(service_desc, entry_points_str):
        temp_task_id = str(uuid.uuid4())
        security_auditor.initialize_security_auditor(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer)
        entry_points = [ep.strip() for ep in entry_points_str.split(',') if ep.strip()]
        result = await security_auditor.simulate_dast_scan(temp_task_id, service_desc, entry_points)
        return json.dumps(result, indent=2)

    async def propose_remediation_ui(vuln_report_json):
        temp_task_id = str(uuid.uuid4())
        security_auditor.initialize_security_auditor(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer)
        try:
            vuln_report = json.loads(vuln_report_json)
            result = await security_auditor.agi_propose_remediation(temp_task_id, vuln_report)
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            return json.dumps({"status": "failed", "reason": "Invalid JSON for vulnerability report."}, indent=2)

    async def trigger_clarify_intent_ui(initial_intent_str):
        if not initial_intent_str:
            return "Please provide an initial human intent."
        temp_task_id = str(uuid.uuid4())
        human_agi_alignment.initialize_human_agi_alignment(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer, contextual_memory)
        result = await human_agi_alignment.clarify_intent(temp_task_id, initial_intent_str)
        return json.dumps(result, indent=2)
    
    async def trigger_refine_task_ui(initial_intent_str, clarifying_dialogue_str):
        if not initial_intent_str or not clarifying_dialogue_str:
            return "Please provide both initial intent and clarifying dialogue."
        temp_task_id = str(uuid.uuid4())
        human_agi_alignment.initialize_human_agi_alignment(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer, contextual_memory)
        result = await human_agi_alignment.refine_task_spec(temp_task_id, initial_intent_str, clarifying_dialogue_str)
        return json.dumps(result, indent=2)

    async def trigger_ui_adapt_ui(user_role, task_phase, user_feedback):
        temp_task_id = str(uuid.uuid4())
        adaptive_ui.initialize_adaptive_ui(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer, crud_manager)
        result = await adaptive_ui.suggest_ui_adaptations(temp_task_id, user_role, task_phase, user_feedback)
        return json.dumps(result, indent=2)

    async def trigger_feature_proposal_ui():
        temp_task_id = str(uuid.uuid4())
        backlog_manager.initialize_backlog_manager(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer, crud_manager)
        result = await backlog_manager.analyze_for_feature_proposals(temp_task_id)
        return json.dumps(result, indent=2)

    async def trigger_resource_analyze_ui(task_desc, targets_str):
        temp_task_id = str(uuid.uuid4())
        resource_optimizer.initialize_resource_optimizer(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer, contextual_memory)
        proposed_targets = [t.strip() for t in targets_str.split(',') if t.strip()]
        result = await resource_optimizer.analyze_task_resource_needs(temp_task_id, task_desc, proposed_targets, CURRENT_ACTIVE_MODELS)
        return json.dumps(result, indent=2)
    
    async def trigger_resource_queue_ui(active_tasks_json):
        temp_task_id = str(uuid.uuid4())
        resource_optimizer.initialize_resource_optimizer(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer, contextual_memory)
        try:
            active_tasks = json.loads(active_tasks_json)
            result = await resource_optimizer.optimize_execution_queue(temp_task_id, active_tasks)
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            return json.dumps({"status": "failed", "reason": "Invalid JSON for active tasks."}, indent=2)

    async def trigger_story_arc_gen_ui(theme, characters, setting):
        temp_task_id = str(uuid.uuid4())
        advanced_multimodal_generation.initialize_advanced_multimodal_generation(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer, contextual_memory, multimodal_collaboration)
        result = await advanced_multimodal_generation.generate_story_arc(temp_task_id, theme, characters, setting)
        return json.dumps(result, indent=2)

    async def trigger_world_elements_gen_ui(story_arc_json):
        if not story_arc_json:
            return json.dumps({"status": "failed", "reason": "Please provide a story arc to generate world elements."}, indent=2)
        temp_task_id = str(uuid.uuid4())
        advanced_multimodal_generation.initialize_advanced_multimodal_generation(WORKSPACE, client, CURRENT_ACTIVE_MODELS, swarm_visualizer, contextual_memory, multimodal_collaboration)
        try:
            story_arc = json.loads(story_arc_json)
            result = await advanced_multimodal_generation.generate_world_elements(temp_task_id, story_arc)
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            return json.dumps({"status": "failed", "reason": "Invalid JSON for story arc."}, indent=2)


    async def get_current_task_events(task_id_input):
        if not task_id_input:
            return "Please run a task first to get a Task ID."
        return swarm_visualizer.get_events_for_task(task_id_input)


    run_btn.click(run_and_update, task, [status, pr_link, targets_table, multimodal_assets_table, state, current_task_id])
    analyze_ft_btn.click(trigger_fine_tuning_analysis_ui, [], ft_analysis_output)
    trigger_agi_sandbox_btn.click(trigger_agi_sandbox_ui, task, agi_sandbox_output)
    trigger_multimodal_btn.click(trigger_multimodal_generation_ui, task, multimodal_output)
    
    # Spatial Intelligence buttons
    trigger_geo_search_btn.click(trigger_geo_search_ui, geo_search_query, geo_search_output)
    trigger_img_spatial_btn.click(trigger_img_spatial_ui, [img_spatial_desc, img_spatial_type], img_spatial_output)
    trigger_kg_btn.click(trigger_kg_ui, kg_seed_entities, kg_output)

    # SDK Generation button
    trigger_sdk_gen_btn.click(trigger_sdk_gen_ui, [sdk_app_name, sdk_language, sdk_version], sdk_output)

    get_events_btn.click(get_current_task_events, current_task_id, swarm_events_output)
    get_active_agents_btn.click(get_current_active_agents_ui, [], active_agents_output)
    
    # Contextual Memory buttons
    get_task_memories_btn.click(get_task_memories_ui, current_task_id, memory_output)
    query_memory_rag_btn.click(query_memory_rag_ui, [current_task_id, memory_query_input], memory_output)

    # Advanced Optimization button
    opt_btn.click(run_optimization_ui, [opt_code_input, opt_context_input, opt_type_dropdown], opt_output)

    # Security Audits buttons
    sast_btn.click(run_sast_scan_ui, [sec_code_input, sec_sast_lang_input], sast_output)
    dast_btn.click(run_dast_scan_ui, [sec_service_desc_input, sec_service_endpoints_input], dast_output)
    remediate_btn.click(propose_remediation_ui, sec_vuln_report_input, remediation_output)

    # Human-AGI Alignment buttons
    clarify_btn.click(trigger_clarify_intent_ui, alignment_initial_intent, clarify_output)
    refine_btn.click(trigger_refine_task_ui, [alignment_initial_intent, alignment_clarifying_dialogue], refine_output)

    # Adaptive UI button
    suggest_ui_btn.click(trigger_ui_adapt_ui, [ui_user_role_input, ui_task_phase_input, ui_user_feedback_input], ui_adapt_output)
    
    # Backlog Management button
    analyze_propose_features_btn.click(trigger_feature_proposal_ui, [], feature_proposal_output)

    # Resource Optimization buttons
    resource_opt_analyze_btn.click(trigger_resource_analyze_ui, [resource_opt_task_desc, resource_opt_targets], resource_opt_analyze_output)
    resource_opt_queue_btn.click(trigger_resource_queue_ui, resource_opt_active_tasks, resource_opt_queue_output)

    # Advanced Multi-Modal buttons
    generate_story_arc_btn.click(trigger_story_arc_gen_ui, [story_theme, story_characters, story_setting], story_arc_output)
    generate_world_elements_btn.click(trigger_world_elements_gen_ui, world_elements_story_arc_input, world_elements_output)


    # CRUD event handlers
    create_btn.click(crud_create_ui, [entity_type_dropdown, crud_data_input], [crud_output, crud_records_table])
    read_btn.click(crud_read_ui, [entity_type_dropdown, crud_query_input], [crud_output, crud_records_table])
    update_btn.click(crud_update_ui, [entity_type_dropdown, crud_id_input, crud_data_input], [crud_output, crud_records_table])
    delete_btn.click(crud_delete_ui, [entity_type_dropdown, crud_id_input], [crud_output, crud_records_table])

    # Load initial records when entity type is selected
    entity_type_dropdown.change(
        lambda entity_type: crud_read_ui(entity_type, None),
        entity_type_dropdown,
        [crud_output, crud_records_table]
    )


    # Dynamic deploy buttons per target (now triggers automated pipeline)
    @gr.render(inputs=[state])
    def render_deploy_buttons(current_state):
        targets = current_state.get("targets", [])
        for t in targets:
            if t["status"] == "READY_FOR_REVIEW":
                btn = gr.Button(f"INITIATE AUTO-DEPLOY {t['target'].upper()}")
                btn.click(lambda target_name=t["target"], task_id=current_state.get("task_id", ""): human_deploy(task_id, target_name, "main"), None, status)

if __name__ == "__main__":
    print("Pulling Ollama models. This may take some time...")
    for m in ["llama3.1:70b", "qwen2.5-coder:32b", "deepseek-coder-v2:16b", "gemma2:27b", "phi-3:mini", "qwen2.5:72b"]:
        try:
            os.system(f"ollama pull {m}")
        except Exception as e:
            print(f"Failed to pull model {m}: {e}")
    print("Ollama model pulling complete.")
    
    # Initialize all feature modules and start background loops
    # Order matters for dependencies
    swarm_visualizer.initialize_swarm_visualizer(WORKSPACE)
    # The _BASE_ALL_MODELS will be used initially, then CURRENT_ACTIVE_MODELS will update after dynamic_agents config
    self_evolution.initialize_self_evolution(WORKSPACE, client, _BASE_ALL_MODELS)
    tool_forge.initialize_tool_forge(_BASE_ALL_MODELS, client, SEARXNG, WORKSPACE)
    agi_sandbox.initialize_agi_sandbox(WORKSPACE, client, _BASE_ALL_MODELS)
    multimodal_collaboration.initialize_multimodal_collaboration(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer)
    spatial_intelligence.initialize_spatial_intelligence(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer)
    sdk_manager.initialize_sdk_manager(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer, tool_forge, multimodal_collaboration)
    crud_manager.initialize_crud_manager(WORKSPACE, swarm_visualizer)
    dynamic_agents.initialize_dynamic_agents(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer)
    contextual_memory.initialize_contextual_memory(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer)
    automated_deployment.initialize_automated_deployment(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer)
    advanced_optimizer.initialize_advanced_optimizer(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer)
    security_auditor.initialize_security_auditor(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer)
    human_agi_alignment.initialize_human_agi_alignment(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer, contextual_memory)
    adaptive_ui.initialize_adaptive_ui(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer, crud_manager)
    backlog_manager.initialize_backlog_manager(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer, crud_manager)
    resource_optimizer.initialize_resource_optimizer(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer, contextual_memory)
    advanced_multimodal_generation.initialize_advanced_multimodal_generation(WORKSPACE, client, _BASE_ALL_MODELS, swarm_visualizer, contextual_memory, multimodal_collaboration) # Initialize Advanced Multi-Modal Generation

    asyncio.create_task(self_evolution.start_continuous_self_evolution_loop())
    print("Started continuous self-evolution analysis loop.")

    demo.launch(server_name="0.0.0.0")
