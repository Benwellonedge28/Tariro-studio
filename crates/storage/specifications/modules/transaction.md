# Transaction, revision and receipt contract

**ZIP-STO-TXN-001 · v1.1 candidate · Owner** Storage maintainers

**Planned source** `crates/storage/src/transaction.rs`

## Records and interfaces

```rust
pub struct WriteBatch {
    pub id: TransactionId,
    pub expected: Vec<ExpectedRevision>,
    pub mutations: Vec<Mutation>,
    pub outbox: Vec<PendingEvent>,
}
pub enum ExpectedRevisionValue { Missing, Present(u64) }
pub struct CommitReceipt { pub id: TransactionId, pub generation: u64, pub digest: Digest }
pub fn validate_batch(batch: &WriteBatch, limits: &WriteLimits) -> Result<(), StorageError>;
```

`TransactionId` wraps a nonnil 16-byte UUID scoped to the logical store. `ExpectedRevision` contains a canonical record key and expected state. Mutation variants are Insert, Replace and Tombstone. Insert contains key and versioned payload; Replace contains the same fields; Tombstone contains only the key. Domain mutations cannot write the accounting, receipt or outbox keyspaces directly. The payload is opaque and has an explicit sorted set of immutable object references. The owning service validates that set before submission. A PendingEvent supplies stream ID, event ID, schema version, correlation ID, occurrence time and a verified immutable payload reference. Its position within the batch determines sequence order within that stream. Reject duplicate event IDs in a batch or an ID already committed by another batch in the same stream.

One expected entry is required for each mutation. Also allow read-set preconditions for additional keys. Reject duplicate precondition keys and mutation keys. Count one operation per precondition, mutation and event, checked before execution. Charge encoded key bytes, payload bytes and declared references to the write budget. Each encoded record, including event envelope and references, is independently bounded by `storage.max_record_bytes`. Enforce `storage.max_transaction_operations` and intersect byte and operation budgets with backend and admitted limits. Backend overhead and staging bytes must fit the admitted write allowance. Receipt replay uses bounded validation and no new write accounting.

Canonical digest input starts with ASCII `ZIP-STO-BATCH-v1`, followed by the 16-byte transaction ID and three length-prefixed lists. Precondition and mutation lists sort by canonical key bytes. The outbox list retains input order. Use u64 big-endian length/count prefixes, fixed-width key and identifier fields per [schema](schema.md), and one-byte variant tags (Missing/Present 0/1, Insert/Replace/Tombstone 0/1/2). Prefix key and payload byte sequences with their length. Present encodes its expected revision as u64. Mutations encode schema major then minor as u16, payload and a u64-counted sorted object reference list for Insert and Replace. Each object reference encodes the protection-domain UUID, algorithm tag, digest and u64 length. Events encode fixed stream and event UUIDs, schema major/minor, an optional correlation UUID with presence tag 0/1, canonical UTC timestamp bytes with length, and payload reference. Exclude allocated revisions, generations and event sequence numbers. Wire fields and digest encoding are versioned together.

## Atomicity and cancellation

1. Validate trusted write scope, shape, bounds and deadline. A lease is root-epoch scoped and comes from composition. Validate cancellation and authorization again immediately before commit submission. No storage crate dependency on the governance or resource crate is required.
2. Check a matching receipt first under the serialized writer. An equal digest replays the durable receipt. A different digest is Conflict. For a new commit, acquire and validate read pins for new object references before entering the writer. Follow global lock order from [metadata](objects/metadata.md).
3. Compare all preconditions against one writer view. Missing denotes a key that never existed. First insert uses revision 1. Replace requires an existing live record or matching tombstone revision; Tombstone requires a matching live record. Increase revision with checked arithmetic. Reads used for CAS expose tombstone revisions. A retained tombstone prevents a stale Missing precondition from succeeding.
4. Stage domain writes, indexes, object deltas, per-stream sequence numbers, event-ID uniqueness index and receipt together. Each stream starts at sequence 1. Commit one root generation per new batch. An outbox reader only sees committed events.
5. Cancellation before backend commit submission rolls back. After submission preserve the committed, definitely aborted or unknown outcome. Retrying an unknown effect requires [reconciliation](recovery/reconciliation.md) under its original transaction ID.

A matching replay remains subject to current scope. Receipt pruning cannot make old requests eligible again. Retain receipts or an authoritative retirement fence covering those transaction IDs before removal, and keep tombstone keys or equivalent revision protection while stale clients remain eligible.

**STO-TXN-T01, STO-TXN-T02, STO-TXN-T03 and STO-TXN-T04.** Exercise all-or-nothing conflict, outbox and receipt atomicity, matching and conflicting replay, and exact byte and operation bounds under two configurations.
