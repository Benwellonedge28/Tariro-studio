# Storage backend contract

**ZIP-STO-BACK-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D4 candidate. **Planned source:** `crates/storage/src/backend.rs`.

## API

```rust
pub trait StorageBackend: Send + Sync {
    fn capabilities(&self) -> BackendCapabilities;
    fn snapshot(&self) -> Result<Box<dyn ReadSnapshot + '_>, StorageError>;
    fn commit(&self, batch: WriteBatch, lease: &WriteLease)
        -> Result<CommitReceipt, StorageError>;
}
```

`BackendCapabilities` exposes format major, maximum supported key/value size, snapshot isolation, writer serialization and sync guarantee. `ReadSnapshot` is a synchronous immutable generation guard with bounded point reads and prefix scans. `WriteBatch`, `WriteLease` and `CommitReceipt` follow [transaction.md](transaction.md). `StorageError` distinguishes unavailable capability, conflict, corrupt state, lease invalid, quota exceeded, I/O failure and unknown commit outcome. Return owned values only after charging byte read/write bounds.

## Execution contract

Open starts in validation mode. Check header and compatibility before opening writable handles. Reject backends that cannot guarantee writer serialization and required durability. Hold a read snapshot only through bounded scans. A single writer serializes commits across handles; multiple process support depends on an enforceable backend lock.

Read-only fallback is explicit when repair is required. Never map corruption or an unknown commit to successful empty state. Closing a read guard does not mutate state. Commit returns durable success only after the backend's qualified persistence boundary. Where outcome is ambiguous, callers reconcile using the transaction ID before retry.

## Tests

STO-BACK-T01 runs two contending writers from one revision and verifies one succeeds. T02 shows a snapshot reads a stable generation during writes. T03 fails open for incompatible writer schema without changing bytes. T04 simulates sync failure and distinguishes confirmed abort from unknown outcome. Conformance runs against memory and the qualified embedded backend; memory-only tests cannot demonstrate disk durability.
