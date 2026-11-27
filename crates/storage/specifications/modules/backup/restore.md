# Staged restore and activation

**ZIP-STORAGE-BACKUP-RESTORE-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/backup/restore.rs`

## Required implementation behavior

Restore into new private root, verify manifest and all objects, migrate if approved, and atomically activate generation only after checks. Prior root remains available for qualified rollback.

## Acceptance

**ZIP-STORAGE-BACKUP-RESTORE-T01.** Corrupt or incomplete archive cannot become active; crash after selector flip reconciles to one active root.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
