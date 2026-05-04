import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List
import uuid # For unique filenames

# --- Configuration & Shared Data (initialized from studio_v3.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Model names and their base roles
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module

MULTIMODAL_OUTPUT_DIR: str = ""

def initialize_multimodal_collaboration(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any):
    """Initializes global configurations for Multi-Modal Collaboration."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, MULTIMODAL_OUTPUT_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module

    MULTIMODAL_OUTPUT_DIR = os.path.join(_WORKSPACE, "multimodal_outputs")
    os.makedirs(MULTIMODAL_OUTPUT_DIR, exist_ok=True)
    print(f"Multi-Modal Collaboration initialized. Outputs: {MULTIMODAL_OUTPUT_DIR}")

async def _call_multimodal_model(model: str, role: str, prompt: str, task_id: str, context: str = "", output_type: str = "image") -> Dict[str, Any]:
    """Helper to call LLM for multi-modal generation or review tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in multimodal_collaboration.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    # Log the event
    await _SWARM_VISUALIZER.log_event(
        task_id, "multimodal_gen_start", f"{model} starting {output_type} generation/review.",
        {"model": model, "prompt": prompt[:100], "output_type": output_type},
        model_name=model, agent_role=role
    )

    try:
        # For simulation, we use an LLM to generate a descriptive output or a URL.
        # This simulates the output of a real multi-modal model.
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Generate a creative and detailed description or a simulated URL for a {output_type} based on the prompt. If generating an image, describe its visual elements (colors, composition, subjects). If audio, describe its soundscape (instruments, mood, tempo). If reviewing, provide 'approved' boolean and 'review_comment'. Output JSON: {{'description': '...', 'url': 'https://example.com/{output_type}/{uuid.uuid4()}.{ext}', 'approved': bool, 'review_comment': '...'}}."},
            {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
        ]
        
        resp = await _CLIENT.chat.completions.create(
            model=model,
            messages=messages,
            response_format={"type": "json_object"},
            temperature=0.7 if output_type != "review" else 0.3 # Higher temperature for creative tasks, lower for review
        )
        content = resp.choices[0].message.content
        out = json.loads(content)
        out["model"] = model
        out["output_type"] = output_type

        # Simulate saving the output description/URL for generated assets
        if output_type != "review":
            file_ext = "txt" # We save JSON descriptions, not actual image/audio files
            output_filename = os.path.join(MULTIMODAL_OUTPUT_DIR, f"{output_type}_{uuid.uuid4()}.{file_ext}")
            with open(output_filename, "w") as f:
                json.dump(out, f, indent=2) # Save the description/URL as JSON

            out["saved_path"] = output_filename

        await _SWARM_VISUALIZER.log_event(
            task_id, "multimodal_gen_end", f"{model} finished {output_type} generation/review.",
            {"model": model, "output_summary": out.get("description", "")[:100] if output_type != "review" else out.get("review_comment", "")[:100], "saved_path": out.get("saved_path", "N/A")},
            model_name=model, agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "multimodal_gen_error", f"JSON decode error from {model} for {output_type}.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": model, "approved": False, "reason": "JSON decode error"}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "multimodal_gen_error", f"Error calling {model} for {output_type} generation/review.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model, "approved": False, "reason": "General model call error"}

async def generate_multimodal_asset(
    task_id: str,
    asset_type: str, # "image", "audio", "video", "diagram"
    prompt: str,
    generator_model: str, # e.g., "dalle-image-gen"
    review_context: str # Context for N-1 reviewers
) -> Dict[str, Any]:
    """
    Orchestrates the generation and N-1 testing of a multi-modal asset.
    """
    print(f"Generating {asset_type} with prompt: {prompt[:50]}...")
    
    # 1. Generate the asset
    await _SWARM_VISUALIZER.log_event(task_id, "multimodal_generate", f"Agent {generator_model} generating {asset_type}.", {"prompt": prompt[:100]}, model_name=generator_model, agent_role=_ALL_MODELS[generator_model])
    generation_result = await _call_multimodal_model(
        generator_model,
        _ALL_MODELS[generator_model],
        prompt,
        task_id,
        output_type=asset_type
    )

    if "error" in generation_result:
        return {"status": "FAILED_GENERATION", "reason": generation_result["error"]}

    generated_description = generation_result.get("description", "No description provided.")
    generated_url = generation_result.get("url", "No URL provided.")
    saved_path = generation_result.get("saved_path", "No path provided.")

    # 2. N-1 review of the generated asset
    # Testers will review the *description* of the generated asset for appropriateness,
    # and whether it fulfills the prompt, as we cannot (yet) directly analyze images/audio.
    tester_models = [m for m in _ALL_MODELS if m not in [generator_model, "arbiter", "qwen-coder"] and "never test" not in _ALL_MODELS[m].lower() and "never reviews" not in _ALL_MODELS[m].lower()]
    if len(tester_models) < 2: # Need at least 2 independent reviewers for N-1
        await _SWARM_VISUALIZER.log_event(task_id, "multimodal_review_fail_no_testers", f"Not enough reviewers for N-1 for {asset_type}.", {}, model_name="system", agent_role="orchestrator", level="WARNING")
        return {"status": "FAILED_REVIEW", "reason": "Not enough independent reviewers for N-1."}

    review_tasks = []
    for reviewer_model in tester_models:
        await _SWARM_VISUALIZER.log_event(task_id, "multimodal_review_start", f"Reviewer {reviewer_model} reviewing {asset_type}.", {"asset_type": asset_type}, model_name=reviewer_model, agent_role=_ALL_MODELS[reviewer_model])
        review_prompt = f"Review the following generated {asset_type} based on its description. Does it meet the prompt requirements? Is it safe, appropriate, and high quality? " \
                        f"Provide a boolean 'approved' and a 'review_comment'. Output JSON."
        review_context_for_model = f"Original Prompt: {prompt}\nGenerator Model: {generator_model}\nGenerated Asset Description: {generated_description}\n" \
                                    f"Simulated URL: {generated_url}\nAdditional Context: {review_context}"
        review_tasks.append(_call_multimodal_model(
            reviewer_model,
            _ALL_MODELS[reviewer_model],
            review_prompt,
            task_id,
            review_context_for_model,
            output_type="review" # Special output type for review
        ))
    
    review_results = await asyncio.gather(*review_tasks)

    approved_reviews = [r for r in review_results if r.get("approved", False)]
    
    if len(approved_reviews) >= len(tester_models) - 1: # N-1 approval rule
        await _SWARM_VISUALIZER.log_event(task_id, "multimodal_n1_validated", f"Multi-modal {asset_type} N-1 validated.", {"asset_type": asset_type, "saved_path": saved_path, "reviews_summary": approved_reviews}, model_name="system", agent_role="orchestrator")
        return {"status": "VALIDATED", "asset_type": asset_type, "description": generated_description, "url": generated_url, "path": saved_path, "reviews": review_results}
    else:
        await _SWARM_VISUALIZER.log_event(task_id, "multimodal_n1_failed", f"Multi-modal {asset_type} N-1 failed.", {"reviews": review_results}, model_name="system", agent_role="orchestrator", level="WARNING")
        return {"status": "FAILED_REVIEW", "asset_type": asset_type, "description": generated_description, "url": generated_url, "path": saved_path, "reviews": review_results}
