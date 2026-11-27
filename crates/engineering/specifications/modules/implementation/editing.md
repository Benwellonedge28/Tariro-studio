# Conditional edits

**ZIP-ENGINEERING-IMPLEMENTATION-EDITING-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/implementation/editing.rs`

## Required implementation behavior

Resolve exact base and file identity, normalize scoped ranges and expected blob. Preserve unrelated work and refuse stale changes.

## Acceptance

**ZIP-ENGINEERING-IMPLEMENTATION-EDITING-T01.** Concurrent edit cannot be overwritten by stale exact blob.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
