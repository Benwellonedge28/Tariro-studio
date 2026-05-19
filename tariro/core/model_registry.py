import logging
from typing import Dict, List, Optional
from tariro.core.models import RegisteredModel

logger = logging.getLogger("RuntimeModelRegistry")

class RuntimeModelRegistry:
    """
    Manages the registration and lookup of available LLM models.
    """
    def __init__(self):
        self.models: Dict[str, RegisteredModel] = {}

    def register_model(self, model: RegisteredModel):
        """Registers a model with the runtime."""
        if model.model_id in self.models:
            logger.warning(f"Model {model.model_id} already registered. Overwriting.")
        self.models[model.model_id] = model
        logger.info(f"Model {model.model_id} registered (Provider: {model.provider}).")

    def get_model(self, model_id: str) -> Optional[RegisteredModel]:
        """Retrieves a registered model by its ID."""
        return self.models.get(model_id)

    def list_models(self) -> List[RegisteredModel]:
        """Returns a list of all registered models."""
        return list(self.models.values())
