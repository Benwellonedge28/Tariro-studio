# Filesystem failure decisions

**ZIP-FILESYSTEM-ERROR-001 · v1.0 · Owner:** Filesystem maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/filesystem/src/error.rs`

## Required implementation behavior

Distinguish denied scope, invalid component, unsafe link, stale identity, unsupported platform, quota, transient I/O and ambiguous rename. Redact native paths outside current scope.

## Acceptance

**ZIP-FILESYSTEM-ERROR-T01.** An ambiguous rename cannot be safely reported as definite absence.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
