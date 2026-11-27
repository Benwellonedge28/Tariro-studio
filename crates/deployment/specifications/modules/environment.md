# Verified deployment target

**ZIP-DEPLOYMENT-ENVIRONMENT-001 · v1.0 · Owner:** Deployment maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/deployment/src/environment.rs`

## Required implementation behavior

Bind stable target/tenant identity, allowed scope, platform, health capabilities and current revision. Separate staging and production environments.

## Acceptance

**ZIP-DEPLOYMENT-ENVIRONMENT-T01.** Matching display name cannot substitute another target.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
