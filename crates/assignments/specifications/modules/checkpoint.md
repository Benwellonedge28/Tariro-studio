# Verified unit commit

**ZIP-ASG-CHK-001 · v1.1 candidate · Owner** Assignments maintainers

**Planned source** `crates/assignments/src/checkpoint.rs`

The aggregate owns the committed prefix of the immutable plan's ordered unit list. An ordered unit is one normalized output identity with an explicit evidence gate. Executors may stage candidates ahead within policy. They cannot advance verified progress past a gap.

```rust
pub fn commit_unit(
    store: &dyn AssignmentStore,
    input: VerifiedUnit,
    expected_revision: u64,
    lease: &ExecutionLease,
) -> Result<CheckpointReceipt, AssignmentError>;
```

`AssignmentStore` is the injected [aggregate store](persistence.md). Inputs bind assignment, plan digest, unit index, authorized path identity, exact staged artifact digest, source revision, authority revision, verifier evidence and live worker epoch. The receipt identifies assignment, plan, index, committed assignment revision and immutable artifact/evidence references. Only a trusted verifier can supply qualified evidence.

Authorize and validate the immutable bytes first. Under the writer compare current aggregate revision, Executing state, current worker epoch and plan. Require the next positive index, exactly matching the plan entry, and check the configured count and integer bounds. Commit checkpoint, progress, command receipt and outbox together. A matching replay returns the retained receipt under current read scope. A different artifact or verifier evidence for the same plan and index conflicts. Staged artifacts never count as verified before commit.

On cancellation before submission preserve the previous prefix. After an uncertain commit reconcile the original transaction before rerunning the unit. Restart scans the highest contiguous committed prefix of the active plan and validates all referenced objects and evidence within admitted budgets. A missing or conflicting checkpoint blocks rather than silently regressing.

**ASG-CHK-T01.** Commit unit 17, interrupt, and resume only from unit 18. **ASG-CHK-T02.** Test a stale worker epoch, changed plan, mismatched artifact and exact duplicate.
