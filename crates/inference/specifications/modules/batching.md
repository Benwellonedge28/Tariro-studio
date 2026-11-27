# Resource- and scope-safe batching

**ZIP-INFERENCE-BATCHING-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/batching.rs`

## Required implementation behavior

Group only compatible backend/model/workspace scope and authorized data class. Reserve summed capacity and keep per-request output boundaries.

## Acceptance

**ZIP-INFERENCE-BATCHING-T01.** Two incompatible scopes cannot be combined even if shapes match.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
