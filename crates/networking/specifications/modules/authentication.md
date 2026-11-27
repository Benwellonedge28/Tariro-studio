# Audience-bound peer authentication

**ZIP-NETWORKING-AUTHENTICATION-001 · v1.0 · Owner:** Networking maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/networking/src/authentication.rs`

## Required implementation behavior

Verify peer identity, issuer, required proof and audience against configured trust. Resolve own credential reference within the admitted adapter only.

## Acceptance

**ZIP-NETWORKING-AUTHENTICATION-T01.** Wrong audience cannot authenticate to a new origin.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
