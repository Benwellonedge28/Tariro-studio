# Stable authenticated principal

**ZIP-IDENTITY-PRINCIPAL-001 · v1.0 · Owner:** Identity maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/identity/src/principal.rs`

## Required implementation behavior

Pair typed principal ID and kind with trusted issuer, workspace membership revision and status. Agent, device and user roles have distinct namespaces.

## Acceptance

**ZIP-IDENTITY-PRINCIPAL-T01.** An agent cannot deserialize itself as an authenticated user.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
