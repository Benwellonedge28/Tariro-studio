# Scoped maintenance facade

**ZIP-MAINTENANCE-LIB-001 · v1.0 · Owner:** Maintenance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/maintenance/src/lib.rs`

## Required implementation behavior

Expose monitoring, proposal, backup and recovery ports. Linking starts no cleanup or updates.

## Acceptance

**ZIP-MAINTENANCE-LIB-T01.** Import does not alter repository or storage.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
