# Object staging identity

**ZIP-STORAGE-OBJECTS-CONTENT-ADDRESSED-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/objects/content_addressed.rs`

## Required implementation behavior

put(input: BoundedReader, lease: &WriteLease) -> Result<StagedObject, StorageError>. Hash staged bytes, compare existing digest and length, promote atomically and sync before metadata activation.

## Acceptance

**ZIP-STORAGE-OBJECTS-CONTENT-ADDRESSED-T01.** Equal content yields same object ID; same stored digest with damaged bytes raises corruption.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
