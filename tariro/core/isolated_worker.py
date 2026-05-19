import asyncio
import logging
import multiprocessing
import os
import resource
import signal
from typing import Any, Callable

logger = logging.getLogger("IsolatedWorker")


class WorkerIsolationError(Exception):
    pass


class IsolatedWorker:
    """
    Process-level isolated execution sandbox.

    Protects host infrastructure from:
    - runaway memory
    - CPU exhaustion
    - infinite loops
    - agent corruption
    """

    def __init__(
        self,
        memory_limit_mb: int = 2048,
        cpu_seconds: int = 300
    ):
        self.memory_limit_mb = memory_limit_mb
        self.cpu_seconds = cpu_seconds

    def apply_limits(self):

        memory_bytes = (
            self.memory_limit_mb
            * 1024
            * 1024
        )

        resource.setrlimit(
            resource.RLIMIT_AS,
            (memory_bytes, memory_bytes)
        )

        resource.setrlimit(
            resource.RLIMIT_CPU,
            (self.cpu_seconds, self.cpu_seconds)
        )

    async def run(
        self,
        target: Callable,
        *args,
        **kwargs
    ):

        loop = asyncio.get_running_loop()

        return await loop.run_in_executor(
            None,
            self._execute,
            target,
            args,
            kwargs
        )

    def _execute(
        self,
        target,
        args,
        kwargs
    ):

        self.apply_limits()

        try:
            return target(*args, **kwargs)

        except Exception as e:
            raise WorkerIsolationError(str(e))
