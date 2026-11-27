# Changed-content update

**ZIP-SEARCH-INCREMENTAL-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/incremental.rs`

## Required implementation behavior

Diff source revisions, stage updated/deleted records and publish atomically, guard old cursors by generation.

## Acceptance

**ZIP-SEARCH-INCREMENTAL-T01.** Removed record cannot reappear via stale cursor.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
