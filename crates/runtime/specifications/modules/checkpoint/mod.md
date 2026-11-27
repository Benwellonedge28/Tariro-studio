# Checkpoint boundaries

**ZIP-RUNTIME-CHECKPOINT-MOD-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/checkpoint/mod.rs`

## Required implementation behavior

Export immutable record, writer and restore ports. Own no checkpoint titles or arbitrary filepaths; all writes follow typed storage protocol.

## Acceptance

**ZIP-RUNTIME-CHECKPOINT-MOD-T01.** A raw payload cannot be restored without validated manifest.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
