# Staged restore and active-root cutover

**ZIP-STORAGE-BACKUP-RESTORE-001 · v1.1 candidate · Owner** Storage maintainers

**Planned source** `crates/storage/src/backup/restore.rs`

Restore into a new uniquely owned root. Validate archive closure, authorized scope and migration compatibility before exposing a writable handle. Build the full storage set in staging, synchronize contents and verify the final candidate and all required objects. Quiesce the current writer, acquire the installation cutover fence and compare the expected selector. Record the restore operation ID, intended manifest digest, previous root, candidate root, and next root epoch in a durable control journal outside either replaceable data root.

Publish the candidate with an atomic, durably synchronized selector replacement qualified for the platform. The selector records logical store identity, root epoch, opaque root ID and restore intent ID. An interrupted operation after selector submission remains UnknownCommit until the selector and intent reconcile. Open the selector once under the fence, validate the chosen root and persist the final receipt before allowing service startup. Reject multiple active writers or missing roots. Previous root stays intact under retention control. A rollback repeats verified activation with a new epoch and its own authority. It cannot silently reset epoch or transaction replay fences.

A restore can rewind local domain and effect receipts. Before enabling external effects, fence old workers and grants and reconcile effect identities and pending outcomes against trusted records outside the rewound root or the relevant external providers. Missing history is unresolved and keeps affected dispatch blocked. A valid archive alone does not prove an external operation is absent.

**ZIP-STORAGE-BACKUP-RESTORE-T01.** Restore a complete archive and compare generation, records, outbox and logical object digests. Crash just before and after selector replacement and verify one validated root. An invalid package or unresolved effect cannot enable writes or dispatch beyond its verified scope.
