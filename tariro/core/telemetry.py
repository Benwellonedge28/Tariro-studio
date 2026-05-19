import logging
from typing import Any, Dict

logger = logging.getLogger("TelemetryManager")

class TelemetryManager:
    """
    Manages telemetry data, metrics, and logging.
    """
    def __init__(self):
        logger.info("TelemetryManager initialized.")

    def record_event(self, event_name: str, data: Dict[str, Any]):
        """Records a generic telemetry event."""
        logger.info(f"Telemetry Event: {event_name}, Data: {data}")

    def record_metric(self, metric_name: str, value: float, tags: Optional[Dict[str, str]] = None):
        """Records a specific metric."""
        tags_str = ", ".join([f"{k}={v}" for k, v in tags.items()]) if tags else ""
        logger.info(f"Telemetry Metric: {metric_name}={value} (Tags: {tags_str})")
