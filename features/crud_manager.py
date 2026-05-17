import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid

# --- Configuration & Shared Data ---
_WORKSPACE: str = ""
_POLICY_AUDIT_TRAIL: Any = None # Reference to Policy Audit Trail module

CRUD_MANAGER_LOG_DIR: str = ""

# In-memory mock database for entities. In a real system, this would be a persistent DB.
_MOCKED_DATABASE: Dict[str, Dict[str, Any]] = {}

def initialize_crud_manager(workspace_path: str, policy_audit_trail_module: Any):
    """Initializes global CRUD configurations."""
    global _WORKSPACE, _POLICY_AUDIT_TRAIL, CRUD_MANAGER_LOG_DIR
    
    _WORKSPACE = workspace_path
    _POLICY_AUDIT_TRAIL = policy_audit_trail_module

    CRUD_MANAGER_LOG_DIR = os.path.join(_WORKSPACE, "crud_manager_logs")
    os.makedirs(CRUD_MANAGER_LOG_DIR, exist_ok=True)
    print(f"CRUD Manager initialized. Logs: {CRUD_MANAGER_LOG_DIR}")

async def create_entity(entity_type: str, data: Dict[str, Any], user_id: str = "Tariro_System") -> Dict[str, Any]:
    """
    Creates a new entity of a given type.
    
    Args:
        entity_type (str): The type of the entity (e.g., "Goal", "Task", "AuditLog").
        data (Dict[str, Any]): The data for the new entity. Must contain an 'id' field or one will be generated.
        user_id (str): The ID of the user or entity creating this record.

    Returns:
        Dict[str, Any]: The created entity data with an 'id' and metadata.
    """
    if entity_type not in _MOCKED_DATABASE:
        _MOCKED_DATABASE[entity_type] = {}

    entity_id = data.get("id", str(uuid.uuid4()))
    if "id" not in data: # Ensure the 'id' is in the data dict
        data["id"] = entity_id
    
    # Add creation/update metadata
    data["created_at"] = datetime.now().isoformat()
    data["created_by"] = user_id
    data["updated_at"] = datetime.now().isoformat()
    data["updated_by"] = user_id

    _MOCKED_DATABASE[entity_type][entity_id] = data

    if _POLICY_AUDIT_TRAIL:
        await _POLICY_AUDIT_TRAIL.log_event(
            session_id=str(uuid.uuid4()),
            event_type="crud_create",
            description=f"Created entity {entity_type} with ID {entity_id}.",
            metadata={
                "entity_type": entity_type,
                "entity_id": entity_id,
                "data_preview": str(data)[:100] # Log a preview
            },
            user_id=user_id,
            agent_role="CRUD_Manager",
            level="INFO"
        )

    return {"status": "success", "entity_id": entity_id, "data": data}

async def read_entity(entity_type: str, entity_id: str) -> Optional[Dict[str, Any]]:
    """
    Reads an entity of a given type by its ID.
    """
    entity = _MOCKED_DATABASE.get(entity_type, {}).get(entity_id)
    return entity

async def update_entity(entity_type: str, entity_id: str, updates: Dict[str, Any], user_id: str = "Tariro_System") -> Dict[str, Any]:
    """
    Updates an existing entity of a given type.
    """
    if entity_type not in _MOCKED_DATABASE or entity_id not in _MOCKED_DATABASE[entity_type]:
        return {"status": "failed", "reason": f"Entity {entity_type}:{entity_id} not found."}

    current_data = _MOCKED_DATABASE[entity_type][entity_id]
    current_data.update(updates)
    current_data["updated_at"] = datetime.now().isoformat()
    current_data["updated_by"] = user_id

    if _POLICY_AUDIT_TRAIL:
        await _POLICY_AUDIT_TRAIL.log_event(
            session_id=str(uuid.uuid4()),
            event_type="crud_update",
            description=f"Updated entity {entity_type} with ID {entity_id}.",
            metadata={
                "entity_type": entity_type,
                "entity_id": entity_id,
                "updates_preview": str(updates)[:100]
            },
            user_id=user_id,
            agent_role="CRUD_Manager",
            level="INFO"
        )

    return {"status": "success", "entity_id": entity_id, "data": current_data}

async def delete_entity(entity_type: str, entity_id: str, user_id: str = "Tariro_System") -> Dict[str, Any]:
    """
    Deletes an entity of a given type by its ID.
    """
    if entity_type in _MOCKED_DATABASE and entity_id in _MOCKED_DATABASE[entity_type]:
        del _MOCKED_DATABASE[entity_type][entity_id]
        if _POLICY_AUDIT_TRAIL:
            await _POLICY_AUDIT_TRAIL.log_event(
                session_id=str(uuid.uuid4()),
                event_type="crud_delete",
                description=f"Deleted entity {entity_type} with ID {entity_id}.",
                metadata={
                    "entity_type": entity_type,
                    "entity_id": entity_id
                },
                user_id=user_id,
                agent_role="CRUD_Manager",
                level="WARNING"
            )
        return {"status": "success", "message": f"Entity {entity_type}:{entity_id} deleted."}
    return {"status": "failed", "reason": f"Entity {entity_type}:{entity_id} not found."}

async def filter_entities(entity_type: str, query: Dict[str, Any], limit: int = 100, sort_by: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Filters entities of a given type based on query parameters.
    (Basic implementation: exact match for query values. No complex operators like $gt, $lt).
    """
    if entity_type not in _MOCKED_DATABASE:
        return []

    results = []
    for entity_id, entity_data in _MOCKED_DATABASE[entity_type].items():
        match = True
        for key, value in query.items():
            if entity_data.get(key) != value:
                match = False
                break
        if match:
            results.append(entity_data)
    
    if sort_by and results:
        results.sort(key=lambda x: x.get(sort_by, x["created_at"]))

    return results[:limit]

