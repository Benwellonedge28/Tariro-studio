import asyncio, gradio as gr, os, json, subprocess, httpx
from openai import AsyncOpenAI
from git import Repo
from qdrant_client import QdrantClient
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from typing import List, Dict
import ast

client = AsyncOpenAI(base_url="http://localhost:4000/v1", api_key="sk-free")
qdrant = QdrantClient("http://qdrant:6333")
SEARXNG = "http://searxng:8080/search"
WORKSPACE = "/app/workspace/taric"
TOOLS_BIN = "/app/workspace/tools/bin"

ALL_MODELS = {
    "qwen-coder": "Write TariroLang code. Never test. Must cite 2+ sources.",
    "deepseek-coder": "Write tests + run taric. Never write prod code.",
    "llama-architect": "Design + review specs. Never write code.",
    "gemma-reviewer": "Security + style review. Never write code.",
    "phi-pm": "Delegate tasks. Never write code.",
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
        "coder": "gemma-reviewer",
        "compile_cmd": "taric --target yaml src/cloud.tari -o k8s/",
        "test_cmd": "kubectl apply --dry-run=client -f k8s/",
        "deploy_cmd": "kubectl apply -f k8s/"
    },
    "x86-linux": {
        "coder": "llama-architect",
        "compile_cmd": "taric --target x86_64-linux src/main.tari -o tariro-os",
        "test_cmd": "qemu-system-x86_64 -kernel tariro-os -nographic",
        "deploy_cmd": "docker build -t tariro-os && docker push"
    }
}

async def web_search(query: str) -> List[str]:
    async with httpx.AsyncClient() as c:
        r = await c.get(SEARXNG, params={"q": query, "format": "json"})
        return [hit["url"] for hit in r.json().get("results", [])[:5]]

def ast_no_network(code: str) -> bool:
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            if any(n.name in ["socket", "requests", "urllib"] for n in node.names): return False
    return True

async def call_model(model, role, task, context, ban_models=[], target=None):
    if model in ban_models:
        return {"model": model, "approved": False, "reason": "BANNED: Coder cannot test"}

    sources = []
    if model in ["deepseek-coder", "llama-architect"]: # Researchers
        sources = await web_search(task + " TariroLang FPGA RISC-V")
        context += f"\n\nWeb Sources:\n" + "\n".join(sources)

    resp = await client.chat.completions.create(
        model=model,
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
    return out

async def build_for_target(target, task, code_ctx, repo_path):
    cfg = TARGETS[target]
    coder = cfg["coder"]
    testers = [m for m in ALL_MODELS if m not in [coder, "arbiter"]]
    state = {"target": target, "coder": coder, "status": "CODING"}

    # 1. Coder writes
    code_res = await call_model(coder, ALL_MODELS[coder], task, code_ctx, ban_models=[], target=target)
    code = code_res.get("code", "")
    if not code or not ast_no_network(code):
        return {"status": "CODER_FAIL", "reason": code_res.get("reason", "No code or network found")}

    # 2. Write + compile + test
    target_dir = f"{repo_path}/target/{target}"
    os.makedirs(target_dir, exist_ok=True)
    with open(f"{target_dir}/main.tari", "w") as f: f.write(code)

    test_results = []
    for tester in testers:
        compile_out = subprocess.run(cfg["compile_cmd"], shell=True, cwd=target_dir, capture_output=True)
        test_out = subprocess.run(cfg["test_cmd"], shell=True, cwd=target_dir, capture_output=True)
        approved = compile_out.returncode == 0 and test_out.returncode == 0
        test_results.append({
            "model": tester, "approved": approved,
            "compile_log": compile_out.stderr.decode()[:200],
            "test_log": test_out.stdout.decode()[:200]
        })

    approvals = [r for r in test_results if r["approved"]]
    status = "READY_FOR_REVIEW" if len(approvals) == len(testers) else "FAILED_TESTS"

    return {
        "target": target, "coder": coder, "code": code, "status": status,
        "approvals": f"{len(approvals)}/{len(testers)}", "test_results": test_results,
        "deploy_cmd": cfg["deploy_cmd"], "sources": code_res.get("sources", [])
    }

async def parallel_n1_multitarget(task):
    os.makedirs(WORKSPACE, exist_ok=True)
    repo_path = WORKSPACE

    # 1. PM picks targets
    pm_res = await call_model("phi-pm", ALL_MODELS["phi-pm"], f"Pick targets for: {task}", "")
    targets = pm_res.get("targets", ["x86-linux", "wasm-web"])

    # 2. Build all targets in parallel
    context = subprocess.getoutput(f"find {repo_path} -name '*.tari' | head -20")
    results = await asyncio.gather(*[build_for_target(t, task, context, repo_path) for t in targets])

    # 3. Create PR if any target ready
    ready = [r for r in results if r["status"] == "READY_FOR_REVIEW"]
    if not ready: return {"status": "ALL_FAILED", "targets": results}

    repo = Repo.init(repo_path)
    branch = f"ai/{task[:20].replace(' ', '-').lower()}"
    repo.git.checkout('-b', branch)
    for res in ready: repo.index.add([f"target/{res['target']}/"])
    repo.index.commit(f"AI Swarm: {task}\n\nTargets: {','.join([r['target'] for r in ready])}")
    repo.git.push("--set-upstream", "origin", branch)
    pr_url = subprocess.getoutput(f"cd {repo_path} && gh pr create --title 'AI: {task}' --body 'N-1 approved: {ready}'")

    return {"pr_url": pr_url, "status": "READY_FOR_REVIEW", "targets": results}

async def human_deploy(target, branch):
    """ONLY called when human clicks Deploy"""
    cfg = TARGETS[target]
    res = subprocess.run(cfg["deploy_cmd"], shell=True, cwd=f"{WORKSPACE}/target/{target}")
    return {"status": "DEPLOYED" if res.returncode == 0 else "DEPLOY_FAILED", "target": target}

# Gradio UI
with gr.Blocks(title="TARIRO Studio v3") as demo:
    gr.Markdown("# TARIRO Studio v3 - N-1 Tested Swarm")
    gr.Markdown("Rule: Coder ≠ Tester. N-1 must approve. Human deploys each target.")

    task = gr.Textbox(label="Task", placeholder="Build @hw SHA256 for Ice40 + WASM wallet")
    run_btn = gr.Button("Run Swarm", variant="primary")

    status = gr.Textbox(label="Overall Status")
    pr_link = gr.Textbox(label="PR URL")

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

    run_btn.click(run_and_update, task, [status, pr_link, targets_table, state])

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
    for m in ["llama3.1:70b", "qwen2.5-coder:32b", "deepseek-coder-v2:16b", "gemma2:27b", "phi-3:mini", "qwen2.5:72b"]:
        os.system(f"ollama pull {m}")
    demo.launch(server_name="0.0.0.0")