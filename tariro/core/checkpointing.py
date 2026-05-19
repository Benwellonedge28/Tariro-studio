import hashlib
import json
import time
from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass
class PipelineCheckpoint:
    pipeline_id: str
    stage_id: str
    state: Dict[str, Any]
    version: int
    created_at: float

    def checksum(self) -> str:
        payload = json.dumps(
            self.state,
            sort_keys=True
        ).encode()

        return hashlib.sha256(payload).hexdigest()


class CheckpointManager:
    """
    Transaction-safe resumable execution layer.
    """

    def __init__(self, persistence):
        self.persistence = persistence

    async def save_checkpoint(
        self,
        pipeline_id: str,
        stage_id: str,
        state: Dict[str, Any]
    ):

        checkpoint = PipelineCheckpoint(
            pipeline_id=pipeline_id,
            stage_id=stage_id,
            state=state,
            version=int(time.time()),
            created_at=time.time()
        )

        await self.persistence.set_state(
            f"checkpoint:{pipeline_id}",
            {
                **asdict(checkpoint),
                "checksum": checkpoint.checksum()
            }
        )

    async def restore_checkpoint(
        self,
        pipeline_id: str
    ) -> Dict[str, Any]:

        return await self.persistence.get_state(
            f"checkpoint:{pipeline_id}"
        )
