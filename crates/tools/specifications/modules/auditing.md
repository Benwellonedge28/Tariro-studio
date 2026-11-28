# Tool effect evidence

**ZIP-TOOLS-AUDITING-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/auditing.rs`

## Boundary and inputs

Record redacted intent before privileged dispatch, binding tool identity and edition, request digest, actor, grant, lease, policy and scoped artifact references. Use the injected required audit owner. Keep raw tool inputs and outputs outside general audit records.

## Behavior and failure handling

Append settlement under the original operation identity and keep known status separate from unknown effect. An unavailable mandatory intent append blocks dispatch. Ambiguous append status requires original-identity reconciliation. A safe status may report no verified result without revealing secrets or other scope.

## Acceptance

**ZIP-TOOLS-AUDITING-T01.** Fail the required intent write and verify zero dispatches. After a synthetic confirmed operation, lose the audit reply and reconcile exactly one final record. Inspect retained bytes for absent secret canaries.
