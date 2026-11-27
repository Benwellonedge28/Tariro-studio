# Immutable file payload adapter

**ZIP-STORAGE-BACKENDS-FILESYSTEM-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/backends/filesystem.rs`

## Required implementation behavior

Store objects in an admitted rooted directory; create private same-volume staging files, verify and sync before atomic promotion. No domain transaction is implemented by filename rename alone.

## Acceptance

**ZIP-STORAGE-BACKENDS-FILESYSTEM-T01.** Interrupt before rename and validate no active metadata reference appears; concurrent equal digest converges.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
