# Deployment provider selection

**ZIP-DEPLOYMENT-PROVIDERS-MOD-001 · v1.0 · Owner:** Deployment maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/deployment/src/providers/mod.rs`

## Required implementation behavior

Negotiate qualified stage/apply/status/rollback capabilities under explicit scope and version. No silent fallback target.

## Acceptance

**ZIP-DEPLOYMENT-PROVIDERS-MOD-T01.** Missing rollback capability blocks strategy that requires it.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
