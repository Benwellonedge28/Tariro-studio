# Qualified sampling controls

**ZIP-INFERENCE-SAMPLING-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/sampling.rs`

## Required implementation behavior

Validate temperature, seed, selection mode and backend semantics before generation. Reject unsupported values and record deterministic options only when qualified.

## Acceptance

**ZIP-INFERENCE-SAMPLING-T01.** Unsupported seed cannot be silently treated as deterministic.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
