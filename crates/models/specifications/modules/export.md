# Scoped model export

**ZIP-MODELS-EXPORT-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/export.rs`

## Required implementation behavior

Verify license permits destination/use, pin exact digest and stage bounded manifest and assets. Require separately approved destination.

## Acceptance

**ZIP-MODELS-EXPORT-T01.** Unknown model license cannot be exported.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
