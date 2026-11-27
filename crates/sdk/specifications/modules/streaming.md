# Bounded reconnect and stream status

**ZIP-SDK-STREAMING-001 · v1.0 · Owner:** Sdk maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sdk/src/streaming.rs`

## Required implementation behavior

Honor negotiated sequence/cursor, application limits and cancellation; retries only for safe supported resumptions. Mark incomplete prefixes.

## Acceptance

**ZIP-SDK-STREAMING-T01.** Disconnect before end never yields completed result.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
