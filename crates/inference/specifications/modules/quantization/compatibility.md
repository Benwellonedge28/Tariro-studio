# Backend quantization gate

**ZIP-INFERENCE-QUANTIZATION-COMPATIBILITY-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/quantization/compatibility.rs`

## Required implementation behavior

Verify exact model format, scheme, backend version and device support. Blended or unknown support remains unqualified.

## Acceptance

**ZIP-INFERENCE-QUANTIZATION-COMPATIBILITY-T01.** CPU support does not imply same scheme is qualified on GPU.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
