# Bounded verified reading

**ZIP-FILESYSTEM-READER-001 · v1.0 · Owner:** Filesystem maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/filesystem/src/reader.rs`

## Required implementation behavior

Read only owned scoped regular files under byte and deadline lease; enforce stable identity and expected digest for snapshot reads. Treat partial bytes as partial.

## Acceptance

**ZIP-FILESYSTEM-READER-T01.** Truncated stream cannot emit a successful digest receipt.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
