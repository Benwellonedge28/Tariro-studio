import asyncio
import uvicorn
import json
import os
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from studio_v3_core import TariroStudio, RequestContext, WORKSPACE, TARIRO_ENV, TARIRO_ROOT_ADMIN # Import core components

# --- Logging ─────────────────────────────────────────────────────────────────
logger = logging.getLogger("TariroStudioApp")

# --- FastAPI App Lifespan (Initialization & Shutdown) ────────────────────────
# This context manager handles the startup and shutdown events of the FastAPI application.
@asynccontextmanager
async def lifespan(app: FastAPI): # app parameter is required by FastAPI
    logger.info("Tariro Studio FastAPI app starting up...")

    # Initialize TariroStudio core
    app.state.tariro_studio = TariroStudio()
    logger.info("Tariro Studio core initialized.")

    # Start background workers (if module is loaded)
    if app.state.tariro_studio.background_worker_framework:
        app.state.tariro_studio.start_background_workers() # Default to 2 workers

    # Schedule a self-hardening check if the module exists
    if app.state.tariro_studio.self_repairing_auto_healing:
        try:
            task_id = f"initial_self_hardening_check_{uuid.uuid4().hex}"
            await app.state.tariro_studio.persistent_task_manager.submit_task(
                task_type="self_repairing_auto_healing.start_continuous_self_hardening_loop",
                payload={"interval_seconds": 3600}, # Run hourly
                user_id=TARIRO_ROOT_ADMIN,
                priority=1,
                initial_status="PENDING_BACKGROUND_LOOP",
                initiating_session_id=task_id
            )
            logger.info(f"Initial self-hardening loop task {task_id} submitted.")
        except Exception as e:
            logger.error(f"Failed to submit initial self-hardening task: {e}")

    # Schedule resource management check if the module exists
    if app.state.tariro_studio.dynamic_resource_allocator:
        try:
            task_id = f"initial_resource_mgmt_check_{uuid.uuid4().hex}"
            await app.state.tariro_studio.persistent_task_manager.submit_task(
                task_type="dynamic_resource_allocator.start_continuous_resource_management_loop",
                payload={"interval_seconds": 300}, # Run every 5 minutes
                user_id=TARIRO_ROOT_ADMIN,
                priority=1,
                initial_status="PENDING_BACKGROUND_LOOP",
                initiating_session_id=task_id
            )
            logger.info(f"Initial resource management loop task {task_id} submitted.")
        except Exception as e:
            logger.error(f"Failed to submit initial resource management task: {e}")

    yield

    logger.info("Tariro Studio FastAPI app shutting down...")
    # Perform graceful shutdown of TariroStudio core components
    await app.state.tariro_studio.shutdown()
    logger.info("Tariro Studio FastAPI app shutdown complete.")

# --- FastAPI App Instance ──────────────────────────────────────────────────
app = FastAPI(lifespan=lifespan,
              title="Tariro Studio API",
              description="Omniversal AGI Development Environment - Core API",
              version="0.0.1")

# --- CORS Middleware ───────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- API Routes ────────────────────────────────────────────────────────────
@app.get("/health")
async def health_check():
    """Health check endpoint."""
    # Access TariroStudio instance via app.state
    studio: TariroStudio = app.state.tariro_studio

    # Basic checks for core components
    core_status = {
        "core_initialized": True,
        "openai_client_ready": studio.client is not None,
        "scheduler_running": studio.scheduler.running,
        "loaded_modules_count": len(studio.loaded_modules),
        "failed_modules_count": len(studio.failed_modules),
        "background_workers_started": studio.background_workers_started,
    }

    # More detailed status from loaded modules
    module_health = {}
    if studio.persistent_task_manager:
        module_health["persistent_task_manager"] = {"status": "ready"}
    if studio.redis_task_queue:
        try:
            ping_result = await studio.redis_task_queue._REDIS_CLIENT.ping()
            module_health["redis_task_queue"] = {"status": "ready" if ping_result else "not_ready"}
        except Exception:
            module_health["redis_task_queue"] = {"status": "error"}
    # Add more module-specific health checks as needed

    return {"status": "healthy", "core": core_status, "modules": module_health, "env": TARIRO_ENV}

@app.post("/chat")
async def chat_endpoint(request: Request):
    """Main chat endpoint for streaming responses."""
    studio: TariroStudio = app.state.tariro_studio
    
    # In a real app, user_id and session_id would come from auth/session management.
    # For this example, we'll use defaults or extract from headers if available.
    user_id = request.headers.get("X-User-ID", TARIRO_ROOT_ADMIN)
    session_id = request.headers.get("X-Session-ID", str(uuid.uuid4()))

    request_data = await request.json()
    text = request_data.get("text")
    if not text:
        raise HTTPException(status_code=400, detail="'text' field is required in the request body.")

    context = RequestContext(user_id=user_id, session_id=session_id, studio=studio)

    # Use StreamingResponse to send LLM chunks as they arrive
    return StreamingResponse(studio.chat(text, context), media_type="text/event-stream")

@app.post("/task/{task_type:path}")
async def submit_generic_task(task_type: str, request: Request):
    """Endpoint for submitting generic tasks to the Persistent Task Manager."""
    studio: TariroStudio = app.state.tariro_studio

    user_id = request.headers.get("X-User-ID", TARIRO_ROOT_ADMIN)
    session_id = request.headers.get("X-Session-ID", str(uuid.uuid4()))

    payload = await request.json()

    if not studio.persistent_task_manager:
        raise HTTPException(status_code=503, detail="Persistent Task Manager is not available.")
    
    # Submit the task to the persistent task manager
    task_submission_result = await studio.persistent_task_manager.submit_task(
        task_type=task_type,
        payload=payload,
        user_id=user_id,
        initiating_session_id=session_id
    )

    if task_submission_result.get("status") == "success":
        return {"message": "Task submitted successfully", "task_id": task_submission_result["task_id"], "status": "PENDING"}
    else:
        raise HTTPException(status_code=500, detail=f"Task submission failed: {task_submission_result.get('reason', 'Unknown error')}")

@app.get("/task/{task_id}")
async def get_task_status(task_id: str, request: Request):
    """Endpoint to get the status of a submitted task."""
    studio: TariroStudio = app.state.tariro_studio
    user_id = request.headers.get("X-User-ID", TARIRO_ROOT_ADMIN)

    if not studio.persistent_task_manager:
        raise HTTPException(status_code=503, detail="Persistent Task Manager is not available.")
    
    task_status_result = await studio.persistent_task_manager.get_task_status(task_id)

    if task_status_result.get("status") == "success":
        # Basic RBAC check: only task owner or root admin can view status
        if task_status_result["task"].get("user_id") == user_id or user_id == TARIRO_ROOT_ADMIN:
            return task_status_result["task"]
        else:
            raise HTTPException(status_code=403, detail="Unauthorized to view this task status.")
    else:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found.")

# --- Main entry point for local development ────────────────────────────────
if __name__ == "__main__":
    # When running with `python app.py`, use uvicorn to run the app
    # In production, this might be handled by Gunicorn or similar WSGI server
    print("Starting Tariro Studio FastAPI application...")
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True, lifespan="on")
