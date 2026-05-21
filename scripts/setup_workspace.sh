#!/bin/sh
# Setup all Tariro Studio workspace directories
# Usage: ./scripts/setup_workspace.sh [BASE_PATH]

BASE="${1:-${TARIRO_WORKSPACE:-./workspace}}"
echo "Setting up workspace at: $BASE"

dirs="
advanced_multimodal_outputs
adversarial_ai_logs
agent_configs
agi_sandbox/execution_logs
agi_sandbox/risk_reports
alignment_logs
anomaly_detection_logs
automation_scripts
autonomy_policies
backlog_proposals
causal_inference_logs
cognitive_allocation_logs
contextual_memory_data
data_integrity_logs
decision_path_logs
deployment_logs
emergent_behavior_logs
entity_data
ethical_conflict_logs
goal_recalibration_logs
meta_learning_logs
multimodal_outputs
network_healer_logs
optimization_logs
policy_audit_logs
policy_enforcement_logs
quantum_crypto_manager
resource_optimization_logs
sdk_outputs
security_audits
self_evolution
sensory_fusion_logs
simulated_codebase
spatial_data
swarm_events
task_automation_logs
threat_model_logs
tools/bin
tools/specs
ui_adaptation_logs
vulnerability_remediation_logs
workflows
zero_trust_logs
"

for d in $dirs; do
  mkdir -p "$BASE/$d"
  echo "  OK: $BASE/$d"
done

echo "Workspace setup complete."
