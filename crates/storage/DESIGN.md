# Storage crate design

**Contract version** 1.0. Master design §12. Planned implementation.

## Responsibility and dependencies

Use a single redb writer and snapshot readers. Write object to private temporary sibling, hash and sync, rename and sync directory where supported, then reference the object in the metadata transaction.

First-party dependencies: [foundation](../foundation/DESIGN.md)

- [Assignments](../../specifications/1200-assignments/assignments.md)
- [Storage](../../specifications/2500-storage/storage.md)
- [Maintenance](../../specifications/3400-maintenance/maintenance.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `read_snapshot()`
- `transact(expected_revision, operations)`
- `put_object(stream)`
- `restore(manifest)`

Record families: Namespaced records, record revision, content-addressed object and migration ledger. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `RecordEnvelope { schema_major, schema_minor, revision, payload_digest, payload }`
- `ObjectRef { digest, length_bytes }`
- `Batch { preconditions, writes, events }`

- `transact(batch: Batch) -> Result<CommitReceipt>`
- `put_object(input: BoundedReader) -> Result<ObjectRef>`

## Failure, safety and resource limits

Resolve record byte and transaction operation limits from `storage.max_record_bytes` and `storage.max_transaction_operations`, then tighten to backend capability. Check free space before staging. Never publish metadata for a missing object.

- `Conflict`
- `QuotaExceeded`
- `CorruptObject`
- `MigrationRequired`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/storage/src/
├── lib.rs
├── error.rs
├── backend.rs
├── transaction.rs
├── repository.rs
├── schema.rs
├── migration.rs
├── integrity.rs
├── encryption.rs
├── retention.rs
├── backends/
│   ├── mod.rs
│   ├── memory.rs
│   ├── redb.rs
│   ├── sqlite.rs
│   ├── filesystem.rs
│   └── remote.rs
├── objects/
│   ├── mod.rs
│   ├── content_addressed.rs
│   ├── blobs.rs
│   └── metadata.rs
├── backup/
│   ├── mod.rs
│   ├── snapshot.rs
│   ├── restore.rs
│   └── verification.rs
└── recovery/
    ├── mod.rs
    ├── journal.rs
    └── reconciliation.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Crash before and after metadata commit, test duplicate object insertion and full backup restoration.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`backend.rs`](specifications/modules/backend.md)
- [`transaction.rs`](specifications/modules/transaction.md)
- [`repository.rs`](specifications/modules/repository.md)
- [`schema.rs`](specifications/modules/schema.md)
- [`migration.rs`](specifications/modules/migration.md)
- [`integrity.rs`](specifications/modules/integrity.md)
- [`encryption.rs`](specifications/modules/encryption.md)
- [`retention.rs`](specifications/modules/retention.md)
- [`backends/mod.rs`](specifications/modules/backends/mod.md)
- [`backends/memory.rs`](specifications/modules/backends/memory.md)
- [`backends/redb.rs`](specifications/modules/backends/redb.md)
- [`backends/sqlite.rs`](specifications/modules/backends/sqlite.md)
- [`backends/filesystem.rs`](specifications/modules/backends/filesystem.md)
- [`backends/remote.rs`](specifications/modules/backends/remote.md)
- [`objects/mod.rs`](specifications/modules/objects/mod.md)
- [`objects/content_addressed.rs`](specifications/modules/objects/content_addressed.md)
- [`objects/blobs.rs`](specifications/modules/objects/blobs.md)
- [`objects/metadata.rs`](specifications/modules/objects/metadata.md)
- [`backup/mod.rs`](specifications/modules/backup/mod.md)
- [`backup/snapshot.rs`](specifications/modules/backup/snapshot.md)
- [`backup/restore.rs`](specifications/modules/backup/restore.md)
- [`backup/verification.rs`](specifications/modules/backup/verification.md)
- [`recovery/mod.rs`](specifications/modules/recovery/mod.md)
- [`recovery/journal.rs`](specifications/modules/recovery/journal.md)
- [`recovery/reconciliation.rs`](specifications/modules/recovery/reconciliation.md)
