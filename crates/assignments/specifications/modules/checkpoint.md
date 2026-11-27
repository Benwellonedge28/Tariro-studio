# Assignment checkpoint and verified unit commit

**ZIP-ASG-CHK-001 · v1.0 · Owner:** Assignment maintainers. **Maturity:** D4 candidate. **Planned source:** `crates/assignments/src/checkpoint.rs`.

A checkpoint key combines the local assignment UUID and an unsigned big-endian unit index starting at one. Value v1 records plan digest, candidate path identity, artifact digest, verifier evidence ID/digest, policy revision, source commit, attempt epoch and next unit index. The canonical payload belongs to the assignment schema. The artifact is already staged and verified before commit.

```rust
pub fn commit_unit(
    store: &dyn AssignmentStore,
    input: VerifiedUnit,
    expected_revision: u64,
    lease: &ExecutionLease,
) -> Result<CheckpointReceipt, AssignmentError>;
```

Validate actor/scope, typed evidence and verifier identity, contiguous next unit, live lease and same source/plan, then use one transaction to insert checkpoint, update progress/revision, append event and store the effect ID. An exact replay returns the existing receipt; same unit with different digests yields Conflict. Never mark a staged file verified before the transaction completes. After restart select the highest contiguous verified unit and revalidate its artifacts and referenced evidence. Missing bytes or gaps block resume.

Cancellation before transaction leaves the last durable checkpoint authoritative. An unknown commit queries by key and intended digest; do not rerun authorship for that unit until reconciled. ASG-CHK-T01 verifies Vimbai unit 17 persisted, process killed, then resume at 18. ASG-CHK-T02 covers stale epoch, changed plan, mismatched digest and duplicate result delivery. See [assignment persistence](../../../../specifications/1200-assignments/assignments.md).
