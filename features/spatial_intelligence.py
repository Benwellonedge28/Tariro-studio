import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List

# --- Configuration & Shared Data (initialized from studio_v3.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Model names and their base roles
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module

SPATIAL_OUTPUT_DIR: str = ""

def initialize_spatial_intelligence(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any):
    """Initializes global configurations for Spatial Intelligence."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, SPATIAL_OUTPUT_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module

    SPATIAL_OUTPUT_DIR = os.path.join(_WORKSPACE, "spatial_data")
    os.makedirs(SPATIAL_OUTPUT_DIR, exist_ok=True)
    print(f"Spatial Intelligence initialized. Outputs: {SPATIAL_OUTPUT_DIR}")


async def _call_spatial_llm(model: str, role: str, prompt: str, task_id: str, context: str = "", response_format_type: str = "json_object") -> Dict[str, Any]:
    """Helper to call LLM for spatial analysis related tasks."""
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in spatial_intelligence.")
    if model not in _ALL_MODELS:
        return {"error": f"Model {model} not found in _ALL_MODELS.", "model": model}

    await _SWARM_VISUALIZER.log_event(
        task_id, "spatial_llm_call_start", f"{model} starting spatial task: {prompt[:50]}...",
        {"model": model, "prompt_summary": prompt[:100]},
        model_name=model, agent_role=role
    )

    try:
        messages = [
            {"role": "system", "content": f"You are {model}. Role: {role}. Your output format is strict. Output {response_format_type} only. Focus on accurate spatial descriptions and data."},
            {"role": "user", "content": f"Prompt: {prompt}\nContext:\n{context}"}
        ]
        
        resp = await _CLIENT.chat.completions.create(
            model=model,
            messages=messages,
            response_format={"type": response_format_type},
            temperature=0.1
        )
        content = resp.choices[0].message.content
        
        if response_format_type == "json_object":
            out = json.loads(content)
        else:
            out = {"content": content}
        out["model"] = model

        await _SWARM_VISUALIZER.log_event(
            task_id, "spatial_llm_call_end", f"{model} completed spatial task.",
            {"model": model, "response_summary": content[:100]},
            model_name=model, agent_role=role
        )
        return out
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "spatial_llm_error", f"JSON decode error from {model} for spatial task.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "raw_content": content, "model": model}
    except Exception as e:
        error_details = {"error": str(e), "prompt_summary": prompt[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "spatial_llm_error", f"Error calling {model} for spatial task.", error_details, model_name=model, agent_role=role, level="ERROR")
        return {"error": str(e), "model": model}


async def perform_geographic_search(task_id: str, query: str, model_caller: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates a geographic search and provides spatial analysis.
    """
    print(f"Performing geographic search for: {query}")
    prompt = f"Provide a detailed geographic analysis for '{query}'. Include: major landmarks, terrain, climate, and notable features. Also suggest a central lat/long and a few points of interest with descriptions. Output JSON: {{'location_name': str, 'summary': str, 'center_lat': float, 'center_lon': float, 'points_of_interest': list[dict]}}"
    
    result = await _call_spatial_llm(
        model_caller,
        _ALL_MODELS[model_caller],
        prompt,
        task_id,
        context=f"Request initiated by {model_caller} for query: {query}"
    )
    
    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    # Simulate saving this analysis
    output_filename = os.path.join(SPATIAL_OUTPUT_DIR, f"geo_analysis_{datetime.now().strftime('%Y%m%d%H%M%S')}.json")
    with open(output_filename, "w") as f:
        json.dump(result, f, indent=2)
    result["saved_path"] = output_filename
    result["status"] = "success"
    print(f"Geographic analysis saved to {output_filename}")
    return result


async def analyze_image_spatially(task_id: str, image_description: str, analysis_type: str = "layout", model_caller: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates spatial analysis of an image based on its description.
    Analysis types: "layout", "depth", "objects", "navigation".
    """
    print(f"Analyzing image spatially for: {image_description[:50]} (type: {analysis_type})")
    
    analysis_prompts = {
        "layout": "Describe the spatial layout: how is space organized, foreground vs background, object relative positions?",
        "depth": "Analyze depth and distance: near/far relationships, depth cues, estimated distances.",
        "objects": "List all objects, their estimated spatial positions (e.g., top-left, center), and relative placements.",
        "navigation": "Describe possible navigation paths, obstacles, open spaces, and directionality if moving through this scene."
    }
    
    specific_prompt = analysis_prompts.get(analysis_type, analysis_prompts["layout"])
    prompt = f"Perform a detailed spatial analysis of an image described as: '{image_description}'. {specific_prompt} Be specific, use spatial vocabulary, and respond as natural language text."
    
    result = await _call_spatial_llm(
        model_caller,
        _ALL_MODELS[model_caller],
        prompt,
        task_id,
        context=f"Image spatial analysis requested by {model_caller} for description: {image_description[:100]}",
        response_format_type="text" # Expecting natural language description
    )
    
    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    # Simulate saving this analysis
    output_filename = os.path.join(SPATIAL_OUTPUT_DIR, f"image_spatial_analysis_{datetime.now().strftime('%Y%m%d%H%M%S')}_{analysis_type}.txt")
    with open(output_filename, "w") as f:
        f.write(result["content"])
    result["saved_path"] = output_filename
    result["status"] = "success"
    print(f"Image spatial analysis saved to {output_filename}")
    return result


async def generate_knowledge_graph(task_id: str, seed_entities: List[str], model_caller: str = "llama-architect") -> Dict[str, Any]:
    """
    Simulates generating a knowledge graph from existing Studio entities (or conceptual seed entities).
    """
    print(f"Generating knowledge graph from seed entities: {', '.join(seed_entities)}")
    # In a real system, this would query Qdrant, Memory, Goals, etc.
    # For simulation, we'll ask LLM to synthesize a conceptual graph.
    
    prompt = f"Generate a conceptual knowledge graph (nodes and edges) for the following seed entities: {', '.join(seed_entities)}. Focus on semantic relationships, dependencies, and connections. Nodes should have 'id', 'label', 'type' (e.g., 'task', 'goal', 'file'), 'description'. Edges should have 'source', 'target', 'relation'. Output JSON: {{'nodes': list[dict], 'edges': list[dict], 'summary': str}}."
    
    result = await _call_spatial_llm(
        model_caller,
        _ALL_MODELS[model_caller],
        prompt,
        task_id,
        context=f"Knowledge graph generation requested by {model_caller} for: {', '.join(seed_entities)}"
    )
    
    if "error" in result:
        return {"status": "failed", "reason": result["error"]}
    
    # Simulate saving this analysis
    output_filename = os.path.join(SPATIAL_OUTPUT_DIR, f"knowledge_graph_{datetime.now().strftime('%Y%m%d%H%M%S')}.json")
    with open(output_filename, "w") as f:
        json.dump(result, f, indent=2)
    result["saved_path"] = output_filename
    result["status"] = "success"
    print(f"Knowledge graph saved to {output_filename}")
    return result
