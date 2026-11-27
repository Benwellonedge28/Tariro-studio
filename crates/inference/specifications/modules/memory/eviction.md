# Deterministic eligible reclamation

**ZIP-INFERENCE-MEMORY-EVICTION-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/memory/eviction.rs`

## Required implementation behavior

Evict only unpinned compatible device entries according to approved usage/age order. Reconcile release before admitting new capacity.

## Acceptance

**ZIP-INFERENCE-MEMORY-EVICTION-T01.** Pinned model survives eviction pressure.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
