# Consistent backup manifest

**ZIP-STORAGE-BACKUP-SNAPSHOT-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/backup/snapshot.rs`

## Required implementation behavior

Pin database and object generation, enumerate reachable objects under bounded cursor, copy/verify staged bytes and seal manifest. Record format, policy, digests and omission of live credentials.

## Acceptance

**ZIP-STORAGE-BACKUP-SNAPSHOT-T01.** Concurrent write after pin appears in neither restored metadata nor referenced-object set.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
