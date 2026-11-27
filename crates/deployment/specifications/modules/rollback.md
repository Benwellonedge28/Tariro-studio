# Separately governed rollback

**ZIP-DEPLOYMENT-ROLLBACK-001 · v1.0 · Owner:** Deployment maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/deployment/src/rollback.rs`

## Required implementation behavior

Verify compatible known-good artifact, current target and applicable scope. Reconcile unknown results and preserve prior receipts.

## Acceptance

**ZIP-DEPLOYMENT-ROLLBACK-T01.** Incompatible previous release cannot be activated by automatic rollback.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
