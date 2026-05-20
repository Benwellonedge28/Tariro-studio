import os
import asyncio
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

from tariro.runtime.autonomy_runtime import AutonomyRuntime

logger = logging.getLogger("TariroStudioApp")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Booting AutonomyRuntime (v4)...")
    runtime = AutonomyRuntime()
    app.state.runtime = runtime
    await runtime.boot()
    logger.info("AutonomyRuntime v4 ONLINE.")
    yield
    logger.info("Shutting down AutonomyRuntime v4...")
    await runtime.shutdown()
    logger.info("Shutdown complete.")


app = FastAPI(title="Tariro Studio v4", lifespan=lifespan)


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


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=7860, reload=False)
