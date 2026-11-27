# Scoped release signature

**ZIP-DEPLOYMENT-SIGNING-001 · v1.0 · Owner:** Deployment maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/deployment/src/signing.rs`

## Required implementation behavior

Request signing through qualified key adapter only after verifying artifact and authorization. Bind domain, release manifest and version.

## Acceptance

**ZIP-DEPLOYMENT-SIGNING-T01.** Wrong domain or key purpose fails.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
