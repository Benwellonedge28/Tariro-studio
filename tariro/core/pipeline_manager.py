import logging
from typing import Dict, Any, List
from tariro.core.models import DynamicPipeline, PipelineStage

logger = logging.getLogger("DistributedPipelineManager")

class DistributedPipelineManager:
    """
    Manages the lifecycle and state of dynamic, distributed pipelines.
    """
    def __init__(self, runtime):
        self.runtime = runtime  # Reference to the AutonomyRuntime instance
        self.pipelines: Dict[str, DynamicPipeline] = {}

    def register_pipeline(self, pipeline: DynamicPipeline):
        """Registers a new dynamic pipeline."""
        if pipeline.pipeline_id in self.pipelines:
            logger.warning(f"Pipeline {pipeline.pipeline_id} already registered. Overwriting.")
        self.pipelines[pipeline.pipeline_id] = pipeline
        logger.info(f"Pipeline {pipeline.name} ({pipeline.pipeline_id}) registered with {len(pipeline.stages)} stages.")

    def get_pipeline(self, pipeline_id: str) -> Optional[DynamicPipeline]:
        """Retrieves a registered pipeline by its ID."""
        return self.pipelines.get(pipeline_id)

    async def execute_pipeline(self, pipeline_id: str, initial_payload: Dict[str, Any]):
        """Executes a registered pipeline."""
        pipeline = self.get_pipeline(pipeline_id)
        if not pipeline:
            raise ValueError(f"Pipeline {pipeline_id} not found.")
        
        logger.info(f"Starting execution of pipeline {pipeline.name} ({pipeline_id})...")
        current_output = initial_payload

        for stage in pipeline.stages:
            logger.info(f"Executing stage {stage.name} ({stage.stage_id}) in pipeline {pipeline_id}...")
            
            if stage.execution_mode == "parallel":
                results = await asyncio.gather(*[
                    self._execute_agent_task(agent.agent_id, stage.stage_id, current_output)
                    for agent in stage.agents
                ])
                # For simplicity, combine parallel results. Real-world might need complex merge logic.
                current_output = {"parallel_results": results, "previous_output": current_output}
            elif stage.execution_mode == "sequential":
                for agent in stage.agents:
                    current_output = await self._execute_agent_task(agent.agent_id, stage.stage_id, current_output)
            else:
                raise ValueError(f"Unknown execution mode: {stage.execution_mode}")
            
            await self.runtime.checkpoint_manager.save_checkpoint(pipeline_id, stage.stage_id, current_output)
            logger.info(f"Stage {stage.stage_id} completed for pipeline {pipeline_id}.")

        logger.info(f"Pipeline {pipeline.name} ({pipeline_id}) execution completed.")
        return current_output

    async def _execute_agent_task(self, agent_id: str, stage_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Submits a task to the distributed task queue for an agent."""
        agent = self.runtime.agent_registry.get_agent(agent_id)
        if not agent:
            raise ValueError(f"Agent {agent_id} not found.")

        # Here, a real task would be created and enqueued to the DistributedTaskQueue
        # For now, simulate direct execution for simplicity
        logger.debug(f"Simulating agent {agent.display_name} ({agent_id}) execution for stage {stage_id}...")

        # In a real scenario, this would involve:
        # 1. Creating a DistributedTask
        # 2. Enqueuing it to self.runtime.task_queue
        # 3. Waiting for the result (e.g., via polling a result queue or using a Future)
        # For this mock, we'll just return a dummy result.
        
        # Simulate LLM call based on agent's role and model
        model = self.runtime.model_registry.get_model(agent.model_id)
        if not model:
            raise ValueError(f"Model {agent.model_id} not found for agent {agent_id}.")
        
        # Construct LLM prompt based on agent's system prompt and current payload
        messages = [
            {"role": "system", "content": agent.role.system_prompt},
            {"role": "user", "content": json.dumps(payload)}
        ]
        
        try:
            response = await self.runtime.client.chat.completions.create(
                model=model.model_id,
                messages=messages,
                temperature=0.7,
                max_tokens=self.runtime.execution_budget.max_tokens_per_task
            )
            agent_output = json.loads(response.choices[0].message.content) # Assuming JSON output
        except Exception as e:
            logger.error(f"Agent {agent_id} LLM call failed: {e}", exc_info=True)
            agent_output = {"error": str(e), "agent_id": agent_id, "stage_id": stage_id}

        return {"agent_id": agent_id, "output": agent_output}
