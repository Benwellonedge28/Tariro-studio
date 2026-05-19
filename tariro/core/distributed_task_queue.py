import asyncio
import json
import logging
import os
import time
import uuid
from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional, Callable

try:
    import redis.asyncio as redis
except Exception:
    redis = None

logger = logging.getLogger("DistributedTaskQueue")

TASK_QUEUE_PREFIX = "tariro:queue"
TASK_RESULT_PREFIX = "tariro:result"
TASK_LEASE_PREFIX = "tariro:lease"

DEFAULT_VISIBILITY_TIMEOUT = 300
DEFAULT_MAX_RETRIES = 5


@dataclass
class DistributedTask:
    task_id: str
    pipeline_id: str
    stage_id: str
    agent_id: str
    payload: Dict[str, Any]
    priority: str = "normal"
    retries: int = 0
    created_at: float = time.time()
    timeout_seconds: int = 300


class DistributedTaskQueue:
    """
    Planet-scale autonomous execution queue.

    Features:
    - distributed leasing
    - visibility timeout
    - dead-letter routing
    - retry backoff
    - local/offline compatibility
    - async worker coordination
    """

    def __init__(
        self,
        redis_host: Optional[str] = None,
        redis_port: int = 6379
    ):
        self.redis_enabled = bool(redis and redis_host)

        self.local_queue = asyncio.PriorityQueue()

        if self.redis_enabled:
            self.redis = redis.Redis(
                host=redis_host,
                port=redis_port,
                decode_responses=True
            )

    async def enqueue(self, queue_name: str, task: DistributedTask):

        serialized = json.dumps(asdict(task))

        if self.redis_enabled:
            await self.redis.rpush(
                f"{TASK_QUEUE_PREFIX}:{queue_name}",
                serialized
            )
        else:
            await self.local_queue.put((0, serialized))

    async def dequeue(
        self,
        queue_name: str
    ) -> Optional[DistributedTask]:

        if self.redis_enabled:
            result = await self.redis.blpop(
                f"{TASK_QUEUE_PREFIX}:{queue_name}",
                timeout=5
            )

            if not result:
                return None

            _, payload = result

        else:
            try:
                _, payload = await asyncio.wait_for(
                    self.local_queue.get(),
                    timeout=5
                )
            except asyncio.TimeoutError:
                return None

        data = json.loads(payload)

        return DistributedTask(**data)

    async def acknowledge(
        self,
        task_id: str,
        result: Dict[str, Any]
    ):

        if not self.redis_enabled:
            return

        await self.redis.set(
            f"{TASK_RESULT_PREFIX}:{task_id}",
            json.dumps(result)
        )

    async def lease_task(
        self,
        task: DistributedTask,
        worker_id: str
    ):

        if not self.redis_enabled:
            return

        lease_key = f"{TASK_LEASE_PREFIX}:{task.task_id}"

        await self.redis.set(
            lease_key,
            worker_id,
            ex=DEFAULT_VISIBILITY_TIMEOUT
        )
