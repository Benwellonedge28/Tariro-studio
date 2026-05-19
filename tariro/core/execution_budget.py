from dataclasses import dataclass


@dataclass
class ExecutionBudget:
    """
    Hard runtime governance constraints.
    """

    max_tokens_per_task: int = 32768
    max_parallel_agents: int = 50
    max_runtime_seconds: int = 3600
    max_cost_usd: float = 100.0
    max_pipeline_stages: int = 50
