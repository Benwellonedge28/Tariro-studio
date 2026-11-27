# Bounded SafeTensors validation

**ZIP-MODELS-FORMATS-SAFETENSORS-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/formats/safetensors.rs`

## Required implementation behavior

Validate header and tensor names/shapes/offset ranges, data length and disallowed overlap under configured bounds. Do not execute content.

## Acceptance

**ZIP-MODELS-FORMATS-SAFETENSORS-T01.** Overlapping or out-of-file spans cannot produce tensors.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
