import os
import json
import asyncio
import multiprocessing
import time
import signal
import sys
from typing import Dict, Any, List, Optional, Callable

# --- Configuration & Shared Data (initialized from studio_v3_core.py) ---
_WORKSPACE: str = ""
_CLIENT: Any = None # AsyncOpenAI client
_ALL_MODELS: Dict[str, str] = {} # Base model definitions from studio_v3_core.py
_SWARM_VISUALIZER: Any = None # Reference to the swarm_visualizer module
_CONTEXTUAL_MEMORY: Any = None # For worker to access RAG
_CRUD_MANAGER: Any = None # For worker to access persistent storage
_PERSISTENT_TASK_MANAGER: Any = None # For worker to update task status
_ASYNC_NOTIFICATION_SYSTEM: Any = None # For worker to send notifications
_RBAC_MANAGER: Any = None # For worker to perform RBAC checks
_SECURE_COGNITIVE_DEFENSE_GRID: Any = None # For worker to apply firewall
_POLICY_AUDIT_TRAIL: Any = None # For worker to log audit events
_STUDIO_CORE_REF: Any = None # Reference to the main TariroStudio instance for internal task functions

BACKGROUND_WORKER_FRAMEWORK_LOG_DIR: str = ""

_WORKER_POOL: List[multiprocessing.Process] = []
_STOP_EVENT: multiprocessing.Event = multiprocessing.Event()
_TASK_MODULE_MAPPING: Dict[str, Callable] = {}

def initialize_background_worker_framework(workspace_path: str, openai_client: Any, all_models: Dict[str, str], swarm_visualizer_module: Any, contextual_memory_module: Any, crud_manager_module: Any, persistent_task_manager_module: Any, async_notification_system_module: Any, rbac_manager_module: Any, secure_cognitive_defense_grid_module: Any, policy_audit_trail_module: Any, studio_core_ref_module: Any):
    """Initializes global configurations for the Background Worker Framework module."""
    global _WORKSPACE, _CLIENT, _ALL_MODELS, _SWARM_VISUALIZER, _CONTEXTUAL_MEMORY, _CRUD_MANAGER, _PERSISTENT_TASK_MANAGER, _ASYNC_NOTIFICATION_SYSTEM, _RBAC_MANAGER, _SECURE_COGNITIVE_DEFENSE_GRID, _POLICY_AUDIT_TRAIL, _STUDIO_CORE_REF, BACKGROUND_WORKER_FRAMEWORK_LOG_DIR
    
    _WORKSPACE = workspace_path
    _CLIENT = openai_client
    _ALL_MODELS = all_models
    _SWARM_VISUALIZER = swarm_visualizer_module
    _CONTEXTUAL_MEMORY = contextual_memory_module
    _CRUD_MANAGER = crud_manager_module
    _PERSISTENT_TASK_MANAGER = persistent_task_manager_module
    _ASYNC_NOTIFICATION_SYSTEM = async_notification_system_module
    _RBAC_MANAGER = rbac_manager_module
    _SECURE_COGNITIVE_DEFENSE_GRID = secure_cognitive_defense_grid_module
    _POLICY_AUDIT_TRAIL = policy_audit_trail_module
    _STUDIO_CORE_REF = studio_core_ref_module

    BACKGROUND_WORKER_FRAMEWORK_LOG_DIR = os.path.join(_WORKSPACE, "background_worker_framework_logs")
    os.makedirs(BACKGROUND_WORKER_FRAMEWORK_LOG_DIR, exist_ok=True)
    print(f"Background Worker Framework initialized. Logs: {BACKGROUND_WORKER_FRAMEWORK_LOG_DIR}")

    # Register task functions dynamically from modules
    _register_task_functions()

def _register_task_functions():
    """
    Dynamically registers task functions from loaded modules.
    This function needs to be called after all modules are loaded in studio_v3_core.py.
    """
    global _TASK_MODULE_MAPPING
    if _STUDIO_CORE_REF is None:
        print("WARNING: _STUDIO_CORE_REF not available to register task functions. Some tasks may not execute.")
        return

    # Iterate through all loaded modules in studio_v3_core
    for module_name, module_obj in _STUDIO_CORE_REF.loaded_modules.items():
        # Convention: Task functions are prefixed with 'handle_' or directly named as 'task_type'
        for attr_name in dir(module_obj):
            if attr_name.startswith('handle_') or attr_name.endswith('_task'):
                func = getattr(module_obj, attr_name)
                if callable(func):
                    # Create a task_type string like 'module_name.function_name'
                    task_type = f"{module_name}.{attr_name}"
                    _TASK_MODULE_MAPPING[task_type] = func
                    # print(f"Registered task function: {task_type}")
        # Also check for internal task functions in studio_v3_core itself
        for attr_name in dir(_STUDIO_CORE_REF):
            if attr_name.startswith('_handle_') and attr_name.endswith('_task'):
                func = getattr(_STUDIO_CORE_REF, attr_name)
                if callable(func):
                    task_type = f"TariroStudio.{attr_name}"
                    _TASK_MODULE_MAPPING[task_type] = func

    print(f"Registered {len(_TASK_MODULE_MAPPING)} task functions.")

async def _execute_task(task_entry: Dict[str, Any]):
    """
    Executes a single task in the worker process.
    """
    task_id = task_entry["task_id"]
    task_type = task_entry["task_type"]
    user_id = task_entry["user_id"]
    payload = task_entry["payload"]

    print(f"[Worker] Executing task {task_id} ({task_type}) for user {user_id}.")
    await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "RUNNING", 0, "Starting task execution.")

    try:
        task_func = _TASK_MODULE_MAPPING.get(task_type)
        if task_func is None:
            # Try to dynamically import the module if it wasn't registered during init
            # This can happen if a module was added AFTER framework init.
            module_name = task_type.split('.')[0]
            func_name = task_type.split('.')[1]
            if module_name == "TariroStudio": # Special handling for internal Studio tasks
                task_func = getattr(_STUDIO_CORE_REF, func_name, None)
            else:
                module_obj = _STUDIO_CORE_REF._safe_import(module_name) # Use studio_core_ref's safe_import
                if module_obj:
                    task_func = getattr(module_obj, func_name, None)
                    if task_func: # Register it for future use
                        _TASK_MODULE_MAPPING[task_type] = task_func
        
        if task_func is None:
            raise ValueError(f"No handler found for task type: {task_type}")

        # Reconstruct necessary module references for the task function from payload. 
        # This is because multiprocessing workers don't share memory directly with main process,
        # and thus won't have the initialized _MODULE_X references.
        # The studio_v3_core.py should pass these as part of the payload.
        reconstructed_kwargs = {
            k: _STUDIO_CORE_REF.loaded_modules.get(k.replace('_module', '')) 
            for k in payload if k.endswith('_module') and _STUDIO_CORE_REF
        }
        # Special handling for studio_core_ref itself
        if "studio_core_ref_placeholder" in payload and _STUDIO_CORE_REF:
            reconstructed_kwargs["studio_core_ref"] = _STUDIO_CORE_REF

        # Add common references that are always needed by task functions
        reconstructed_kwargs.update({
            "task_id": task_id,
            "user_id": user_id,
            "openai_client": _CLIENT,
            "all_models": _ALL_MODELS,
            "swarm_visualizer_module": _SWARM_VISUALIZER,
            "contextual_memory_module": _CONTEXTUAL_MEMORY,
            "crud_manager_module": _CRUD_MANAGER,
            "persistent_task_manager_module": _PERSISTENT_TASK_MANAGER,
            "async_notification_system_module": _ASYNC_NOTIFICATION_SYSTEM,
            "rbac_manager_module": _RBAC_MANAGER,
            "secure_cognitive_defense_grid_module": _SECURE_COGNITIVE_DEFENSE_GRID,
            "policy_audit_trail_module": _POLICY_AUDIT_TRAIL,
            # Exclude the 'payload' key if the function signature expects direct args
        })
        # Filter args for task_func based on its signature
        import inspect
        func_signature = inspect.signature(task_func)
        final_kwargs = {k: v for k, v in reconstructed_kwargs.items() if k in func_signature.parameters}
        final_kwargs.update({k: v for k,v in payload.items() if k not in final_kwargs and k not in ["studio_core_ref_placeholder"]})

        result = await task_func(**final_kwargs)
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "COMPLETED", 100, "Task completed successfully.", output=result)
        await _PERSISTENT_TASK_MANAGER.complete_task(task_id, user_id) # Remove from Redis processing list
        print(f"[Worker] Task {task_id} completed successfully.")

    except Exception as e:
        error_message = f"Task failed: {e}"
        print(f"[Worker] ERROR executing task {task_id}: {e}", file=sys.stderr)
        await _PERSISTENT_TASK_MANAGER.update_task_status(task_id, "FAILED", 0, error_message, output={"error": str(e)})
        await _PERSISTENT_TASK_MANAGER.complete_task(task_id, user_id) # Remove from Redis processing list even if failed
        if _ASYNC_NOTIFICATION_SYSTEM:
            await _ASYNC_NOTIFICATION_SYSTEM.send_notification(
                user_id, task_id,
                f"Your task {task_id[:8]} ({task_type}) failed. Details: {e}",
                title="Task Failed", category="system_update", causal_priority="critical"
            )
        if _SWARM_VISUALIZER:
            await _SWARM_VISUALIZER.log_event(
                session_id=task_id,
                event_type="task_failed",
                message=f"Task {task_id} failed.",
                details={"error": str(e), "task_type": task_type},
                agent_id=user_id,
                agent_role="BackgroundWorkerFramework",
                level="ERROR"
            )

def _worker_process_main(stop_event: multiprocessing.Event):
    """
    The main loop for a single worker process.
    """
    # Each worker needs to re-initialize necessary components if they rely on non-picklable objects
    # or have their own event loop.
    print(f"[Worker {os.getpid()}] Starting worker process.")
    
    # Workers should get their own instance of TariroStudio or at least its essential components
    # For now, we reuse the globally initialized references, assuming they are set up to handle
    # multiprocessing safely (e.g., Redis client, OpenAI client for async operations).
    # If not, a new TariroStudio instance needs to be created here within each worker process.
    
    # Setup its own asyncio loop if needed
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Re-register task functions in this process's memory space
    _register_task_functions()

    while not stop_event.is_set():
        try:
            task_entry = loop.run_until_complete(_PERSISTENT_TASK_MANAGER._REDIS_TASK_QUEUE.dequeue_task())
            if task_entry:
                # Reconstruct references for the task function execution in this new process
                # This is a critical point. Modules passed in payload are proxies. Actual objects must be available in this process.
                # The easiest way is to ensure all globally referenced singletons (_CRUD_MANAGER, _SWARM_VISUALIZER, etc.)
                # are re-initialized or are thread/process safe. For simplicity, we directly reference the global vars here.
                # A more robust solution involves passing minimal config and re-instantiating within worker.
                loop.run_until_complete(_execute_task(task_entry))
            else:
                time.sleep(0.1) # Short sleep to prevent busy-waiting
        except Exception as e:
            print(f"[Worker {os.getpid()}] Unhandled error in worker loop: {e}", file=sys.stderr)
            time.sleep(1) # Sleep before retrying to prevent tight error loop

    print(f"[Worker {os.getpid()}] Stopping worker process.")

def start_worker_pool(num_workers: int = 2):
    """
    Starts a pool of background worker processes.
    """
    global _WORKER_POOL, _STOP_EVENT
    if not _WORKER_POOL:
        _STOP_EVENT.clear()
        for i in range(num_workers):
            worker = multiprocessing.Process(target=_worker_process_main, args=(_STOP_EVENT,))
            _WORKER_POOL.append(worker)
            worker.start()
            print(f"Started worker process {worker.pid}.")
    else:
        print("Worker pool already running.")

def stop_worker_pool():
    """
    Stops all worker processes in the pool.
    """
    global _WORKER_POOL, _STOP_EVENT
    if _WORKER_POOL:
        _STOP_EVENT.set()
        for worker in _WORKER_POOL:
            worker.join(timeout=5) # Give workers a chance to finish current task
            if worker.is_alive():
                print(f"Terminating unresponsive worker {worker.pid}.")
                worker.terminate()
            worker.join()
        _WORKER_POOL = []
        print("Worker pool stopped.")
    else:
        print("No worker pool running.")

