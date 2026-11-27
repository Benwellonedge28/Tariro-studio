# Consistent backup manifest

**ZIP-STORAGE-BACKUP-SNAPSHOT-001 · v1.1 candidate · Owner** Storage maintainers

**Planned source** `crates/storage/src/backup/snapshot.rs`

Begin under the serialized metadata writer. Commit a durable backup pin for the selected generation and capture a matching metadata snapshot before releasing writer coordination. The logical snapshot excludes the operational pin itself. A backup pin transaction does not advance the domain commit generation. After the pin commits, prohibit new garbage-collection marks while any backup pin is live. An earlier committed deletion marker cannot correspond to a committed live reference in the selected view. Copy outside the writer transaction. Walk the pinned metadata and derive the full reachable object set, including retained outbox payloads and audit references. Concurrent writes can continue and do not alter that set.

A manifest records version, logical store UUID, source root epoch, metadata generation and schema, canonical metadata export digest and size, scope identifier, approved encryption format and key references if any, and ordered object entries containing protection domain, logical digest, logical length, archived-byte digest and archived length. Use stable field names and canonical bytes defined by the selected manifest codec. The manifest contains no live credentials. Charge copy, manifest and temporary storage against the backup's admitted resources. Preserve the manifest and entries in private staging until the entire package validates and is sealed.

On completion or authorized cancellation, durably record the outcome and release the backup pin. After a crash, a pin survives until takeover verifies output or proves the old copy stopped and removes its private staging. Never release a pin solely because its deadline elapsed. Apply bounded traversal, configured deadline and backpressure to protect normal writes.

**ZIP-STORAGE-BACKUP-SNAPSHOT-T01.** Commit a new record and remove an old reference after capture. Verify the export contains the old record and its reachable object only, and that GC cannot delete that object during the copy.
