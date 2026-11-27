# Admitted model loading

**ZIP-MODELS-LOADER-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/loader.rs`

## Required implementation behavior

Verify immutable manifest, device/format, policy and finite memory lease before map/read. Publish handle only after verified initialization.

## Acceptance

**ZIP-MODELS-LOADER-T01.** Allocation failure returns cleanup status and no usable handle.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
