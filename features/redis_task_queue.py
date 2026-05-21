import os
import json
import asyncio
import redis.asyncio as redis
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
import uuid

# --- Configuration & Shared Data ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Base model definitions from studio_v3_core.py
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module
_CRUD_MANAGER: Any = None # Reference to CRUD Manager for Task entities
_PERSISTENT_TASK_MANAGER: Any = None # For updating task status in persistent storage
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For sending notifications

_REDIS_URL: str = "redis://localhost:6379/0" # Initialized from studio_v3_core
_REDIS_CLIENT: Any = None # Redis client instance

REDIS_TASK_QUEUE_LOG_DIR: str = ""
TASK_QUEUE_KEY = "tariro_task_queue"
TASK_PROCESSING_KEY_PREFIX = "tariro_task_processing:"
TASK_TIMEOUT_SECONDS = 300 # 5 minutes for a task to be processed

def initialize_redis_task_queue(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any):
    """Initializes global Redis Task Queue configurations."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _REDIS_CLIENT, REDIS_TASK_QUEUE_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module

    # Instantiate Redis client
    _REDIS_CLIENT = redis.from_url(_REDIS_URL)

    REDIS_TASK_QUEUE_LOG_DIR = os.path.join(_WORKSPACE, "redis_task_queue_logs")
    os.makedirs(REDIS_TASK_QUEUE_LOG_DIR, exist_ok=True)
    print(f"Redis Task Queue initialized. Logs: {REDIS_TASK_QUEUE_LOG_DIR}")

async def enqueue_task(task_payload: Dict[str, Any], task_id: str, user_id: str = "Tariro_System") -> Dict[str, Any]:
    """
    Adds a task to the Redis queue for asynchronous processing.

    Args:
        task_payload (Dict[str, Any]): The full payload of the task.
        task_id (str): The unique ID of the task.
        user_id (str): The ID of the user who submitted the task.

    Returns:
        Dict[str, Any]: Status of the enqueue operation.
    """
    if not _REDIS_CLIENT:
        return {"status": "failed", "reason": "Redis client not initialized."}

    try:
        queue_entry = {"task_id": task_id, "user_id": user_id, "payload": task_payload, "enqueued_at": datetime.now().isoformat()}
        await _REDIS_CLIENT.rpush(TASK_QUEUE_KEY, json.dumps(queue_entry))

        if _SWARM_VISUALIZER:
            await _SWARM_VISUALIZER.log_event(
                session_id=task_id,
                event_type="task_enqueued",
                message=f"Task {task_id} enqueued.",
                details=queue_entry,
                agent_id=user_id,
                agent_role="RedisTaskQueue",
                level="INFO"
            )
        print(f"[RedisTaskQueue] Task {task_id} enqueued.")
        return {"status": "success", "task_id": task_id}
    except Exception as e:
        print(f"ERROR: Failed to enqueue task {task_id}: {e}")
        return {"status": "failed", "reason": str(e)}

async def dequeue_task() -> Optional[Dict[str, Any]]:
    """
    Retrieves and reserves a task from the Redis queue for processing.
    Marks the task as "processing" with a timeout.

    Returns:
        Optional[Dict[str, Any]]: The task payload if available, None otherwise.
    """
    if not _REDIS_CLIENT:
        return None

    try:
        # Atomically pop a task from the queue and mark it as processing
        # using BRPOPLPUSH for reliability - move from queue to processing list
        queue_entry_str = await _REDIS_CLIENT.brpoplpush(TASK_QUEUE_KEY, TASK_PROCESSING_KEY_PREFIX + os.uname().nodename, timeout=1)
        
        if queue_entry_str:
            queue_entry = json.loads(queue_entry_str)
            task_id = queue_entry["task_id"]
            user_id = queue_entry["user_id"]
            processing_key = TASK_PROCESSING_KEY_PREFIX + task_id

            # Set an expiry on the processing key to detect stalled tasks
            await _REDIS_CLIENT.setex(processing_key, TASK_TIMEOUT_SECONDS, json.dumps(queue_entry))

            if _SWARM_VISUALIZER:
                await _SWARM_VISUALIZER.log_event(
                    session_id=task_id,
                    event_type="task_dequeued",
                    message=f"Task {task_id} dequeued for processing.",
                    details=queue_entry,
                    agent_id=user_id,
                    agent_role="RedisTaskQueue",
                    level="INFO"
                )
            print(f"[RedisTaskQueue] Task {task_id} dequeued.")
            return queue_entry
        return None
    except Exception as e:
        print(f"ERROR: Failed to dequeue task: {e}")
        return None

async def complete_task(task_id: str, user_id: str = "Tariro_System") -> Dict[str, Any]:
    """
    Marks a task as completed, removing it from the processing list.
    """
    if not _REDIS_CLIENT:
        return {"status": "failed", "reason": "Redis client not initialized."}
    try:
        processing_key = TASK_PROCESSING_KEY_PREFIX + task_id
        removed_count = await _REDIS_CLIENT.delete(processing_key)

        if removed_count > 0:
            if _SWARM_VISUALIZER:
                await _SWARM_VISUALIZER.log_event(
                    session_id=task_id,
                    event_type="task_completed",
                    message=f"Task {task_id} marked as completed.",
                    details={
                        "task_id": task_id
                    },
                    agent_id=user_id,
                    agent_role="RedisTaskQueue",
                    level="INFO"
                )
            print(f"[RedisTaskQueue] Task {task_id} completed.")
            return {"status": "success", "task_id": task_id}
        return {"status": "failed", "reason": f"Task {task_id} not found in processing list."}
    except Exception as e:
        print(f"ERROR: Failed to mark task {task_id} as complete: {e}")
        return {"status": "failed", "reason": str(e)}

async def check_stalled_tasks(task_id: str, check_interval_seconds: int, user_id: str = "Tariro_System"): # task_id added for SwarmVisualizer logging
    """
    Checks for stalled tasks in the processing lists and re-enqueues them.
    This function should be run periodically by a background process.
    """
    if not _REDIS_CLIENT:
        print("WARNING: Redis client not initialized. Cannot check for stalled tasks.")
        return

    print(f"[RedisTaskQueue] Checking for stalled tasks. Max processing time: {TASK_TIMEOUT_SECONDS}s")
    if _SWARM_VISUALIZER:
        await _SWARM_VISUALIZER.log_event(
            session_id=task_id,
            event_type="stalled_task_check_start",
            message="Starting check for stalled tasks.",
            details={
                "check_interval_seconds": check_interval_seconds,
                "task_timeout_seconds": TASK_TIMEOUT_SECONDS
            },
            agent_id=user_id,
            agent_role="RedisTaskQueue",
            level="INFO"
        )

    # Iterate over all processing lists (one per worker node) to find stalled tasks
    # In a real distributed system, we would need to know all worker node IDs
    # For this mock, we assume tasks are simply moved to a processing key with an expiry
    
    # Find all processing keys
    stalled_count = 0
    try:
        async for key in _REDIS_CLIENT.scan_iter(match=TASK_PROCESSING_KEY_PREFIX + "*"):
            # Get the task payload and check its age
            task_entry_str = await _REDIS_CLIENT.get(key)
            if task_entry_str:
                task_entry = json.loads(task_entry_str)
                enqueued_at_str = task_entry.get("enqueued_at")
                if enqueued_at_str:
                    enqueued_at = datetime.fromisoformat(enqueued_at_str)
                    time_in_processing = datetime.now() - enqueued_at

                    # Check if the task has exceeded its processing timeout
                    # Note: The SETEX command already handles this. This check is an additional layer
                    # to catch tasks that might have been processed by a failed worker without completing.
                    if time_in_processing > timedelta(seconds=TASK_TIMEOUT_SECONDS):
                        print(f"[RedisTaskQueue] Detected stalled task {task_entry['task_id']}. Re-enqueuing.")
                        await _REDIS_CLIENT.lpush(TASK_QUEUE_KEY, json.dumps(task_entry)) # Re-enqueue
                        await _REDIS_CLIENT.delete(key) # Remove from processing
                        stalled_count += 1
                        if _SWARM_VISUALIZER:
                            await _SWARM_VISUALIZER.log_event(
                                session_id=task_entry["task_id"],
                                event_type="task_stalled_re_enqueued",
                                message=f"Task {task_entry['task_id']} detected as stalled and re-enqueued.",
                                details=task_entry,
                                agent_id=user_id,
                                agent_role="RedisTaskQueue",
                                level="WARNING"
                            )
                        if _ASYNC_NOTIFICATION_SYSTEM:
                            await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
                                task_entry["user_id"],
                                task_entry["task_id"],
                                f"Your task {task_entry['task_id'][:8]} was detected as stalled and has been re-enqueued. It will be processed shortly.",
                                title="Task Stalled and Re-enqueued",
                                category="system_update",
                                causal_priority="high"
                            )
                else:
                    # Task entry without enqueued_at, might be malformed or old
                    print(f"[RedisTaskQueue] Malformed or old task entry found: {task_entry.get('task_id', 'Unknown')}. Removing.")
                    await _REDIS_CLIENT.delete(key)
                    if _SWARM_VISUALIZER:
                        await _SWARM_VISUALIZER.log_event(
                            session_id=task_entry.get("task_id", "unknown"),
                            event_type="malformed_task_removed",
                            message=f"Malformed task entry {task_entry.get('task_id', 'Unknown')} removed from processing.",
                            details=task_entry,
                            agent_id=user_id,
                            agent_role="RedisTaskQueue",
                            level="ERROR"
                        )

    except Exception as e:
        print(f"ERROR: Error during stalled task check: {e}")
        if _SWARM_VISUALIZER:
            await _SWARM_VISUALIZER.log_event(
                session_id=task_id,
                event_type="stalled_task_check_error",
                message=f"Error during stalled task check: {e}",
                details={
                    "error": str(e)
                },
                agent_id=user_id,
                agent_role="RedisTaskQueue",
                level="CRITICAL"
            )

    if _SWARM_VISUALIZER:
        await _SWARM_VISUALIZER.log_event(
            session_id=task_id,
            event_type="stalled_task_check_end",
            message=f"Completed check for stalled tasks. Re-enqueued {stalled_count} tasks.",
            details={
                "stalled_tasks_re_enqueued": stalled_count
            },
            agent_id=user_id,
            agent_role="RedisTaskQueue",
            level="INFO"
        )
    print(f"[RedisTaskQueue] Completed check for stalled tasks. Re-enqueued {stalled_count} tasks.")

