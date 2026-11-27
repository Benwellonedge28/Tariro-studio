# Qualified transport dispatch

**ZIP-NETWORKING-TRANSPORT-001 · v1.0 · Owner:** Networking maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/networking/src/transport.rs`

## Required implementation behavior

Choose adapter by approved scheme, negotiated capabilities and exact endpoint policy. Bind admitted bytes, time and connection scope before opening.

## Acceptance

**ZIP-NETWORKING-TRANSPORT-T01.** Unsupported transport cannot fall back to an unapproved scheme.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
