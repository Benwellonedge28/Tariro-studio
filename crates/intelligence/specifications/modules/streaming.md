# Bounded ordered response stream

**ZIP-INTELLIGENCE-STREAMING-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/streaming.rs`

## Required implementation behavior

Require monotonic chunks and terminal marker, enforce cancellation, deadline and backpressure, preserve received prefix as incomplete on error.

## Acceptance

**ZIP-INTELLIGENCE-STREAMING-T01.** Missing final marker never yields successful complete response.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
