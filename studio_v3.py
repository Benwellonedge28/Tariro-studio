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
from contextlib import asynccontextmanager
from typing import Any, Dict, List, Optional, Tuple, Set, Callable

# ─── Third-Party ─────────────────────────────────────────────────────────────
import gradio as gr
import httpx
from fastapi import FastAPI, Request
import uvicorn
from openai import AsyncOpenAI
import qdrant_client
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# ─── Environment & Constants ──────────────────────────────────────────────────
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
QDRANT_URL = os.getenv("QDRANT_URL", "http://qdrant:6333")

LLM_API_TIMEOUT = 120.0
FIREWALL_TIMEOUT = 30.0
PIPELINE_TIMEOUT = 600.0

# ─── Logging ─────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler(os.path.join(WORKSPACE, "tariro_studio.log"))]
)
logger = logging.getLogger("TariroStudio")

# ─── Model Config ────────────────────────────────────────────────────────────
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

# ─── Immutable Core Verification ─────────────────────────────────────────────
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

# ─── Stateless Request Context ───────────────────────────────────────────────
class RequestContext:
    def __init__(self, user_id: str, session_id: str, studio: 'TariroStudio'):
        self.user_id = user_id
        self.session_id = session_id
        self.client = studio.client
        self.modules = studio.loaded_modules
        self.audit = studio.policy_audit_trail
        self.rbac = studio.rbac
        self.firewall = studio.secure_firewall
        self._rbac_fn = studio._perform_rbac_check
        self._firewall_fn = studio._apply_anti_leak_firewall

    async def check_rbac(self, permission: str) -> bool:
        return await self._rbac_fn(permission, self.user_id)

    async def apply_firewall(self, content: str, context: str = "output") -> str:
        return await self._firewall_fn(content, context, self.user_id)

# ─── TariroStudio Class ──────────────────────────────────────────────────────
class TariroStudio:
    def __init__(self):
        verify_hashes()
        self.client = AsyncOpenAI(base_url=OPENAI_BASE_URL, api_key=OPENAI_API_KEY, timeout=LLM_API_TIMEOUT)
        self.scheduler = AsyncIOScheduler()
        self.loaded_modules: Dict[str, Any] = {}
        self.failed_modules: Dict[str, str] = {}
        self.available_models = _MODEL_DESCRIPTIONS

        # Core Bootstrap
        self.policy_audit_trail = self._safe_import("policy_audit_trail")
        self.rbac = self._safe_import("rbac_manager")
        self.secure_firewall = self._safe_import("secure_cognitive_defense_grid")

        global _RBAC_GLOBAL_STATUS
        if self.rbac:
            self.rbac.initialize_rbac_manager(self.policy_audit_trail)
            _RBAC_GLOBAL_STATUS = True
        
        self._load_all_features()
        self.scheduler.start()
        self.scheduler.add_job(self._scheduled_scan, 'interval', seconds=60, max_instances=1)
        logger.info("Tariro Studio Instance Initialized")

    def _safe_import(self, name: str) -> Optional[Any]:
        with _import_lock:
            path = os.path.join(FEATURES_DIR, f"{name}.py")
            if os.path.exists(path):
                hasher = hashlib.sha256()
                with open(path, "rb") as f:
                    while chunk := f.read(8192): hasher.update(chunk)
                file_hash = "sha256:" + hasher.hexdigest()
                expected = _ALLOWED_HASHES.get(f"features/{name}.py")
                if expected and not hmac.compare_digest(file_hash, expected):
                    logger.error(f"Hash mismatch for {name}")
                    self.failed_modules[name] = "Integrity violation"
                    return None
            try:
                if FEATURES_DIR not in sys.path: sys.path.insert(0, FEATURES_DIR)
                mod = importlib.import_module(name)
                if TARIRO_ENV != 'prod': importlib.reload(mod)
                self.loaded_modules[name] = mod
                return mod
            except Exception as e:
                self.failed_modules[name] = str(e)
                return None

    def _load_all_features(self):
        for f in os.listdir(FEATURES_DIR):
            if f.endswith(".py") and f != "__init__.py":
                self._safe_import(f[:-3])

    async def _scheduled_scan(self):
        self._load_all_features()
        logger.debug("Scheduled features scan complete")

    async def _perform_rbac_check(self, perm: str, uid: str) -> bool:
        if not _RBAC_GLOBAL_STATUS: return False
        try:
            return await asyncio.wait_for(self.rbac.check_permission(uid, perm, self.policy_audit_trail), timeout=FIREWALL_TIMEOUT)
        except: return False

    async def _apply_anti_leak_firewall(self, content: str, context: str, uid: str) -> str:
        if not self.secure_firewall: return content
        try:
            return await asyncio.wait_for(self.secure_firewall.filter_sensitive_data(content, context, self.policy_audit_trail), timeout=FIREWALL_TIMEOUT)
        except: return "[REDACTED DUE TO TIMEOUT/ERROR]"

    async def chat(self, text: str, ctx: RequestContext) -> str:
        if not await ctx.check_rbac("chat"): return "Denied."
        # Autonomous routing logic
        prompt = f"System Context: Autonomous Studio. User: {ctx.user_id}. Message: {text}"
        res = await self.client.chat.completions.create(model=get_model_id("llama-architect"), messages=[{"role": "user", "content": prompt}])
        return await ctx.apply_firewall(res.choices[0].message.content)

# ─── FastAPI & Lifespan ──────────────────────────────────────────────────────
_studio: Optional[TariroStudio] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global _studio
    _studio = TariroStudio()
    yield
    if _studio:
        _studio.scheduler.shutdown()
        await _studio.client.close()

app = FastAPI(lifespan=lifespan)

# ─── Gradio App ──────────────────────────────────────────────────────────────
def create_ui():
    with gr.Blocks(title="TARIRO Omniversal Studio") as demo:
        user_id_state = gr.State(value=TARIRO_ROOT_ADMIN)
        with gr.Tab("Omni-Chat"):
            chatbot = gr.Chatbot()
            msg = gr.Textbox()
            async def h(m, h, uid):
                ctx = RequestContext(uid, str(uuid.uuid4()), _studio)
                r = await _studio.chat(m, ctx)
                h.append((m, r))
                return "", h
            msg.submit(h, [msg, chatbot, user_id_state], [msg, chatbot])
        
        with gr.Tab("Pipelines"):
            p_type = gr.Dropdown(["Language", "Software", "OS"])
            p_prompt = gr.Textbox(label="Mission")
            p_out = gr.Textbox(label="Status")
            async def run_p(t, pr, uid):
                ctx = RequestContext(uid, str(uuid.uuid4()), _studio)
                mod_name = {"Language":"lang_dev_goals_requirements", "Software":"app_dev_concept_ideation", "OS":"os_dev_goals_requirements"}[t]
                mod = _studio.loaded_modules.get(mod_name)
                if not mod: return "Module not loaded."
                func = getattr(mod, list(mod.__dict__.keys())[0]) # Heuristic
                res = await asyncio.wait_for(func(task_id=ctx.session_id, user_prompt=pr, openai_client=ctx.client, requester=uid), timeout=PIPELINE_TIMEOUT)
                return str(res)
            gr.Button("Execute Mission").click(run_p, [p_type, p_prompt, user_id_state], [p_out])
            
        with gr.Tab("System"):
            status = gr.Textbox(label="Loaded Modules")
            demo.load(lambda: f"Loaded: {len(_studio.loaded_modules)}, Failed: {list(_studio.failed_modules.keys())}", outputs=status)
    return demo

app = gr.mount_gradio_app(app, create_ui(), path="/")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
