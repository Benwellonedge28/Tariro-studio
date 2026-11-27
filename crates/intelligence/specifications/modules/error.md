# Inference decision errors

**ZIP-INTELLIGENCE-ERROR-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/error.rs`

## Required implementation behavior

Distinguish no route, incompatible capability, denied disclosure, quota, invalid structured output, cancellation, partial stream and provider failure.

## Acceptance

**ZIP-INTELLIGENCE-ERROR-T01.** Partial stream is never emitted as a complete response.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
