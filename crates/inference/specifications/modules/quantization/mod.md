# Quantization negotiation boundary

**ZIP-INFERENCE-QUANTIZATION-MOD-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/quantization/mod.rs`

## Required implementation behavior

Map qualified formats, compatibility and estimation. Never infer tensor layout or backend support from label.

## Acceptance

**ZIP-INFERENCE-QUANTIZATION-MOD-T01.** Unknown quantization is rejected before model load.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
