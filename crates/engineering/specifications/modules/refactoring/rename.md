# Scope-aware symbol rename

**ZIP-ENGINEERING-REFACTORING-RENAME-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/refactoring/rename.rs`

## Required implementation behavior

Resolve declaration and qualified references at pinned snapshot, validate collision and changed paths, then stage exact diff.

## Acceptance

**ZIP-ENGINEERING-REFACTORING-RENAME-T01.** Unresolved reference makes complete rename claim unavailable.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
