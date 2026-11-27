# Typed quantization format registry

**ZIP-INFERENCE-QUANTIZATION-FORMATS-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/quantization/formats.rs`

## Required implementation behavior

Represent exact version, tensor block or element shape, encoding and supported adapters. Validate metadata under bounded parser.

## Acceptance

**ZIP-INFERENCE-QUANTIZATION-FORMATS-T01.** Unsupported block/type fails decode without default interpretation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
