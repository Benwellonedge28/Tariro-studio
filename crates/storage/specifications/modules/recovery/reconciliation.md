# Storage effect recovery

**ZIP-STORAGE-RECOVERY-RECONCILIATION-001 · v1.1 candidate · Owner** Storage maintainers

**Planned source** `crates/storage/src/recovery/reconciliation.rs`

```rust
pub enum CommitStatus {
    Committed(crate::transaction::CommitReceipt),
    Absent,
    Conflicting,
    Unresolved,
}
```

For an authorized transaction, use its original ID and canonical batch digest. Read a qualified committed snapshot. A matching retained receipt proves Committed. A different digest is Conflicting and cannot be replayed. Absent requires that the original writer can no longer commit, the observed root covers the original operation, and receipt retention or a replay fence establishes complete visibility. No receipt after a restore, retention, an unreliable read or an unfenced writer means Unresolved. An Absent result allows retry only under live authority using the same request identity and immutable input. Resolving a retired request never authorizes a new write under that identity.

For restore, reconcile the selection under the installation fence against the out-of-root journal. If the old selector matches, prove the original switch cannot still occur before discarding the candidate. If the new selector and root match the intent, verify durable metadata and bytes and publish one completion receipt. A different or invalid selector is RecoveryRequired. For object deletion, a marker with no durable link permits completion after verified removal and directory sync. A marker with live references is corruption. Preserve original evidence and prohibit affected writes.

**ZIP-STORAGE-RECOVERY-RECONCILIATION-T01.** Lose a commit reply and prove the retained receipt. Replace the root with an older image that omits the receipt and verify lookup remains Unresolved. A selector naming incomplete staging must never yield successful recovery.
