# Layer policy routing

**ZIP-MEMORY-LAYERS-MOD-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/layers/mod.rs`

## Required implementation behavior

Select qualified layer from requested purpose, scope, persistence and retention. No fallback to broader owner or archival scope.

## Acceptance

**ZIP-MEMORY-LAYERS-MOD-T01.** Missing layer returns denial or unavailable rather than escalating.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
