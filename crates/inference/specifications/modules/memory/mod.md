# Memory accounting boundary

**ZIP-INFERENCE-MEMORY-MOD-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/memory/mod.rs`

## Required implementation behavior

Expose reservation, KV/model caches and eviction through lease ownership. Capacities derive from resource manager.

## Acceptance

**ZIP-INFERENCE-MEMORY-MOD-T01.** Model code cannot allocate an unbounded cache through facade.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
