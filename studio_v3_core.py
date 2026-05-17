import asyncio
import ast
import importlib
import json
import logging
import os
import re
import shlex
import subprocess
import threading
import time
import uuid
import random
import hashlib
import hmac
import signal
import sys
import atexit
import multiprocessing # Added for background worker framework
from contextlib import asynccontextmanager
from typing import Any, Dict, List, Optional, Tuple, Set, Callable, AsyncGenerator

# --- Third-Party ─────────────────────────────────────────────────────────────
# Removed gradio, httpx, fastapi, uvicorn imports - these are now in app.py
from openai import AsyncOpenAI
# import qdrant_client # No longer needed directly, handled by contextual_memory
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# --- Environment & Constants ──────────────────────────────────────────────────
WORKSPACE = os.getenv("WORKSPACE", "/app/workspace")
os.makedirs(WORKSPACE, exist_ok=True)
FEATURES_DIR = os.path.join(WORKSPACE, "features")
os.makedirs(FEATURES_DIR, exist_ok=True)

TARIRO_ENV = os.getenv('TARIRO_ENV', 'dev').lower()
TARIRO_ROOT_ADMIN = os.getenv('TARIRO_ROOT_ADMIN', '')
if TARIRO_ENV == 'prod' and not TARIRO_ROOT_ADMIN:
    print("FATAL: TARIRO_ROOT_ADMIN must be set in production.")
    sys.exit(1)
if not TARIRO_ROOT_ADMIN: TARIRO_ROOT_ADMIN = "Samuel Mukandara"

TARIRO_SECRET_KEY = os.getenv('TARIRO_SECRET_KEY', '')
if TARIRO_ENV == 'prod' and not TARIRO_SECRET_KEY:
    print("FATAL: TARIRO_SECRET_KEY must be set in production.")
    sys.exit(1)
if not TARIRO_SECRET_KEY: TARIRO_SECRET_KEY = "dev-secret-key-change-me"

OPENAI_BASE_URL = os.getenv("OPENAI_API_BASE", "http://localhost:4000/v1")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-free")
QDRANT_URL = os.getenv("QDRANT_URL", "http://qdrant:6333") # Moved here for modules to access
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0") # For Redis Task Queue

LLM_API_TIMEOUT = 120.0
FIREWALL_TIMEOUT = 30.0
PIPELINE_TIMEOUT = 600.0

# --- Logging ─────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler(os.path.join(WORKSPACE, "tariro_studio.log"))]
)
logger = logging.getLogger("TariroStudio")
# Setup multiprocessing logging for background workers
multiprocessing.log_to_stderr()
multiprocessing.get_logger().setLevel(logging.INFO)


# --- Model Config ────────────────────────────────────────────────────────────
_MODEL_MAP: Dict[str, str] = {
    "qwen-coder": os.getenv("QWEN_CODER_MODEL", "qwen2.5-coder-32b"),
    "deepseek-coder": os.getenv("DEEPSEEK_CODER_MODEL", "deepseek-coder-33b"),
    "llama-architect": os.getenv("LLAMA_ARCHITECT_MODEL", "llama-3.1-70b"),
    "gemma-reviewer": os.getenv("GEMMA_REVIEWER_MODEL", "gemma2-27b"),
    "arbiter-model": os.getenv("ARBITER_MODEL", "llama-3.1-70b"),
    "intent-synthesizer": os.getenv("INTENT_SYNTHESIZER_MODEL", "llama-3.1-70b"),
    "mixtral-analyst": os.getenv("MIXTRAL_ANALYST_MODEL", "mixtral-8x22b"),
    "claude-communicator": os.getenv("CLAUDE_COMMUNICATOR_MODEL", "claude-3.5-sonnet"),
}

_MODEL_DESCRIPTIONS = {k: f"Specialized {k} for autonomous operations." for k in _MODEL_MAP}

def get_model_id(role: str) -> str:
    return _MODEL_MAP.get(role, _MODEL_MAP["qwen-coder"])

# --- Immutable Core Verification ─────────────────────────────────────────────
_import_lock = threading.Lock()
_ALLOWED_HASHES: Dict[str, str] = {}
_RBAC_GLOBAL_STATUS: bool = False

def verify_hashes():
    global _ALLOWED_HASHES
    hash_file = os.path.join(WORKSPACE, "allowed_hashes.json")
    if not os.path.exists(hash_file):
        logger.warning("allowed_hashes.json missing. System running in unverified mode.")
        return
    try:
        with open(hash_file, "r") as f:
            data = json.load(f)
            content = data.get("content", "{}")
            signature = data.get("signature", "")
            expected = hmac.new(TARIRO_SECRET_KEY.encode(), content.encode(), hashlib.sha256).hexdigest()
            if not hmac.compare_digest(signature, expected):
                logger.critical("Security breach: allowed_hashes.json signature mismatch!")
                if TARIRO_ENV == 'prod': sys.exit(1)
            _ALLOWED_HASHES = json.loads(content).get("files", {})
    except Exception as e:
        logger.error(f"Hash verification failed: {e}")
        if TARIRO_ENV == 'prod': sys.exit(1)

# --- Stateless Request Context ───────────────────────────────────────────────
class RequestContext:
    def __init__(self, user_id: str, session_id: str, studio: 'TariroStudio'):
        self.user_id = user_id
        self.session_id = session_id
        self.client = studio.client
        self.modules = studio.loaded_modules
        self.audit = studio.policy_audit_trail # Ensure this is loaded in studio
        self.rbac = studio.rbac # Ensure this is loaded in studio
        self.firewall = studio.secure_firewall # Ensure this is loaded in studio
        self._rbac_fn = studio._perform_rbac_check
        self._firewall_fn = studio._apply_anti_leak_firewall

    async def check_rbac(self, permission: str) -> bool:
        return await self._rbac_fn(permission, self.user_id)

    async def apply_firewall(self, content: str, context: str = "output") -> str:
        return await self._firewall_fn(content, context, self.user_id)

# --- TariroStudio Class ──────────────────────────────────────────────────────
class TariroStudio:
    def __init__(self):
        verify_hashes()
        self.client = AsyncOpenAI(base_url=OPENAI_BASE_URL, api_key=OPENAI_API_KEY, timeout=LLM_API_TIMEOUT)
        self.scheduler = AsyncIOScheduler()
        self.loaded_modules: Dict[str, Any] = {}
        self.failed_modules: Dict[str, str] = {}
        self.available_models = _MODEL_DESCRIPTIONS
        self.background_workers_started = False

        # Phase 1: Core Bootstrap - Modules essential for security and basic ops
        self.policy_audit_trail = self._safe_import("policy_audit_trail")
        self.rbac = self._safe_import("rbac_manager")
        self.secure_firewall = self._safe_import("secure_cognitive_defense_grid")
        self.crud_manager = self._safe_import("crud_manager") # New: Essential for persistent tasks/notifications
        self.swarm_visualizer = self._safe_import("swarm_visualizer") # New: Essential for logging events
        self.contextual_memory = self._safe_import("contextual_memory") # New: Essential for RAG

        global _RBAC_GLOBAL_STATUS
        if self.rbac and self.policy_audit_trail:
            self.rbac.initialize_rbac_manager(self.policy_audit_trail)
            _RBAC_GLOBAL_STATUS = True
        
        # Initialize early modules if they have an init function
        if self.contextual_memory and hasattr(self.contextual_memory, 'initialize_contextual_memory'):
            asyncio.run(self.contextual_memory.initialize_contextual_memory(qdrant_url=QDRANT_URL))
        if self.swarm_visualizer and hasattr(self.swarm_visualizer, 'initialize_swarm_visualizer'):
            self.swarm_visualizer.initialize_swarm_visualizer(WORKSPACE) # Assuming it takes WORKSPACE


        # Phase 2 & 3: Load and Initialize Persistent Autonomy & Advanced State/Resource Management Modules
        self.redis_task_queue = self._safe_import("redis_task_queue") # NEW: From batch 3
        self.persistent_task_manager = self._safe_import("persistent_task_manager")
        self.async_notification_system = self._safe_import("async_notification_system")
        self.global_state_manager = self._safe_import("global_state_manager") # NEW: From batch 3
        self.dynamic_resource_allocator = self._safe_import("dynamic_resource_allocator") # NEW: From batch 3
        self.background_worker_framework = self._safe_import("background_worker_framework")
        
        # Phase 4: Load and Initialize Hyper-Adaptive & Omni-Operational Autonomy Modules
        self.self_architecting_engine = self._safe_import("self_architecting_engine") # NEW: From batch 4
        self.cognitive_planning = self._safe_import("cognitive_planning") # NEW: From batch 4
        self.omni_perceptual_fusion = self._safe_import("omni_perceptual_fusion") # NEW: From batch 4

        # Phase 5: Load and Initialize Meta-Cognition & Adaptive Interaction Modules
        self.meta_cognitive_reflection = self._safe_import("meta_cognitive_reflection") # NEW: From batch 5
        self.proactive_human_ai_teaming = self._safe_import("proactive_human_ai_teaming") # NEW: From batch 5
        self.dynamic_policy_synthesis = self._safe_import("dynamic_policy_synthesis") # NEW: From batch 5

        # Phase 6: Load and Initialize Environmental Awareness & Strategic Foresight Modules
        self.global_environmental_model = self._safe_import("global_environmental_model") # NEW: From batch 6
        self.strategic_foresight = self._safe_import("strategic_foresight") # NEW: From batch 6
        self.external_agency = self._safe_import("external_agency") # NEW: From batch 6

        # Phase 7: Load and Initialize Adaptive Learning & Cognitive Optimization Modules
        self.real_time_model_adaptation = self._safe_import("real_time_model_adaptation") # NEW: From batch 7
        self.cognitive_architecture_optimizer = self._safe_import("cognitive_architecture_optimizer") # NEW: From batch 7
        self.dynamic_swarm_orchestration = self._safe_import("dynamic_swarm_orchestration") # NEW: From batch 7

        # Phase 8: Load and Initialize Omniversal Self-Sustainability & Self-Extension Modules
        self.autonomous_knowledge_graph_genesis = self._safe_import("autonomous_knowledge_graph_genesis") # NEW: From batch 8
        self.self_repairing_auto_healing = self._safe_import("self_repairing_auto_healing") # NEW: From batch 8
        self.self_replicating_expansion = self._safe_import("self_replicating_expansion") # NEW: From batch 8


        # Initialize these new modules, passing necessary references
        if self.redis_task_queue and hasattr(self.redis_task_queue, 'initialize_redis_task_queue'):
            self.redis_task_queue.initialize_redis_task_queue(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, 
                self.persistent_task_manager, self.async_notification_system
            )
        if self.persistent_task_manager and hasattr(self.persistent_task_manager, 'initialize_persistent_task_manager'):
            self.persistent_task_manager.initialize_persistent_task_manager(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.contextual_memory, 
                self.crud_manager, self.async_notification_system, self.redis_task_queue
            )
        if self.async_notification_system and hasattr(self.async_notification_system, 'initialize_async_notification_system'):
            self.async_notification_system.initialize_async_notification_system(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, self.persistent_task_manager
            )
        if self.global_state_manager and hasattr(self.global_state_manager, 'initialize_global_state_manager'):
            self.global_state_manager.initialize_global_state_manager(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, self.policy_audit_trail, self.async_notification_system
            )
        if self.dynamic_resource_allocator and hasattr(self.dynamic_resource_allocator, 'initialize_dynamic_resource_allocator'):
            self.dynamic_resource_allocator.initialize_dynamic_resource_allocator(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, self.global_state_manager,
                self.persistent_task_manager, self.background_worker_framework, self.async_notification_system,
                self.loaded_modules.get("autonomy_governance"), self.loaded_modules.get("meta_learner"), self.loaded_modules.get("self_evolution")
            )
        if self.background_worker_framework and hasattr(self.background_worker_framework, 'initialize_background_worker_framework'):
            self.background_worker_framework.initialize_background_worker_framework(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.contextual_memory, self.crud_manager,
                self.persistent_task_manager, self.async_notification_system, self.rbac, self.secure_firewall,
                self.policy_audit_trail, self # Pass self reference to the main TariroStudio instance
            )
        if self.self_architecting_engine and hasattr(self.self_architecting_engine, 'initialize_self_architecting_engine'):
            self.self_architecting_engine.initialize_self_architecting_engine(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, self.global_state_manager,
                self.persistent_task_manager, self.async_notification_system, self.loaded_modules.get("autonomy_governance"),
                self.loaded_modules.get("self_evolution"), self.loaded_modules.get("formal_verification"),
                self.loaded_modules.get("universal_deployment_manager"), self.contextual_memory
            )
        if self.cognitive_planning and hasattr(self.cognitive_planning, 'initialize_cognitive_planning'):
            self.cognitive_planning.initialize_cognitive_planning(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, self.global_state_manager,
                self.persistent_task_manager, self.async_notification_system, self.loaded_modules.get("autonomy_governance"),
                self.dynamic_resource_allocator, self.contextual_memory, self.loaded_modules.get("meta_orchestrator")
            )
        if self.omni_perceptual_fusion and hasattr(self.omni_perceptual_fusion, 'initialize_omni_perceptual_fusion'):
            self.omni_perceptual_fusion.initialize_omni_perceptual_fusion(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, self.global_state_manager,
                self.persistent_task_manager, self.async_notification_system, self.contextual_memory,
                self.loaded_modules.get("advanced_multimodal_generation"), self.loaded_modules.get("meta_learner")
            )
        if self.meta_cognitive_reflection and hasattr(self.meta_cognitive_reflection, 'initialize_meta_cognitive_reflection'):
            self.meta_cognitive_reflection.initialize_meta_cognitive_reflection(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, self.global_state_manager,
                self.persistent_task_manager, self.async_notification_system, self.policy_audit_trail,
                self.loaded_modules.get("meta_learner"), self.loaded_modules.get("self_evolution"),
                self.loaded_modules.get("tool_forge"), self.loaded_modules.get("evas_ethical_alignment"), self.rbac
            )
        if self.proactive_human_ai_teaming and hasattr(self.proactive_human_ai_teaming, 'initialize_proactive_human_ai_teaming'):
            self.proactive_human_ai_teaming.initialize_proactive_human_ai_teaming(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, self.global_state_manager,
                self.persistent_task_manager, self.async_notification_system, self.contextual_memory,
                self.cognitive_planning, self.loaded_modules.get("autonomy_governance"),
                self.loaded_modules.get("meta_learner"), self.loaded_modules.get("intent_synthesizer")
            )
        if self.dynamic_policy_synthesis and hasattr(self.dynamic_policy_synthesis, 'initialize_dynamic_policy_synthesis'):
            self.dynamic_policy_synthesis.initialize_dynamic_policy_synthesis(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, self.global_state_manager,
                self.persistent_task_manager, self.async_notification_system, self.loaded_modules.get("autonomy_governance"),
                self.loaded_modules.get("evas_ethical_alignment"), self.loaded_modules.get("formal_verification"),
                self.policy_audit_trail, self.loaded_modules.get("meta_learner")
            )
        if self.global_environmental_model and hasattr(self.global_environmental_model, 'initialize_global_environmental_model'):
            self.global_environmental_model.initialize_global_environmental_model(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, self.global_state_manager,
                self.persistent_task_manager, self.async_notification_system, self.omni_perceptual_fusion,
                self.contextual_memory, self.meta_cognitive_reflection, self.loaded_modules.get("meta_learner")
            )
        if self.strategic_foresight and hasattr(self.strategic_foresight, 'initialize_strategic_foresight'):
            self.strategic_foresight.initialize_strategic_foresight(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, self.global_state_manager,
                self.persistent_task_manager, self.async_notification_system, self.global_environmental_model,
                self.cognitive_planning, self.dynamic_resource_allocator, self.loaded_modules.get("meta_learner"),
                self.loaded_modules.get("threat_modeler"), self.self_architecting_engine
            )
        if self.external_agency and hasattr(self.external_agency, 'initialize_external_agency'):
            self.external_agency.initialize_external_agency(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, self.global_state_manager,
                self.persistent_task_manager, self.async_notification_system, self.dynamic_policy_synthesis,
                self.loaded_modules.get("autonomy_governance"), self.secure_firewall, self.global_environmental_model,
                self.loaded_modules.get("universal_deployment_manager"), self.loaded_modules.get("evas_ethical_alignment")
            )
        if self.real_time_model_adaptation and hasattr(self.real_time_model_adaptation, 'initialize_real_time_model_adaptation'):
            self.real_time_model_adaptation.initialize_real_time_model_adaptation(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, self.global_state_manager,
                self.persistent_task_manager, self.async_notification_system, self.loaded_modules.get("meta_learner"),
                self.omni_perceptual_fusion, self.meta_cognitive_reflection
            )
        if self.cognitive_architecture_optimizer and hasattr(self.cognitive_architecture_optimizer, 'initialize_cognitive_architecture_optimizer'):
            self.cognitive_architecture_optimizer.initialize_cognitive_architecture_optimizer(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, self.global_state_manager,
                self.persistent_task_manager, self.async_notification_system, self.self_architecting_engine,
                self.meta_cognitive_reflection, self.dynamic_resource_allocator, self.loaded_modules.get("autonomy_governance"),
                self.loaded_modules.get("meta_learner")
            )
        if self.dynamic_swarm_orchestration and hasattr(self.dynamic_swarm_orchestration, 'initialize_dynamic_swarm_orchestration'):
            self.dynamic_swarm_orchestration.initialize_dynamic_swarm_orchestration(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, self.global_state_manager,
                self.persistent_task_manager, self.async_notification_system, self.cognitive_planning,
                self.external_agency, self.meta_cognitive_reflection, self.loaded_modules.get("meta_orchestrator")
            )
        if self.autonomous_knowledge_graph_genesis and hasattr(self.autonomous_knowledge_graph_genesis, 'initialize_autonomous_knowledge_graph_genesis'):
            self.autonomous_knowledge_graph_genesis.initialize_autonomous_knowledge_graph_genesis(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, self.global_state_manager,
                self.persistent_task_manager, self.async_notification_system, self.contextual_memory,
                self.meta_cognitive_reflection, self.external_agency, self.omni_perceptual_fusion,
                self.loaded_modules.get("meta_learner"), self.dynamic_policy_synthesis
            )
        if self.self_repairing_auto_healing and hasattr(self.self_repairing_auto_healing, 'initialize_self_repairing_auto_healing'):
            self.self_repairing_auto_healing.initialize_self_repairing_auto_healing(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, self.global_state_manager,
                self.persistent_task_manager, self.async_notification_system, self.dynamic_resource_allocator,
                self.meta_cognitive_reflection, self.loaded_modules.get("self_evolution"),
                self.self_architecting_engine, self.loaded_modules.get("universal_deployment_manager"),
                self.loaded_modules.get("meta_learner"), self.loaded_modules.get("formal_verification"), self.policy_audit_trail
            )
        if self.self_replicating_expansion and hasattr(self.self_replicating_expansion, 'initialize_self_replicating_expansion'):
            self.self_replicating_expansion.initialize_self_replicating_expansion(
                WORKSPACE, self.client, _MODEL_MAP, self.swarm_visualizer, self.crud_manager, self.global_state_manager,
                self.persistent_task_manager, self.async_notification_system, self.strategic_foresight,
                self.global_environmental_model, self.self_architecting_engine,
                self.loaded_modules.get("universal_deployment_manager"), self.external_agency,
                self.dynamic_swarm_orchestration, self.secure_firewall, self.loaded_modules.get("autonomy_governance")
            )


        # Load all other features (including the self-development core from last batch)
        self._load_all_features()
        # Re-initialize all features to ensure they get references to newly initialized modules
        self._initialize_all_features() 

        self.scheduler.start()
        # Schedule periodic tasks
        self.scheduler.add_job(self._scheduled_scan_for_features, 'interval', seconds=60, max_instances=1)
        # Schedule the continuous resource management loop in redis_task_queue to check for stalled tasks
        self.scheduler.add_job(
            self._scheduled_redis_stalled_task_check,
            'interval', seconds=self.redis_task_queue.TASK_TIMEOUT_SECONDS // 2, max_instances=1, # Check every half task timeout
            id='scheduled_redis_stalled_task_check', replace_existing=True
        )
        logger.info("Tariro Studio Instance Initialized")

    def _safe_import(self, name: str) -> Optional[Any]:
        """Safely imports a feature module, verifies its hash, and stores it."""
        with _import_lock:
            # First, check if the module is already loaded to prevent re-hashing/re-importing
            if name in self.loaded_modules:
                return self.loaded_modules[name]

            path = os.path.join(FEATURES_DIR, f"{name}.py")
            if not os.path.exists(path):
                self.failed_modules[name] = f"Module file not found at {path}"
                logger.error(f"Module '{name}' file not found.")
                return None
            
            # Hash verification
            hasher = hashlib.sha256()
            try:
                with open(path, "rb") as f:
                    while chunk := f.read(8192): hasher.update(chunk)
                file_hash = "sha256:" + hasher.hexdigest()
                expected = _ALLOWED_HASHES.get(f"features/{name}.py")
                if expected and not hmac.compare_digest(file_hash, expected):
                    logger.critical(f"Hash mismatch for {name}. Expected: {expected}, Got: {file_hash}")
                    self.failed_modules[name] = "Integrity violation"
                    if TARIRO_ENV == 'prod': sys.exit(1)
                    return None
                elif not expected:
                    logger.warning(f"No allowed hash found for {name}. Running unverified.")
            except Exception as e:
                logger.error(f"Error hashing module {name}: {e}")
                self.failed_modules[name] = f"Hashing error: {e}"
                if TARIRO_ENV == 'prod': sys.exit(1)
                return None
            
            # Import the module
            try:
                if FEATURES_DIR not in sys.path: sys.path.insert(0, FEATURES_DIR)
                mod = importlib.import_module(name)
                if TARIRO_ENV != 'prod': importlib.reload(mod) # Reload in dev for faster iteration
                self.loaded_modules[name] = mod
                logger.info(f"Module '{name}' loaded successfully.")
                return mod
            except Exception as e:
                self.failed_modules[name] = str(e)
                logger.error(f"Failed to import module '{name}': {e}", exc_info=True)
                return None

    def _load_all_features(self):
        """Loads all feature modules found in FEATURES_DIR."""
        logger.info("Loading all feature modules...")
        for f in os.listdir(FEATURES_DIR):
            if f.endswith(".py") and f != "__init__.py":
                module_name = f[:-3]
                # Only attempt to load if not already loaded or failed in core bootstrap phase
                if module_name not in self.loaded_modules and module_name not in self.failed_modules:
                    self._safe_import(module_name)
        logger.info(f"Finished loading features. Loaded: {len(self.loaded_modules)}, Failed: {len(self.failed_modules)}")

    def _initialize_all_features(self):
        """Calls initialize functions on all loaded feature modules."""
        logger.info("Initializing loaded feature modules (second pass)...")
        for name, module in self.loaded_modules.items():
            init_func_name = f"initialize_{name}"
            if hasattr(module, init_func_name):
                try:
                    # Generic kwargs for initialization
                    init_kwargs = {
                        "workspace_path": WORKSPACE,
                        "openai_client": self.client,
                        "all_models": _MODEL_MAP,
                        "swarm_visualizer_module": self.swarm_visualizer,
                        "contextual_memory_module": self.contextual_memory,
                        "crud_manager_module": self.crud_manager,
                        "persistent_task_manager_module": self.persistent_task_manager,
                        "async_notification_system_module": self.async_notification_system,
                        "rbac_manager_module": self.rbac,
                        "secure_firewall_module": self.secure_firewall,
                        "policy_audit_trail_module": self.policy_audit_trail,
                        "self_evolution_module": self.loaded_modules.get("self_evolution"),
                        "autonomy_governance_module": self.loaded_modules.get("autonomy_governance"),
                        "threat_modeler_module": self.loaded_modules.get("threat_modeler"),
                        "security_auditor_module": self.loaded_modules.get("security_auditor"),
                        "vulnerability_remediation_module": self.loaded_modules.get("vulnerability_remediation"),
                        "zero_trust_segmentation_module": self.loaded_modules.get("zero_trust_segmentation"),
                        "global_regulatory_change_monitoring_module": self.loaded_modules.get("global_regulatory_change_monitoring"),
                        "os_dev_packaging_build_system_module": self.loaded_modules.get("os_dev_packaging_build_system"),
                        "studio_core_ref": self, # Pass self reference to the main TariroStudio instance
                        "intent_synthesizer_module": self.loaded_modules.get("intent_synthesizer"),
                        "meta_orchestrator_module": self.loaded_modules.get("meta_orchestrator"),
                        "lang_dev_goals_requirements_module": self.loaded_modules.get("lang_dev_goals_requirements"),
                        "app_dev_concept_ideation_module": self.loaded_modules.get("app_dev_concept_ideation"),
                        "os_dev_goals_requirements_module": self.loaded_modules.get("os_dev_goals_requirements"),
                        # New for all batches
                        "redis_task_queue_module": self.redis_task_queue,
                        "global_state_manager_module": self.global_state_manager,
                        "dynamic_resource_allocator_module": self.dynamic_resource_allocator,
                        "self_architecting_engine_module": self.self_architecting_engine,
                        "cognitive_planning_module": self.cognitive_planning,
                        "omni_perceptual_fusion_module": self.omni_perceptual_fusion,
                        "meta_cognitive_reflection_module": self.meta_cognitive_reflection,
                        "proactive_human_ai_teaming_module": self.proactive_human_ai_teaming,
                        "dynamic_policy_synthesis_module": self.dynamic_policy_synthesis,
                        "global_environmental_model_module": self.global_environmental_model,
                        "strategic_foresight_module": self.strategic_foresight,
                        "external_agency_module": self.external_agency,
                        "real_time_model_adaptation_module": self.real_time_model_adaptation,
                        "cognitive_architecture_optimizer_module": self.cognitive_architecture_optimizer,
                        "dynamic_swarm_orchestration_module": self.dynamic_swarm_orchestration,
                        "autonomous_knowledge_graph_genesis_module": self.autonomous_knowledge_graph_genesis,
                        "self_repairing_auto_healing_module": self.self_repairing_auto_healing,
                        "self_replicating_expansion_module": self.self_replicating_expansion,
                        "meta_learner_module": self.loaded_modules.get("meta_learner"),
                        "formal_verification_module": self.loaded_modules.get("formal_verification"),
                        "universal_deployment_manager_module": self.loaded_modules.get("universal_deployment_manager"),
                        "advanced_multimodal_generation_module": self.loaded_modules.get("advanced_multimodal_generation"),
                        "tool_forge_module": self.loaded_modules.get("tool_forge"), # For meta_cognitive_reflection
                        "evas_ethical_alignment_module": self.loaded_modules.get("evas_ethical_alignment"), # For dynamic_policy_synthesis and meta_cognitive_reflection
                    }
                    
                    # Filter kwargs to only those accepted by the init function
                    import inspect
                    init_func = getattr(module, init_func_name)
                    func_signature = inspect.signature(init_func)
                    filtered_init_kwargs = {k: v for k, v in init_kwargs.items() if k in func_signature.parameters}
                    
                    if inspect.iscoroutinefunction(init_func):
                        asyncio.run(init_func(**filtered_init_kwargs))
                    else:
                        init_func(**filtered_init_kwargs)
                    logger.info(f"Module '{name}' initialized.")
                except Exception as e:
                    logger.error(f"Failed to initialize module '{name}': {e}", exc_info=True)
                    self.failed_modules[name] = f"Initialization error: {e}"
        logger.info("Finished initializing feature modules (second pass).")

    async def _scheduled_scan_for_features(self):
        """Periodically scans FEATURES_DIR for new modules and loads them."""
        logger.debug("Scheduled features scan for new modules initiated.")
        initial_loaded_count = len(self.loaded_modules)
        self._load_all_features() # Load new modules
        if len(self.loaded_modules) > initial_loaded_count:
            # If new modules were loaded, initialize them
            self._initialize_all_features() 
            logger.info(f"New modules detected and loaded/initialized: {len(self.loaded_modules) - initial_loaded_count}.")
        logger.debug("Scheduled features scan complete.")

    async def _scheduled_self_hardening_check(self):
        """Triggers the self-hardening defense module periodically. Called by app.py lifespan."""
        if "self_hardening_defense" in self.loaded_modules and hasattr(self.loaded_modules["self_hardening_defense"], "start_continuous_self_hardening_loop"):
            logger.info("Initiating scheduled self-hardening check...")
            try:
                if self.persistent_task_manager:
                    task_id = f"scheduled_self_hardening_{uuid.uuid4().hex}"
                    # Submit the self-hardening loop as a persistent task to be run by a worker
                    await self.persistent_task_manager.submit_task(
                        task_type="self_hardening_defense.start_continuous_self_hardening_loop", # Target function in module
                        payload={"interval_seconds": 3600}, # Pass interval as payload
                        user_id=TARIRO_ROOT_ADMIN,
                        priority=1, # Critical system task
                        initial_status="PENDING_BACKGROUND_LOOP",
                        initiating_session_id=task_id
                    )
                    logger.info(f"Continuous self-hardening loop task {task_id} submitted.")
                else:
                    logger.warning("Persistent Task Manager not available to schedule self-hardening.")

            except Exception as e:
                logger.error(f"Error scheduling self-hardening check: {e}")
        else:
            logger.warning("Self-hardening defense module not loaded or not properly initialized for scheduled check.")

    async def _scheduled_resource_management_check(self):
        """Triggers the dynamic resource allocator module periodically."""
        if self.dynamic_resource_allocator and hasattr(self.dynamic_resource_allocator, "start_continuous_resource_management_loop"):
            logger.info("Initiating scheduled resource management check...")
            try:
                if self.persistent_task_manager:
                    task_id = f"scheduled_resource_mgmt_{uuid.uuid4().hex}"
                    await self.persistent_task_manager.submit_task(
                        task_type="dynamic_resource_allocator.start_continuous_resource_management_loop",
                        payload={"interval_seconds": 300}, # Every 5 minutes
                        user_id=TARIRO_ROOT_ADMIN,
                        priority=1, # Critical system task
                        initial_status="PENDING_BACKGROUND_LOOP",
                        initiating_session_id=task_id
                    )
                    logger.info(f"Continuous resource management loop task {task_id} submitted.")
                else:
                    logger.warning("Persistent Task Manager not available to schedule resource management.")
            except Exception as e:
                logger.error(f"Error scheduling resource management check: {e}")
        else:
            logger.warning("Dynamic Resource Allocator module not loaded or not properly initialized.")

    async def _scheduled_redis_stalled_task_check(self):
        """Triggers the Redis task queue's stalled task check periodically."""
        if self.redis_task_queue and hasattr(self.redis_task_queue, "check_stalled_tasks"):
            logger.debug("Initiating scheduled Redis stalled task check...")
            try:
                task_id_stalled = f"scheduled_stalled_check_{uuid.uuid4().hex}"
                await self.redis_task_queue.check_stalled_tasks(task_id_stalled, check_interval_seconds=self.redis_task_queue.TASK_TIMEOUT_SECONDS // 2)
            except Exception as e:
                logger.error(f"Error during scheduled Redis stalled task check: {e}")
        else:
            logger.warning("Redis Task Queue not loaded or not properly initialized for stalled task check.")


    async def _perform_rbac_check(self, perm: str, uid: str) -> bool:
        """Internal RBAC check, wrapped with timeout."""
        if not self.rbac or not _RBAC_GLOBAL_STATUS: return False
        try:
            return await asyncio.wait_for(self.rbac.check_permission(uid, perm, self.policy_audit_trail), timeout=FIREWALL_TIMEOUT)
        except asyncio.TimeoutError:
            logger.error(f"RBAC check timed out for user {uid}, permission {perm}.")
            return False
        except Exception as e:
            logger.error(f"RBAC check failed for user {uid}, permission {perm}: {e}")
            return False

    async def _apply_anti_leak_firewall(self, content: str, context: str, uid: str) -> str:
        """Internal firewall application, wrapped with timeout."""
        if not self.secure_firewall: return content
        try:
            return await asyncio.wait_for(self.secure_firewall.filter_sensitive_data(content, context, self.policy_audit_trail), timeout=FIREWALL_TIMEOUT)
        except asyncio.TimeoutError:
            logger.error(f"Firewall filter timed out for user {uid}, context {context}.")
            return "[REDACTED DUE TO TIMEOUT]"
        except Exception as e:
            logger.error(f"Firewall filter failed for user {uid}, context {context}: {e}")
            return "[REDACTED DUE TO ERROR]"

    async def chat(self, text: str, ctx: RequestContext) -> AsyncGenerator[str, None]:
        """Handles streaming chat responses."""
        if not await ctx.check_rbac("chat"):
            yield "Denied."
            return

        # Autonomous routing logic - this is a simplified example
        # In a full setup, the intent_synthesizer or a meta_orchestrator would route
        prompt = f"System Context: Autonomous Studio. User: {ctx.user_id}. Message: {text}"
        
        try:
            stream = await self.client.chat.completions.create(
                model=get_model_id("llama-architect"), # Using architect for general chat
                messages=[{"role": "user", "content": prompt}],
                stream=True
            )
            full_response_content = ""
            async for chunk in stream:
                content = chunk.choices[0].delta.content or ""
                full_response_content += content
                yield content # Yield raw content for streaming
            
            # Apply firewall to the full response before final logging/storage
            final_content = await ctx.apply_firewall(full_response_content)
            
            # Log chat event (possibly to policy_audit_trail or contextual_memory)
            if self.policy_audit_trail:
                await self.policy_audit_trail.log_event(
                    ctx.session_id, "chat_response", f"User: {ctx.user_id}, Prompt: {text}, Response: {final_content}",
                    {"user_id": ctx.user_id, "session_id": ctx.session_id, "prompt": text, "response": final_content}
                )
            if self.contextual_memory:
                await self.contextual_memory.store(
                    ctx.user_id, ctx.session_id, "user", text, {"type": "chat_prompt"}
                )
                await self.contextual_memory.store(
                    ctx.user_id, ctx.session_id, "assistant", final_content, {"type": "chat_response"}
                )

        except Exception as e:
            logger.error(f"Error in chat function for user {ctx.user_id}: {e}", exc_info=True)
            yield await ctx.apply_firewall(f"An internal error occurred: {e}. Please try again.")

    async def _handle_self_upgrade_infrastructure_task(self, task_id: str, user_id: str, payload: Dict[str, Any], **kwargs):
        """
        Task function for self-upgrade/infrastructure check, executed by a worker.
        """
        logger.info(f"Task {task_id}: Initiating self-upgrade/infrastructure check by worker.")
        if self.persistent_task_manager:
            await self.persistent_task_manager.update_task_status(task_id, "PROCESSING", 10, "Starting self-upgrade process.")
        
        try:
            # Simulate actual self-upgrade actions:
            # 1. Pull latest code (or trigger CI/CD)
            # 2. Re-verify hashes
            # 3. Trigger re-load of modules
            # 4. Perform system health checks
            
            # Example: Triggering a simulated git pull and re-scan
            if self.async_notification_system:
                await self.async_notification_system.send_notification(user_id, task_id, "Simulating git pull and code verification...", title="Self-Upgrade Progress")
            
            await asyncio.sleep(5) # Simulate work

            # Rescan and reload modules
            await self._scheduled_scan_for_features()
            
            if self.async_notification_system:
                await self.async_notification_system.send_notification(user_id, task_id, "Code re-scanned and modules reloaded. Running diagnostics...", title="Self-Upgrade Progress")

            # Add more complex logic here for actual self-evolution, formal verification etc.
            if self.persistent_task_manager:
                await self.persistent_task_manager.update_task_status(task_id, "COMPLETED", 100, "Self-upgrade/infrastructure check completed successfully.", output={"action": "self_upgrade_completed"})
            if self.async_notification_system:
                await self.async_notification_system.send_notification(user_id, task_id, "Self-upgrade/infrastructure check completed.", title="Self-Upgrade Complete")
            logger.info(f"Task {task_id}: Self-upgrade/infrastructure check completed successfully.")
        except Exception as e:
            logger.error(f"Task {task_id}: Error during self-upgrade/infrastructure check: {e}", exc_info=True)
            if self.persistent_task_manager:
                await self.persistent_task_manager.update_task_status(task_id, "FAILED", 0, f"Self-upgrade failed: {e}", output={"error": str(e)})
            if self.async_notification_system:
                await self.async_notification_system.send_notification(user_id, task_id, f"Self-upgrade/infrastructure check failed: {e}", title="Self-Upgrade Failed", causal_priority="critical")


    async def _monitor_features_directory_task(self, task_id: str, user_id: str, payload: Dict[str, Any], **kwargs):
        """
        Task function for manual scan and load of new feature modules, executed by a worker.
        """
        logger.info(f"Task {task_id}: Manual scan for new feature modules initiated by worker.")
        if self.persistent_task_manager:
            await self.persistent_task_manager.update_task_status(task_id, "PROCESSING", 10, "Starting features directory scan.")
        
        try:
            initial_loaded_count = len(self.loaded_modules)
            await self._scheduled_scan_for_features() # Use await for async method
            
            new_modules_count = len(self.loaded_modules) - initial_loaded_count
            message = f"Features directory scan completed. {new_modules_count} new modules detected and loaded/initialized."
            
            if self.persistent_task_manager:
                await self.persistent_task_manager.update_task_status(task_id, "COMPLETED", 100, message, output={"new_modules_count": new_modules_count})
            if self.async_notification_system:
                await self.async_notification_system.send_notification(user_id, task_id, message, title="Module Scan Complete")
            logger.info(f"Task {task_id}: {message}")
        except Exception as e:
            logger.error(f"Task {task_id}: Error during features directory scan: {e}", exc_info=True)
            if self.persistent_task_manager:
                await self.persistent_task_manager.update_task_status(task_id, "FAILED", 0, f"Module scan failed: {e}", output={"error": str(e)})
            if self.async_notification_system:
                await self.async_notification_system.send_notification(user_id, task_id, f"Module scan failed: {e}", title="Module Scan Failed", causal_priority="critical")


    # New: Methods to manage background workers
    def start_background_workers(self, num_workers: int = 2):
        if not self.background_workers_started and self.background_worker_framework and hasattr(self.background_worker_framework, "start_worker_pool"):
            logger.info(f"Starting {num_workers} background worker(s)...")
            self.background_worker_framework.start_worker_pool(num_workers)
            self.background_workers_started = True
        else:
            logger.warning("Background worker framework not loaded or workers already started.")

    def stop_background_workers(self):
        if self.background_workers_started and self.background_worker_framework and hasattr(self.background_worker_framework, "stop_worker_pool"):
            logger.info("Stopping background worker(s)...")
            self.background_worker_framework.stop_worker_pool()
            self.background_workers_started = False
        else:
            logger.warning("Background worker framework not loaded or no workers running.")


    async def shutdown(self):
        """Graceful shutdown for Tariro Studio."""
        logger.info("Tariro Studio shutting down...")
        self.scheduler.shutdown(wait=False) # Don't wait for tasks to complete
        await self.client.aclose() # Use aclose for AsyncOpenAI
        self.stop_background_workers() # Stop background workers
        logger.info("Tariro Studio shutdown complete.")

# Removed FastAPI and Gradio related code as it moves to app.py
# ─── FastAPI & Lifespan ──────────────────────────────────────────────────────
# Moved to app.py

# ─── Gradio App ──────────────────────────────────────────────────────────────
# Moved to app.py
