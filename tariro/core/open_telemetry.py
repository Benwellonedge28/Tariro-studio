import logging
import time
from typing import Dict, Any

logger = logging.getLogger("OpenTelemetry")


class DistributedTrace:
    def __init__(
        self,
        trace_id: str,
        pipeline_id: str,
        stage_id: str,
        agent_id: str
    ):
        self.trace_id = trace_id
        self.pipeline_id = pipeline_id
        self.stage_id = stage_id
        self.agent_id = agent_id
        self.started_at = time.time()

    def duration(self):
        return time.time() - self.started_at


class OpenTelemetryManager:
    """
    Distributed observability layer.
    """

    async def trace(
        self,
        trace: DistributedTrace,
        metadata: Dict[str, Any]
    ):

        logger.info(
            "distributed_trace",
            extra={
                "trace_id": trace.trace_id,
                "pipeline_id": trace.pipeline_id,
                "stage_id": trace.stage_id,
                "agent_id": trace.agent_id,
                "duration": trace.duration(),
                "metadata": metadata
            }
        )
