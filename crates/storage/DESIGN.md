# Storage crate design

**Contract version** 1.1 candidate. Master design §12. Planned implementation.

## Responsibility and dependencies

Use a single redb writer and snapshot readers. Write object to private temporary sibling, hash and sync, rename and sync directory where supported, then reference the object in the metadata transaction.

First-party dependencies: [foundation](../foundation/DESIGN.md)

- [Assignments](../../specifications/1200-assignments/assignments.md)
- [Storage](../../specifications/2500-storage/storage.md)
- [Maintenance](../../specifications/3400-maintenance/maintenance.md)

## API and data

The [backend port](specifications/modules/backend.md) owns snapshots, commits and reconciliation. [Transactions](specifications/modules/transaction.md) bind canonical immutable input, compare-and-swap conditions, object links, outbox and the durable receipt. [Schema](specifications/modules/schema.md) defines logical keys and references. Keep redb as the preferred embedded candidate and qualify its persistence and filesystem boundaries before release. The memory adapter can validate logical behavior.

Promote verified immutable bytes before committing any metadata link. A staging pin fences garbage collection until the writer commits. Backups pin one metadata generation and its complete reachable objects. Restore validates a new private root before a fenced selector cutover and reconciles rewound external effects before dispatch.

## Failure, safety and resource limits

Resolve `storage.max_record_bytes` and `storage.max_transaction_operations` from typed configuration at composition. Intersect with backend ceilings and admitted byte and time budgets. Check available space before staging. Use [typed errors](specifications/modules/error.md) and reconcile ambiguous commit by its original transaction identity. Authorization, configuration and resource adapters remain injected. Foundation remains the only first-party dependency.

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

Run the [durability fixtures](../../contracts/acceptance/storage/durability-fixtures.json) for atomicity, duplicate insertion, deletion fencing, pinned backup and complete restore. Qualify disk and process crash behavior on each supported adapter.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. The transaction, object and backup slice is a candidate for independent review. Other modules retain their recorded maturity.

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
