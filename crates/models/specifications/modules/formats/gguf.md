# Bounded GGUF metadata validation

**ZIP-MODELS-FORMATS-GGUF-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/formats/gguf.rs`

## Required implementation behavior

Use qualified parser, validate header/version, tensor dimensions, byte offsets and declared types with checked arithmetic. Reject unsupported quantization.

## Acceptance

**ZIP-MODELS-FORMATS-GGUF-T01.** Malformed offset or overflow returns typed invalid data without allocation over budget.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
