# Actual response representation

**ZIP-INFERENCE-RESPONSE-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/response.rs`

## Required implementation behavior

Distinguish complete, partial, failed and cancelled, with exact chunks and observed usage provenance. Reject invalid finish reason.

## Acceptance

**ZIP-INFERENCE-RESPONSE-T01.** Backend disconnect leaves prefix marked partial.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
