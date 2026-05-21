"""
Tariro Studio Workspace
=======================
This package provides helpers to ensure all required workspace
subdirectories exist at runtime. Called automatically by AutonomyRuntime
on boot, and can also be run as a standalone script.
"""

import os
import logging

logger = logging.getLogger("workspace")

WORKSPACE_DIRS = [
    "advanced_multimodal_outputs",
    "adversarial_ai_logs",
    "agent_configs",
    "agi_sandbox/execution_logs",
    "agi_sandbox/risk_reports",
    "alignment_logs",
    "anomaly_detection_logs",
    "automation_scripts",
    "autonomy_policies",
    "backlog_proposals",
    "causal_inference_logs",
    "cognitive_allocation_logs",
    "contextual_memory_data",
    "data_integrity_logs",
    "decision_path_logs",
    "deployment_logs",
    "emergent_behavior_logs",
    "entity_data",
    "ethical_conflict_logs",
    "goal_recalibration_logs",
    "meta_learning_logs",
    "multimodal_outputs",
    "network_healer_logs",
    "optimization_logs",
    "policy_audit_logs",
    "policy_enforcement_logs",
    "quantum_crypto_manager",
    "resource_optimization_logs",
    "sdk_outputs",
    "security_audits",
    "self_evolution",
    "sensory_fusion_logs",
    "simulated_codebase",
    "spatial_data",
    "swarm_events",
    "task_automation_logs",
    "threat_model_logs",
    "tools/bin",
    "tools/specs",
    "ui_adaptation_logs",
    "vulnerability_remediation_logs",
    "workflows",
    "zero_trust_logs",
]


def setup_workspace(base_path: str) -> None:
    """Create all required workspace subdirectories under base_path."""
    created = 0
    for subdir in WORKSPACE_DIRS:
        full = os.path.join(base_path, subdir)
        if not os.path.exists(full):
            os.makedirs(full, exist_ok=True)
            logger.debug(f"Created workspace dir: {full}")
            created += 1
    if created:
        logger.info(f"Workspace setup: created {created} directories under {base_path}")
    else:
        logger.info(f"Workspace OK: all directories exist under {base_path}")


def get_workspace_dir(name: str, base_path: str | None = None) -> str:
    """Return absolute path to a named workspace subdirectory, creating it if needed."""
    if base_path is None:
        base_path = os.getenv("TARIRO_WORKSPACE", "/app/workspace")
    full = os.path.join(base_path, name)
    os.makedirs(full, exist_ok=True)
    return full


if __name__ == "__main__":
    import sys
    base = sys.argv[1] if len(sys.argv) > 1 else os.getenv("TARIRO_WORKSPACE", "./workspace")
    logging.basicConfig(level=logging.INFO)
    setup_workspace(base)
    print(f"Workspace ready at: {base}")
