import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import random
import uuid

# --- Configuration & Shared Data (initialized from studio_v3.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Base model definitions from studio_v3.py
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module
_CONTEXTUAL_MEMORY: Any = None # Reference to contextual_memory module
_MULTIMODAL_COLLABORATION: Any = None # Reference to multimodal_collaboration module

ADVANCED_MULTIMODAL_OUTPUT_DIR: str = ""

def initialize_advanced_multimodal_generation(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, contextual_memory_module: Any, multimodal_collaboration_module: Any):
    """Initializes global configurations for Advanced Multi-Modal Storytelling."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CONTEXTUAL_MEMORY, _MULTIMODAL_COLLABORATION, ADVANCED_MULTIMODAL_OUTPUT_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CONTEXTUAL_MEMORY = contextual_memory_module
    _MULTIMODAL_COLLABORATION = multimodal_collaboration_module

    ADVANCED_MULTIMODAL_OUTPUT_DIR = os.path.join(_WORKSPACE, "advanced_multimodal_outputs")
    os.makedirs(ADVANCED_MULTIMODAL_OUTPUT_DIR, exist_ok=True)
    print(f"Advanced Multi-Modal Generation initialized. Outputs: {ADVANCED_MULTIMODAL_OUTPUT_DIR}")

async def _call_llm_for_story_generation(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for story/world generation tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in advanced_multimodal_generation.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "adv_mm_llm_call_start", f"{model} evaluating advanced multi-modal task: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    try:
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on creative, coherent, and interlinked multi-modal content generation."},
            {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
        ]
        
        resp = await _CLIENT.chat.completions.create(
            model=model,
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.7 # Higher temperature for creative tasks
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = model

        await _SWARM_VISUALIZER.log_event(
            task_id, "adv_mm_llm_call_end", f"{model} completed advanced multi-modal task.",
            {"model": model, "response_summary": content[:100]},
            model_name=model, agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "adv_mm_llm_error", f"JSON decode error from {model} for advanced multi-modal.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": model}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "adv_mm_llm_error", f"Error calling {model} for advanced multi-modal.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model}

async def generate_story_arc(task_id: str, theme: str, characters: str, setting: str, generator_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Generates a high-level story arc or narrative outline.
    """
    print(f"Generating story arc for theme '{theme[:50]}'...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "story_arc_gen_start", f"AGI ({generator_model}) generating story arc.",
        {"theme": theme, "characters": characters, "setting": setting}, model_name=generator_model, agent_role=_ALL_MODELS.get(generator_model, "Storyteller")
    )

    prompt = f"""You are a master storyteller. Create a concise yet compelling story arc (outline) based on the following inputs:
    Theme: {theme}
    Main Characters: {characters}
    Setting: {setting}
    
    The story arc should include:
    - Logline (1-2 sentences)
    - Key Plot Points (3-5 bullet points)
    - Tonal/Mood Description
    - Suggestions for key visual elements (for image generation)
    - Suggestions for key audio elements (for audio generation)
    
    Output JSON: {{'logline': str, 'plot_points': list[str], 'mood': str, 'visual_suggestions': list[str], 'audio_suggestions': list[str]}}
    """
    
    result = await _call_llm_for_story_generation(
        generator_model,
        _ALL_MODELS.get(generator_model, "Storyteller"),
        prompt,
        task_id
    )

    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    log_filename = os.path.join(ADVANCED_MULTIMODAL_OUTPUT_DIR, f"story_arc_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump(result, f, indent=2)
    result["saved_path"] = log_filename
    result["status"] = "success"
    print(f"Story arc saved to {log_filename}")

    await _CONTEXTUAL_MEMORY.store_memory(task_id, generator_model, "story_arc_generated", result, "Generated story arc outline.")
    
    return result

async def generate_world_elements(task_id: str, story_arc: Dict[str, Any], world_generator_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Generates interconnected multi-modal assets based on a story arc.
    """
    print(f"Generating multi-modal world elements for story: {story_arc.get('logline', '')[:50]}...")
    await _SWARM_VISUALIZER.log_event(
        task_id, "world_elements_gen_start", f"AGI ({world_generator_model}) generating world elements.",
        {"story_logline": story_arc.get('logline', '')[:100]}, model_name=world_generator_model, agent_role=_ALL_MODELS.get(world_generator_model, "World Builder")
    )

    generated_assets = []

    # Use visual suggestions to generate images
    for visual_prompt in story_arc.get("visual_suggestions", []):
        image_gen_result = await _MULTIMODAL_COLLABORATION.generate_multimodal_asset(
            task_id, "image", visual_prompt, "dalle-image-gen", f"Part of story: {story_arc.get('logline', '')}"
        )
        if image_gen_result["status"] == "VALIDATED":
            generated_assets.append({"type": "image", "prompt": visual_prompt, "path": image_gen_result["path"]})
            await _CONTEXTUAL_MEMORY.store_memory(task_id, "dalle-image-gen", f"image_for_story_{uuid.uuid4()}", image_gen_result["path"], f"Generated image for story element: {visual_prompt}")
        else:
            await _SWARM_VISUALIZER.log_event(task_id, "world_elements_gen_fail", f"Image generation failed for: {visual_prompt}", image_gen_result, level="ERROR")

    # Use audio suggestions to generate audio
    for audio_prompt in story_arc.get("audio_suggestions", []):
        audio_gen_result = await _MULTIMODAL_COLLABORATION.generate_multimodal_asset(
            task_id, "audio", audio_prompt, "musicgen-audio-gen", f"Part of story: {story_arc.get('logline', '')}"
        )
        if audio_gen_result["status"] == "VALIDATED":
            generated_assets.append({"type": "audio", "prompt": audio_prompt, "path": audio_gen_result["path"]})
            await _CONTEXTUAL_MEMORY.store_memory(task_id, "musicgen-audio-gen", f"audio_for_story_{uuid.uuid4()}", audio_gen_result["path"], f"Generated audio for story element: {audio_prompt}")
        else:
            await _SWARM_VISUALIZER.log_event(task_id, "world_elements_gen_fail", f"Audio generation failed for: {audio_prompt}", audio_gen_result, level="ERROR")
    
    # Generate a descriptive text for the world/story
    text_prompt = f"""Based on the following story arc, write a detailed descriptive text (200-300 words) for the world or scene, weaving together visual and auditory elements.
    Story Arc: {json.dumps(story_arc, indent=2)}
    Generated Visual Elements: {json.dumps([a for a in generated_assets if a['type'] == 'image'], indent=2)}
    Generated Audio Elements: {json.dumps([a for a in generated_assets if a['type'] == 'audio'], indent=2)}
    """
    text_result = await _call_llm_for_story_generation(
        world_generator_model,
        _ALL_MODELS.get(world_generator_model, "World Builder"),
        text_prompt,
        task_id,
        response_format_type="text" # Expecting plain text
    )

    if "error" in text_result:
        return {"status": "failed", "reason": text_result["error"]}
    
    world_text = text_result.get("content", "No world description generated.")
    text_log_filename = os.path.join(ADVANCED_MULTIMODAL_OUTPUT_DIR, f"world_description_{task_id}_{datetime.now().strftime('%H%M%S')}.txt")
    with open(text_log_filename, "w") as f:
        f.write(world_text)
    generated_assets.append({"type": "text_description", "path": text_log_filename, "content_summary": world_text[:100]})
    await _CONTEXTUAL_MEMORY.store_memory(task_id, world_generator_model, "world_description", text_log_filename, "Path to generated world description.")


    log_filename = os.path.join(ADVANCED_MULTIMODAL_OUTPUT_DIR, f"world_elements_{task_id}_{datetime.now().strftime('%H%M%S')}.json")
    with open(log_filename, "w") as f:
        json.dump(generated_assets, f, indent=2)
    
    print(f"Multi-modal world elements generated and saved to {log_filename}")

    await _SWARM_VISUALIZER.log_event(
        task_id, "world_elements_gen_complete", f"Multi-modal world elements generated for story.",
        {"total_assets": len(generated_assets)}, model_name=world_generator_model, agent_role=_ALL_MODELS.get(world_generator_model, "World Builder")
    )
    
    return {"status": "success", "total_assets_generated": len(generated_assets), "assets_overview": generated_assets, "saved_path": log_filename}
