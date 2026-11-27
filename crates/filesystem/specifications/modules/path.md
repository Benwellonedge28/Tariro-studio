# Typed relative path

**ZIP-FILESYSTEM-PATH-001 · v1.0 · Owner:** Filesystem maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/filesystem/src/path.rs`

## Required implementation behavior

Reject empty, absolute, drive-qualified and parent-traversal components. Keep validated raw repository spelling distinct from display text and platform lookup keys.

## Acceptance

**ZIP-FILESYSTEM-PATH-T01.** Windows drive names and absolute POSIX paths fail at construction.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
