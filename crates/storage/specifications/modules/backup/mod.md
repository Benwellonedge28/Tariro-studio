# Backup authority boundary

**ZIP-STORAGE-BACKUP-MOD-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/backup/mod.rs`

## Required implementation behavior

Expose snapshot, restore and verification as separate ports. Creating a backup does not authorize transfer or activation of restored data.

## Acceptance

**ZIP-STORAGE-BACKUP-MOD-T01.** A backup grant cannot replace the active database selector.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
