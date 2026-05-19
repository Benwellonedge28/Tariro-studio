import asyncio
import logging
import random
from typing import Dict, List, Optional

logger = logging.getLogger("AdaptiveModelRouter")


class AdaptiveModelRouter:
    """
    Intelligent multi-provider routing layer.

    Dynamically selects:
    - fastest endpoint
    - cheapest provider
    - local-first execution
    - offline-safe fallback
    """

    def __init__(self, model_registry):
        self.model_registry = model_registry

        self.latency_scores: Dict[str, float] = {}
        self.failure_scores: Dict[str, int] = {}

    async def select_model(
        self,
        capability: str,
        prefer_local: bool = True
    ):

        candidates = []

        for model in self.model_registry.list_models():

            if capability not in model.capabilities:
                continue

            candidates.append(model)

        if not candidates:
            raise RuntimeError(
                f"No compatible model for capability={capability}"
            )

        if prefer_local:
            local_models = [
                m for m in candidates
                if m.provider == "local"
            ]

            if local_models:
                candidates = local_models

        ranked = sorted(
            candidates,
            key=lambda m: (
                self.failure_scores.get(m.model_id, 0),
                self.latency_scores.get(m.model_id, 0)
            )
        )

        return ranked[0]

    async def record_latency(
        self,
        model_id: str,
        latency: float
    ):
        self.latency_scores[model_id] = latency

    async def record_failure(
        self,
        model_id: str
    ):
        self.failure_scores[model_id] = (
            self.failure_scores.get(model_id, 0) + 1
        )
