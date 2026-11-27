# Qualified ONNX graph import

**ZIP-MODELS-FORMATS-ONNX-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/formats/onnx.rs`

## Required implementation behavior

Parse bounded graph metadata under approved schema, validate shape and supported operations without executing graph. External assets require explicit scoped resolution.

## Acceptance

**ZIP-MODELS-FORMATS-ONNX-T01.** External reference outside admitted root cannot be loaded.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
