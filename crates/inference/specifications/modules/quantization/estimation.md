# Checked resource estimate

**ZIP-INFERENCE-QUANTIZATION-ESTIMATION-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/quantization/estimation.rs`

## Required implementation behavior

Compute bytes and overhead from validated tensor dimensions and qualified layout. Reject overflow, unknown layout and unsupported required precision.

## Acceptance

**ZIP-INFERENCE-QUANTIZATION-ESTIMATION-T01.** Malformed dimensions cannot overflow into small admitted allocation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
