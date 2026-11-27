# Backend format compatibility

**ZIP-MODELS-COMPATIBILITY-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/compatibility.rs`

## Required implementation behavior

Intersect verified format/tokenizer, backend versions and resource requirements; return qualified support or typed gap. No inference based on filename.

## Acceptance

**ZIP-MODELS-COMPATIBILITY-T01.** Unsupported quantization variant fails before loading weights.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
