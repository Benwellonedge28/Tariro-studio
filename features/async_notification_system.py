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
_SWARM_VISUALIZER: Any = None # Reference to Swarm Visualizer module
_CRUD_MANAGER: Any = None # Reference to CRUD Manager for Notification entities
_PERSISTENT_TASK_MANAGER: Any = None # For linking notifications to tasks

ASYNC_NOTIFICATION_SYSTEM_LOG_DIR: str = ""

def initialize_async_notification_system(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, crud_manager_module: Any, persistent_task_manager_module: Any):
    """Initializes global configurations for the Asynchronous Notification System module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CRUD_MANAGER, _PERSISTENT_TASK_MANAGER, ASYNC_NOTIFICATION_SYSTEM_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CRUD_MANAGER = crud_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module

    ASYNC_NOTIFICATION_SYSTEM_LOG_DIR = os.path.join(_WORKSPACE, "async_notification_system_logs")
    os.makedirs(ASYNC_NOTIFICATION_SYSTEM_LOG_DIR, exist_ok=True)
    print(f"Asynchronous Notification System initialized. Logs: {ASYNC_NOTIFICATION_SYSTEM_LOG_DIR}")

async def send_notification(user_id: str, linked_task_id: str, content: str, title: str = "Tariro Studio Notification", category: str = "system_update", causal_priority: str = "medium", is_read: bool = False) -> Dict[str, Any]:
    """
    Sends an asynchronous notification to a user, potentially linked to a task.

    Args:
        user_id (str): The ID of the user to notify.
        linked_task_id (str): The ID of the task this notification relates to.
        content (str): The main message content of the notification.
        title (str): The title of the notification.
        category (str): The category of the notification (e.g., "system_update", "task_completion").
        causal_priority (str): The priority level (e.g., "low", "medium", "high", "critical").
        is_read (bool): Initial read status.

    Returns:
        Dict[str, Any]: Status of the notification sending operation.
    """
    notification_id = str(uuid.uuid4())
    notification_entry = {
        "id": notification_id,
        "user_id": user_id,
        "linked_task_id": linked_task_id,
        "title": title,
        "content": content,
        "category": category,
        "causal_priority": causal_priority,
        "created_at": datetime.now().isoformat(),
        "is_read": is_read
    }

    if _CRUD_MANAGER:
        try:
            await _CRUD_MANAGER.create_entity("Notification", notification_entry)
        except Exception as e:
            print(f"ERROR: Failed to store notification in CRUD Manager: {e}")
            return {"status": "failed", "reason": f"Failed to store notification: {e}"}

    if _SWARM_VISUALIZER:
        await _SWARM_VISUALIZER.log_event(
            session_id=linked_task_id,
            event_type="notification_sent",
            message=f"Notification sent to {user_id}: {title}",
            details={
                "notification_id": notification_id,
                "user_id": user_id,
                "title": title,
                "category": category,
                "priority": causal_priority
            },
            agent_id="Tariro_System",
            agent_role="AsyncNotificationSystem",
            level="INFO"
        )

    print(f"[NotificationSystem] Notification to {user_id} (Task: {linked_task_id}): {title} - {content[:50]}...")
    return {"status": "success", "notification_id": notification_id, "notification": notification_entry}

async def get_user_notifications(user_id: str, include_read: bool = False, limit: int = 50) -> List[Dict[str, Any]]:
    """
    Retrieves notifications for a specific user.
    """
    if not _CRUD_MANAGER:
        print("WARNING: CRUD Manager not initialized. Cannot retrieve notifications.")
        return []
    
    query = {"user_id": user_id}
    if not include_read:
        query["is_read"] = False # Assuming CRUD Manager supports filtering booleans
    
    try:
        notifications = await _CRUD_MANAGER.filter_entities("Notification", query, limit=limit, sort_by="-created_at") # Descending order
        return notifications
    except Exception as e:
        print(f"ERROR: Failed to retrieve notifications from CRUD Manager: {e}")
        return []

async def mark_notification_as_read(notification_id: str, user_id: str) -> Dict[str, Any]:
    """
    Marks a specific notification as read.
    """
    if not _CRUD_MANAGER:
        return {"status": "failed", "reason": "CRUD Manager not initialized."}

    notification = await _CRUD_MANAGER.read_entity("Notification", notification_id)
    if not notification:
        return {"status": "failed", "reason": f"Notification {notification_id} not found."}
    
    if notification.get("user_id") != user_id: # Ensure only the owner can mark as read
        return {"status": "failed", "reason": "Unauthorized to mark this notification as read."}

    if notification.get("is_read"): # Already read
        return {"status": "success", "message": "Notification already marked as read."}

    updated_notification = await _CRUD_MANAGER.update_entity("Notification", notification_id, {"is_read": True}, user_id=user_id)
    
    if updated_notification.get("status") == "success" and _SWARM_VISUALIZER:
        await _SWARM_VISUALIZER.log_event(
            session_id=notification.get("linked_task_id", "unknown"),
            event_type="notification_read",
            message=f"Notification {notification_id} marked as read by {user_id}",
            details={
                "notification_id": notification_id,
                "user_id": user_id,
                "title": notification.get("title")
            },
            agent_id=user_id,
            agent_role="AsyncNotificationSystem",
            level="INFO"
        )

    return updated_notification
