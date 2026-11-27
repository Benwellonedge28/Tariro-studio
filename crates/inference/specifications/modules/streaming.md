# Ordered token/chunk delivery

**ZIP-INFERENCE-STREAMING-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/streaming.rs`

## Required implementation behavior

Assign monotonic sequence, enforce byte/token/account deadlines and backpressure, differentiate final completion from interrupted stream.

## Acceptance

**ZIP-INFERENCE-STREAMING-T01.** Missing terminal marker prevents a completed response.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
