# Supervised invocation execution

**ZIP-TOOLS-EXECUTION-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/execution.rs`

## Boundary and inputs

Verify normalized invocation, live actor and capability, lease, budget and qualified adapter before any effect. Commit stable intent and required audit evidence first. The adapter may dispatch only the exact reviewed effect under the current owner and dedicated claim.

## Behavior and failure handling

Collect bounded results and verify receipt provenance independently from output text. Unknown response preserves the intent and invokes separately authorized read-only reconciliation. No adapter acknowledgement or timeout releases unsettled occupancy. Supervisor owns stop and cleanup. Replay returns authorized status rather than invoking again.

## Acceptance

**ZIP-TOOLS-EXECUTION-T01.** Lose a simulated response for a known successful mutation and verify one dispatch. Keep the effect unresolved until trusted read proves matching scope and outcome. Reject a different payload under the same identity.
