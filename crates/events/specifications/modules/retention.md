# Retention and replay boundary

**ZIP-EVENTS-RETENTION-001 · v1.0 · Owner:** Events maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/events/src/retention.rs`

## Required implementation behavior

Calculate reaping only from approved retention, pinned evidence and declared consumer protections. Commit new low watermark and deletions together. Snapshot manifest remains accessible under scope.

## Acceptance

**ZIP-EVENTS-RETENTION-T01.** Retain pinned evidence and verify old remembered cursors distinctly expire.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
