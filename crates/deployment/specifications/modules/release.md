# Reviewed release intent

**ZIP-DEPLOYMENT-RELEASE-001 · v1.0 · Owner:** Deployment maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/deployment/src/release.rs`

## Required implementation behavior

Bind exact artifact, target, policy, schedule, evidence and effect key. Release status uses actual observed state, not compilation outcome.

## Acceptance

**ZIP-DEPLOYMENT-RELEASE-T01.** Production release cannot start from successful build alone.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
