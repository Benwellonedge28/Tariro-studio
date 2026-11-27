# Scoped cursor and event client

**ZIP-SDK-EVENTS-001 · v1.0 · Owner:** Sdk maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sdk/src/events.rs`

## Required implementation behavior

Validate stream identity, version and auth, page bounded events and handle gaps by explicit resnapshot.

## Acceptance

**ZIP-SDK-EVENTS-T01.** A stale/expired cursor cannot silently skip required events.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
