# Bounded working memory

**ZIP-MEMORY-LAYERS-WORKING-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/layers/working.rs`

## Required implementation behavior

Keep live task state under resource lease and assignment epoch only. Discard on completed/revoked task cleanup.

## Acceptance

**ZIP-MEMORY-LAYERS-WORKING-T01.** Stale execution cannot read replacement attempt memory.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
