# Pinned loaded model cache

**ZIP-INFERENCE-MEMORY-MODEL-CACHE-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/memory/model_cache.rs`

## Required implementation behavior

Track digest, device/adapter, bytes and active handles, retain pins and verify release. Identity includes format and qualified capability.

## Acceptance

**ZIP-INFERENCE-MEMORY-MODEL-CACHE-T01.** Session keeps its required model pinned during pressure.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
