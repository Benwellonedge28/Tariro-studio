# Atomic object references and deletion fencing

**ZIP-STORAGE-OBJECTS-METADATA-001 · v1.1 candidate · Owner** Storage maintainers

**Planned source** `crates/storage/src/objects/metadata.rs`

Resolve protection domain from the owning store and workspace policy, then use digest and length within that domain. Metadata records verified readiness, checked reference count and deletion marker. Count one reference per distinct object link in each domain record and per retained outbox event or audit reference. Replacing a record subtracts its previous links and adds new links in the same transaction. Never subtract from a count that cannot cover the delta, and never publish a link for a deleting or unverified object.

Acquire per-object gates by protection-domain and digest byte order before entering metadata serialization. A staged pin stays held through the reference commit. An installer, garbage collector and backup coordinator use the same lock order. A metadata writer never waits for an object gate. Competing GC first checks no active backup pin and no link, and commits a deletion marker under these gates. New links cannot attach until deletion resolves. After committing the marker, remove bytes outside metadata serialization, sync the qualified directory and record completion. If removal or sync is uncertain, retain the marker for recovery. An orphan scan uses the same gates and validated grace policy, and skips any in-progress staging. Backend/process lock or storage ownership capability must enforce these rules across participating processes.

**ZIP-STORAGE-OBJECTS-METADATA-T01.** Roll back a batch that would add a reference and verify neither link nor count changes. Race a link against a deleting marker and verify that a committed reference never points to absent bytes.
