import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid

# --- Configuration & Shared Data (initialized from studio_v3.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Base model definitions from studio_v3.py
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module

MEMORY_DATA_DIR: str = ""

def initialize_contextual_memory(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any):
    """Initializes global configurations for Contextual Memory."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, MEMORY_DATA_DIR
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module

    MEMORY_DATA_DIR = os.path.join(_WORKSPACE, "contextual_memory_data")
    os.makedirs(MEMORY_DATA_DIR, exist_ok=True)
    print(f"Contextual Memory initialized. Memory data: {MEMORY_DATA_DIR}")

def _get_memory_file_path(task_id: str) -> str:
    """Returns the file path for memories of a given task ID."""
    return os.path.join(MEMORY_DATA_DIR, f"task_{task_id}.json")

def _load_task_memories(task_id: str) -> List[Dict[str, Any]]:
    """Loads all memories for a given task ID."""
    file_path = _get_memory_file_path(task_id)
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return [] # Return empty list if file is corrupted
    return []

def _save_task_memories(task_id: str, memories: List[Dict[str, Any]]):
    """Saves all memories for a given task ID."""
    file_path = _get_memory_file_path(task_id)
    with open(file_path, "w") as f:
        json.dump(memories, f, indent=2)

async def store_memory(task_id: str, agent_name: str, key: str, value: Any, description: str):
    """Stores a piece of contextual memory for a given task."""
    memories = _load_task_memories(task_id)
    timestamp = datetime.now().isoformat()
    memory_entry = {
        "timestamp": timestamp,
        "agent_name": agent_name,
        "key": key,
        "value": value,
        "description": description
    }
    memories.append(memory_entry)
    _save_task_memories(task_id, memories)

    await _SWARM_VISUALIZER.log_event(
        task_id, "memory_store", f"Agent {agent_name} stored memory: {key}",
        {"agent": agent_name, "key": key, "description": description, "value_summary": str(value)[:100]},
        model_name=agent_name, agent_role=_ALL_MODELS.get(agent_name, "Unknown")
    )
    print(f"[{agent_name}] Stored memory '{key}' for task {task_id}")

async def retrieve_memory(task_id: str, key: str) -> Optional[Any]:
    """Retrieves the latest value for a specific memory key for a given task."""
    memories = _load_task_memories(task_id)
    # Return the most recent entry for the key
    for entry in reversed(memories):
        if entry["key"] == key:
            await _SWARM_VISUALIZER.log_event(
                task_id, "memory_retrieve", f"Retrieved memory: {key}",
                {"key": key, "value_summary": str(entry["value"])[:100]},
                model_name="system", agent_role="orchestrator"
            )
            return entry["value"]
    return None

async def query_memory_rag(task_id: str, query: str, agent_name: str, rag_model: str = "llama-architect") -> Dict[str, Any]:
    """
    Performs a RAG query over all stored memories for a task, synthesizing a coherent answer.
    """
    if _CLIENT is None:
        raise ValueError("OpenAI client not initialized in contextual_memory.")
    if rag_model not in _ALL_MODELS:
        return {"error": f"RAG model {rag_model} not found in _ALL_MODELS.", "model": rag_model}

    memories = _load_task_memories(task_id)
    if not memories:
        return {"response": "No relevant context found in memory.", "sources": []}

    # Prepare context for the RAG model
    context_str = "\n".join([f"[{m['agent_name']}/{m['key']} @ {m['timestamp']}] {m['description']}: {m['value']}" for m in memories])
    
    rag_prompt = f"""You are a highly capable RAG system. Based on the following contextual memories for a task, answer the user's query.
    
Contextual Memories:
---
{context_str}
---

User Query from {agent_name}: "{query}"

Synthesize a concise and accurate answer, citing the memory keys used as sources. If the information is not directly available, state that.
Output JSON: {{'response': str, 'sources': list[str] (memory keys)}}
"""
    await _SWARM_VISUALIZER.log_event(
        task_id, "memory_rag_query", f"Agent {agent_name} querying contextual memory: {query[:50]}",
        {"agent": agent_name, "query": query, "rag_model": rag_model},
        model_name=agent_name, agent_role=_ALL_MODELS.get(agent_name, "Unknown")
    )

    try:
        resp = await _CLIENT.chat.completions.create(
            model=rag_model,
            messages=[
                {"role": "system", "content": f"You are {rag_model}. Role: {_ALL_MODELS.get(rag_model, 'RAG Processor')}. Output JSON only."},
                {"role": "user", "content": rag_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.1
        )
        content = resp.choices[0].message.content
        out = json.loads(content)
        await _SWARM_VISUALIZER.log_event(
            task_id, "memory_rag_response", f"RAG query answered for {agent_name}: {query[:50]}",
            {"response_summary": out.get("response", "")[:100], "sources": out.get("sources", [])},
            model_name=rag_model, agent_role=_ALL_MODELS.get(rag_model, "RAG Processor")
        )
        return {"response": out.get("response"), "sources": out.get("sources", []), "model": rag_model}
    except json.JSONDecodeError as e:
        error_details = {"error": f"JSON decode error: {e}", "raw_content": content[:500]}
        await _SWARM_VISUALIZER.log_event(task_id, "memory_rag_error", f"RAG model {rag_model} JSON decode error.", error_details, model_name=rag_model, agent_role=_ALL_MODELS.get(rag_model, "RAG Processor"), level="ERROR")
        return {"error": str(e), "response": "Error processing RAG query.", "model": rag_model}
    except Exception as e:
        error_details = {"error": str(e), "query_summary": query[:100]}
        await _SWARM_VISUALIZER.log_event(task_id, "memory_rag_error", f"RAG model {rag_model} general error.", error_details, model_name=rag_model, agent_role=_ALL_MODELS.get(rag_model, "RAG Processor"), level="ERROR")
        return {"error": str(e), "response": "Error processing RAG query.", "model": rag_model}


def get_all_memories(task_id: str) -> List[Dict[str, Any]]:
    """Retrieves all stored memory entries for a specific task."""
    return _load_task_memories(task_id)

def clear_task_memory(task_id: str):
    """Clears all memories for a given task ID."""
    file_path = _get_memory_file_path(task_id)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Cleared all memories for task {task_id}")
    else:
        print(f"No memories found for task {task_id} to clear.")
