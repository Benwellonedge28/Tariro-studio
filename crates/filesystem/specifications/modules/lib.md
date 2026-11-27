# Rooted filesystem facade

**ZIP-FILESYSTEM-LIB-001 · v1.0 · Owner:** Filesystem maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/filesystem/src/lib.rs`

## Required implementation behavior

Expose typed paths, scoped readers and conditional writers. Raw unrestricted native handles never cross into a task or plugin.

## Acceptance

**ZIP-FILESYSTEM-LIB-T01.** Callers cannot construct an unrestricted write handle via facade exports.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
