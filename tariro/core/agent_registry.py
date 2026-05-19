import logging
from typing import Dict, List, Optional
from tariro.core.models import RuntimeAgent

logger = logging.getLogger("RuntimeAgentRegistry")

class RuntimeAgentRegistry:
    """
    Manages the registration and lookup of autonomous agents.
    """
    def __init__(self):
        self.agents: Dict[str, RuntimeAgent] = {}

    def register_agent(self, agent: RuntimeAgent):
        """Registers an agent with the runtime."""
        if agent.agent_id in self.agents:
            logger.warning(f"Agent {agent.agent_id} already registered. Overwriting.")
        self.agents[agent.agent_id] = agent
        logger.info(f"Agent {agent.display_name} ({agent.agent_id}) registered.")

    def get_agent(self, agent_id: str) -> Optional[RuntimeAgent]:
        """Retrieves a registered agent by its ID."""
        return self.agents.get(agent_id)

    def list_agents(self) -> List[RuntimeAgent]:
        """Returns a list of all registered agents."""
        return list(self.agents.values())
