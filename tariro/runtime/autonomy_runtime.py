import asyncio
import logging
import os
import signal
import uuid

from openai import AsyncOpenAI

from tariro.core.event_bus import AsyncEventBus
from tariro.core.persistence import HybridStateStore
from tariro.core.pipeline_manager import DistributedPipelineManager
from tariro.core.model_registry import RuntimeModelRegistry
from tariro.core.agent_registry import RuntimeAgentRegistry
from tariro.core.telemetry import TelemetryManager
from tariro.core.security import SecurityKernel
from tariro.core.registry import ModuleRegistry

from tariro.core.distributed_task_queue import (
    DistributedTaskQueue
)

from tariro.core.adaptive_model_router import (
    AdaptiveModelRouter
)

from tariro.core.checkpointing import (
    CheckpointManager
)

from tariro.core.execution_budget import (
    ExecutionBudget
)

from tariro.core.open_telemetry import (
    OpenTelemetryManager
)

from tariro.core.models import (
    RegisteredModel,
    RuntimeAgent,
    AgentRole,
    PipelineStage,
    DynamicPipeline
)

logger = logging.getLogger("AutonomyRuntime")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)


class AutonomyRuntime:
    """
    Infinite Distributed Sovereign Intelligence Fabric.
    """

    def __init__(self):

        self.workspace = os.getenv(
            "TARIRO_WORKSPACE",
            "/app/workspace"
        )

        os.makedirs(self.workspace, exist_ok=True)

        self.node_id = str(uuid.uuid4())

        self.event_bus = AsyncEventBus()

        self.persistence = HybridStateStore(
            local_path=os.path.join(
                self.workspace,
                "runtime.db"
            ),
            redis_host=os.getenv("REDIS_HOST")
        )

        self.telemetry = TelemetryManager()

        self.security = SecurityKernel()

        self.registry = ModuleRegistry(
            self.workspace,
            self.security
        )

        self.model_registry = RuntimeModelRegistry()

        self.agent_registry = RuntimeAgentRegistry()

        self.task_queue = DistributedTaskQueue(
            redis_host=os.getenv("REDIS_HOST")
        )

        self.model_router = AdaptiveModelRouter(
            self.model_registry
        )

        self.checkpoint_manager = CheckpointManager(
            self.persistence
        )

        self.otel = OpenTelemetryManager()

        self.execution_budget = ExecutionBudget()

        self.client = AsyncOpenAI(
            api_key=os.getenv(
                "OPENAI_API_KEY",
                "sk-local"
            ),
            base_url=os.getenv(
                "OPENAI_API_BASE",
                "http://localhost:11434/v1"
            ),
            timeout=120.0
        )

        self.pipeline_manager = DistributedPipelineManager(
            self
        )

    async def boot(self):

        logger.info(
            f"Node booting | node_id={self.node_id}"
        )

        await self._verify_environment()

        await self._initialize_models()

        await self._initialize_agents()

        await self._initialize_pipeline()

        asyncio.create_task(
            self._autonomous_worker_loop()
        )

        logger.info("Autonomous fabric ONLINE.")

    async def _verify_environment(self):

        if not await self.persistence.health_check():
            raise RuntimeError(
                "Persistence layer unavailable."
            )

    async def _initialize_models(self):

        self.model_registry.register_model(
            RegisteredModel(
                model_id="llama-architect",
                provider="local",
                endpoint="http://localhost:11434",
                api_key=None,
                capabilities=[
                    "architecture",
                    "reasoning"
                ]
            )
        )

        self.model_registry.register_model(
            RegisteredModel(
                model_id="qwen-editor",
                provider="local",
                endpoint="http://localhost:11434",
                api_key=None,
                capabilities=[
                    "editing",
                    "refinement"
                ]
            )
        )

    async def _initialize_agents(self):

        architect = RuntimeAgent(
            agent_id=str(uuid.uuid4()),
            display_name="Architect",
            model_id="llama-architect",
            role=AgentRole(
                name="architect",
                description="System architect",
                system_prompt=(
                    "Design resilient distributed systems."
                )
            )
        )

        editor = RuntimeAgent(
            agent_id=str(uuid.uuid4()),
            display_name="Editor",
            model_id="qwen-editor",
            role=AgentRole(
                name="editor",
                description="Output refinement",
                system_prompt=(
                    "Refine technical accuracy and clarity."
                )
            )
        )

        self.agent_registry.register_agent(architect)

        self.agent_registry.register_agent(editor)

    async def _initialize_pipeline(self):

        agents = self.agent_registry.list_agents()

        pipeline = DynamicPipeline(
            pipeline_id="core-pipeline",
            name="Infinite Fabric",
            stages=[
                PipelineStage(
                    stage_id="architecture",
                    name="Architecture Generation",
                    execution_mode="parallel",
                    agents=[agents[0]]
                ),
                PipelineStage(
                    stage_id="editorial",
                    name="Editorial Refinement",
                    execution_mode="sequential",
                    agents=[agents[1]],
                    editor_stage=True
                )
            ]
        )

        self.pipeline_manager.register_pipeline(
            pipeline
        )

    async def _autonomous_worker_loop(self):

        while True:

            try:
                task = await self.task_queue.dequeue(
                    "critical"
                )

                if not task:
                    await asyncio.sleep(1)
                    continue

                logger.info(
                    f"Executing task={task.task_id}"
                )

            except Exception as e:
                logger.error(
                    f"Worker loop failure: {e}"
                )

                await asyncio.sleep(5)

    async def shutdown(self):

        logger.info("Shutdown initiated.")

        await self.client.aclose()

        logger.info("Runtime offline.")


async def main():

    runtime = AutonomyRuntime()

    loop = asyncio.get_running_loop()

    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(
            sig,
            lambda: asyncio.create_task(
                runtime.shutdown()
            )
        )

    await runtime.boot()

    while True:
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())
