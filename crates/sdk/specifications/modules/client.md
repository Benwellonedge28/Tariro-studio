# Versioned scoped API client

**ZIP-SDK-CLIENT-001 · v1.0 · Owner:** Sdk maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sdk/src/client.rs`

## Required implementation behavior

Negotiate transport, identity and capabilities; configure finite time/body/queue limits and enforce scope per request. No hidden remote provider.

## Acceptance

**ZIP-SDK-CLIENT-T01.** Offline configuration produces no external connection.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
