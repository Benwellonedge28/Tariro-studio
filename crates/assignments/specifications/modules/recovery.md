# Assignment restart reconciliation

**ZIP-ASG-RCV-001 · v1.0 · Owner:** Assignment maintainers. **Maturity:** D4 candidate. **Planned source:** `crates/assignments/src/recovery.rs`.

Expose `recover(request: RecoveryRequest, services: &RecoveryServices) -> Result<RecoveryDecision, AssignmentError>`. Request binds assignment ID, expected revision, pinned plan, grant, checkpoints and operation history. Services inject storage, verifier, authorization and read-only provider reconciliation. Decisions are Ready(next unit), AwaitingApproval, Blocked(reason), Terminal(previous receipt). The recovery algorithm itself has no publication capability.

1. Read the last durable snapshot and validate schema and revision. A terminal state returns its prior receipt without starting work.
2. Fence prior worker epoch before considering replacement lease. Check active authority, approved plan, pinned input, expected policies and required resource availability.
3. Validate contiguous checkpoints and independently inspect referenced artifacts/evidence. Treat conflicting artifacts as corruption rather than rolling silently back to an earlier unit.
4. Reconcile unresolved external effects by recorded key, expected target and payload digest. Record exact existing state, proven absence or ambiguity. Ambiguity blocks; proven absence can proceed only through an explicitly authorized retry on the original key.
5. Persist recovery verdict with a revision check and outbox event. Re-enter Executing only after acquiring a new lease. Cancellation before the verdict leaves prior durable state recoverable.

ASG-RCV-T01 kills after unit 17 and starts unit 18. T02 loses a push/PR acknowledgement and verifies no duplicate effect. T03 denies expired and revoked grants while preserving completed work. T04 observes a digest mismatch and blocks recovery. See [recovery standard](../../../../RECOVERY_STANDARD.md).
