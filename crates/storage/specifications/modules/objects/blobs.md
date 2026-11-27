# Verified streaming reads

**ZIP-STORAGE-OBJECTS-BLOBS-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/objects/blobs.rs`

## Required implementation behavior

open(reference: ObjectRef, grant: ReadGrant, budget: ReadBudget) -> Result<BlobReader, StorageError>. Validate scope and existence; stream bounded bytes. Verification is final only after digest and expected length match.

## Acceptance

**ZIP-STORAGE-OBJECTS-BLOBS-T01.** Caller cancels halfway and receives no completed verification receipt.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
