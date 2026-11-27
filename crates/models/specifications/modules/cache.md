# Model cache accounting

**ZIP-MODELS-CACHE-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/cache.rs`

## Required implementation behavior

Key immutable weight/tokenizer artifacts by digest and scope. Track size, last use and pins; capacity uses resource policy. Verify reads before activation.

## Acceptance

**ZIP-MODELS-CACHE-T01.** Cache hit with corrupted bytes cannot return qualified model.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
