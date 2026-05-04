import os
import json
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid

# --- Configuration & Shared Data (initialized from studio_v3.py) ---
_WORKSPACE: str = ""
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module

ENTITY_DATA_DIR: str = ""

def initialize_crud_manager(workspace_path: str, swarm_visualizer_module: Any):
    """Initializes global configurations for the CRUD Manager."""
    global _WORKSPACE, _SWARM_VISUALIZER, ENTITY_DATA_DIR
    _WORKSPACE = workspace_path
    _SWARM_VISUALIZER = swarm_visualizer_module

    ENTITY_DATA_DIR = os.path.join(_WORKSPACE, "entity_data")
    os.makedirs(ENTITY_DATA_DIR, exist_ok=True)
    print(f"CRUD Manager initialized. Entity data: {ENTITY_DATA_DIR}")

def _get_entity_file_path(entity_name: str) -> str:
    """Returns the file path for a given entity type."""
    return os.path.join(ENTITY_DATA_DIR, f"{entity_name.lower()}.json")

def _load_entities(entity_name: str) -> List[Dict[str, Any]]:
    """Loads all records for a given entity type."""
    file_path = _get_entity_file_path(entity_name)
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return [] # Return empty list if file is corrupted
    return []

def _save_entities(entity_name: str, entities: List[Dict[str, Any]]):
    """Saves all records for a given entity type."""
    file_path = _get_entity_file_path(entity_name)
    with open(file_path, "w") as f:
        json.dump(entities, f, indent=2)

async def create_entity(task_id: str, entity_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """Creates a new entity record."""
    entities = _load_entities(entity_name)
    new_id = str(uuid.uuid4())
    new_entity = {
        "id": new_id,
        "created_at": datetime.now().isoformat(),
        **data
    }
    entities.append(new_entity)
    _save_entities(entity_name, entities)

    await _SWARM_VISUALIZER.log_event(
        task_id, "crud_create", f"Created new {entity_name} record.",
        {"entity_name": entity_name, "id": new_id, "data_summary": json.dumps(data)[:100]},
        model_name="human", agent_role="user"
    )
    print(f"Created new {entity_name} with ID: {new_id}")
    return {"status": "success", "id": new_id, "entity": new_entity}

async def read_entities(task_id: str, entity_name: str, query: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    """Reads entity records, optionally filtered by query."""
    entities = _load_entities(entity_name)
    if query:
        filtered_entities = []
        for entity in entities:
            match = True
            for key, value in query.items():
                if entity.get(key) != value:
                    match = False
                    break
            if match:
                filtered_entities.append(entity)
        entities = filtered_entities

    await _SWARM_VISUALIZER.log_event(
        task_id, "crud_read", f"Read {len(entities)} {entity_name} records.",
        {"entity_name": entity_name, "query_summary": json.dumps(query)[:100] if query else "None"},
        model_name="human", agent_role="user"
    )
    print(f"Read {len(entities)} {entity_name} records.")
    return entities

async def update_entity(task_id: str, entity_name: str, entity_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
    """Updates an existing entity record."""
    entities = _load_entities(entity_name)
    found = False
    updated_entity = None
    for i, entity in enumerate(entities):
        if entity.get("id") == entity_id:
            entities[i] = {**entity, **updates, "updated_at": datetime.now().isoformat()}
            updated_entity = entities[i]
            found = True
            break
    
    if found:
        _save_entities(entity_name, entities)
        await _SWARM_VISUALIZER.log_event(
            task_id, "crud_update", f"Updated {entity_name} record {entity_id}.",
            {"entity_name": entity_name, "id": entity_id, "updates_summary": json.dumps(updates)[:100]},
            model_name="human", agent_role="user"
        )
        print(f"Updated {entity_name} with ID: {entity_id}")
        return {"status": "success", "id": entity_id, "entity": updated_entity}
    else:
        await _SWARM_VISUALIZER.log_event(
            task_id, "crud_update_fail", f"Failed to update {entity_name} record {entity_id}.",
            {"entity_name": entity_name, "id": entity_id, "reason": "Not found"},
            model_name="human", agent_role="user", level="ERROR"
        )
        print(f"Failed to update {entity_name} with ID: {entity_id} - Not Found")
        return {"status": "failed", "reason": "Entity not found"}

async def delete_entity(task_id: str, entity_name: str, entity_id: str) -> Dict[str, Any]:
    """Deletes an entity record."""
    entities = _load_entities(entity_name)
    initial_count = len(entities)
    entities = [entity for entity in entities if entity.get("id") != entity_id]
    
    if len(entities) < initial_count:
        _save_entities(entity_name, entities)
        await _SWARM_VISUALIZER.log_event(
            task_id, "crud_delete", f"Deleted {entity_name} record {entity_id}.",
            {"entity_name": entity_name, "id": entity_id},
            model_name="human", agent_role="user"
        )
        print(f"Deleted {entity_name} with ID: {entity_id}")
        return {"status": "success", "id": entity_id}
    else:
        await _SWARM_VISUALIZER.log_event(
            task_id, "crud_delete_fail", f"Failed to delete {entity_name} record {entity_id}.",
            {"entity_name": entity_name, "id": entity_id, "reason": "Not found"},
            model_name="human", agent_role="user", level="ERROR"
        )
        print(f"Failed to delete {entity_name} with ID: {entity_id} - Not Found")
        return {"status": "failed", "reason": "Entity not found"}
