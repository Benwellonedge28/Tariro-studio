import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid

# --- Configuration & Shared Data ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Base model definitions from studio_v3_core.py
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module
_CONTEXTUAL_MEMORY: Any = None # For storing task context and results
_CRUD_MANAGER: Any = None # For persisting Task entities
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For sending task updates
_REDIS_TASK_QUEUE: Any = None # For queuing tasks for workers

PERSISTENT_TASK_MANAGER_LOG_DIR: str = ""

def initialize_persistent_task_manager(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, contextual_memory_module: Any, crud_manager_module: Any, async_notification_system_module: Any, redis_task_queue_module: Any):
    """Initializes global Persistent Task Manager configurations."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CONTEXTUAL_MEMORY, _CRUD_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _REDIS_TASK_QUEUE, PERSISTENT_TASK_MANAGER_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CONTEXTUAL_MEMORY = contextual_memory_module
    _CRUD_MANAGER = crud_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _REDIS_TASK_QUEUE = redis_task_queue_module

    PERSISTENT_TASK_MANAGER_LOG_DIR = os.path.join(_WORKSPACE, "persistent_task_manager_logs")
    os.makedirs(PERSISTENT_TASK_MANAGER_LOG_DIR, exist_ok=True)
    print(f"Persistent Task Manager initialized. Logs: {PERSISTENT_TASK_MANAGER_LOG_DIR}")

async def submit_task(task_type: str, payload: Dict[str, Any], user_id: str, priority: int = 5, initial_status: str = "PENDING", initiating_session_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Submits a new task to be processed asynchronously and persistently.

    Args:
        task_type (str): A string identifying the type of task (e.g., "code_generation", "self_upgrade").
        payload (Dict[str, Any]): The input data required for the task.
        user_id (str): The ID of the user or entity submitting the task.
        priority (int): Priority level of the task (1=highest, 10=lowest).
        initial_status (str): The initial status of the task (e.g., "PENDING", "QUEUED").
        initiating_session_id (Optional[str]): The session ID from which the task was initiated.

    Returns:
        Dict[str, Any]: A dictionary containing the status of the submission and the task ID.
    """
    task_id = str(uuid.uuid4())
    task_entry = {
        "task_id": task_id,
        "task_type": task_type,
        "user_id": user_id,
        "priority": priority,
        "status": initial_status,
        "progress": 0.0,
        "current_step": "Initialized",
        "payload": payload,
        "output": {},
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
        "initiating_session_id": initiating_session_id
    }

    if _CRUD_MANAGER:
        try:
            # Store task in persistent storage
            await _CRUD_MANAGER.create_entity("Task", task_entry)
        except Exception as e:
            print(f"ERROR: Failed to create task {task_id} in CRUD Manager: {e}")
            return {"status": "failed", "reason": f"Failed to persist task: {e}"}

    if _REDIS_TASK_QUEUE:
        try:
            # Enqueue task for worker processing
            await _REDIS_TASK_QUEUE.enqueue_task(task_entry, task_id, user_id)
        except Exception as e:
            print(f"ERROR: Failed to enqueue task {task_id} in Redis: {e}")
            # If queuing fails, consider marking task as failed or pending retry in CRUD
            await _CRUD_MANAGER.update_entity("Task", task_id, {"status": "QUEUING_FAILED", "current_step": f"Failed to enqueue: {e}"})
            return {"status": "failed", "reason": f"Failed to enqueue task: {e}"}

    if _SWARM_VISUALIZER:
        await _SWARM_VISUALIZER.log_event(
            session_id=initiating_session_id or task_id,
            event_type="task_submitted",
            message=f"Task {task_id} ({task_type}) submitted by {user_id}.",
            details=task_entry,
            agent_id=user_id,
            agent_role="PersistentTaskManager",
            level="INFO"
        )

    print(f"[PersistentTaskManager] Task {task_id} ({task_type}) submitted by {user_id}.")
    return {"status": "success", "task_id": task_id, "task_type": task_type}

async def get_task_status(task_id: str) -> Dict[str, Any]:
    """
    Retrieves the current status of a task.
    """
    if not _CRUD_MANAGER:
        return {"status": "failed", "reason": "CRUD Manager not initialized."}
    try:
        task = await _CRUD_MANAGER.read_entity("Task", task_id)
        if task:
            return {"status": "success", "task": task}
        return {"status": "failed", "reason": f"Task {task_id} not found."}
    except Exception as e:
        print(f"ERROR: Failed to retrieve task {task_id} status: {e}")
        return {"status": "failed", "reason": str(e)}

async def update_task_status(task_id: str, status: str, progress: float = -1.0, current_step: Optional[str] = None, output: Optional[Dict[str, Any]] = None, user_id: str = "Tariro_System") -> Dict[str, Any]:
    """
    Updates the status, progress, current step, and output of a persistent task.
    """
    if not _CRUD_MANAGER:
        return {"status": "failed", "reason": "CRUD Manager not initialized."}

    updates = {"status": status, "updated_at": datetime.now().isoformat()}
    if progress >= 0:
        updates["progress"] = progress
    if current_step:
        updates["current_step"] = current_step
    if output:
        # Merge output. This allows incremental updates to the output dict.
        current_task = await _CRUD_MANAGER.read_entity("Task", task_id)
        if current_task and "output" in current_task:
            current_task["output"].update(output)
            updates["output"] = current_task["output"]
        else:
            updates["output"] = output

    try:
        updated_task = await _CRUD_MANAGER.update_entity("Task", task_id, updates, user_id=user_id)
        if updated_task.get("status") == "success" and _SWARM_VISUALIZER:
            await _SWARM_VISUALIZER.log_event(
                session_id=task_id, # Use task_id as session for internal task events
                event_type="task_update",
                message=f"Task {task_id} status updated to {status}.",
                details=updated_task["data"],
                agent_id=user_id,
                agent_role="PersistentTaskManager",
                level="INFO"
            )
        print(f"[PersistentTaskManager] Task {task_id} updated: Status={status}, Progress={progress:.1f}%, Step='{current_step}'.")

        # Optional: Notify user on critical status changes or completion
        if _ASYNC_NOTIFICATION_SYSTEM and (status in ["COMPLETED", "FAILED", "CRITICAL_ERROR"] or progress >= 99.9):
            notification_title = f"Task {task_id[:8]} {status.replace('_', ' ').title()}"
            notification_content = f"Task of type '{updated_task["data"]["task_type"]}' has changed status to {status}. Current step: {current_step}."
            if status == "FAILED" or status == "CRITICAL_ERROR":
                notification_content += f" Error details: {output}"
            await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
                updated_task["data"]["user_id"],
                task_id,
                notification_content,
                title=notification_title,
                category="task_status",
                causal_priority="high" if status in ["FAILED", "CRITICAL_ERROR"] else "medium"
            )

        return updated_task
    except Exception as e:
        print(f"ERROR: Failed to update task {task_id} status: {e}")
        return {"status": "failed", "reason": str(e)}

async def get_tasks_by_user(user_id: str, status: Optional[str] = None, limit: int = 100) -> List[Dict[str, Any]]:
    """
    Retrieves tasks submitted by a specific user, optionally filtered by status.
    """
    if not _CRUD_MANAGER:
        print("WARNING: CRUD Manager not initialized. Cannot retrieve tasks.")
        return []
    query = {"user_id": user_id}
    if status:
        query["status"] = status
    try:
        tasks = await _CRUD_MANAGER.filter_entities("Task", query, limit=limit, sort_by="-updated_at")
        return tasks
    except Exception as e:
        print(f"ERROR: Failed to retrieve tasks for user {user_id}: {e}")
        return []
