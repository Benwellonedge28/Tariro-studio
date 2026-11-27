# Identity failure classes

**ZIP-IDENTITY-ERROR-001 · v1.0 · Owner:** Identity maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/identity/src/error.rs`

## Required implementation behavior

Distinguish malformed, unauthenticated, expired, revoked, wrong audience, stale revision and unavailable issuer. Keep sensitive context internal.

## Acceptance

**ZIP-IDENTITY-ERROR-T01.** Unauthorized caller cannot learn whether a principal exists.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
