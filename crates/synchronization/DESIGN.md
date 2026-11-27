# Synchronization crate design

**Contract version** 1.0. Master design §47. Planned implementation.

## Responsibility and dependencies

Authenticate counterpart, compare manifest inventory, stage verified chunks, apply causally ordered versioned changes, preserve competing writes for resolution.

First-party dependencies: [foundation](../foundation/DESIGN.md), [networking](../networking/DESIGN.md), [storage](../storage/DESIGN.md), [audit](../audit/DESIGN.md)

- [Networking](../../specifications/2600-networking/networking.md)
- [Distributed](../../specifications/2700-distributed/distributed.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `offer_manifest(scope)`
- `pull(cursor)`
- `apply(delta)`
- `reconcile()`

Record families: ReplicaId, sequence cursor, artifact digest, conflict record and receipt. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `DeltaManifest { replica_id, scope, schema, base_cursor, end_cursor, objects, digest }`
- `ApplyReceipt { cursor, accepted_changes, conflicts }`

- `apply(delta: VerifiedDelta, target: ReplicaScope) -> Result<ApplyReceipt>`

## Failure, safety and resource limits

Bound batch bytes and artifact size. Unknown schema quarantined. Resume from last applied cursor and dedupe repeated chunks.

- `ReplicaDenied`
- `Conflict`
- `IntegrityMismatch`
- `UnsupportedSchema`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/synchronization/src/
├── lib.rs
├── error.rs
├── synchronization.rs
├── manifest.rs
├── change_set.rs
├── version.rs
├── conflict.rs
├── reconciliation.rs
├── replication.rs
├── compression.rs
├── encryption.rs
├── integrity.rs
├── checkpoint.rs
├── offline_queue.rs
└── transport.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Drop connection mid-transfer, resume, preserve divergent histories.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`synchronization.rs`](specifications/modules/synchronization.md)
- [`manifest.rs`](specifications/modules/manifest.md)
- [`change_set.rs`](specifications/modules/change_set.md)
- [`version.rs`](specifications/modules/version.md)
- [`conflict.rs`](specifications/modules/conflict.md)
- [`reconciliation.rs`](specifications/modules/reconciliation.md)
- [`replication.rs`](specifications/modules/replication.md)
- [`compression.rs`](specifications/modules/compression.md)
- [`encryption.rs`](specifications/modules/encryption.md)
- [`integrity.rs`](specifications/modules/integrity.md)
- [`checkpoint.rs`](specifications/modules/checkpoint.md)
- [`offline_queue.rs`](specifications/modules/offline_queue.md)
- [`transport.rs`](specifications/modules/transport.md)
