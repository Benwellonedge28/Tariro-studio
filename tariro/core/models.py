from dataclasses import dataclass
from typing import Dict, Any, List, Optional

@dataclass
class RegisteredModel:
    model_id: str
    provider: str
    endpoint: str
    api_key: Optional[str]
    capabilities: List[str]

@dataclass
class AgentRole:
    name: str
    description: str
    system_prompt: str

@dataclass
class RuntimeAgent:
    agent_id: str
    display_name: str
    model_id: str
    role: AgentRole

@dataclass
class PipelineStage:
    stage_id: str
    name: str
    execution_mode: str # e.g., "parallel", "sequential"
    agents: List[RuntimeAgent]
    editor_stage: bool = False

@dataclass
class DynamicPipeline:
    pipeline_id: str
    name: str
    stages: List[PipelineStage]
