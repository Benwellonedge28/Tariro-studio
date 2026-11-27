# Explicit external identity negotiation

**ZIP-IDENTITY-FEDERATION-001 · v1.0 · Owner:** Identity maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/identity/src/federation.rs`

## Required implementation behavior

Pin issuer and subject mapping, advertised protocol major and local approval. No implicit user creation on issuer collision.

## Acceptance

**ZIP-IDENTITY-FEDERATION-T01.** Same subject from another issuer cannot access local account.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
