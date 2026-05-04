import os
import json
import subprocess
import httpx
from openai import AsyncOpenAI
from typing import List, Dict, Any
import ast
import tempfile
import asyncio

# --- Configuration (These would ideally come from a central config or passed in) ---
# Placeholder for models and their roles (should be passed from studio_v3.py)
_ALL_MODELS: Dict[str, str] = {}
_CLIENT: AsyncOpenAI = None
_SEARXNG_URL: str = ""
_WORKSPACE: str = ""

TOOL_SPEC_DIR = os.path.join(_WORKSPACE, "tools/specs") # This will be set dynamically


def initialize_tool_forge(all_models: Dict[str, str], openai_client: AsyncOpenAI, searxng_url: str, workspace_path: str):
    """Initializes global configurations for tool forge functions."""
    global _ALL_MODELS, _CLIENT, _SEARXNG_URL, _WORKSPACE, TOOL_SPEC_DIR
    _ALL_MODELS = all_models
    _CLIENT = openai_client
    _SEARXNG_URL = searxng_url
    _WORKSPACE = workspace_path
    TOOL_SPEC_DIR = os.path.join(_WORKSPACE, "tools/specs")
    os.makedirs(TOOL_SPEC_DIR, exist_ok=True)
    print(f"Tool Forge initialized. Tool specs will be stored in: {TOOL_SPEC_DIR}")


async def _web_search(query: str) -> List[str]:
    """Internal web search function for agents."""
    async with httpx.AsyncClient() as c:
        r = await c.get(_SEARXNG_URL, params={"q": query, "format": "json"})
        return [hit["url"] for hit in r.json().get("results", [])[:5]]

def _ast_no_network(code: str) -> bool:
    """Checks Python code for network-related imports."""
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                for n in node.names:
                    # Check both top-level imports and from-imports
                    if any(keyword in n.name for keyword in ["socket", "requests", "urllib", "http.client", "asyncio.open_connection"]):
                        return False
            # Also check for direct calls to subprocess that might contain network commands
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr == 'run' and isinstance(node.func.value, ast.Name) and node.func.value.id == 'subprocess':
                    if any(arg.value.s and any(net_cmd in arg.value.s for net_cmd in ["curl", "wget", "nc", "ssh"]) for arg in node.args if isinstance(arg, ast.Constant)):
                        return False
    except SyntaxError:
        # If code is not valid Python, we can't parse it, so err on the side of caution
        return False
    return True

async def _call_model_for_tool_gen(model: str, role: str, task: str, context: str, response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for tool generation related tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in tool_forge.")

    sources = []
    # Only researchers (llama-architect, deepseek-coder) perform web search here
    if model in ["llama-architect"]: # Can expand to other research models
        sources = await _web_search(task + " command-line tool design specification")
        context += f"\n\nWeb Search Sources:\n" + "\n".join(sources)

    try:
        resp = await _CLIENT.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": f"You are {model}. Role: {role}. Output {response_format_type} only. If providing code, ensure it's functional and safe. Cite sources if applicable."},
                {"role": "user", "content": f"Task: {task}\nContext:\n{context}"}
            ],
            response_format={"type": response_format_type},
            temperature=0.2 # Slightly higher temperature for creative tool design
        )
        content = resp.choices[0].message.content
        if response_format_type == "json_object":
            out = json.loads(content)
        else: # Assuming plain text for code generation
            out = {"code": content}
        out["model"] = model
        out["sources"] = sources + out.get("sources", []) # Combine search sources with model-cited sources
        return out
    except json.JSONDecodeError as e:
        print(f"Tool Forge: JSON decode error from model {model}: {e}. Content: {content}")
        return {"error": f"JSON decode error: {e}", "raw_content": content, "model": model}
    except Exception as e:
        print(f"Tool Forge: Error calling model {model}: {e}")
        return {"error": str(e), "model": model}


async def propose_new_tool_spec(task: str, proposed_by_model: str) -> Dict[str, Any]:
    """
    Orchestrates the proposal of a new tool specification by a designated agent.
    """
    # Phi-PM decides if a tool is needed, delegates to Llama-Architect to define
    pm_tool_decision = await _call_model_for_tool_gen(
        "phi-pm",
        _ALL_MODELS["phi-pm"],
        f"Analyze task: '{task}'. Do we need a new command-line tool to achieve this task more efficiently or to extend existing capabilities? If so, suggest its name, a concise description, a precise CLI command template (using placeholders like {{input_path}}, {{output_path}}, {{param_name}}), and a realistic example usage. Focus on a single, well-defined CLI command. Respond with JSON: {{'needs_tool': bool, 'tool_name': str, 'description': str, 'cli_template': str, 'example_usage': str}}",
        ""
    )

    if not pm_tool_decision.get("needs_tool"):
        print(f"Phi-PM decided no new tool is needed for task: '{task}'")
        return {"status": "no_tool_needed"}

    tool_name = pm_tool_decision.get("tool_name")
    description = pm_tool_decision.get("description")
    cli_template = pm_tool_decision.get("cli_template")
    example_usage = pm_tool_decision.get("example_usage")

    if not all([tool_name, description, cli_template, example_usage]):
        return {"status": "failed", "reason": "Phi-PM failed to provide complete tool definition."}

    # Delegate detailed tool code generation to qwen-coder
    tool_code_gen = await _call_model_for_tool_gen(
        "qwen-coder",
        _ALL_MODELS["qwen-coder"],
        f"Generate a self-contained Python script for a command-line tool named '{tool_name}' that implements the following functionality: '{description}'. It should adhere to this CLI template: '{cli_template}'. Provide all necessary code including argument parsing. Do NOT include network-related code (imports like requests, urllib, socket or calls like curl, wget). Ensure it handles input/output paths as specified. Include comments. Return ONLY the Python code, wrapped in ```python ... ```, no other text or explanation. Example Usage: '{example_usage}'",
        f"Tool Name: {tool_name}\nDescription: {description}\nCLI Template: {cli_template}\nExample: {example_usage}",
        response_format_type="text" # Expecting code, not JSON
    )

    generated_code_raw = tool_code_gen.get("code", "")
    if "```python" in generated_code_raw and "```" in generated_code_raw:
        generated_code = generated_code_raw.split("```python")[1].split("```")[0].strip()
    else:
        generated_code = generated_code_raw.strip()

    if not generated_code:
        return {"status": "failed", "reason": "Qwen-Coder failed to generate tool code."}

    if not _ast_no_network(generated_code):
        return {"status": "failed", "reason": "Qwen-Coder generated network-related code. Tool rejected."}

    # Save the tool Python script
    tool_script_path = os.path.join(_WORKSPACE, "tools/bin", f"{tool_name}.py")
    os.makedirs(os.path.dirname(tool_script_path), exist_ok=True)
    with open(tool_script_path, "w") as f:
        f.write(generated_code)
    os.chmod(tool_script_path, 0o755) # Make executable

    # Save the tool specification JSON
    tool_spec = {
        "name": tool_name,
        "description": description,
        "cli_command_template": cli_template,
        "example_usage": example_usage,
        "proposed_by": proposed_by_model,
        "script_path": tool_script_path,
        "status": "proposed", # Will change to 'validated' after N-1 testing
        "generated_code_sources": tool_code_gen.get("sources", [])
    }
    spec_file_name = f"{tool_name}.json"
    spec_path = os.path.join(TOOL_SPEC_DIR, spec_file_name)
    with open(spec_path, "w") as f:
        json.dump(tool_spec, f, indent=2)

    print(f"Tool '{tool_name}' script saved to {tool_script_path} and spec to {spec_path}")
    return {"status": "success", "tool_name": tool_name, "spec_path": spec_path, "script_path": tool_script_path}


async def n1_test_tool(tool_spec_path: str, testing_task_description: str) -> Dict[str, Any]:
    """
    Orchestrates N-1 testing for a proposed tool.
    Each tester model attempts to run the tool based on its spec and verify behavior.
    """
    if _ALL_MODELS is None or _CLIENT is None:
        raise ValueError("Tool Forge not initialized with all_models or OpenAI client.")

    with open(tool_spec_path, "r") as f:
        tool_spec = json.load(f)

    tool_name = tool_spec["name"]
    script_path = tool_spec["script_path"]
    cli_template = tool_spec["cli_command_template"]
    example_usage = tool_spec["example_usage"]

    # Filter out the coder and arbiter, and the original proposer of the tool
    tester_roles = {k: v for k, v in _ALL_MODELS.items() if k not in ["qwen-coder", "arbiter", tool_spec.get("proposed_by")]}
    testers = list(tester_roles.keys())

    if len(testers) < 4: # N-1 rule, needs at least 4 testers from the available roles
        return {"status": "FAILED_TESTS", "tool_name": tool_name, "reason": "Not enough independent testers for N-1 rule (need 4)."}

    print(f"Starting N-1 testing for tool '{tool_name}' with testers: {testers}")
    individual_test_results = []
    
    # Each tester model gets a chance to "test" the tool.
    # This involves:
    # 1. Understanding the tool spec.
    # 2. Generating a test case (e.g., mock input data).
    # 3. Executing the tool script with the test case.
    # 4. Verifying the output.
    # This is a highly complex, conceptual simulation for now.

    # Simulate running the tool with a test case derived from example_usage
    # For a real implementation, testers would interact with the tool via subprocess,
    # generate mock inputs, and assert outputs.
    async def run_single_tester_simulation(tester_model: str) -> Dict[str, Any]:
        tester_role = tester_roles[tester_model]
        test_context = f"You are testing a new command-line tool. Your role is '{tester_role}'.\n" \
                       f"Tool Name: {tool_name}\nDescription: {tool_spec['description']}\n" \
                       f"CLI Template: {cli_template}\nExample Usage: {example_usage}\n" \
                       f"The tool's Python script is located at: {script_path}\n" \
                       f"Task: {testing_task_description}\n\n" \
                       "You must simulate executing this tool script with a relevant test case and report if it functions correctly. Focus on parsing inputs, processing, and producing expected outputs. Provide a clear 'approved': true/false and 'log': str."

        # Ask the tester model to "simulate" testing and report
        simulated_test_output = await _call_model_for_tool_gen(
            tester_model,
            tester_role,
            "Simulate testing this tool and report outcome.",
            test_context,
            response_format_type="json_object"
        )
        
        approved = simulated_test_output.get("approved", False)
        log = simulated_test_output.get("log", "No log provided by tester.")
        error = simulated_test_output.get("error")
        if error:
            approved = False
            log = f"Tester simulation failed: {error}"

        # In a real system, you'd run the actual script:
        # with tempfile.TemporaryDirectory() as tmpdir:
        #     test_input_path = os.path.join(tmpdir, "test_input.txt")
        #     # Generate some mock test_input_path based on example_usage
        #     # Run: subprocess.run([sys.executable, script_path, ...])

        return {"model": tester_model, "approved": approved, "log": log[:500]} # Truncate log

    tasks = [run_single_tester_simulation(tester) for tester in testers]
    individual_test_results = await asyncio.gather(*tasks)

    approvals = [r for r in individual_test_results if r["approved"]]
    
    if len(approvals) >= len(testers) - 1: # N-1 approval rule (e.g., 3/4 or 4/4)
        tool_spec["status"] = "validated"
        with open(tool_spec_path, "w") as f:
            json.dump(tool_spec, f, indent=2)
        print(f"Tool '{tool_name}' N-1 validated!")
        return {"status": "VALIDATED", "tool_name": tool_name, "test_results": individual_test_results}
    else:
        tool_spec["status"] = "failed_n1_test"
        with open(tool_spec_path, "w") as f:
            json.dump(tool_spec, f, indent=2)
        print(f"Tool '{tool_name}' FAILED N-1 validation.")
        return {"status": "FAILED_TESTS", "tool_name": tool_name, "test_results": individual_test_results}

# --- Utility to get available tools (for other agents) ---
def get_validated_tools() -> List[Dict[str, Any]]:
    """Retrieves all N-1 validated tool specifications."""
    validated_tools = []
    if not os.path.exists(TOOL_SPEC_DIR):
        return []
    for filename in os.listdir(TOOL_SPEC_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(TOOL_SPEC_DIR, filename), "r") as f:
                tool_spec = json.load(f)
                if tool_spec.get("status") == "validated":
                    validated_tools.append(tool_spec)
    return validated_tools
