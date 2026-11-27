# Session, audience and revocation

**ZIP-SERVER-AUTHENTICATION-001 · v1.0 · Owner:** Server maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/server/src/authentication.rs`

## Required implementation behavior

Verify authenticated session, target audience, workspace and live revocation epoch before accessing route resources. Distinguish identity failure from scope denial without disclosing private existence.

## Acceptance

**ZIP-SERVER-AUTHENTICATION-T01.** Wrong audience, revoked session and stale epoch cannot enter handlers.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
