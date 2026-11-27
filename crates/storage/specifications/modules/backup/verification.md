# Backup integrity proof

**ZIP-STORAGE-BACKUP-VERIFICATION-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/backup/verification.rs`

## Required implementation behavior

Verify signed/qualified manifest where policy mandates, then verify every declared object's digest and reference consistency. Reject unexpected paths and entries outside authorized workspace.

## Acceptance

**ZIP-STORAGE-BACKUP-VERIFICATION-T01.** Obsolete schema without migration chain, digest mismatch and path escape all block restore.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
