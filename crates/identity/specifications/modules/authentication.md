# Authentication proof binding

**ZIP-IDENTITY-AUTHENTICATION-001 · v1.0 · Owner:** Identity maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/identity/src/authentication.rs`

## Required implementation behavior

Validate qualified issuer, audience, nonce or transport binding, time and current identity status. Reject unsupported provider without fallback.

## Acceptance

**ZIP-IDENTITY-AUTHENTICATION-T01.** Replay proof in another workspace or audience fails.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
