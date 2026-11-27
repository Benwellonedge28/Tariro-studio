# Typed record repository

**ZIP-STORAGE-REPOSITORY-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/repository.rs`

## Required implementation behavior

get(snapshot: &dyn ReadSnapshot, key: &LogicalKey) -> Result<Option<RecordEnvelope>, StorageError>. Validate table and record schema, then reference digest. Mutation builders emit version-checked entries for transaction.rs.

## Acceptance

**ZIP-STORAGE-REPOSITORY-T01.** A stale expected revision yields conflict; a mismatched type does not expose opaque payload.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
