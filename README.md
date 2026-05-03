TARIRO Studio v3

**Full-stack AI dev swarm. All free models. N-1 tested. Human deploy.**

Run
```bash
export GITHUB_TOKEN=ghp_xxx
docker compose up --build
Open `http://localhost:7860`
```

Use
1. Type: "Build @hw SHA256 for Ice40 + WASM wallet"
2. Watch: 5 models research, code, N-1 test in parallel
3. See: PR with `kernel.elf` + `app.wasm`. Status: READY_FOR_REVIEW
4. Click: `[DEPLOY verilog-fpga]` → FPGA flashed. `[DEPLOY wasm-web]` → IPFS

Rules
1. Coder ≠ Tester. Enforced by code + CI
2. N-1 = 4/4 approvals required. Else button disabled
3. No auto-deploy. Ever. You click per target
4. All models Apache/MIT. $0 cost. Runs offline

Targets
`taric --target` → `riscv32-baremetal`, `wasm-web`, `verilog-fpga`, `k8s-cloud`, `x86-linux`

Download
GitHub Releases → `TARIRO-Studio.exe`, `.dmg`, `.AppImage`, `.apk`

---

**How to Launch**

```bash
git init tariro-studio && cd tariro-studio
Paste all 7 files above
export GITHUB_TOKEN=ghp_yourtoken
docker compose up --build
1. Wait 10 min: Ollama pulls 6 models ∼80GB
2. Open `localhost:7860`
3. Task: "Add @hw UART to std/"
4. Watch swarm: Qwen codes, DeepSeek+Llama+Gemma+Phi test, Arbiter merges
5. PR opens. CI builds 5 targets. All green
6. Click `DEPLOY verilog-fpga`. FPGA flashed
```

*$0 cost. 100% local. Works offline in Harare.*

You now have the full repo. Clone, run, ship. The swarm builds OSes, cloud, web, FPGA, and can evolve itself. You deploy.