import asyncio
import json
import logging
import os
from typing import Any, Dict, Optional

try:
    import redis.asyncio as redis
except ImportError:
    redis = None

logger = logging.getLogger("HybridStateStore")

class HybridStateStore:
    """
    A hybrid state persistence layer supporting local JSON files and Redis.
    """
    def __init__(self, local_path: str, redis_host: Optional[str] = None, redis_port: int = 6379):
        self.local_path = local_path
        self.redis_enabled = bool(redis and redis_host)
        self.redis_client = None
        
        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        if self.redis_enabled:
            self.redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
            logger.info(f"Redis persistence enabled at {redis_host}:{redis_port}")
        else:
            logger.warning("Redis not enabled or available. Using local persistence only.")
        logger.info(f"Local persistence path: {local_path}")

    async def set_state(self, key: str, value: Dict[str, Any]):
        serialized_value = json.dumps(value)
        if self.redis_enabled and self.redis_client:
            await self.redis_client.set(key, serialized_value)
        with open(f"{self.local_path}.{key}.json", "w") as f:
            f.write(serialized_value)
        logger.debug(f"State for key '{key}' saved.")

    async def get_state(self, key: str) -> Optional[Dict[str, Any]]:
        if self.redis_enabled and self.redis_client:
            redis_value = await self.redis_client.get(key)
            if redis_value:
                logger.debug(f"State for key '{key}' retrieved from Redis.")
                return json.loads(redis_value)
        
        local_file_path = f"{self.local_path}.{key}.json"
        if os.path.exists(local_file_path):
            with open(local_file_path, "r") as f:
                local_value = f.read()
                logger.debug(f"State for key '{key}' retrieved from local file.")
                return json.loads(local_value)
        logger.debug(f"State for key '{key}' not found.")
        return None

    async def delete_state(self, key: str):
        if self.redis_enabled and self.redis_client:
            await self.redis_client.delete(key)
        local_file_path = f"{self.local_path}.{key}.json"
        if os.path.exists(local_file_path):
            os.remove(local_file_path)
        logger.debug(f"State for key '{key}' deleted.")

    async def health_check(self) -> bool:
        if self.redis_enabled and self.redis_client:
            try:
                await self.redis_client.ping()
                return True
            except Exception as e:
                logger.error(f"Redis health check failed: {e}")
                return False
        return True # If Redis is not enabled, local storage is always considered healthy
