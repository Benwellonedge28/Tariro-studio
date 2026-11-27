# Maintenance failure vocabulary

**ZIP-MAINTENANCE-ERROR-001 · v1.0 · Owner:** Maintenance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/maintenance/src/error.rs`

## Required implementation behavior

Separate insufficient capacity, migration busy, unverified backup, denied cleanup, unsupported upgrade and recovery incomplete.

## Acceptance

**ZIP-MAINTENANCE-ERROR-T01.** A missing restore check never maps to safe cleanup.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
