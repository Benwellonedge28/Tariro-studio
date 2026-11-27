# Verified maintenance backup

**ZIP-MAINTENANCE-BACKUP-001 · v1.0 · Owner:** Maintenance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/maintenance/src/backup.rs`

## Required implementation behavior

Pin consistent snapshot and retention rules, stage bounded backup and verify restore manifest before dependent maintenance.

## Acceptance

**ZIP-MAINTENANCE-BACKUP-T01.** Backup missing required object denies cleanup dependent on it.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
