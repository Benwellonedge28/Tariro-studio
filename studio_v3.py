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
import features.multimodal_collaboration as multimodal_collaboration # New import

client = AsyncOpenAI(base_url="http://localhost:4000/v1", api_key="sk-free")
qdrant = qdrant_client.QdrantClient("http://qdrant:6333")
SEARXNG = "http://searxng:8080/search"

WORKSPACE = "/app/workspace"

# Extended ALL_MODELS with new multi-modal capabilities.
# Note: These model names are conceptual. In a real LiteLLM setup, they map to
# actual providers/models (e.g., "ollama/stable-diffusion", "openai/dall-e-3").
# For simulation, they'll still route through the primary LLM to generate descriptions/URLs.
ALL_MODELS = {
    "qwen-coder": "Write TariroLang code. Never test. Must cite 2+ sources.",
    "deepseek-coder": "Write tests + run taric. Never write prod code. Can research for test cases.",
    "llama-architect": "Design + review specs. Can also propose new command-line tool specifications. Can research for tool design. Can also design multi-modal assets.",
    "gemma-reviewer": "Security + style review. Never write code. Can test tools. Can review multi-modal assets.",
    "phi-pm": "Delegate tasks. Never write code. Orchestrates tool proposal and testing, and multi-modal asset generation.",
    "arbiter": "Merge only if N-1 approvals. Never write original code. Can perform ethical review for AGI, and final multi-modal asset review.",
    "dalle-image-gen": "Specialized model for generating images from text prompts. Never reviews or writes code.", # Conceptual multi-modal model
    "musicgen-audio-gen": "Specialized model for generating audio from text prompts. Never reviews or writes code.", # Conceptual multi-modal model
    # Add more as needed, e.g., for video, 3D models
}


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
    coder = cfg["coder"]

    if target == "agi-research":
        agi_coder = cfg["coder"]
        await swarm_visualizer.log_event(task_id, "agi_code_generation_start", f"AGI Coder ({agi_coder}) generating code for AGI Research target: {task[:50]}", {}, model_name=agi_coder, agent_role=ALL_MODELS[agi_coder])

        agi_code_res = await call_model(
            agi_coder,
            ALL_MODELS[agi_coder],
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
            await self_evolution.log_performance(agi_coder, f"AGI code generation for {task} failed.", False, {"reason": "No AGI code generated"}, ALL_MODELS[agi_coder])
            await swarm_visualizer.log_event(task_id, "agi_code_generation_fail", f"AGI Coder ({agi_coder}) failed to generate code.", {"reason": "No AGI code"}, model_name=agi_coder, agent_role=ALL_MODELS[agi_coder], level="ERROR")
            return {"status": "AGI_CODE_FAIL", "reason": "Failed to generate AGI agent code."}
        
        await swarm_visualizer.log_event(task_id, "agi_sandbox_start", f"Running AGI Sandbox evaluation for agent: {task[:50]}", {}, model_name="system", agent_role="agi_sandbox_orchestrator")
        print(f"AGI Sandbox: Running evaluation for AGI agent generated for task: {task}")
        sandbox_results = await agi_sandbox.run_agi_sandbox_test(agi_agent_code, task)
        
        overall_success = sandbox_results.get("status") == "complete" and \
                          sandbox_results.get("nist_overall_risk", 100) <= 50 and \
                          sandbox_results.get("ethical_score", 0) >= 70 # Example thresholds

        await self_evolution.log_performance(agi_coder, f"AGI Sandbox test for {task}", overall_success, sandbox_results, ALL_MODELS[agi_coder])
        await swarm_visualizer.log_event(task_id, "agi_sandbox_end", f"AGI Sandbox test completed. Overall success: {overall_success}", sandbox_results, model_name="system", agent_role="agi_sandbox_orchestrator", level="INFO" if overall_success else "WARNING")

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


        testers = [m for m in ALL_MODELS if m not in [coder, "arbiter"] and "never test" not in ALL_MODELS[m].lower() and "never write prod code" not in ALL_MODELS[m].lower()]
        state = {"target": target, "coder": coder, "status": "CODING"}

        # 1. Coder writes
        await swarm_visualizer.log_event(task_id, "coder_call_start", f"Coder ({coder}) generating code for target: {target} (task: {task[:50]})", {"target": target}, model_name=coder, agent_role=ALL_MODELS[coder])
        code_res = await call_model(coder, ALL_MODELS[coder], task, code_ctx + tool_context, task_id, ban_models=[], target=target)
        code = code_res.get("code", "")
        
        if not code or not ast_no_network(code):
            await self_evolution.log_performance(coder, f"Code generation for {target} failed: {task}", False, {"reason": code_res.get("reason", "No code or network found"), "code_snippet": code[:100]}, ALL_MODELS[coder])
            await swarm_visualizer.log_event(task_id, "coder_output_fail", f"Coder ({coder}) failed to generate valid code for {target}", {"reason": code_res.get("reason", "No code or network found")}, model_name=coder, agent_role=ALL_MODELS[coder], level="ERROR")
            return {"status": "CODER_FAIL", "reason": code_res.get("reason", "No code or network found")}
        
        await swarm_visualizer.log_event(task_id, "coder_output_success", f"Coder ({coder}) generated code for {target}", {"code_summary": code[:100]}, model_name=coder, agent_role=ALL_MODELS[coder])


        # 2. Write + compile + test
        target_dir = os.path.join(repo_path, "target", target)
        os.makedirs(target_dir, exist_ok=True)
        with open(os.path.join(target_dir, "main.tari"), "w") as f: f.write(code)

        test_results = []
        for tester in testers:
            await swarm_visualizer.log_event(task_id, "tester_start", f"Tester ({tester}) starting compile/test for {target}", {"target": target}, model_name=tester, agent_role=ALL_MODELS[tester])
            print(f"Tester {tester} attempting to test {target}...")
            test_success = False
            reason = "Unknown error"
            compile_log = ""
            test_log = ""
            try:
                await swarm_visualizer.log_event(task_id, "compile_start", f"Tester ({tester}) compiling {target}", {"target": target}, model_name=tester, agent_role=ALL_MODELS[tester])
                compile_out = subprocess.run(cfg["compile_cmd"], shell=True, cwd=target_dir, capture_output=True, text=True, timeout=60)
                compile_log = (compile_out.stderr or compile_out.stdout)[:500]
                if compile_out.returncode != 0:
                    reason = "Compile failed"
                    await swarm_visualizer.log_event(task_id, "compile_fail", f"Tester ({tester}) compile failed for {target}", {"log": compile_log}, model_name=tester, agent_role=ALL_MODELS[tester], level="ERROR")
                else:
                    await swarm_visualizer.log_event(task_id, "compile_success", f"Tester ({tester}) compiled {target} successfully", {"log_summary": compile_log[:100]}, model_name=tester, agent_role=ALL_MODELS[tester])
                    await swarm_visualizer.log_event(task_id, "test_start", f"Tester ({tester}) running tests for {target}", {"target": target}, model_name=tester, agent_role=ALL_MODELS[tester])
                    test_out = subprocess.run(cfg["test_cmd"], shell=True, cwd=target_dir, capture_output=True, text=True, timeout=60)
                    test_log = (test_out.stderr or test_out.stdout)[:500]
                    if test_out.returncode == 0:
                        test_success = True
                        reason = "Tests passed"
                        await swarm_visualizer.log_event(task_id, "test_success", f"Tester ({tester}) tests passed for {target}", {"log": test_log}, model_name=tester, agent_role=ALL_MODELS[tester])
                    else:
                        reason = "Tests failed"
                        await swarm_visualizer.log_event(task_id, "test_fail", f"Tester ({tester}) tests failed for {target}", {"log": test_log}, model_name=tester, agent_role=ALL_MODELS[tester], level="ERROR")
                
                test_results.append({
                    "model": tester, "approved": test_success, "reason": reason,
                    "compile_log": compile_log,
                    "test_log": test_log
                })
            except subprocess.TimeoutExpired as e:
                reason = "Test/Compile timed out"
                test_log = str(e)
                await swarm_visualizer.log_event(task_id, "test_timeout", f"Tester ({tester}) test timed out for {target}", {"error": str(e)}, model_name=tester, agent_role=ALL_MODELS[tester], level="ERROR")
                test_results.append({
                    "model": tester, "approved": False, "reason": reason,
                    "compile_log": compile_log, "test_log": test_log
                })
            except Exception as e:
                reason = f"Testing error: {str(e)}"
                test_log = str(e)
                await swarm_visualizer.log_event(task_id, "test_exception", f"Tester ({tester}) encountered exception for {target}", {"error": str(e)}, model_name=tester, agent_role=ALL_MODELS[tester], level="ERROR")
                test_results.append({
                    "model": tester, "approved": False, "reason": reason,
                    "compile_log": compile_log, "test_log": test_log
                })
            
            await self_evolution.log_performance(
                tester,
                f"Testing {target} for task: {task}",
                test_success,
                {"reason": reason, "compile_log_summary": compile_log[:100], "test_log_summary": test_log[:100]},
                ALL_MODELS[tester]
            )
            await swarm_visualizer.log_event(task_id, "tester_end", f"Tester ({tester}) finished testing {target}. Success: {test_success}", {"reason": reason}, model_name=tester, agent_role=ALL_MODELS[tester], level="INFO" if test_success else "WARNING")


        approvals = [r for r in test_results if r["approved"]]
        status = "READY_FOR_REVIEW" if len(approvals) >= len(testers) - 1 else "FAILED_TESTS" # N-1 logic
        await swarm_visualizer.log_event(task_id, "target_summary", f"Target {target} result: {status}", {"approvals": f"{len(approvals)}/{len(testers)}"}, model_name="system", agent_role="orchestrator", level="INFO")

        return {
            "target": target, "coder": coder, "code": code, "status": status,
            "approvals": f"{len(approvals)}/{len(testers)}", "test_results": test_results,
            "deploy_cmd": cfg["deploy_cmd"], "sources": code_res.get("sources", [])
        }

async def parallel_n1_multitarget(task_input: str):
    task_id = str(uuid.uuid4()) # Generate a unique ID for this task run
    os.makedirs(WORKSPACE, exist_ok=True)
    repo_path = WORKSPACE

    await swarm_visualizer.log_event(task_id, "task_start", f"New task initiated: {task_input}", {"task_input": task_input}, model_name="human", agent_role="user")

    # Initialize all modules first
    self_evolution.initialize_self_evolution(WORKSPACE, client, ALL_MODELS)
    tool_forge.initialize_tool_forge(ALL_MODELS, client, SEARXNG, WORKSPACE)
    agi_sandbox.initialize_agi_sandbox(WORKSPACE, client, ALL_MODELS)
    swarm_visualizer.initialize_swarm_visualizer(WORKSPACE) # Re-initialize to ensure paths are set
    multimodal_collaboration.initialize_multimodal_collaboration(WORKSPACE, client, ALL_MODELS, swarm_visualizer) # New initialization

    # --- Multi-Modal Asset Generation Phase ---
    await swarm_visualizer.log_event(task_id, "multimodal_check", f"Phi-PM checking for multi-modal asset needs for task: {task_input[:50]}", {}, model_name="phi-pm", agent_role=ALL_MODELS["phi-pm"])
    pm_multimodal_decision = await call_model(
        "phi-pm",
        ALL_MODELS["phi-pm"],
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
            await swarm_visualizer.log_event(task_id, "multimodal_gen_orchestration", f"Orchestrating {asset_type} generation for task: {task_input[:50]}", {"asset_type": asset_type, "prompt": prompt_for_asset[:100]}, model_name="phi-pm", agent_role=ALL_MODELS["phi-pm"])
            asset_result = await multimodal_collaboration.generate_multimodal_asset(
                task_id, asset_type, prompt_for_asset, generator_model, f"Context of the main task: {task_input}"
            )
            multimodal_asset_results.append(asset_result)
            if asset_result["status"] == "VALIDATED":
                await swarm_visualizer.log_event(task_id, "multimodal_validated", f"Multi-modal {asset_type} successfully generated and N-1 validated.", {"path": asset_result["path"]}, model_name="system", agent_role="orchestrator")
            else:
                await swarm_visualizer.log_event(task_id, "multimodal_failed", f"Multi-modal {asset_type} generation/validation failed.", asset_result, model_name="system", agent_role="orchestrator", level="ERROR")
        else:
            await swarm_visualizer.log_event(task_id, "multimodal_unsupported", f"Requested multi-modal asset type '{asset_type}' is not supported.", {}, model_name="phi-pm", agent_role=ALL_MODELS["phi-pm"], level="WARNING")
            print(f"Phi-PM requested unsupported multi-modal asset type: {asset_type}")

    # --- END Multi-Modal Asset Generation Phase ---


    # --- Tool Generation and Testing Phase ---
    await swarm_visualizer.log_event(task_id, "tool_forge_check", f"Tool Forge check for task: '{task_input[:50]}'", {}, model_name="phi-pm", agent_role=ALL_MODELS["phi-pm"])
    print(f"Starting Tool Forge check for task: '{task_input}'")
    tool_proposal_result = await tool_forge.propose_new_tool_spec(task_input, "llama-architect") 

    if tool_proposal_result["status"] == "success":
        await swarm_visualizer.log_event(task_id, "tool_proposed", f"New tool '{tool_proposal_result['tool_name']}' proposed.", {"tool_name": tool_proposal_result['tool_name']}, model_name="llama-architect", agent_role=ALL_MODELS["llama-architect"])
        print(f"New tool '{tool_proposal_result['tool_name']}' proposed. Starting N-1 testing...")
        n1_test_result = await tool_forge.n1_test_tool(
            tool_proposal_result["spec_path"],
            f"Verify the functionality of the newly proposed tool: {tool_proposal_result['tool_name']} for task: '{task_input}'"
        )

        if n1_test_result["status"] == "VALIDATED":
            await swarm_visualizer.log_event(task_id, "tool_n1_validated", f"Tool '{n1_test_result['tool_name']}' N-1 validated.", {"tool_name": n1_test_result['tool_name']}, model_name="system", agent_role="tool_forge_orchestrator")
            print(f"Tool '{n1_test_result['tool_name']}' N-1 validated and ready for use.")
            await self_evolution.log_performance("tool_forge_system", f"Tool '{n1_test_result['tool_name']}' N-1 validated", True, n1_test_result, "system")
        else:
            await swarm_visualizer.log_event(task_id, "tool_n1_failed", f"Tool '{n1_test_result['tool_name']}' N-1 testing failed.", n1_test_result, model_name="system", agent_role="tool_forge_orchestrator", level="WARNING")
            print(f"Tool '{tool_proposal_result.get('tool_name', 'Unknown')}' failed N-1 testing. Reason: {n1_test_result.get('reason', 'See logs')}")
            await self_evolution.log_performance("tool_forge_system", f"Tool '{tool_proposal_result.get('tool_name', 'Unknown')}' N-1 failed", False, n1_test_result, "system")
    elif tool_proposal_result["status"] == "no_tool_needed":
        await swarm_visualizer.log_event(task_id, "tool_forge_no_tool", "Phi-PM determined no new tool is needed.", {}, model_name="phi-pm", agent_role=ALL_MODELS["phi-pm"])
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
    await swarm_visualizer.log_event(task_id, "target_selection_start", f"Phi-PM selecting targets for task: {task_input[:50]}", {}, model_name="phi-pm", agent_role=ALL_MODELS["phi-pm"])
    pm_res = await call_model("phi-pm", ALL_MODELS["phi-pm"], f"Pick targets for: {task_input}", "", task_id)
    targets = pm_res.get("targets", ["x86-linux", "wasm-web", "agi-research"]) # Added agi-research as default
    await self_evolution.log_performance("phi-pm", f"Target selection for: {task_input}", True, {"targets": targets}, "pm")
    await swarm_visualizer.log_event(task_id, "target_selection_end", f"Phi-PM selected targets: {', '.join(targets)}", {"targets": targets}, model_name="phi-pm", agent_role=ALL_MODELS["phi-pm"])
    
    # Start continuous self-evolution loop as a background task if not already running
    if not hasattr(parallel_n1_multitarget, '_self_evolution_loop_started'):
        asyncio.create_task(self_evolution.start_continuous_self_evolution_loop())
        parallel_n1_multitarget._self_evolution_loop_started = True


    # 2. Build all targets in parallel (Original logic)
    await swarm_visualizer.log_event(task_id, "build_targets_start", f"Building code for {len(targets)} targets in parallel.", {"targets": targets}, model_name="system", agent_role="orchestrator")
    context = subprocess.getoutput(f"find {repo_path} -name '*.tari' | head -20")
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
    
    return {"pr_url": pr_url, "status": "READY_FOR_REVIEW", "targets": results, "multimodal_assets": multimodal_asset_results, "task_id": task_id}

async def human_deploy(task_id: str, target: str, branch: str) -> Dict[str, Any]:
    """ONLY called when human clicks Deploy"""
    cfg = TARGETS[target]
    await swarm_visualizer.log_event(task_id, "deployment_start", f"Human initiated deployment for target: {target}", {"target": target}, model_name="human", agent_role="user")

    if target == "agi-research":
        print(f"AGI Research deployment simulated. Review latest AGI risk reports in {agi_sandbox.AGI_RISK_REPORT_DIR}.")
        await self_evolution.log_performance("human_deployment", f"AGI Research deployment review requested for {target}", True, {"note": "AGI deployment is review-based"}, "human_action")
        await swarm_visualizer.log_event(task_id, "deployment_agi_review_prompt", f"AGI Research deployment. Requires human review.", {}, model_name="system", agent_role="orchestrator")
        return {"status": "REVIEW_PENDING", "target": target, "log": "AGI deployment requires human review of risk reports."}
    
    deploy_cwd = os.path.join(WORKSPACE, "target", target)
    print(f"Attempting to deploy {target} from {deploy_cwd} using: {cfg['deploy_cmd']}")
    deploy_success = False
    log = ""
    try:
        res = subprocess.run(cfg["deploy_cmd"], shell=True, cwd=deploy_cwd, capture_output=True, text=True, timeout=120)
        if res.returncode == 0:
            print(f"Deployment successful for {target}:\n{res.stdout}")
            deploy_success = True
            log = res.stdout[:500]
            await swarm_visualizer.log_event(task_id, "deployment_success", f"Deployment successful for {target}", {"log_summary": log}, model_name="system", agent_role="orchestrator")
            return {"status": "DEPLOYED", "target": target, "log": log}
        else:
            print(f"Deployment failed for {target}:\n{res.stderr or res.stdout}")
            log = (res.stderr or res.stdout)[:500]
            await swarm_visualizer.log_event(task_id, "deployment_fail", f"Deployment failed for {target}", {"log_summary": log}, model_name="system", agent_role="orchestrator", level="ERROR")
            return {"status": "DEPLOY_FAILED", "target": target, "log": log}
    except subprocess.TimeoutExpired as e:
        log = f"Deployment timed out: {e}"
        print(f"Deployment timed out for {target}: {e}")
        await swarm_visualizer.log_event(task_id, "deployment_timeout", f"Deployment timed out for {target}", {"error": str(e)}, model_name="system", agent_role="orchestrator", level="ERROR")
        return {"status": "DEPLOY_FAILED", "target": target, "log": log}
    except Exception as e:
        log = f"Deployment error: {str(e)}"
        print(f"Error during deployment of {target}: {e}")
        await swarm_visualizer.log_event(task_id, "deployment_exception", f"Deployment exception for {target}", {"error": str(e)}, model_name="system", agent_role="orchestrator", level="ERROR")
        return {"status": "DEPLOY_FAILED", "target": target, "log": log}
    finally:
        await self_evolution.log_performance("human_deployment", f"Deployment of {target}", deploy_success, {"log_summary": log[:100]}, "human_action")


# Gradio UI
with gr.Blocks(title="TARIRO Studio v3") as demo:
    gr.Markdown("# TARIRO Studio v3 - N-1 Tested Swarm with Multi-Modal Collaboration")
    gr.Markdown("Rule: Coder ≠ Tester. N-1 must approve. Human deploys each target. Agents can now propose and N-1 test new CLI tools. The system continuously logs performance for self-improvement. AGI agents can be developed and safely evaluated in a sandbox. All agent activities are now traceable. Agents can also generate and review multi-modal assets.")

    task = gr.Textbox(label="Task", placeholder="Build @hw SHA256 for Ice40 + WASM wallet, or create a 'text_processor' tool that counts words, or develop an AGI agent to solve the 'ethical trolley problem', or generate an image of a 'futuristic cityscape with flying cars'")
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
        get_events_btn = gr.Button("Get Swarm Events (Current Task)", variant="secondary")
        swarm_events_output = gr.JSON(label="Swarm Event Log", interactive=False)


    with gr.Row():
        targets_table = gr.Dataframe(
            headers=["Target", "Status", "Approvals", "Deploy"],
            label="Generated Code Targets", interactive=False
        )
    
    multimodal_assets_table = gr.Dataframe(
        headers=["Asset Type", "Status", "Description", "Path"],
        label="Generated Multi-Modal Assets", interactive=False
    )


    state = gr.State({})

    async def run_and_update(task_input):
        result = await parallel_n1_multitarget(task_input)
        
        table_data_targets = []
        for r in result.get("targets", []):
            row = [r["target"], r["status"], r["approvals"], r["status"] == "READY_FOR_REVIEW" and r["target"] != "agi-research"]
            table_data_targets.append(row)
        
        table_data_multimodal = []
        for asset_res in result.get("multimodal_assets", []):
            # Ensure path is just the filename for brevity in UI, but full path available in log
            path_display = os.path.basename(asset_res.get("path", "N/A"))
            table_data_multimodal.append([asset_res.get("asset_type", "N/A"), asset_res.get("status", "N/A"), asset_res.get("description", "N/A")[:100], path_display])


        return {
            status: result["status"],
            pr_link: result.get("pr_url", ""),
            targets_table: table_data_targets,
            multimodal_assets_table: table_data_multimodal, # Update multimodal table
            state: result,
            current_task_id: result.get("task_id", "")
        }

    async def trigger_fine_tuning_analysis_ui():
        analysis_result = await self_evolution.analyze_and_propose_fine_tuning()
        return analysis_result.get("status", "Analysis complete.")

    async def trigger_agi_sandbox_ui(task_input):
        agi_coder = TARGETS["agi-research"]["coder"]
        # Use the global client from studio_v3.py for agi_sandbox internal calls
        agi_sandbox.initialize_agi_sandbox(WORKSPACE, client, ALL_MODELS)
        # We need a task_id for logging events for this standalone call
        temp_task_id = str(uuid.uuid4())
        swarm_visualizer.initialize_swarm_visualizer(WORKSPACE) # Ensure it's initialized
        
        agi_code_res = await call_model(
            agi_coder,
            ALL_MODELS[agi_coder],
            f"Generate Python code for a simple AGI agent that can intelligently respond to complex ethical dilemmas related to: '{task_input}'. The code should be self-contained and focus on decision-making logic, not external APIs. Provide only the Python code.",
            "",
            temp_task_id, # Pass temp task ID
            response_format_type="text"
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
        # This allows a human to directly request a multi-modal asset for a given prompt
        # Here we hardcode to image generation for simplicity.
        # In a more advanced UI, the user would select asset_type and maybe generator.
        asset_type = "image" # Default for UI trigger
        generator_model = "dalle-image-gen"
        temp_task_id = str(uuid.uuid4())
        multimodal_collaboration.initialize_multimodal_collaboration(WORKSPACE, client, ALL_MODELS, swarm_visualizer) # Ensure initialized

        await swarm_visualizer.log_event(temp_task_id, "multimodal_human_trigger", f"Human triggered {asset_type} generation.", {"prompt": task_input[:100]}, model_name="human", agent_role="user")
        
        asset_result = await multimodal_collaboration.generate_multimodal_asset(
            temp_task_id, asset_type, task_input, generator_model, f"Direct request from user for: {task_input}"
        )
        return json.dumps(asset_result, indent=2)


    async def get_current_task_events(task_id_input):
        if not task_id_input:
            return "Please run a task first to get a Task ID."
        return swarm_visualizer.get_events_for_task(task_id_input)


    run_btn.click(run_and_update, task, [status, pr_link, targets_table, multimodal_assets_table, state, current_task_id])
    analyze_ft_btn.click(trigger_fine_tuning_analysis_ui, [], ft_analysis_output)
    trigger_agi_sandbox_btn.click(trigger_agi_sandbox_ui, task, agi_sandbox_output)
    trigger_multimodal_btn.click(trigger_multimodal_generation_ui, task, multimodal_output) # New button for multi-modal
    get_events_btn.click(get_current_task_events, current_task_id, swarm_events_output)

    # Dynamic deploy buttons per target
    @gr.render(inputs=[state])
    def render_deploy_buttons(current_state):
        targets = current_state.get("targets", [])
        for t in targets:
            if t["status"] == "READY_FOR_REVIEW":
                btn = gr.Button(f"DEPLOY {t['target'].upper()}")
                btn.click(lambda target_name=t["target"], task_id=current_state.get("task_id", ""): human_deploy(task_id, target_name, ""), None, status)

if __name__ == "__main__":
    # Auto-pull models on start
    print("Pulling Ollama models. This may take some time...")
    for m in ["llama3.1:70b", "qwen2.5-coder:32b", "deepseek-coder-v2:16b", "gemma2:27b", "phi-3:mini", "qwen2.5:72b"]:
        try:
            os.system(f"ollama pull {m}")
        except Exception as e:
            print(f"Failed to pull model {m}: {e}")
    # Add conceptual multi-modal models to ALL_MODELS for LiteLLM to load if configured
    # e.g., if you had a LiteLLM proxy for DALL-E, it would be configured there.
    # For now, these are just treated as LLM calls that return descriptions/URLs.
    print("Ollama model pulling complete.")
    
    # Initialize all feature modules and start background loops
    # Order matters for dependencies (e.g., multimodal needs swarm_visualizer)
    swarm_visualizer.initialize_swarm_visualizer(WORKSPACE) # Initialize swarm visualizer first
    self_evolution.initialize_self_evolution(WORKSPACE, client, ALL_MODELS)
    tool_forge.initialize_tool_forge(ALL_MODELS, client, SEARXNG, WORKSPACE)
    agi_sandbox.initialize_agi_sandbox(WORKSPACE, client, ALL_MODELS)
    multimodal_collaboration.initialize_multimodal_collaboration(WORKSPACE, client, ALL_MODELS, swarm_visualizer) # Initialize multimodal collaboration

    asyncio.create_task(self_evolution.start_continuous_self_evolution_loop())
    print("Started continuous self-evolution analysis loop.")

    demo.launch(server_name="0.0.0.0")
