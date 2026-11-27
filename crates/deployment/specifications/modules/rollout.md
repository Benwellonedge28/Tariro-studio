# Durable staged rollout

**ZIP-DEPLOYMENT-ROLLOUT-001 · v1.0 · Owner:** Deployment maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/deployment/src/rollout.rs`

## Required implementation behavior

Record intent and apply one approved stage under current revision and lease, observe health, then promote or pause. Reconcile ambiguous remote acknowledgment before retry.

## Acceptance

**ZIP-DEPLOYMENT-ROLLOUT-T01.** Partial rollout is reported with exact completed stages and no duplicate apply.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
