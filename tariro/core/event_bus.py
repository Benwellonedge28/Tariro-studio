import asyncio
import logging
from collections import defaultdict
from typing import Callable, Dict, Any, List

logger = logging.getLogger("AsyncEventBus")

class AsyncEventBus:
    """
    An asynchronous event bus for inter-module communication.
    """
    def __init__(self):
        self._listeners: Dict[str, List[Callable[[Any], None]]] = defaultdict(list)

    def subscribe(self, event_type: str, listener: Callable[[Any], None]):
        """Subscribe a listener function to an event type."""
        self._listeners[event_type].append(listener)
        logger.debug(f"Listener {listener.__name__} subscribed to {event_type}")

    def unsubscribe(self, event_type: str, listener: Callable[[Any], None]):
        """Unsubscribe a listener function from an event type."""
        if listener in self._listeners[event_type]:
            self._listeners[event_type].remove(listener)
            logger.debug(f"Listener {listener.__name__} unsubscribed from {event_type}")

    async def publish(self, event_type: str, payload: Any):
        """Publish an event to all subscribed listeners."""
        logger.debug(f"Publishing event '{event_type}' with payload: {payload}")
        for listener in self._listeners[event_type]:
            try:
                if asyncio.iscoroutinefunction(listener):
                    asyncio.create_task(listener(payload))
                else:
                    listener(payload)
            except Exception as e:
                logger.error(f"Error in event listener for '{event_type}': {e}", exc_info=True)
