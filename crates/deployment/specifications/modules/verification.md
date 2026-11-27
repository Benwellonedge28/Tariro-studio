# Release artifact qualification

**ZIP-DEPLOYMENT-VERIFICATION-001 · v1.0 · Owner:** Deployment maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/deployment/src/verification.rs`

## Required implementation behavior

Match signatures, digest, build provenance, policy and required evidence to exact candidate. Missing or blocked checks deny promotion.

## Acceptance

**ZIP-DEPLOYMENT-VERIFICATION-T01.** Artifact altered after review fails.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
