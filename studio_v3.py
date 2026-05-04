import asyncio, gradio as gr, os, json, subprocess, httpx
from openai import AsyncOpenAI
from git import Repo
# from qdrant_client import QdrantClient # Commented out if not directly used here or causing issues
import qdrant_client # Keeping the import for QdrantClient for potential future use or to avoid removing it entirely
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from typing import List, Dict, Any
import ast

# Import new feature modules
import features.tool_forge as tool_forge
import features.self_evolution as self_evolution

client = AsyncOpenAI(base_url="http://localhost:4000/v1", api_key="sk-free")
qdrant = qdrant_client.QdrantClient("http://qdrant:6333") # Use qdrant_client.QdrantClient explicitly
SEARXNG = "http://searxng:8080/search"

# Define WORKSPACE earlier for module initialization
WORKSPACE = "/app/workspace"
# TOOLS_BIN is now managed within tool_forge.py


ALL_MODELS = {
    "qwen-coder": "Write TariroLang code. Never test. Must cite 2+ sources.",
    "deepseek-coder": "Write tests + run taric. Never write prod code. Can research for test cases.",
    "llama-architect": "Design + review specs. Can also propose new command-line tool specifications. Can research for tool design.",
    "gemma-reviewer": "Security + style review. Never write code. Can test tools.",
    "phi-pm": "Delegate tasks. Never write code. Orchestrates tool proposal and testing.",
    "arbiter": "Merge only if N-1 approvals. Never write original code."
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
        "coder": "qwen-coder", # Corrected from gemma-reviewer
        "compile_cmd": "taric --target yaml src/cloud.tari -o k8s/",
        "test_cmd": "kubectl apply --dry-run=client -f k8s/",
        "deploy_cmd": "kubectl apply -f k8s/"
    },
    "x86-linux": {
        "coder": "deepseek-coder", # Corrected from llama-architect
        "compile_cmd": "taric --target x86_64-linux src/main.tari -o tariro-os",
        "test_cmd": "qemu-system-x86_64 -kernel tariro-os -nographic",
        "deploy_cmd": "docker build -t tariro-os && docker push"
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

async def call_model(model: str, role: str, task: str, context: str, ban_models: List[str] = [], target: Optional[str] = None) -> Dict[str, Any]:
    # Use the potentially fine-tuned version of the model
    effective_model_name = self_evolution.get_current_model_version(model)
    print(f"Calling model: {model} (effective: {effective_model_name}) for role: {role}")

    if model in ban_models:
        return {"model": model, "approved": False, "reason": "BANNED: Coder cannot test"}

    sources = []
    if model in ["deepseek-coder", "llama-architect"]: # Researchers
        sources = await web_search(task + " TariroLang FPGA RISC-V")
        context += f"\n\nWeb Sources:\n" + "\n".join(sources)

    resp = await client.chat.completions.create(
        model=effective_model_name, # Use effective model name here
        messages=[
            {"role": "system", "content": f"You are {model}. Role: {role}. Output JSON only. Cite sources."},
            {"role": "user", "content": f"Task: {task}\nTarget: {target}\nContext:\n{context}\n\nOutput: {{\"code\": \"...\", \"sources\": [url1, url2], \"approved\": bool, \"reason\": \"...\"}}"}
        ],
        response_format={"type": "json_object"},
        temperature=0.1
    )
    out = json.loads(resp.choices[0].message.content)
    out["model"], out["sources"] = model, sources + out.get("sources", [])

    # Enforce source citation for coders
    if model in ["qwen-coder", "deepseek-coder"] and len(out.get("sources", [])) < 2:
        out["approved"] = False
        out["reason"] = "Rejected: Must cite 2+ sources"
    
    # Log performance for this model call
    await self_evolution.log_performance(
        model_name=model,
        task_description=task,
        success=out.get("approved", True), # Assume success if no explicit rejection
        details={"output_summary": out.get("reason", out.get("code", "")[:100])},
        role=role
    )
    return out

async def build_for_target(target: str, task: str, code_ctx: str, repo_path: str) -> Dict[str, Any]:
    cfg = TARGETS[target]
    coder = cfg["coder"]
    # Pass available tools to coders if they need to integrate them
    available_tools = tool_forge.get_validated_tools()
    tool_context = f"\n\nAvailable Tools:\n{json.dumps(available_tools, indent=2)}" if available_tools else ""


    testers = [m for m in ALL_MODELS if m not in [coder, "arbiter"] and "never test" not in ALL_MODELS[m].lower() and "never write prod code" not in ALL_MODELS[m].lower()]
    state = {"target": target, "coder": coder, "status": "CODING"}

    # 1. Coder writes
    code_res = await call_model(coder, ALL_MODELS[coder], task, code_ctx + tool_context, ban_models=[], target=target)
    code = code_res.get("code", "")
    # Use tool_forge's more robust network check if needed, or keep this one for main code
    if not code or not ast_no_network(code):
        await self_evolution.log_performance(coder, f"Code generation for {target} failed: {task}", False, {"reason": code_res.get("reason", "No code or network found"), "code_snippet": code[:100]}, ALL_MODELS[coder])
        return {"status": "CODER_FAIL", "reason": code_res.get("reason", "No code or network found")}

    # 2. Write + compile + test
    target_dir = os.path.join(repo_path, "target", target)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "main.tari"), "w") as f: f.write(code)

    test_results = []
    for tester in testers:
        print(f"Tester {tester} attempting to test {target}...")
        test_success = False
        reason = "Unknown error"
        compile_log = ""
        test_log = ""
        try:
            compile_out = subprocess.run(cfg["compile_cmd"], shell=True, cwd=target_dir, capture_output=True, text=True, timeout=60)
            compile_log = (compile_out.stderr or compile_out.stdout)[:500]
            if compile_out.returncode != 0:
                print(f"Compile failed for {target} by {tester}:\n{compile_log}")
                reason = "Compile failed"
            else:
                test_out = subprocess.run(cfg["test_cmd"], shell=True, cwd=target_dir, capture_output=True, text=True, timeout=60)
                test_log = (test_out.stderr or test_out.stdout)[:500]
                if test_out.returncode == 0:
                    test_success = True
                    reason = "Tests passed"
                else:
                    reason = "Tests failed"
            
            test_results.append({
                "model": tester, "approved": test_success, "reason": reason,
                "compile_log": compile_log,
                "test_log": test_log
            })
        except subprocess.TimeoutExpired as e:
            reason = "Test/Compile timed out"
            test_log = str(e)
            test_results.append({
                "model": tester, "approved": False, "reason": reason,
                "compile_log": compile_log, "test_log": test_log
            })
        except Exception as e:
            reason = f"Testing error: {str(e)}"
            test_log = str(e)
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


    approvals = [r for r in test_results if r["approved"]]
    status = "READY_FOR_REVIEW" if len(approvals) >= len(testers) - 1 else "FAILED_TESTS" # N-1 logic

    return {
        "target": target, "coder": coder, "code": code, "status": status,
        "approvals": f"{len(approvals)}/{len(testers)}", "test_results": test_results,
        "deploy_cmd": cfg["deploy_cmd"], "sources": code_res.get("sources", [])
    }

async def parallel_n1_multitarget(task):
    os.makedirs(WORKSPACE, exist_ok=True)
    repo_path = WORKSPACE

    # Initialize self_evolution module first
    self_evolution.initialize_self_evolution(WORKSPACE, client, ALL_MODELS)
    # Initialize tool_forge module with necessary global configurations
    tool_forge.initialize_tool_forge(ALL_MODELS, client, SEARXNG, WORKSPACE)

    # --- NEW: Step 0 - Tool Generation and Testing Phase ---
    print(f"Starting Tool Forge check for task: '{task}'")
    # Using 'phi-pm' to orchestrate tool proposal, 'llama-architect' to propose detailed spec
    tool_proposal_result = await tool_forge.propose_new_tool_spec(task, "llama-architect") 

    if tool_proposal_result["status"] == "success":
        print(f"New tool '{tool_proposal_result['tool_name']}' proposed. Starting N-1 testing...")
        n1_test_result = await tool_forge.n1_test_tool(
            tool_proposal_result["spec_path"],
            f"Verify the functionality of the newly proposed tool: {tool_proposal_result['tool_name']} for task: '{task}'"
        )

        if n1_test_result["status"] == "VALIDATED":
            print(f"Tool '{n1_test_result['tool_name']}' N-1 validated and ready for use.")
            # The tool script is already in TOOLS_BIN_DIR and its spec in TOOL_SPEC_DIR
            # Other agents can now discover it via tool_forge.get_validated_tools()
            await self_evolution.log_performance("tool_forge_system", f"Tool '{n1_test_result['tool_name']}' N-1 validated", True, n1_test_result, "system")
        else:
            print(f"Tool '{tool_proposal_result.get('tool_name', 'Unknown')}' failed N-1 testing. Reason: {n1_test_result.get('reason', 'See logs')}")
            await self_evolution.log_performance("tool_forge_system", f"Tool '{tool_proposal_result.get('tool_name', 'Unknown')}' N-1 failed", False, n1_test_result, "system")
            # Decide whether to proceed with main task or halt if tool was critical
    elif tool_proposal_result["status"] == "no_tool_needed":
        print("Phi-PM determined no new tool is needed for this task.")
        await self_evolution.log_performance("phi-pm", f"Decision: No new tool needed for {task}", True, {"task": task}, "pm")
    else:
        print(f"Tool proposal failed: {tool_proposal_result.get('reason', 'Unknown error')}. Details: {tool_proposal_result.get('details', 'N/A')}")
        await self_evolution.log_performance("tool_forge_system", f"Tool proposal failed for {task}", False, tool_proposal_result, "system")
        # Decide whether to proceed with main task or halt if tool was critical
    
    # After potential tool generation, now get any newly validated tools or existing ones
    available_tools = tool_forge.get_validated_tools()
    if available_tools:
        print(f"Currently available validated tools for use in coding phase: {[t['name'] for t in available_tools]}")

    # --- END NEW TOOL GENERATION PHASE ---

    # 1. PM picks targets (Original logic)
    pm_res = await call_model("phi-pm", ALL_MODELS["phi-pm"], f"Pick targets for: {task}", "")
    targets = pm_res.get("targets", ["x86-linux", "wasm-web"])
    await self_evolution.log_performance("phi-pm", f"Target selection for: {task}", True, {"targets": targets}, "pm")
    
    # Start continuous self-evolution loop as a background task if not already running
    # This ensures the loop runs once even if parallel_n1_multitarget is called multiple times
    if not hasattr(parallel_n1_multitarget, '_self_evolution_loop_started'):
        asyncio.create_task(self_evolution.start_continuous_self_evolution_loop())
        parallel_n1_multitarget._self_evolution_loop_started = True


    # 2. Build all targets in parallel (Original logic)
    context = subprocess.getoutput(f"find {repo_path} -name '*.tari' | head -20")
    results = await asyncio.gather(*[build_for_target(t, task, context, repo_path) for t in targets])

    # 3. Create PR if any target ready (Original logic)
    ready = [r for r in results if r["status"] == "READY_FOR_REVIEW"]
    if not ready: 
        await self_evolution.log_performance("system_orchestrator", f"Overall task failed: {task}", False, {"targets_results": results}, "system")
        return {"status": "ALL_FAILED", "targets": results}

    repo = Repo.init(repo_path)
    # Ensure the branch name is valid GitHub format
    branch = f"ai/{task[:20].replace(' ', '-').lower().replace('/', '-')}"
    try:
        # Check if branch exists
        current_branches = [head.name for head in repo.heads]
        if branch in current_branches:
            repo.git.checkout(branch)
            print(f"Checked out existing branch: {branch}")
        else:
            repo.git.checkout('-b', branch)
            print(f"Created and checked out new branch: {branch}")
    except Exception as e:
        print(f"Error creating/checking out branch {branch}. Falling back to main. Error: {e}")
        repo.git.checkout('main') # Fallback
        # If fallback, then we would need to commit to main or fail.
        # For this example, let's assume we can create the branch.

    for res in ready:
        target_path = os.path.join("target", res['target'])
        full_target_path = os.path.join(repo_path, target_path)
        if os.path.exists(full_target_path):
            repo.index.add([full_target_path])
        else:
            print(f"Warning: Target path {target_path} not found in repository, skipping add to index.")

    commit_message = f"AI Swarm: {task}\n\nTargets: {','.join([r['target'] for r in ready])}"
    repo.index.commit(commit_message)
    repo.git.push("--set-upstream", "origin", branch)
    
    # This `gh pr create` will require the gh CLI tool to be configured in the container or host
    # and the GITHUB_TOKEN environment variable to have appropriate scopes.
    # It also needs the 'gh' CLI tool installed, which is in the Dockerfile.
    pr_url = "PR creation skipped (requires 'gh' CLI login or specific GITHUB_TOKEN setup for CLI)"
    try:
        pr_command = f"cd {repo_path} && gh pr create --title 'AI: {task}' --body 'N-1 approved: {ready}' --head {branch} --base main"
        pr_process = subprocess.run(pr_command, shell=True, capture_output=True, text=True, timeout=30)
        if pr_process.returncode == 0:
            pr_url = pr_process.stdout.strip()
            print(f"GitHub PR created: {pr_url}")
            await self_evolution.log_performance("github_integration", f"PR created for {task}", True, {"pr_url": pr_url}, "system")
        else:
            print(f"Failed to create GitHub PR: {pr_process.stderr.strip()}")
            await self_evolution.log_performance("github_integration", f"PR creation failed for {task}", False, {"error": pr_process.stderr.strip()}, "system")
    except Exception as e:
        print(f"Error executing gh pr create: {e}")
        await self_evolution.log_performance("github_integration", f"PR creation exception for {task}", False, {"exception": str(e)}, "system")

    await self_evolution.log_performance("system_orchestrator", f"Overall task completed: {task}", True, {"pr_url": pr_url, "targets_results": results}, "system")
    return {"pr_url": pr_url, "status": "READY_FOR_REVIEW", "targets": results}

async def human_deploy(target: str, branch: str) -> Dict[str, Any]:
    """ONLY called when human clicks Deploy"""
    cfg = TARGETS[target]
    # Ensure cwd is correct for deployment
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
            return {"status": "DEPLOYED", "target": target, "log": log}
        else:
            print(f"Deployment failed for {target}:\n{res.stderr or res.stdout}")
            log = (res.stderr or res.stdout)[:500]
            return {"status": "DEPLOY_FAILED", "target": target, "log": log}
    except subprocess.TimeoutExpired as e:
        log = f"Deployment timed out: {e}"
        print(f"Deployment timed out for {target}: {e}")
        return {"status": "DEPLOY_FAILED", "target": target, "log": log}
    except Exception as e:
        log = f"Deployment error: {str(e)}"
        print(f"Error during deployment of {target}: {e}")
        return {"status": "DEPLOY_FAILED", "target": target, "log": log}
    finally:
        await self_evolution.log_performance("human_deployment", f"Deployment of {target}", deploy_success, {"log_summary": log[:100]}, "human_action")


# Gradio UI
with gr.Blocks(title="TARIRO Studio v3") as demo:
    gr.Markdown("# TARIRO Studio v3 - N-1 Tested Swarm with Tool Forge & Self-Evolution")
    gr.Markdown("Rule: Coder ≠ Tester. N-1 must approve. Human deploys each target. Agents can now propose and N-1 test new CLI tools. The system continuously logs performance for self-improvement.")

    task = gr.Textbox(label="Task", placeholder="Build @hw SHA256 for Ice40 + WASM wallet, or create a 'text_processor' tool that counts words")
    run_btn = gr.Button("Run Swarm", variant="primary")

    status = gr.Textbox(label="Overall Status")
    pr_link = gr.Textbox(label="PR URL")
    
    with gr.Row():
        # Added a button to manually trigger fine-tuning analysis
        analyze_ft_btn = gr.Button("Analyze for Fine-Tuning", variant="secondary")
        ft_analysis_output = gr.Textbox(label="Fine-Tuning Analysis Result", interactive=False)


    with gr.Row():
        targets_table = gr.Dataframe(
            headers=["Target", "Status", "Approvals", "Deploy"],
            label="Targets", interactive=False
        )

    state = gr.State({})

    async def run_and_update(task_input):
        result = await parallel_n1_multitarget(task_input)
        table_data = []
        for r in result.get("targets", []):
            # Ensure each row has 4 elements
            row = [r["target"], r["status"], r["approvals"], r["status"] == "READY_FOR_REVIEW"]
            table_data.append(row)
        return {
            status: result["status"],
            pr_link: result.get("pr_url", ""),
            targets_table: table_data,
            state: result
        }

    async def trigger_fine_tuning_analysis_ui():
        analysis_result = await self_evolution.analyze_and_propose_fine_tuning()
        return analysis_result.get("status", "Analysis complete.")

    run_btn.click(run_and_update, task, [status, pr_link, targets_table, state])
    analyze_ft_btn.click(trigger_fine_tuning_analysis_ui, [], ft_analysis_output)

    # Dynamic deploy buttons per target
    @gr.render(inputs=[state])
    def render_deploy_buttons(current_state):
        targets = current_state.get("targets", [])
        for t in targets:
            if t["status"] == "READY_FOR_REVIEW":
                btn = gr.Button(f"DEPLOY {t['target'].upper()}")
                # Using lambda to capture t at definition time
                btn.click(lambda target_name=t["target"]: human_deploy(target_name, ""), None, status)

if __name__ == "__main__":
    # Auto-pull models on start
    print("Pulling Ollama models. This may take some time...")
    for m in ["llama3.1:70b", "qwen2.5-coder:32b", "deepseek-coder-v2:16b", "gemma2:27b", "phi-3:mini", "qwen2.5:72b"]:
        try:
            os.system(f"ollama pull {m}")
        except Exception as e:
            print(f"Failed to pull model {m}: {e}")
    print("Ollama model pulling complete.")
    
    # Initialize self-evolution and start its continuous loop as soon as possible
    self_evolution.initialize_self_evolution(WORKSPACE, client, ALL_MODELS)
    # Create the background task for self-evolution analysis
    asyncio.create_task(self_evolution.start_continuous_self_evolution_loop())
    print("Started continuous self-evolution analysis loop.")

    demo.launch(server_name="0.0.0.0")
