# GPU memory by device

**ZIP-RESOURCES-DISCOVERY-GPU-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/discovery/gpu.rs`

## Required implementation behavior

Expose stable device ID, backend compatibility, allocatable bytes and observation freshness. No automatic cross-device aggregation. Separate physical total from allocatable memory.

## Acceptance

**ZIP-RESOURCES-DISCOVERY-GPU-T01.** Two small devices cannot admit a single-device demand larger than either.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
