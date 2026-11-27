# Model registry boundary

**ZIP-MODELS-LIB-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/lib.rs`

## Required implementation behavior

Expose model identity, manifests, admission and qualified adapter interfaces. Import does not load weights or use network.

## Acceptance

**ZIP-MODELS-LIB-T01.** Registry-only consumer starts no inference process.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
