# Authenticated actor context

**ZIP-SECURITY-AUTHENTICATION-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/authentication.rs`

## Required implementation behavior

Verify issuer, audience, expiry, current identity epoch and workspace membership; resolve a scoped principal with provenance.

## Acceptance

**ZIP-SECURITY-AUTHENTICATION-T01.** Wrong audience and rotated credential cannot produce a principal.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
