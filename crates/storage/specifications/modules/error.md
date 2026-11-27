# Storage failure taxonomy

**ZIP-STORAGE-ERROR-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/error.rs`

## Required implementation behavior

StorageError distinguishes InvalidSchema, Unsupported, Conflict, NotFound, Corrupt, Quota, Io and UnknownCommit. Carry opaque transaction/key identity in authorized context. Do not convert uncertain commit into conflict or retryable failure.

## Acceptance

**ZIP-STORAGE-ERROR-T01.** Inject sync error after backend submission and preserve UnknownCommit until reconciliation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
