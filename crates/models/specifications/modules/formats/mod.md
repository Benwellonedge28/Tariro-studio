# Model format dispatch

**ZIP-MODELS-FORMATS-MOD-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/formats/mod.rs`

## Required implementation behavior

Select a qualified parser by manifest format and known version. Reject unsupported formats before treating bytes as tensors.

## Acceptance

**ZIP-MODELS-FORMATS-MOD-T01.** File extension alone cannot select parser.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
