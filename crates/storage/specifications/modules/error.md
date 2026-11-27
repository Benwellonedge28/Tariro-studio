# Storage failure taxonomy

**ZIP-STORAGE-ERROR-001 · v1.1 candidate · Owner** Storage maintainers

**Planned source** `crates/storage/src/error.rs`

```rust
#[non_exhaustive]
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum StorageError {
    InvalidLease,
    InvalidSchema,
    InvalidRequest,
    Unsupported,
    Conflict,
    NotFound,
    Quota,
    DeadlineExceeded,
    Cancelled,
    Overflow,
    Corrupt,
    Io,
    UnknownCommit,
    RecoveryRequired,
}
```

Check scope before disclosing key, receipt, root or object existence. Check request shape and compatibility before staging, then bounds and deadline. In the serialized writer, check receipt identity before revision conflicts. Recheck scope and cancellation before submission. A verification mismatch or impossible reference is Corrupt and blocks affected operations. An unavailable or inconsistent active-root selector is RecoveryRequired. Log restricted opaque identities without exposing content or credential material.

Before commit submission, errors include no domain mutation. A definitive backend abort may be retried within original authority and bounds. UnknownCommit indicates a possibly committed database or selector action. Do not translate it into a retryable transport failure. After a commit, output cancellation cannot change the stored receipt or retract an outbox event.

**ZIP-STORAGE-ERROR-T01.** Inject a sync error or lost reply after commit submission and require reconciliation. Run a precommit cancellation control and verify zero records, references, receipts and events become visible.
