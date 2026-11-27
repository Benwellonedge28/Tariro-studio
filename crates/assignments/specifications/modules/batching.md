# Exact authorized batch and seal

**ZIP-ASSIGNMENTS-BATCHING-001 · v1.1 candidate · Owner** Assignments maintainers

**Planned source** `crates/assignments/src/batching.rs`

Read batch policy from the live grant and plan. Exact count is an authorized constraint. The reference Vimbai grant uses 30, while a different grant can specify another count. Normal operational ceilings still apply. Count the distinct changed final output paths from the staged tree versus the pinned original tree. An unchanged or duplicate path adds nothing. Reject aliases and ambiguous paths. Validate both sides of any permitted rename and classify operation, mode and content before counting. For a documentation-only grant, accept only scoped Markdown creation or modification under the [repository contract](../../../../specifications/1400-repositories/repositories.md).

Validate projected count and path admission before staging a new unit. Reject a candidate exceeding the exact count. Recompute the count from the final authoritative diff before sealing. A verified short batch enters AwaitingApproval and keeps its checkpoints. It does not automatically publish, add unrelated filler or relax the exact count. A separate grant and updated plan are required to approve a changed batch. Preserve original receipts and intentionally revalidate any reused unit.

Seal the stable provider repository ID, pinned base, reviewed candidate tree and sorted final diff manifest, plan and requirements digests, scoped grant, verification references and exact file count. Use canonical path bytes and stable encodings for operation, path, mode and preimage/postimage blob. The recorded digest makes any change require resealing and review. Recompute and compare the seal immediately before effect claim. A file count alone cannot authorize a diff. A batch is complete only with the matching evidence and configured publication outcome.

**ZIP-ASSIGNMENTS-BATCHING-T01.** Under the 30-file fixture, reject a 31st file and require approval for a final batch of 12. Another grant can approve 12 without changing the implementation.
