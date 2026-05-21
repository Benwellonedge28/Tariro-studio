import os
import sys
import asyncio
import importlib
import inspect
import logging
from contextlib import asynccontextmanager
from typing import Dict, Any, Optional

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import uvicorn

from tariro.runtime.autonomy_runtime import AutonomyRuntime

logger = logging.getLogger("TariroStudioApp")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

# ---------------------------------------------------------------------------
# Feature Registry — auto-discovers and initializes all features/ modules
# ---------------------------------------------------------------------------

FEATURES_DIR = os.path.join(os.path.dirname(__file__), "features")


class FeatureRegistry:
    """
    Scans the features/ directory, imports every module, and calls its
    initialize_<module_name>() function (if present) with the shared runtime
    dependencies (workspace, openai client, models map).
    """

    def __init__(self):
        self.modules: Dict[str, Any] = {}
        self.failed: Dict[str, str] = {}

    def load_all(self, runtime: AutonomyRuntime):
        if not os.path.isdir(FEATURES_DIR):
            logger.warning(f"features/ directory not found at {FEATURES_DIR}")
            return

        # Build a minimal models map from the runtime model registry
        all_models: Dict[str, str] = {
            m.model_id: m.endpoint
            for m in runtime.model_registry.list_models()
        }

        # Add features/ to sys.path so imports resolve
        if FEATURES_DIR not in sys.path:
            sys.path.insert(0, os.path.dirname(FEATURES_DIR))

        feature_files = sorted(
            f[:-3] for f in os.listdir(FEATURES_DIR)
            if f.endswith(".py") and f != "__init__.py"
        )

        logger.info(f"Loading {len(feature_files)} feature modules...")

        for module_name in feature_files:
            try:
                mod = importlib.import_module(f"features.{module_name}")
                self.modules[module_name] = mod

                # Call initialize_<module_name>() if it exists
                init_fn_name = f"initialize_{module_name}"
                init_fn = getattr(mod, init_fn_name, None)

                if init_fn and callable(init_fn):
                    sig = inspect.signature(init_fn)
                    params = list(sig.parameters.keys())

                    # Build kwargs based on what the init function expects
                    kwargs: Dict[str, Any] = {}
                    for p in params:
                        if p in ("workspace_path", "workspace"):
                            kwargs[p] = runtime.workspace
                        elif p in ("openai_client", "client"):
                            kwargs[p] = runtime.client
                        elif p in ("all_models",):
                            kwargs[p] = all_models
                        elif p in ("swarm_visualizer_module", "swarm_visualizer"):
                            kwargs[p] = self.modules.get("swarm_visualizer")
                        elif p in ("crud_manager_module", "crud_manager"):
                            kwargs[p] = self.modules.get("crud_manager")
                        elif p in ("global_state_manager_module", "global_state_manager"):
                            kwargs[p] = self.modules.get("global_state_manager")
                        elif p in ("persistent_task_manager_module", "persistent_task_manager"):
                            kwargs[p] = self.modules.get("persistent_task_manager")
                        elif p in ("async_notification_system_module", "async_notification_system"):
                            kwargs[p] = self.modules.get("async_notification_system")
                        elif p in ("contextual_memory_module", "contextual_memory"):
                            kwargs[p] = self.modules.get("contextual_memory")
                        elif p in ("cognitive_planning_module", "cognitive_planning"):
                            kwargs[p] = self.modules.get("cognitive_planning")
                        elif p in ("dynamic_swarm_orchestration_module", "dynamic_swarm_orchestration"):
                            kwargs[p] = self.modules.get("dynamic_swarm_orchestration")
                        elif p in ("meta_cognitive_reflection_module", "meta_cognitive_reflection"):
                            kwargs[p] = self.modules.get("meta_cognitive_reflection")
                        elif p in ("meta_learner_module", "meta_learner"):
                            kwargs[p] = self.modules.get("meta_learner")
                        elif p in ("intent_synthesizer_module", "intent_synthesizer"):
                            kwargs[p] = self.modules.get("intent_synthesizer")
                        elif p in ("autonomy_governance_module", "autonomy_governance"):
                            kwargs[p] = self.modules.get("autonomy_governance")
                        elif p in ("llm_compiler_module", "llm_compiler"):
                            kwargs[p] = self.modules.get("llm_compiler")
                        else:
                            kwargs[p] = None  # Pass None for unknown deps

                    init_fn(**kwargs)
                    logger.info(f"  [OK] {module_name} initialized")
                else:
                    logger.info(f"  [OK] {module_name} loaded (no initializer)")

            except Exception as e:
                self.failed[module_name] = str(e)
                logger.warning(f"  [FAIL] {module_name}: {e}")

        logger.info(
            f"Feature loading complete: "
            f"{len(self.modules)} loaded, {len(self.failed)} failed"
        )

    def get(self, name: str) -> Optional[Any]:
        return self.modules.get(name)

    def call(self, module_name: str, fn_name: str, *args, **kwargs) -> Any:
        mod = self.modules.get(module_name)
        if not mod:
            raise ValueError(f"Feature module '{module_name}' not loaded")
        fn = getattr(mod, fn_name, None)
        if not fn or not callable(fn):
            raise ValueError(f"Function '{fn_name}' not found in '{module_name}'")
        return fn(*args, **kwargs)


# ---------------------------------------------------------------------------
# FastAPI App
# ---------------------------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Booting AutonomyRuntime v4...")
    runtime = AutonomyRuntime()
    app.state.runtime = runtime
    await runtime.boot()

    logger.info("Loading feature registry...")
    registry = FeatureRegistry()
    registry.load_all(runtime)
    app.state.features = registry

    logger.info(
        f"Tariro Studio v4 ONLINE | "
        f"features={len(registry.modules)} | "
        f"failed={len(registry.failed)}"
    )
    yield

    logger.info("Shutting down...")
    await runtime.shutdown()
    logger.info("Shutdown complete.")


app = FastAPI(title="Tariro Studio v4", lifespan=lifespan)


# ---------------------------------------------------------------------------
# Core endpoints
# ---------------------------------------------------------------------------

@app.get("/health")
async def health():
    return JSONResponse({"status": "ok", "version": "v4"})


@app.get("/runtime/status")
async def runtime_status(request: Request):
    runtime: AutonomyRuntime = request.app.state.runtime
    return JSONResponse({
        "node_id": runtime.node_id,
        "agents": [a.display_name for a in runtime.agent_registry.list_agents()],
        "workspace": runtime.workspace,
    })


@app.get("/features")
async def list_features(request: Request):
    """List all loaded feature modules."""
    registry: FeatureRegistry = request.app.state.features
    return JSONResponse({
        "loaded": sorted(registry.modules.keys()),
        "failed": registry.failed,
        "total_loaded": len(registry.modules),
        "total_failed": len(registry.failed),
    })


@app.post("/features/{module_name}/call/{fn_name}")
async def call_feature(module_name: str, fn_name: str, request: Request):
    """
    Dynamically call any function in any loaded feature module.
    POST body: { "args": [], "kwargs": {} }
    """
    registry: FeatureRegistry = request.app.state.features
    body = await request.json()
    args = body.get("args", [])
    kwargs = body.get("kwargs", {})

    try:
        result = registry.call(module_name, fn_name, *args, **kwargs)
        # Await if coroutine
        if asyncio.iscoroutine(result):
            result = await result
        return JSONResponse({"status": "ok", "result": result})
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/features/{module_name}/functions")
async def list_feature_functions(module_name: str, request: Request):
    """List all callable public functions in a feature module."""
    registry: FeatureRegistry = request.app.state.features
    mod = registry.get(module_name)
    if not mod:
        raise HTTPException(status_code=404, detail=f"Module '{module_name}' not loaded")
    fns = [
        name for name, obj in inspect.getmembers(mod, inspect.isfunction)
        if not name.startswith("_")
    ]
    return JSONResponse({"module": module_name, "functions": fns})


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=7860, reload=False)
