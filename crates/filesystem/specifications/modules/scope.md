# Filesystem scope intersection

**ZIP-FILESYSTEM-SCOPE-001 · v1.0 · Owner:** Filesystem maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/filesystem/src/scope.rs`

## Required implementation behavior

Match typed normalized target against allowed root, path and effect. Validate both old and new paths for rename. Missing capability denies before touching storage.

## Acceptance

**ZIP-FILESYSTEM-SCOPE-T01.** A permitted source cannot be moved to an unauthorized target.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
