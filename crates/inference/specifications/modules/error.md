# Inference failure taxonomy

**ZIP-INFERENCE-ERROR-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/error.rs`

## Required implementation behavior

Separate incompatible model, device unavailable, budget/resource exhaustion, denied egress, cancelled, partial response and adapter failure.

## Acceptance

**ZIP-INFERENCE-ERROR-T01.** Partial response cannot be converted to verified success.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
