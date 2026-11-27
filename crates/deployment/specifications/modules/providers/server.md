# Scoped server deployment

**ZIP-DEPLOYMENT-PROVIDERS-SERVER-001 · v1.0 · Owner:** Deployment maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/deployment/src/providers/server.rs`

## Required implementation behavior

Bind authenticated target and activation receipt; verify approved stage, transfer and health checks before promotion.

## Acceptance

**ZIP-DEPLOYMENT-PROVIDERS-SERVER-T01.** Wrong server identity receives no package.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
