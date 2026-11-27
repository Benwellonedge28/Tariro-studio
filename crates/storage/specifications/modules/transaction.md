# Transaction, revision and receipt contract

**ZIP-STO-TXN-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D4 candidate. **Planned source:** `crates/storage/src/transaction.rs`.

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

`TransactionId` is a validated UUID assigned by the caller. `ExpectedRevision` pairs a canonical record key with the expected state. `Mutation` is Insert, Replace or Tombstone, with a key and versioned owned envelope where applicable. `PendingEvent` belongs to the updated stream and references immutable payload bytes. `WriteLimits` contains finite byte and operation ceilings, a deadline and the relevant lease revision. Digests use the Foundation tagged digest type.

## Atomic sequence

1. Validate lease, request ID, schema, normalized unique keys, operation count and total charged bytes. Require one precondition per mutated authoritative record. No two mutations target the same key.
2. Under the serialized writer, look up transaction ID. An equal canonical batch digest replays its receipt. Different bytes for the same ID return conflict. Otherwise check every precondition, enforce checked next revision and verify referenced objects before insertion.
3. Stage record updates, index updates, odometer allocation for per-stream events, outbox envelopes and the receipt in one database transaction. Commit through the durability boundary before returning receipt.
4. On cancellation before commit, roll back. After submission to the backend commit primitive, classify its return as committed, definitively aborted or unknown; reconcile unknown by original transaction ID. No retry synthesizes a new ID for the same unknown operation.

The writer lock cannot be held across external I/O. Receipt and generation update commit together. Return the same failure with no mutation for stale conditions before commit. Purging a receipt requires synchronized replay retention policy.

## Tests

STO-TXN-T01 exercises absent and present revisions and multi-key conflict with zero writes. T02 verifies outbox and receipt atomicity at every injected kill point. T03 replays an equal batch and rejects ID reuse with different input. T04 verifies exact byte and operation boundaries independently using two configurations.
