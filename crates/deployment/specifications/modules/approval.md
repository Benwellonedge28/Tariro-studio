# Independent deployment approval

**ZIP-DEPLOYMENT-APPROVAL-001 · v1.0 · Owner:** Deployment maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/deployment/src/approval.rs`

## Required implementation behavior

Bind owner authority, target, exact artifact, effects and expiry. Revalidate at dispatch and preserve auditable decision.

## Acceptance

**ZIP-DEPLOYMENT-APPROVAL-T01.** Expired or stale review is denied before production operation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
