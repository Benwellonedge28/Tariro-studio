# Qualified link handling

**ZIP-FILESYSTEM-SYMLINK-001 · v1.0 · Owner:** Filesystem maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/filesystem/src/symlink.rs`

## Required implementation behavior

Classify path components without following. Explicitly prohibit link traversal for untrusted writes; support bounded link reads only where policy and platform prove root containment.

## Acceptance

**ZIP-FILESYSTEM-SYMLINK-T01.** A reparse point or symlink to outside root cannot be used for mutation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
