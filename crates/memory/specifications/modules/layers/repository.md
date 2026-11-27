# Pinned repository memory

**ZIP-MEMORY-LAYERS-REPOSITORY-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/layers/repository.rs`

## Required implementation behavior

Bind stable repository ID, revision and evidence, invalidating stale observations according to policy.

## Acceptance

**ZIP-MEMORY-LAYERS-REPOSITORY-T01.** Renamed repo retains stable identity but reused display name does not.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
