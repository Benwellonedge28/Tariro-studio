# Deployment failure vocabulary

**ZIP-DEPLOYMENT-ERROR-001 · v1.0 · Owner:** Deployment maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/deployment/src/error.rs`

## Required implementation behavior

Distinguish integrity, missing qualification, denied approval, stale target, ambiguous apply, unhealthy rollout and rollback blocked.

## Acceptance

**ZIP-DEPLOYMENT-ERROR-T01.** Timeout is not represented as definite absence.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
