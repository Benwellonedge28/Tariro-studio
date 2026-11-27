# Storage backend contract

**ZIP-STO-BACK-001 · v1.1 candidate · Owner** Storage maintainers

**Planned source** `crates/storage/src/backend.rs`

```rust
pub trait StorageBackend: Send + Sync {
    fn capabilities(&self) -> BackendCapabilities;
    fn snapshot(&self) -> Result<Box<dyn ReadSnapshot + '_>, StorageError>;
    fn commit(&self, batch: WriteBatch, lease: &WriteLease)
        -> Result<CommitReceipt, StorageError>;
    fn reconcile(
        &self, id: TransactionId, digest: Digest, lease: &WriteLease
    ) -> Result<CommitStatus, StorageError>;
}
```

Import write, receipt and identity types from [transaction](transaction.md), `StorageError` from [error](error.md), `Digest` from Foundation and `CommitStatus` from [reconciliation](recovery/reconciliation.md). A snapshot is a bounded read guard for one committed generation. Point and prefix reads share that view. Writers and readers may use different generations, but a reader sees a complete old or new transaction. Expose tombstone revision to compare-and-swap readers without returning deleted payload.

Backend capabilities declare format reader/writer ranges, key and record bounds, process writer exclusivity, snapshot isolation, and verified persistence semantics for metadata, object promotion and the active-root selector. Validate format and exclusivity before opening writable handles. The composition selects one qualified embedded backend and releases durable success only after its tested sync boundary. The memory adapter is a logical conformance oracle. An adapter lacking necessary semantics returns Unsupported at open. Open explicitly in recovery-only mode if the integrity or selector checks fail.

No backend may report a definite abort after a synchronization error unless it can prove that the operation did not commit. Return UnknownCommit and require the original identity. Commit may block only within admitted bounds and must classify interruption at its submission boundary. All external file-copy and verification work occurs outside metadata serialization. An object pin bridges the final verification and the database commit.

**STO-BACK-T01–T04.** Compare competing writes, snapshot isolation, incompatible format rejection and sync ambiguity in memory and a qualified embedded adapter. Disk durability requires process and filesystem fault tests.
