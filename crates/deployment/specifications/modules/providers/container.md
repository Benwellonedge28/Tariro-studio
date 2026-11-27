# Qualified container rollout

**ZIP-DEPLOYMENT-PROVIDERS-CONTAINER-001 · v1.0 · Owner:** Deployment maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/deployment/src/providers/container.rs`

## Required implementation behavior

Verify image digest, qualified runtime, namespace and bounded policy before stage. Inspect actual provider receipt and reconcile retargeting.

## Acceptance

**ZIP-DEPLOYMENT-PROVIDERS-CONTAINER-T01.** Mutable image tag alone cannot authorize deployment.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
