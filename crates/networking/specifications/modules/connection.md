# Scoped connection lifecycle

**ZIP-NETWORKING-CONNECTION-001 · v1.0 · Owner:** Networking maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/networking/src/connection.rs`

## Required implementation behavior

Track authority revision, canonical origin, peer identity, lease and state. Reuse only compatible connections and close when rules no longer allow reuse.

## Acceptance

**ZIP-NETWORKING-CONNECTION-T01.** Revoked connection cannot dispatch another request.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
