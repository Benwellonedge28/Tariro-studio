# Opaque credential references

**ZIP-IDENTITY-CREDENTIALS-001 · v1.0 · Owner:** Identity maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/identity/src/credentials.rs`

## Required implementation behavior

Expose owner/adapter-scoped key references only. Resolve in authorized security adapter; never persist credential bytes in identity state.

## Acceptance

**ZIP-IDENTITY-CREDENTIALS-T01.** Serialized session/actor contains reference metadata and no canary secret.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
