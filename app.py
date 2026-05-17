import os
import uuid
import asyncio
from contextlib import asynccontextmanager
from typing import Dict, Any, List, Optional
import json
import tempfile
import httpx # Import httpx for FastAPI endpoints to call other FastAPI endpoints
import base64 # Needed for file processing task

from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
import gradio as gr
import uvicorn

# Import Tariro Studio core logic
from studio_v3_core import (
    TariroStudio,
    RequestContext,
    get_model_id,
    _MODEL_DESCRIPTIONS,
    TARIRO_ROOT_ADMIN,
    logger,
    PIPELINE_TIMEOUT,
    FEATURES_DIR,
    WORKSPACE # Import WORKSPACE for general use
)

# --- FastAPI Lifespan ---
# This ensures TariroStudio is initialized once per worker process.
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Initializing TariroStudio for this worker...")
    app_state = TariroStudio() # Instantiate TariroStudio
    app.state.tariro = app_state
    logger.info("TariroStudio instance ready for this worker.")

    # Start background workers as part of the lifespan
    app_state.start_background_workers()
    
    # Schedule the continuous self-hardening loop as a persistent task
    if app_state.persistent_task_manager:
        task_id_sh = f"scheduled_self_hardening_task_{uuid.uuid4().hex}"
        await app_state.persistent_task_manager.submit_task(
            task_type="self_hardening_defense.start_continuous_self_hardening_loop",
            payload={"interval_seconds": 3600}, # Run hourly
            user_id=TARIRO_ROOT_ADMIN,
            priority=1,
            initial_status="SCHEDULED_BACKGROUND_LOOP",
            initiating_session_id=task_id_sh
        )
        logger.info(f"Scheduled continuous self-hardening loop as task {task_id_sh}.")
        
        # Schedule continuous resource management loop as a persistent task
        task_id_rm = f"scheduled_resource_mgmt_task_{uuid.uuid4().hex}"
        await app_state.persistent_task_manager.submit_task(
            task_type="dynamic_resource_allocator.start_continuous_resource_management_loop",
            payload={"interval_seconds": 300}, # Every 5 minutes
            user_id=TARIRO_ROOT_ADMIN,
            priority=1,
            initial_status="SCHEDULED_BACKGROUND_LOOP",
            initiating_session_id=task_id_rm
        )
        logger.info(f"Scheduled continuous resource management loop as task {task_id_rm}.")
    else:
        logger.warning("Persistent Task Manager not available to schedule background loops.")


    yield # Application runs here

    logger.info("Shutting down TariroStudio for this worker...")
    app_state.stop_background_workers() # Stop background workers
    await app_state.shutdown() # Call the async shutdown method
    logger.info("Shutdown complete for this worker.")

app = FastAPI(lifespan=lifespan)

# --- Helper Functions for Request Context ---
def get_studio(request: Request) -> TariroStudio:
    return request.app.state.tariro

def build_ctx(request: Request, user_id: str, session_id: Optional[str] = None) -> RequestContext:
    studio = get_studio(request)
    return RequestContext(
        user_id=user_id,
        session_id=session_id or str(uuid.uuid4()), # New session_id for each interaction if not provided
        studio=studio # Pass the studio instance
    )

# --- FastAPI Endpoints ---

@app.post("/chat/stream")
async def chat_stream_endpoint(request: Request, message: str):
    user_id = request.headers.get("x-user-id", TARIRO_ROOT_ADMIN)
    ctx = build_ctx(request, user_id)
    studio = get_studio(request)

    # Use the streaming chat method from studio_v3_core.py
    return StreamingResponse(studio.chat(message, ctx), media_type="text/plain")

@app.post("/pipeline/start")
async def pipeline_start_endpoint(
    request: Request,
    pipeline_name: str,
    prompt: str,
    coder_model_key: str,
    tester_model_key: str,
    architect_model_key: str,
    reviewer_model_key: str,
):
    user_id = request.headers.get("x-user-id", TARIRO_ROOT_ADMIN)
    session_id = str(uuid.uuid4()) # Generate a session ID for this specific pipeline initiation
    ctx = build_ctx(request, user_id, session_id)
    studio = get_studio(request)

    pipeline_map = {
        "Language Development": {
            "module": "lang_dev_goals_requirements",
            "permission": "initiate_lang_dev_pipeline",
            "func": "define_language_goals_and_requirements",
            "task_type": "lang_dev_goals_requirements.define_language_goals_and_requirements"
        },
        "Software Development": {
            "module": "app_dev_concept_ideation",
            "permission": "initiate_app_dev_pipeline",
            "func": "concept_ideation",
            "task_type": "app_dev_concept_ideation.concept_ideation"
        },
        "Operating System Development": {
            "module": "os_dev_goals_requirements",
            "permission": "initiate_os_dev_pipeline",
            "func": "define_os_goals_requirements",
            "task_type": "os_dev_goals_requirements.define_os_goals_requirements"
        },
    }

    pipeline_info = pipeline_map.get(pipeline_name)
    if not pipeline_info:
        return JSONResponse({"status": "error", "message": f"Unknown pipeline name '{pipeline_name}'."})

    if not await ctx.check_rbac(pipeline_info["permission"]):
        # The firewall applies to the content of the response, not the entire JSONResponse object directly
        firewalled_message = await ctx.apply_firewall(
            "Permission denied: You cannot initiate this pipeline.",
            "error_message"
        )
        return JSONResponse({"status": "error", "message": firewalled_message}, status_code=403)

    # Enforce coder != tester (Fixes Issue 17: Validate and fallback)
    effective_tester_key = tester_model_key
    if coder_model_key == tester_model_key:
        effective_tester_key = "deepseek-coder"

    # Build model config with actual model IDs using get_model_id
    model_config_for_pipeline = {
        "llama_architect_model": get_model_id(architect_model_key),
        "qwen_coder_model": get_model_id(coder_model_key),
        "deepseek_coder_model": get_model_id(effective_tester_key),
        "gemma_reviewer_model": get_model_id(reviewer_model_key),
        "arbiter_model": get_model_id("arbiter-model"),
        "intent-synthesizer_model": get_model_id("intent-synthesizer"),
        "mixtral_analyst_model": get_model_id("mixtral-analyst"), # Corrected from mixtral_analyst
        "claude_communicator_model": get_model_id("claude-communicator"), # Corrected from claude_communicator
    }
    
    # All modules are now accessible via studio.loaded_modules, pass them as arguments
    if studio.persistent_task_manager:
        task_payload = {
            "user_prompt": prompt,
            "requester": user_id,
            **model_config_for_pipeline,
            # Pass references to *initialized* modules here explicitly, as worker recreates studio instance
            "swarm_visualizer_module": studio.loaded_modules.get("swarm_visualizer"),
            "contextual_memory_module": studio.loaded_modules.get("contextual_memory"),
            "crud_manager_module": studio.loaded_modules.get("crud_manager"),
            "persistent_task_manager_module": studio.loaded_modules.get("persistent_task_manager"),
            "async_notification_system_module": studio.loaded_modules.get("async_notification_system"),
            "rbac_manager_module": studio.rbac,
            "secure_firewall_module": studio.secure_firewall,
            "policy_audit_trail_module": studio.policy_audit_trail,
            "client": studio.client, # Pass the OpenAI client for the worker
            "all_models": _MODEL_DESCRIPTIONS, # Pass the model descriptions for workers to use get_model_id
            # Specific pipeline modules that might be called by the task function
            "lang_dev_goals_requirements_module": studio.loaded_modules.get("lang_dev_goals_requirements"),
            "app_dev_concept_ideation_module": studio.loaded_modules.get("app_dev_concept_ideation"),
            "os_dev_goals_requirements_module": studio.loaded_modules.get("os_dev_goals_requirements"),
            # Add other modules that the specific task_type might need access to
            "self_evolution_module": studio.loaded_modules.get("self_evolution"),
            "autonomy_governance_module": studio.loaded_modules.get("autonomy_governance"),
            "universal_deployment_manager_module": studio.loaded_modules.get("universal_deployment_manager"),
            "self_hardening_defense_module": studio.loaded_modules.get("self_hardening_defense"),
            "intent_synthesizer_module": studio.loaded_modules.get("intent_synthesizer"),
            "meta_orchestrator_module": studio.loaded_modules.get("meta_orchestrator"),
            "global_state_manager_module": studio.loaded_modules.get("global_state_manager"),
            "dynamic_resource_allocator_module": studio.loaded_modules.get("dynamic_resource_allocator"),
            "redis_task_queue_module": studio.loaded_modules.get("redis_task_queue"),
            "self_architecting_engine_module": studio.loaded_modules.get("self_architecting_engine"), # NEW
            "cognitive_planning_module": studio.loaded_modules.get("cognitive_planning"), # NEW
            "omni_perceptual_fusion_module": studio.loaded_modules.get("omni_perceptual_fusion"), # NEW
            "advanced_multimodal_generation_module": studio.loaded_modules.get("advanced_multimodal_generation"), # NEW, if needed by omni_perceptual_fusion
            "meta_cognitive_reflection_module": studio.loaded_modules.get("meta_cognitive_reflection"), # NEW
            "proactive_human_ai_teaming_module": studio.loaded_modules.get("proactive_human_ai_teaming"), # NEW
            "dynamic_policy_synthesis_module": studio.loaded_modules.get("dynamic_policy_synthesis"), # NEW
            "meta_learner_module": studio.loaded_modules.get("meta_learner"),
            "formal_verification_module": studio.loaded_modules.get("formal_verification"),
            "tool_forge_module": studio.loaded_modules.get("tool_forge"),
            "evas_ethical_alignment_module": studio.loaded_modules.get("evas_ethical_alignment"),
            "global_environmental_model_module": studio.loaded_modules.get("global_environmental_model"),
            "strategic_foresight_module": studio.loaded_modules.get("strategic_foresight"),
            "external_agency_module": studio.loaded_modules.get("external_agency"),
            "real_time_model_adaptation_module": studio.loaded_modules.get("real_time_model_adaptation"),
            "cognitive_architecture_optimizer_module": studio.loaded_modules.get("cognitive_architecture_optimizer"),
            "dynamic_swarm_orchestration_module": studio.loaded_modules.get("dynamic_swarm_orchestration"),
            "autonomous_knowledge_graph_genesis_module": studio.loaded_modules.get("autonomous_knowledge_graph_genesis"),
            "self_repairing_auto_healing_module": studio.loaded_modules.get("self_repairing_auto_healing"),
            "self_replicating_expansion_module": studio.loaded_modules.get("self_replicating_expansion"),
        }
        
        submit_result = await studio.persistent_task_manager.submit_task(
            task_type=pipeline_info["task_type"],
            payload=task_payload,
            user_id=user_id,
            priority=3, # Medium-high priority for pipelines
            initial_status="PENDING_PIPELINE", # Updated initial status for clarity
            initiating_session_id=session_id
        )
        if submit_result["status"] == "success":
            return JSONResponse({"status": "success", "message": f"{pipeline_name} task {submit_result["task_id"][:8]} submitted. You will be notified of progress.", "task_id": submit_result["task_id"]})
        else:
            firewalled_message = await ctx.apply_firewall(
                f"Failed to submit task: {submit_result.get('reason', 'Unknown error')}",
                "error_message"
            )
            return JSONResponse({"status": "error", "message": firewalled_message}, status_code=500)
    else:
        return JSONResponse({"status": "error", "message": "Persistent Task Manager not loaded. Cannot submit pipeline tasks."}, status_code=500)

@app.post("/self_management/self_upgrade")
async def self_upgrade_endpoint(request: Request):
    user_id = request.headers.get("x-user-id", TARIRO_ROOT_ADMIN)
    ctx = build_ctx(request, user_id)
    studio = get_studio(request)

    if not await ctx.check_rbac("initiate_self_upgrade"):
        firewalled_message = await ctx.apply_firewall(
            "Permission denied.",
            "error_message"
        )
        return JSONResponse({"status": "error", "message": firewalled_message}, status_code=403)
    
    if studio.persistent_task_manager:
        task_payload = {
            "user_id": user_id, # Pass necessary context for worker
            "swarm_visualizer_module": studio.loaded_modules.get("swarm_visualizer"),
            "async_notification_system_module": studio.loaded_modules.get("async_notification_system"),
            "persistent_task_manager_module": studio.loaded_modules.get("persistent_task_manager"),
            "studio_core_ref_placeholder": "This is a placeholder for studio_core_ref in worker context."
        }
        submit_result = await studio.persistent_task_manager.submit_task(
            task_type="TariroStudio._handle_self_upgrade_infrastructure_task", # Internal task type
            payload=task_payload,
            user_id=user_id,
            priority=1, # Critical system task
            initial_status="PENDING_UPGRADE",
            initiating_session_id=str(uuid.uuid4())
        )
        if submit_result["status"] == "success":
            return JSONResponse({"status": "success", "message": f"Self-upgrade task {submit_result["task_id"][:8]} submitted. Check notifications.", "task_id": submit_result["task_id"]})
        else:
            firewalled_message = await ctx.apply_firewall(
                f"Failed to submit self-upgrade task: {submit_result.get('reason', 'Unknown error')}",
                "error_message"
            )
            return JSONResponse({"status": "error", "message": firewalled_message}, status_code=500)
    else:
        return JSONResponse({"status": "error", "message": "Persistent Task Manager not loaded."}, status_code=500)

@app.post("/self_management/scan_modules")
async def scan_modules_endpoint(request: Request):
    user_id = request.headers.get("x-user-id", TARIRO_ROOT_ADMIN)
    ctx = build_ctx(request, user_id)
    studio = get_studio(request)

    if not await ctx.check_rbac("scan_for_new_modules"):
        firewalled_message = await ctx.apply_firewall(
            "Permission denied.",
            "error_message"
        )
        return JSONResponse({"status": "error", "message": firewalled_message}, status_code=403)
    
    if studio.persistent_task_manager:
        task_payload = {
            "user_id": user_id, # Pass necessary context for worker
            "swarm_visualizer_module": studio.loaded_modules.get("swarm_visualizer"),
            "async_notification_system_module": studio.loaded_modules.get("async_notification_system"),
            "persistent_task_manager_module": studio.loaded_modules.get("persistent_task_manager"),
            "studio_core_ref_placeholder": "This is a placeholder for studio_core_ref in worker context."
        }
        submit_result = await studio.persistent_task_manager.submit_task(
            task_type="TariroStudio._monitor_features_directory_task", # Internal task type
            payload=task_payload,
            user_id=user_id,
            priority=2, # High priority system task
            initial_status="PENDING_SCAN",
            initiating_session_id=str(uuid.uuid4())
        )
        if submit_result["status"] == "success":
            return JSONResponse({"status": "success", "message": f"Module scan task {submit_result["task_id"][:8]} submitted. Check notifications.", "task_id": submit_result["task_id"]})
        else:
            firewalled_message = await ctx.apply_firewall(
                f"Failed to submit module scan task: {submit_result.get('reason', 'Unknown error')}",
                "error_message"
            )
            return JSONResponse({"status": "error", "message": firewalled_message}, status_code=500)
    else:
        return JSONResponse({"status": "error", "message": "Persistent Task Manager not loaded."}, status_code=500)

@app.post("/self_management/learn_lang_framework")
async def learn_lang_framework_endpoint(request: Request):
    user_id = request.headers.get("x-user-id", TARIRO_ROOT_ADMIN)
    ctx = build_ctx(request, user_id)
    studio = get_studio(request)

    if not await ctx.check_rbac("learn_new_lang_framework"):
        firewalled_message = await ctx.apply_firewall(
            "Permission denied.",
            "error_message"
        )
        return JSONResponse({"status": "error", "message": firewalled_message}, status_code=403)
    
    if studio.persistent_task_manager:
        task_payload = {
            "user_prompt": "Learn about a new high-demand programming language/framework",
            "requester": user_id,
            # Pass all relevant modules as arguments. Workers will re-initialize studio, but need these references for the task function.
            "universal_knowledge_integrator_module": studio.loaded_modules.get("universal_knowledge_integrator"),
            "intent_synthesizer_module": studio.loaded_modules.get("intent_synthesizer"),
            "meta_orchestrator_module": studio.loaded_modules.get("meta_orchestrator"),
            "lang_dev_goals_requirements_module": studio.loaded_modules.get("lang_dev_goals_requirements"),
            "contextual_memory_module": studio.loaded_modules.get("contextual_memory"),
            "policy_audit_trail_module": studio.loaded_modules.get("policy_audit_trail"),
            "openai_client": studio.client,
            "all_models": _MODEL_DESCRIPTIONS,
            "swarm_visualizer_module": studio.loaded_modules.get("swarm_visualizer"),
            "crud_manager_module": studio.loaded_modules.get("crud_manager"),
            "persistent_task_manager_module": studio.loaded_modules.get("persistent_task_manager"),
            "async_notification_system_module": studio.loaded_modules.get("async_notification_system"),
            "global_state_manager_module": studio.loaded_modules.get("global_state_manager"),
            "dynamic_resource_allocator_module": studio.loaded_modules.get("dynamic_resource_allocator"),
            "redis_task_queue_module": studio.loaded_modules.get("redis_task_queue"),
            "self_architecting_engine_module": studio.loaded_modules.get("self_architecting_engine"),
            "cognitive_planning_module": studio.loaded_modules.get("cognitive_planning"),
            "omni_perceptual_fusion_module": studio.loaded_modules.get("omni_perceptual_fusion"),
            "advanced_multimodal_generation_module": studio.loaded_modules.get("advanced_multimodal_generation"),
            "meta_cognitive_reflection_module": studio.loaded_modules.get("meta_cognitive_reflection"),
            "proactive_human_ai_teaming_module": studio.loaded_modules.get("proactive_human_ai_teaming"),
            "dynamic_policy_synthesis_module": studio.loaded_modules.get("dynamic_policy_synthesis"),
            "meta_learner_module": studio.loaded_modules.get("meta_learner"),
            "formal_verification_module": studio.loaded_modules.get("formal_verification"),
            "tool_forge_module": studio.loaded_modules.get("tool_forge"),
            "evas_ethical_alignment_module": studio.loaded_modules.get("evas_ethical_alignment"),
            "global_environmental_model_module": studio.loaded_modules.get("global_environmental_model"),
            "strategic_foresight_module": studio.loaded_modules.get("strategic_foresight"),
            "external_agency_module": studio.loaded_modules.get("external_agency"),
            "real_time_model_adaptation_module": studio.loaded_modules.get("real_time_model_adaptation"),
            "cognitive_architecture_optimizer_module": studio.loaded_modules.get("cognitive_architecture_optimizer"),
            "dynamic_swarm_orchestration_module": studio.loaded_modules.get("dynamic_swarm_orchestration"),
            "autonomous_knowledge_graph_genesis_module": studio.loaded_modules.get("autonomous_knowledge_graph_genesis"),
            "self_repairing_auto_healing_module": studio.loaded_modules.get("self_repairing_auto_healing"),
            "self_replicating_expansion_module": studio.loaded_modules.get("self_replicating_expansion"),
        }
        
        submit_result = await studio.persistent_task_manager.submit_task(
            task_type="meta_orchestrator.orchestrate_language_framework_learning", # Assumed function in meta_orchestrator
            payload=task_payload,
            user_id=user_id,
            priority=2, # High priority
            initial_status="PENDING_LEARNING",
            initiating_session_id=str(uuid.uuid4())
        )
        if submit_result["status"] == "success":
            return JSONResponse({"status": "success", "message": f"Autonomous learning task {submit_result["task_id"][:8]} submitted. You will be notified of progress.", "task_id": submit_result["task_id"]})
        else:
            firewalled_message = await ctx.apply_firewall(
                f"Failed to submit learning task: {submit_result.get('reason', 'Unknown error')}",
                "error_message"
            )
            return JSONResponse({"status": "error", "message": firewalled_message}, status_code=500)
    else:
        return JSONResponse({"status": "error", "message": "Persistent Task Manager not loaded."}, status_code=500)

@app.post("/upload")
async def upload_file_endpoint(request: Request, file: UploadFile = File(...)):
    user_id = request.headers.get("x-user-id", TARIRO_ROOT_ADMIN) # Use header for user ID or default
    ctx = build_ctx(request, user_id)
    studio = get_studio(request)

    if not studio.contextual_memory:
        return JSONResponse({"status": "error", "message": "contextual_memory module not loaded"}, status_code=500)
    if not studio.persistent_task_manager:
        return JSONResponse({"status": "error", "message": "Persistent Task Manager not loaded"}, status_code=500)

    # Save file temporarily to disk within WORKSPACE
    uploads_dir = os.path.join(WORKSPACE, "uploads")
    os.makedirs(uploads_dir, exist_ok=True)
    
    # Use a secure filename to prevent path traversal
    safe_filename = os.path.basename(file.filename)
    file_save_path = os.path.join(uploads_dir, safe_filename)
    
    try:
        with open(file_save_path, "wb") as buffer:
            # Read the file content in chunks to handle large files efficiently
            while True:
                chunk = await file.read(1024 * 1024) # Read 1MB chunks
                if not chunk:
                    break
                buffer.write(chunk)
    except Exception as e:
        logger.error(f"Error saving uploaded file {file.filename}: {e}", exc_info=True)
        return JSONResponse({"status": "error", "message": f"Failed to save uploaded file: {e}"}, status_code=500)


    # Submit file processing as a background task
    task_payload = {
        "file_path": file_save_path,
        "original_filename": file.filename,
        "mime_type": file.content_type,
        "user_id": user_id,
        "contextual_memory_module": studio.loaded_modules.get("contextual_memory"), # Pass reference
        "persistent_task_manager_module": studio.loaded_modules.get("persistent_task_manager"), # Pass reference
        "swarm_visualizer_module": studio.loaded_modules.get("swarm_visualizer"),
        "crud_manager_module": studio.loaded_modules.get("crud_manager"),
        "async_notification_system_module": studio.loaded_modules.get("async_notification_system"),
        "global_state_manager_module": studio.loaded_modules.get("global_state_manager"),
        "dynamic_resource_allocator_module": studio.loaded_modules.get("dynamic_resource_allocator"),
        "redis_task_queue_module": studio.loaded_modules.get("redis_task_queue"),
        "omni_perceptual_fusion_module": studio.loaded_modules.get("omni_perceptual_fusion"),
        "global_environmental_model_module": studio.loaded_modules.get("global_environmental_model"),
    }
    submit_result = await studio.persistent_task_manager.submit_task(
        task_type="app.process_uploaded_file_task", # Define this function in app.py if needed, or a feature module
        payload=task_payload,
        user_id=user_id,
        priority=4,
        initial_status="PENDING_UPLOAD_PROCESS",
        initiating_session_id=str(uuid.uuid4())
    )

    if submit_result["status"] == "success":
        return JSONResponse({"status": "success", "message": f"File '{file.filename}' uploaded and processing task {submit_result["task_id"][:8]} submitted.", "task_id": submit_result["task_id"]})
    else:
        # Clean up the file if task submission failed
        if os.path.exists(file_save_path):
            os.unlink(file_save_path)
        firewalled_message = await ctx.apply_firewall(
            f"Failed to submit file processing task: {submit_result.get('reason', 'Unknown error')}",
            "error_message"
        )
        return JSONResponse({"status": "error", "message": firewalled_message}, status_code=500)

# Define a task function for uploaded files that can be run by the worker framework
async def process_uploaded_file_task(task_id: str, file_path: str, original_filename: str, mime_type: str, user_id: str, contextual_memory_module: Any, persistent_task_manager_module: Any, swarm_visualizer_module: Any, async_notification_system_module: Any, omni_perceptual_fusion_module: Any, global_environmental_model_module: Any, **kwargs):
    """
    Background task to process an uploaded file and store its chunks in contextual memory.
    This function will be called by the background worker framework.
    Now uses omni_perceptual_fusion for advanced analysis if it's an image/audio.
    """
    try:
        await persistent_task_manager_module.update_task_status(task_id, "PROCESSING", progress=10, current_step="Starting file extraction.")
        logger.info(f"Task {task_id}: Processing uploaded file {original_filename}")

        text = ""
        suffix = os.path.splitext(original_filename)[1].lower()
        
        # New: Use Omni Perceptual Fusion for image/audio files
        if suffix in [".jpg", ".jpeg", ".png", ".gif"] and omni_perceptual_fusion_module:
            await persistent_task_manager_module.update_task_status(task_id, "PROCESSING", progress=20, current_step="Analyzing image with Omni Perceptual Fusion.")
            with open(file_path, "rb") as f:
                image_data = base64.b64encode(f.read()).decode('utf-8')
            
            image_analysis_result = await omni_perceptual_fusion_module.process_image_stream(
                task_id=f"{task_id}_img_analysis", # Use a sub-task ID for the analysis
                image_data_base64=image_data,
                user_id=user_id,
                analysis_prompt=f"Analyze the content and context of the uploaded image: {original_filename}. Provide key objects, scenes, and any relevant insights for Tariro Studio's operations.",
                image_analyzer_model="llama-architect" # Example model
            )
            text = image_analysis_result.get("analysis", {}).get("visual_analysis_summary", "")
            if not text:
                text = f"Analyzed image: {original_filename}. No detailed summary from fusion."
            
            # Integrate this new data into the Global Environmental Model
            if global_environmental_model_module:
                await global_environmental_model_module.integrate_data_streams(
                    task_id=f"{task_id}_gem_integrate",
                    source_type="image_stream",
                    raw_data={"image_analysis": image_analysis_result},
                    user_id=user_id
                )
        
        elif suffix in [".mp3", ".wav", ".flac"] and omni_perceptual_fusion_module:
            await persistent_task_manager_module.update_task_status(task_id, "PROCESSING", progress=20, current_step="Analyzing audio with Omni Perceptual Fusion.")
            with open(file_path, "rb") as f:
                audio_data = base64.b64encode(f.read()).decode('utf-8')

            audio_analysis_result = await omni_perceptual_fusion_module.analyze_audio_stream(
                task_id=f"{task_id}_aud_analysis", # Use a sub-task ID for the analysis
                audio_data_base64=audio_data,
                user_id=user_id,
                analysis_prompt=f"Analyze the content of the uploaded audio file: {original_filename}. Provide transcription, sound events, and any relevant insights.",
                audio_analyzer_model="mixtral-analyst" # Example model
            )
            text = audio_analysis_result.get("analysis", {}).get("audio_analysis_summary", "")
            if not text:
                text = f"Analyzed audio: {original_filename}. No detailed summary from fusion."

            # Integrate this new data into the Global Environmental Model
            if global_environmental_model_module:
                await global_environmental_model_module.integrate_data_streams(
                    task_id=f"{task_id}_gem_integrate",
                    source_type="audio_stream",
                    raw_data={"audio_analysis": audio_analysis_result},
                    user_id=user_id
                )

        elif suffix == ".pdf":
            import pypdf
            reader = pypdf.PdfReader(file_path)
            text = "\n".join([page.extract_text() or "" for page in reader.pages])
        elif suffix == ".docx":
            import docx
            doc = docx.Document(file_path)
            text = "\n".join([p.text for p in doc.paragraphs])
        else: # .txt, .md, etc.
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
        
        # For non-image/audio text files, also integrate into GEM for comprehensive environmental understanding
        if global_environmental_model_module and text:
            await global_environmental_model_module.integrate_data_streams(
                task_id=f"{task_id}_gem_integrate_text",
                source_type="document",
                raw_data={"filename": original_filename, "summary": text[:500]}, # Pass a summary for brevity
                user_id=user_id
            )


        if not text.strip():
            await persistent_task_manager_module.update_task_status(task_id, "FAILED", current_step="No text extracted/analyzed from file.")
            if os.path.exists(file_path): os.unlink(file_path)
            return {"status": "error", "message": "No text extracted/analyzed from file"}

        await persistent_task_manager_module.update_task_status(task_id, "PROCESSING", progress=40, current_step="Text extracted/analyzed, chunking content.")

        # Chunk text (1000 chars with 200 overlap)
        chunks = [text[i:i+1000] for i in range(0, len(text), 800)]
        stored = 0
        total_chunks = len(chunks)

        if not contextual_memory_module:
            raise ValueError("Contextual memory module not available in worker context.")

        for i, chunk in enumerate(chunks):
            if len(chunk.strip()) < 50: continue # Skip very small chunks
            await contextual_memory_module.store(
                user_id=user_id,
                session_id=task_id, # Use task_id as session for file processing context
                role="document",
                content=chunk,
                metadata={"source": original_filename, "chunk": i, "type": "upload", "task_id": task_id}
            )
            stored += 1
            progress_val = 40 + (i / total_chunks) * 50
            await persistent_task_manager_module.update_task_status(task_id, "PROCESSING", progress=progress_val, current_step=f"Storing chunk {i+1}/{total_chunks}.")

        await persistent_task_manager_module.update_task_status(task_id, "COMPLETED", progress=100.0, current_step="File processed and chunks stored.", output={"filename": original_filename, "chunks_stored": stored, "chars": len(text)})
        logger.info(f"Task {task_id}: Successfully processed {original_filename}, stored {stored} chunks.")
        
        if async_notification_system_module:
             await async_notification_system_module.send_notification(
                 user_id, task_id, f"File '{original_filename}' processed. {stored} chunks stored.",
                 title="File Upload Complete", category="collaboration_activity"
             )

        return {"status": "ok", "filename": original_filename, "chunks_stored": stored, "chars": len(text)}

    except Exception as e:
        logger.error(f"Task {task_id}: Error processing file {original_filename}: {e}", exc_info=True)
        await persistent_task_manager_module.update_task_status(task_id, "FAILED", current_step=f"Error during processing: {e}")
        if async_notification_system_module:
             await async_notification_system_module.send_notification(
                 user_id, task_id, f"File '{original_filename}' processed with errors. Error: {e}",
                 title="File Upload Failed", category="system_update", causal_priority="high"
             )
        return {"status": "error", "message": f"Error processing file: {e}"}
    finally:
        # Clean up the temporary file after processing or failure
        if os.path.exists(file_path):
            os.unlink(file_path)


@app.get("/tasks/{task_id}/status")
async def get_task_status_endpoint(request: Request, task_id: str):
    user_id = request.headers.get("x-user-id", TARIRO_ROOT_ADMIN)
    studio = get_studio(request)

    if not studio.persistent_task_manager:
        return JSONResponse({"status": "error", "message": "Persistent Task Manager not loaded."}, status_code=500)
    
    task_info = await studio.persistent_task_manager.get_task_status(task_id)
    if task_info["status"] == "success":
        # Ensure user can only see their own tasks unless root admin
        if task_info["task"]["user_id"] == user_id or user_id == TARIRO_ROOT_ADMIN:
            return JSONResponse({"status": "success", "task": task_info["task"]})
        else:
            firewalled_message = await build_ctx(request, user_id).apply_firewall(
                "Permission denied to view this task.",
                "error_message"
            )
            return JSONResponse({"status": "error", "message": firewalled_message}, status_code=403)
    else:
        firewalled_message = await build_ctx(request, user_id).apply_firewall(
            task_info.get("reason", "Task not found."),
            "error_message"
        )
        return JSONResponse({"status": "error", "message": firewalled_message}, status_code=404)

@app.get("/notifications")
async def get_notifications_endpoint(request: Request):
    user_id = request.headers.get("x-user-id", TARIRO_ROOT_ADMIN)
    studio = get_studio(request)

    if not studio.async_notification_system:
        return JSONResponse({"status": "error", "message": "Asynchronous Notification System not loaded."}, status_code=500)
    
    notifications = await studio.async_notification_system.get_user_notifications(user_id)
    return JSONResponse({"status": "success", "notifications": notifications})

@app.post("/notifications/{notification_id}/read")
async def mark_notification_read_endpoint(request: Request, notification_id: str):
    user_id = request.headers.get("x-user-id", TARIRO_ROOT_ADMIN)
    studio = get_studio(request)

    if not studio.async_notification_system:
        return JSONResponse({"status": "error", "message": "Asynchronous Notification System not loaded."}, status_code=500)
    
    result = await studio.async_notification_system.mark_notification_as_read(notification_id, user_id)
    # Ensure firewall for result message if any
    if result["status"] == "failed":
        result["reason"] = await build_ctx(request, user_id).apply_firewall(result.get("reason", "Unknown error"), "error_message")
    return JSONResponse(result)


@app.get("/status/modules")
async def get_module_status(request: Request):
    studio = get_studio(request)
    return JSONResponse({"loaded": len(studio.loaded_modules), "failed": len(studio.failed_modules)})

# --- Gradio UI Definition ---
def create_gradio_app():
    with gr.Blocks(title="Tariro Studio - Omniversal AGI Development Environment") as demo:
        gr.Markdown("# Tariro Studio - Omniversal AGI Development Environment")
        gr.Markdown("Welcome Samuel. All systems are online.")
        
        user_id_state = gr.State(value=TARIRO_ROOT_ADMIN) # Initial user is root admin
        
        with gr.Row():
            module_status_output = gr.Textbox(label="Module Load Status", value="Loading...", interactive=False)
            gr.Textbox(label="Current User", value=user_id_state.value, interactive=False) # Display state value, not interactive for security
            
            with gr.Column():
                notifications_btn = gr.Button("Refresh Notifications")
                notifications_display = gr.Textbox(label="Notifications", interactive=False, lines=5)
                task_status_input = gr.Textbox(label="Task ID to Monitor", placeholder="Enter Task ID")
                task_status_btn = gr.Button("Get Task Status")
                task_status_display = gr.Textbox(label="Task Status", interactive=False, lines=5)

        # Chat Tab
        with gr.Tab("Omni-Chat"):
            chatbot = gr.Chatbot()
            msg = gr.Textbox(label="Your Command", placeholder="Ask Tariro to develop a language, app, or OS...")
            clear = gr.Button("Clear Chat")
            
            async def chat_submit_gradio(message, history, user_id):
                client = httpx.AsyncClient()
                async with client.stream("POST", "http://localhost:7860/chat/stream",
                                         json={"message": message},
                                         headers={"x-user-id": user_id},
                                         timeout=None) as response:
                    history.append((message, ""))
                    current_response = ""
                    async for chunk in response.aiter_bytes():
                        decoded_chunk = chunk.decode("utf-8")
                        current_response += decoded_chunk
                        history[-1] = (message, current_response)
                        yield history, gr.update(value="")

            msg.submit(chat_submit_gradio, [msg, chatbot, user_id_state], [chatbot, msg], queue=False)
            clear.click(lambda: [], None, chatbot, queue=False)

        # Pipeline Tabs
        all_model_choices = list(_MODEL_DESCRIPTIONS.keys())
        
        def create_pipeline_tab(pipeline_name: str):
            with gr.Tab(f"{pipeline_name} Pipeline"):
                gr.Markdown(f"## Autonomous {pipeline_name} Development (Background Task)")
                pipeline_prompt = gr.Textbox(label=f"{pipeline_name} Description Prompt", placeholder=f"Describe the {pipeline_name.lower()} you want to develop (e.g., '{pipeline_name} description here').")
                
                with gr.Row():
                    coder_model = gr.Dropdown(label="Coder Agent (qwen-coder)", choices=all_model_choices, value="qwen-coder", allow_custom_value=False)
                    tester_model = gr.Dropdown(label="Tester Agent (deepseek-coder)", choices=all_model_choices, value="deepseek-coder", allow_custom_value=False)
                    architect_model = gr.Dropdown(label="Architect Agent (llama-architect)", choices=all_model_choices, value="llama-architect", allow_custom_value=False)
                    reviewer_model = gr.Dropdown(label="Reviewer Agent (gemma-reviewer)", choices=all_model_choices, value="gemma-reviewer", allow_custom_value=False)

                pipeline_output = gr.Textbox(label=f"{pipeline_name} Task Submission Status", interactive=False)
                start_pipeline_btn = gr.Button(f"Start {pipeline_name} Development as Background Task")

                async def pipeline_submit_gradio(prompt_val, coder, tester, architect, reviewer, user_id):
                    client = httpx.AsyncClient()
                    response = await client.post("http://localhost:7860/pipeline/start",
                                                 json={
                                                     "pipeline_name": pipeline_name,
                                                     "prompt": prompt_val,
                                                     "coder_model_key": coder,
                                                     "tester_model_key": tester,
                                                     "architect_model_key": architect,
                                                     "reviewer_model_key": reviewer,
                                                 },
                                                 headers={"x-user-id": user_id},
                                                 timeout=PIPELINE_TIMEOUT + 60)
                    result = response.json()
                    return result.get("message", json.dumps(result))

                start_pipeline_btn.click(
                    pipeline_submit_gradio,
                    [pipeline_prompt, coder_model, tester_model, architect_model, reviewer_model, user_id_state],
                    [pipeline_output]
                )

        create_pipeline_tab("Language Development")
        create_pipeline_tab("Software Development")
        create_pipeline_tab("Operating System Development")

        # Self-Management Tab
        with gr.Tab("Tariro Self-Management"):
            gr.Markdown("## Autonomous Infrastructure Management & Learning (Background Tasks)")
            self_upgrade_btn = gr.Button("Initiate Self-Upgrade / Infrastructure Check")
            self_upgrade_out = gr.Textbox(label="Self-Upgrade Status", interactive=False)
            
            async def self_upgrade_submit_gradio(user_id):
                client = httpx.AsyncClient()
                response = await client.post("http://localhost:7860/self_management/self_upgrade",
                                             headers={"x-user-id": user_id})
                result = response.json()
                return result.get("message", json.dumps(result))

            self_upgrade_btn.click(self_upgrade_submit_gradio, [user_id_state], [self_upgrade_out])

            scan_modules_btn = gr.Button("Scan for New Feature Modules")
            scan_modules_out = gr.Textbox(label="Module Scan Status", interactive=False)

            async def scan_modules_submit_gradio(user_id):
                client = httpx.AsyncClient()
                response = await client.post("http://localhost:7860/self_management/scan_modules",
                                             headers={"x-user-id": user_id})
                result = response.json()
                return result.get("message", json.dumps(result))
            
            scan_modules_btn.click(scan_modules_submit_gradio, [user_id_state], [scan_modules_out])

            learn_lang_framework_btn = gr.Button("Learn New Language/Framework")
            learn_lang_framework_out = gr.Textbox(label="Learning Status", interactive=False)

            async def learn_lang_framework_submit_gradio(user_id):
                client = httpx.AsyncClient()
                response = await client.post("http://localhost:7860/self_management/learn_lang_framework",
                                             headers={"x-user-id": user_id})
                result = response.json()
                return result.get("message", json.dumps(result))

            learn_lang_framework_btn.click(learn_lang_framework_submit_gradio, [user_id_state], [learn_lang_framework_out])
        
        # Knowledge Base Tab (File Upload)
        with gr.Tab("Knowledge Base"):
            gr.Markdown("Upload PDFs, DOCX, TXT, MD. They’ll be indexed and searchable in chat.")

            file_upload = gr.File(label="Upload Document", file_types=[".pdf", ".docx", ".txt", ".md", ".jpg", ".jpeg", ".png", ".gif", ".mp3", ".wav", ".flac"])
            upload_btn = gr.Button("Index Document")
            upload_out = gr.Textbox(label="Status", interactive=False)

            async def handle_upload_to_fastapi(file_obj, user_id):
                if file_obj is None:
                    return "No file selected."

                client = httpx.AsyncClient()
                # Gradio 4.x file_obj.name is path to temp file, file_obj.orig_name is original name
                if hasattr(file_obj, 'name') and os.path.exists(file_obj.name):
                    with open(file_obj.name, "rb") as f:
                        file_content = f.read()
                    original_name = file_obj.orig_name if hasattr(file_obj, 'orig_name') else os.path.basename(file_obj.name)
                    mime_type = file_obj.mime_type if hasattr(file_obj, 'mime_type') else 'application/octet-stream' # Fallback
                else:
                    return "Error: Could not read uploaded file."


                files = {'file': (original_name, file_content, mime_type)}
                
                response = await client.post("http://localhost:7860/upload",
                                             files=files,
                                             headers={"x-user-id": user_id})
                result = response.json()
                return result.get("message", json.dumps(result))

            upload_btn.click(handle_upload_to_fastapi, [file_upload, user_id_state], [upload_out])
        
        # Global UI event handlers
        module_status_output.attach_load_event(
            async def():
                client = httpx.AsyncClient()
                response = await client.get("http://localhost:7860/status/modules") # New endpoint for module status
                result = response.json()
                return f"Loaded: {result.get('loaded', 0)}, Failed: {result.get('failed', 0)}"
            , None, module_status_output, every=5
        )

        async def get_notifications_gradio(user_id):
            client = httpx.AsyncClient()
            response = await client.get("http://localhost:7860/notifications", headers={"x-user-id": user_id})
            result = response.json()
            if result.get("status") == "success":
                # Format notifications for display
                formatted_n = []
                for n in result["notifications"]:
                    # Limit content length for display
                    content_preview = n['content'][:100] + ('...' if len(n['content']) > 100 else '')
                    formatted_n.append(f"[{n['created_at'].split('T')[1].split('.')[0]}] {n['title']} (Task: {n.get('linked_task_id', 'N/A')[:8]}) - {content_preview}")
                return "\n".join(formatted_n) if formatted_n else "No new notifications."
            return "Failed to load notifications."
        
        async def get_task_status_gradio(task_id_val, user_id):
            if not task_id_val:
                return "Please enter a Task ID."
            client = httpx.AsyncClient()
            response = await client.get(f"http://localhost:7860/tasks/{task_id_val}/status", headers={"x-user-id": user_id})
            result = response.json()
            if result.get("status") == "success":
                task = result["task"]
                # Truncate output for display
                output_summary = json.dumps(task['output'], indent=2)
                output_summary_truncated = output_summary[:200] + ('...' if len(output_summary) > 200 else '')

                return (f"Task ID: {task['task_id'][:8]}\n"
                        f"Type: {task['task_type']}\n"
                        f"Status: {task['status']} ({task['progress']:.1f}%)\n"
                        f"Current Step: {task['current_step']}\n"
                        f"Last Update: {task['updated_at'].split('T')[1].split('.')[0]}\n"
                        f"Output Summary: {output_summary_truncated}")
            return f"Error: {result.get('message', 'Failed to retrieve task status.')}"

        notifications_btn.click(get_notifications_gradio, [user_id_state], [notifications_display])
        task_status_btn.click(get_task_status_gradio, [task_status_input, user_id_state], [task_status_display])
        

    return demo

# Mount Gradio app on FastAPI
gradio_app = create_gradio_app()
app = gr.mount_gradio_app(app, gradio_app, path="/")

# Main entry point for local development via uvicorn
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=7860, workers=1, reload=True)
