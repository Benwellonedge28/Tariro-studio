import os
import json
import asyncio
from datetime import datetime
from typing import List, Dict, Any, Optional

# --- Configuration & Shared Data (initialized from studio_v3.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Model names and their base roles

PERFORMANCE_LOG_DIR: str = ""
FEEDBACK_DATA_DIR: str = ""
FINE_TUNED_MODEL_CONFIG_PATH: str = "" # To simulate updating litellm_config or similar

def initialize_self_evolution(workspace_path: str, openai_client: Any, all_models: Dict[str, str]):
    """Initializes global configurations for self-evolution functions."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, PERFORMANCE_LOG_DIR, FEEDBACK_DATA_DIR, FINE_TUNED_MODEL_CONFIG_PATH
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models # Store a copy of the base models and their roles

    PERFORMANCE_LOG_DIR = os.path.join(_WORKSPACE, "self_evolution/performance_logs")
    FEEDBACK_DATA_DIR = os.path.join(_WORKSPACE, "self_evolution/feedback_data")
    FINE_TUNED_MODEL_CONFIG_PATH = os.path.join(_WORKSPACE, "litellm_fine_tuned_models.json") # A new file for tracking fine-tuned versions

    os.makedirs(PERFORMANCE_LOG_DIR, exist_ok=True)
    os.makedirs(FEEDBACK_DATA_DIR, exist_ok=True)

    # Initialize fine-tuned model config if it doesn't exist
    if not os.path.exists(FINE_TUNED_MODEL_CONFIG_PATH):
        with open(FINE_TUNED_MODEL_CONFIG_PATH, "w") as f:
            json.dump({}, f)
    print(f"Self-Evolution initialized. Logs: {PERFORMANCE_LOG_DIR}, Feedback: {FEEDBACK_DATA_DIR}")

def _load_fine_tuned_models() -> Dict[str, str]:
    """Loads the current mapping of base model to fine-tuned model."""
    if os.path.exists(FINE_TUNED_MODEL_CONFIG_PATH):
        with open(FINE_TUNED_MODEL_CONFIG_PATH, "r") as f:
            return json.load(f)
    return {}

def _save_fine_tuned_models(config: Dict[str, str]):
    """Saves the current mapping of base model to fine-tuned model."""
    with open(FINE_TUNED_MODEL_CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)

def get_current_model_version(base_model_name: str) -> str:
    """Returns the effective model name, potentially a fine-tuned version."""
    fine_tuned_models = _load_fine_tuned_models()
    return fine_tuned_models.get(base_model_name, base_model_name)

async def log_performance(
    model_name: str,
    task_description: str,
    success: bool,
    details: Dict[str, Any],
    role: str
):
    """
    Logs the performance of a model for a specific task.
    """
    timestamp = datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "model_name": model_name,
        "role": role,
        "task_description": task_description,
        "success": success,
        "details": details
    }
    
    log_filename = os.path.join(PERFORMANCE_LOG_DIR, f"{model_name}_{datetime.now().strftime('%Y%m%d')}.jsonl")
    with open(log_filename, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    print(f"Performance logged for {model_name}: {'SUCCESS' if success else 'FAILURE'}")

async def analyze_and_propose_fine_tuning() -> Dict[str, Any]:
    """
    Analyzes performance logs and proposes fine-tuning for models that
    consistently underperform or show areas for improvement.
    """
    print("Analyzing performance logs for fine-tuning opportunities...")
    
    # This is a very simplified analysis.
    # In a real system, this would involve:
    # 1. Parsing all recent logs.
    # 2. Aggregating success/failure rates per model/role.
    # 3. Identifying specific failure patterns or common errors from 'details'.
    # 4. Generating candidate fine-tuning datasets from failures or human corrections.
    # 5. Using an LLM (e.g., llama-architect) to propose a fine-tuning strategy.

    underperforming_models = {} # model_name -> failure_count
    
    for log_file in os.listdir(PERFORMANCE_LOG_DIR):
        if log_file.endswith(".jsonl"):
            file_path = os.path.join(PERFORMANCE_LOG_DIR, log_file)
            with open(file_path, "r") as f:
                for line in f:
                    log_entry = json.loads(line)
                    if not log_entry["success"]:
                        model_name = log_entry["model_name"]
                        underperforming_models[model_name] = underperforming_models.get(model_name, 0) + 1
    
    proposals = []
    for model, failures in underperforming_models.items():
        if failures > 5: # Threshold for proposing fine-tuning
            proposal = {
                "model_name": model,
                "reason": f"High number of failures ({failures}) detected.",
                "proposed_action": "Generate fine-tuning dataset from failures and fine-tune model."
            }
            proposals.append(proposal)
    
    if not proposals:
        print("No models identified for fine-tuning based on current logs.")
        return {"status": "no_fine_tuning_needed"}

    print(f"Proposing fine-tuning for: {[p['model_name'] for p in proposals]}")
    # Here, a dedicated 'fine-tuning-orchestrator' agent could take over
    # For now, we simulate.

    # Example: Llama-Architect proposes a fine-tuning plan for one model
    if proposals:
        target_model = proposals[0]["model_name"]
        architect_role = _ALL_MODELS.get("llama-architect", "Advanced architect for system design and optimization.")
        fine_tuning_plan = await _CLIENT.chat.completions.create(
            model="llama-architect", # Use architect for strategy
            messages=[
                {"role": "system", "content": f"You are {architect_role}. Propose a detailed fine-tuning plan for model {target_model} based on its observed failures. Include: 1) data collection strategy, 2) desired outcomes, 3) metrics for success. Output JSON."},
                {"role": "user", "content": f"Model: {target_model}\nFailure reason: {proposals[0]['reason']}\nRaw logs (sample relevant parts from PERFORMANCE_LOG_DIR): ..."} # In reality, extract relevant logs
            ],
            response_format={"type": "json_object"},
            temperature=0.3
        )
        print(f"Llama-Architect proposed fine-tuning plan for {target_model}:\n{fine_tuning_plan.choices[0].message.content}")

        # Simulate fine-tuning and update the model mapping
        # For a real system, you'd call a fine-tuning API (e.g., OpenAI, LiteLLM with custom backend)
        # and get a new model ID.
        new_model_version_id = f"{target_model}-ft-v{datetime.now().strftime('%Y%m%d%H%M')}"
        fine_tuned_models_map = _load_fine_tuned_models()
        fine_tuned_models_map[target_model] = new_model_version_id
        _save_fine_tuned_models(fine_tuned_models_map)
        
        return {"status": "fine_tuning_proposed_and_simulated", "model": target_model, "new_version": new_model_version_id, "plan": json.loads(fine_tuning_plan.choices[0].message.content)}
    
    return {"status": "analysis_complete"}


# Optional: Background task for continuous analysis
async def start_continuous_self_evolution_loop(interval_seconds: int = 3600): # Hourly check
    """Starts a continuous loop for analyzing and proposing fine-tuning."""
    while True:
        print(f"[{datetime.now().isoformat()}] Running continuous self-evolution analysis...")
        await analyze_and_propose_fine_tuning()
        await asyncio.sleep(interval_seconds) # Wait for the next interval
