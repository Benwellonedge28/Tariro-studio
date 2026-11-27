# Streaming byte integrity

**ZIP-FILESYSTEM-CHECKSUM-001 · v1.0 · Owner:** Filesystem maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/filesystem/src/checksum.rs`

## Required implementation behavior

Hash scoped bytes under budget with qualified algorithm and verify final length; record typed digest with no secret or raw path in errors.

## Acceptance

**ZIP-FILESYSTEM-CHECKSUM-T01.** Single-byte mutation, premature EOF and oversized input are detected.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
