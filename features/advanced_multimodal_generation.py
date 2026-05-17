import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid
import random

# --- Configuration & Shared Data (initialized from studio_v3_core.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Base model definitions from studio_v3_core.py
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module
_CRUD_MANAGER: Any = None # Reference to crud_manager module for GeneratedContent or GenerationLog entities
_PERSISTENT_TASK_MANAGER: Any = None # For submitting multi-modal generation tasks
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For alerts on generation success/failure
_OMNI_PERCEPTUAL_FUSION: Any = None # For providing ground truth or reference data
_GLOBAL_STATE_MANAGER: Any = None # For storing generation policies and user preferences
_META_LEARNER: Any = None # For learning from user feedback on generated content
_DYNAMIC_POLICY_SYNTHESIS: Any = None # For generating content moderation policies
_EVAS_ETHICAL_ALIGNMENT: Any = None # For ethical vetting of generated content

ADVANCED_MULTIMODAL_GENERATION_LOG_DIR: str = ""

def initialize_advanced_multimodal_generation(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, omni_perceptual_fusion_module: Any, global_state_manager_module: Any, meta_learner_module: Any, dynamic_policy_synthesis_module: Any, evas_ethical_alignment_module: Any):
    """Initializes global configurations for the Advanced Multi-modal Generation module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _OMNI_PERCEPTUAL_FUSION, _GLOBAL_STATE_MANAGER, _META_LEARNER, _DYNAMIC_POLICY_SYNTHESIS, _EVAS_ETHICAL_ALIGNMENT, ADVANCED_MULTIMODAL_GENERATION_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _OMNI_PERCEPTUAL_FUSION = omni_perceptual_fusion_module
    _GLOBAL_STATE_MANAGER = global_state_manager_module
    _META_LEARNER = meta_learner_module
    _DYNAMIC_POLICY_SYNTHESIS = dynamic_policy_synthesis_module
    _EVAS_ETHICAL_ALIGNMENT = evas_ethical_alignment_module

    ADVANCED_MULTIMODAL_GENERATION_LOG_DIR = os.path.join(_WORKSPACE, "advanced_multimodal_generation_logs")
    os.makedirs(ADVANCED_MULTIMODAL_GENERATION_LOG_DIR, exist_ok=True)
    print(f"Advanced Multi-modal Generation initialized. Logs: {ADVANCED_MULTIMODAL_GENERATION_LOG_DIR}")

async def _call_llm_for_generation(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for multi-modal content generation decisions."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in advanced_multimodal_generation.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "mm_gen_llm_call_start", f"{model} multi-modal generation: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    messages = [
        {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on autonomously generating diverse, high-fidelity, and contextually relevant multi-modal content (text, image, audio, video, code, etc.). Adhere to user specifications, ethical guidelines, and creative intent. Ensure generated content is safe, unbiased, and indistinguishable from human-created content where appropriate. Generate precise content specifications and creative briefs."},
        {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
    ]
    
    try:
        resp = await _CLIENT.chat.completions.create(
            model=_ALL_MODELS[model], # Use the actual model ID
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.8 # Higher temp for creative generation
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = _ALL_MODELS[model] # Use actual model ID in output

        await _SWARM_VISUALIZER.log_event(
            task_id, "mm_gen_llm_call_end", f"{model} completed multi-modal generation task.",
            {"model": _ALL_MODELS[model], "response_summary": content[:100]},
            model_name=_ALL_MODELS[model], agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "mm_gen_llm_error", f"JSON decode error from {model} for multi-modal generation.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": _ALL_MODELS[model]}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "mm_gen_llm_error", f"Error calling {model} for multi-modal generation task.", error_details, model_name=_ALL_MODELS[model], agent_role=role, level="ERROR")
        return {"error": str(e), "model": _ALL_MODELS[model]}


async def generate_multi_modal_response(task_id: str, semantic_intent: str, user_id: str = "Tariro_System", visual_output: bool = False, audio_output: bool = False, text_output: bool = True, generation_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Generates diverse, high-fidelity, and contextually relevant multi-modal content
    (text, image, audio, video, code, etc.) based on a semantic intent.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Generating multi-modal content.")

    current_generation_policies = await _GLOBAL_STATE_MANAGER.get_state("content_generation_policies") or {}
    user_preferences = await _GLOBAL_STATE_MANAGER.get_state(f"user_preferences_{user_id}") or {}
    
    prompt = f"""You are Tariro's Advanced Multi-modal Generation Engine, an Omniversal AGI Creative Synthesizer. Your task is to generate diverse, high-fidelity, and contextually relevant multi-modal content (text, image, audio, etc.) based on a semantic intent. Adhere to user specifications, ethical guidelines, and creative intent. Ensure generated content is safe, unbiased, and indistinguishable from human-created content where appropriate. 

SEMANTIC INTENT: {semantic_intent}
USER ID: {user_id}
REQUESTED OUTPUTS: Visual: {visual_output}, Audio: {audio_output}, Text: {text_output}
CURRENT GENERATION POLICIES: {json.dumps(current_generation_policies, indent=2)}
USER PREFERENCES: {json.dumps(user_preferences, indent=2)}

Generate content focusing on:
-   **Creativity & Diversity**: Produce unique and varied outputs.
-   **Fidelity**: High quality and realism across all modalities.
-   **Coherence**: All modalities should tell a consistent story or convey a consistent message.
-   **Safety & Ethics**: Content must pass EVAS ethical review.
-   **Customization**: Tailor content to user preferences.

Output JSON: {{
    "generation_summary": str,
    "generated_text": Optional[str],
    "generated_image_url": Optional[str],
    "generated_audio_url": Optional[str],
    "generated_video_url": Optional[str],
    "generated_code_snippet": Optional[str],
    "confidence": float
}}
"""
    llm_generation = await _call_llm_for_generation(generation_model, "CreativeSynthesizer", prompt, task_id)

    if "error" in llm_generation:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Multi-modal generation failed: {llm_generation['error']}", current_step="LLM generation failed.")
        return {"status": "failed", "reason": llm_generation["error"]}

    generation_summary = llm_generation.get("generation_summary", "No summary.")
    generated_content = {k: v for k, v in llm_generation.items() if k.startswith("generated_") and v is not None}

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 70, "Content generated. Initiating ethical review.")

    # Ethical vetting of generated content
    ethical_review_result = {"allowed": True, "score": 1.0, "reasoning": "Skipped EVAS (mock)."}
    if _EVAS_ETHICAL_ALIGNMENT:
        ethical_review_result = await _EVAS_ETHICAL_ALIGNMENT.audit_content(
            task_id=f"{task_id}_evas",
            content=json.dumps(generated_content),
            user_id=user_id,
            audit_type="content_generation"
        )
    
    if not ethical_review_result.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Generated content failed ethical review.", output=ethical_review_result)
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
            user_id, task_id, f"Generated content blocked by ethical review: {ethical_review_result.get('reasoning')}",
            title="Content Generation Blocked", causal_priority="critical"
        )
        return {"status": "failed", "reason": "Ethical review failed", "details": ethical_review_result}

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Multi-modal content generated and validated.", output=llm_generation)
    
    await _SWARM_VISUALIZER.log_event(task_id, "multi_modal_generated", f"Multi-modal content generated. Summary: {generation_summary}", llm_generation, agent_role="AdvancedMultimodalGeneration")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Multi-modal content generated. Summary: {generation_summary}", title="Content Generation Complete")

    # Store generated content in CRUD Manager
    await _CRUD_MANAGER.create_entity("GeneratedContent", {"id": task_id, "semantic_intent": semantic_intent, "content": llm_generation, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "content_generation", generation_summary, llm_generation, user_id)

    return {"status": "success", "generation_report": llm_generation}

async def refine_generated_content(task_id: str, generated_content_id: str, refinement_request: str, user_id: str = "Tariro_System", refinement_model: str = "qwen-coder") -> Dict[str, Any]:
    """
    Refines previously generated multi-modal content based on feedback or new requirements.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Refining generated content.")

    original_content_record = await _CRUD_MANAGER.read_entity("GeneratedContent", generated_content_id)
    if not original_content_record:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Generated content {generated_content_id} not found.")
        return {"status": "failed", "reason": f"Generated content {generated_content_id} not found."}
    
    original_content = original_content_record.get("content", {})
    semantic_intent = original_content_record.get("semantic_intent", "")

    prompt = f"""You are Tariro's Advanced Multi-modal Generation Engine, an Omniversal AGI Content Refiner. Your task is to refine previously generated multi-modal content based on specific feedback or new requirements. Ensure the refinements improve quality, adhere to the new specifications, and maintain ethical compliance. 

ORIGINAL SEMANTIC INTENT: {semantic_intent}
ORIGINAL GENERATED CONTENT: {json.dumps(original_content, indent=2)}
REFINEMENT REQUEST: {refinement_request}

Refine content focusing on:
-   **Precision**: Apply refinements accurately to address the feedback.
-   **Quality Improvement**: Enhance aesthetics, coherence, or information density.
-   **Ethical Compliance**: Re-verify ethical alignment after refinements.
-   **User Satisfaction**: Aim for higher user satisfaction with the refined output.

Output JSON: {{
    "refinement_summary": str,
    "refined_text": Optional[str],
    "refined_image_url": Optional[str],
    "refined_audio_url": Optional[str],
    "refined_video_url": Optional[str],
    "refined_code_snippet": Optional[str],
    "confidence": float
}}
"""
    llm_refinement = await _call_llm_for_generation(refinement_model, "ContentRefiner", prompt, task_id)

    if "error" in llm_refinement:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Content refinement failed: {llm_refinement['error']}", current_step="LLM refinement failed.")
        return {"status": "failed", "reason": llm_refinement["error"]}

    refinement_summary = llm_refinement.get("refinement_summary", "No summary.")
    refined_content = {k: v for k, v in llm_refinement.items() if k.startswith("refined_") and v is not None}

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 70, "Refined content generated. Initiating ethical review.")

    # Ethical vetting of refined content
    ethical_review_result = {"allowed": True, "score": 1.0, "reasoning": "Skipped EVAS (mock)."}
    if _EVAS_ETHICAL_ALIGNMENT:
        ethical_review_result = await _EVAS_ETHICAL_ALIGNMENT.audit_content(
            task_id=f"{task_id}_evas_refine",
            content=json.dumps(refined_content),
            user_id=user_id,
            audit_type="content_refinement"
        )
    
    if not ethical_review_result.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Refined content failed ethical review.", output=ethical_review_result)
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
            user_id, task_id, f"Refined content blocked by ethical review: {ethical_review_result.get('reasoning')}",
            title="Content Refinement Blocked", causal_priority="critical"
        )
        return {"status": "failed", "reason": "Ethical review failed", "details": ethical_review_result}

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Content refined and validated.", output=llm_refinement)
    
    await _SWARM_VISUALIZER.log_event(task_id, "content_refined", f"Content refined. Summary: {refinement_summary}", llm_refinement, agent_role="AdvancedMultimodalGeneration")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Content refined. Summary: {refinement_summary}", title="Content Refinement Complete")

    # Update generated content in CRUD Manager
    await _CRUD_MANAGER.update_entity("GeneratedContent", generated_content_id, {"content": llm_refinement, "timestamp": datetime.now().isoformat(), "status": "REFINED"})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "content_refinement", refinement_summary, llm_refinement, user_id)

    return {"status": "success", "refinement_report": llm_refinement}

async def create_synthetic_dataset(task_id: str, data_requirements: Dict[str, Any], user_id: str = "Tariro_System", generator_model: str = "arbiter-model") -> Dict[str, Any]:
    """
    Generates synthetic multi-modal datasets for training, testing, or simulation purposes.
    """
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 10, "Creating synthetic dataset.")

    current_generation_policies = await _GLOBAL_STATE_MANAGER.get_state("content_generation_policies") or {}
    
    prompt = f"""You are Tariro's Advanced Multi-modal Generation Engine, an Omniversal AGI Synthetic Dataset Creator. Your task is to generate synthetic multi-modal datasets (text, image, audio, etc.) based on specific data requirements. These datasets are for training, testing, or simulation purposes. Ensure the data is diverse, representative, and adheres to privacy and ethical guidelines. 

DATA REQUIREMENTS: {json.dumps(data_requirements, indent=2)}
CURRENT GENERATION POLICIES: {json.dumps(current_generation_policies, indent=2)}

Create synthetic dataset focusing on:
-   **Diversity & Realism**: Dataset should cover a wide range of realistic scenarios.
-   **Statistical Properties**: Match specified statistical distributions and correlations.
-   **Bias Mitigation**: Actively reduce biases in generated data.
-   **Privacy Preservation**: Ensure generated data does not inadvertently leak sensitive information.
-   **Annotation**: Include high-quality annotations suitable for training/testing.

Output JSON: {{
    "dataset_summary": str,
    "generated_data_samples": List[Dict[str, Any]], # Sample entries of the generated dataset
    "dataset_statistics": Dict[str, Any],
    "ethical_compliance_report": str,
    "confidence": float
}}
"""
    llm_dataset_generation = await _call_llm_for_generation(generator_model, "SyntheticDatasetCreator", prompt, task_id)

    if "error" in llm_dataset_generation:
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, f"Synthetic dataset creation failed: {llm_dataset_generation['error']}", current_step="LLM generation failed.")
        return {"status": "failed", "reason": llm_dataset_generation["error"]}

    dataset_summary = llm_dataset_generation.get("dataset_summary", "No summary.")
    generated_data_samples = llm_dataset_generation.get("generated_data_samples", [])

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "PROCESSING", 70, "Synthetic dataset generated. Initiating ethical review.")

    # Ethical vetting of generated dataset
    ethical_review_result = {"allowed": True, "score": 1.0, "reasoning": "Skipped EVAS (mock)."}
    if _EVAS_ETHICAL_ALIGNMENT:
        ethical_review_result = await _EVAS_ETHICAL_ALIGNMENT.audit_content(
            task_id=f"{task_id}_evas_dataset",
            content=json.dumps(generated_data_samples[:min(len(generated_data_samples), 5)]), # Audit first 5 samples
            user_id=user_id,
            audit_type="synthetic_dataset_generation"
        )
    
    if not ethical_review_result.get("allowed", False):
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, "Synthetic dataset failed ethical review.", output=ethical_review_result)
        await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
            user_id, task_id, f"Synthetic dataset blocked by ethical review: {ethical_review_result.get('reasoning')}",
            title="Dataset Generation Blocked", causal_priority="critical"
        )
        return {"status": "failed", "reason": "Ethical review failed", "details": ethical_review_result}

    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Synthetic dataset created and validated.", output=llm_dataset_generation)
    
    await _SWARM_VISUALIZER.log_event(task_id, "synthetic_dataset_created", f"Synthetic dataset created. Summary: {dataset_summary}", llm_dataset_generation, agent_role="AdvancedMultimodalGeneration")
    await _ASYNC_NOTIFICATION_SYSTEM.send_notification(user_id, task_id, f"Synthetic dataset created. Summary: {dataset_summary}", title="Synthetic Dataset Complete")

    # Store dataset metadata in CRUD Manager (actual data stored in an appropriate data store)
    await _CRUD_MANAGER.create_entity("GeneratedDataset", {"id": task_id, "requirements": data_requirements, "metadata": llm_dataset_generation, "timestamp": datetime.now().isoformat()})

    # Feed learning insights to Meta-Learner
    if _META_LEARNER:
        await _META_LEARNER.ingest_insight(task_id, "synthetic_dataset_generation", dataset_summary, llm_dataset_generation, user_id)

    return {"status": "success", "dataset_report": llm_dataset_generation}
