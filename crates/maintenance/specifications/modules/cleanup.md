# Explicit scoped cleanup

**ZIP-MAINTENANCE-CLEANUP-001 · v1.0 · Owner:** Maintenance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/maintenance/src/cleanup.rs`

## Required implementation behavior

Require authorization, verify current retention and pins, pause during migration/low-disk recovery, and reconcile partial removals. No automatic destructive default.

## Acceptance

**ZIP-MAINTENANCE-CLEANUP-T01.** Pinned artifact or required backup is never deleted.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
