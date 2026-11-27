# Transactional scheduling and handoff

**ZIP-SCHEDULER-SCHEDULER-001 · v1.1 candidate · Owner** Scheduler maintainers

**Planned source** `crates/scheduler/src/scheduler.rs`

The scheduler owns queue ordering, claim epochs and retry eligibility. The runtime owns supervised execution and terminal attempt receipts. Resources owns leases and release. Scheduler composition injects live authority and a trusted runtime handoff and receipt verifier. These interfaces introduce no reverse crate dependency.

## Public port

Rust declarations omit bodies. Import `JobSpec`, `JobKey`, `JobClaim` and `JobState` from `crate::job`, `SchedulerError` from `crate::error`, `Digest` from `foundation::types::digest` and `ResourceLease` from `resources::allocation::lease`.

```rust
pub struct Dispatch {
    claim: JobClaim,
    lease: ResourceLease,
}

impl Dispatch {
    pub fn into_parts(self) -> (JobClaim, ResourceLease);
}

pub trait Scheduler: Send + Sync {
    fn enqueue(&self, job: JobSpec) -> Result<JobState, SchedulerError>;
    fn claim_next(&self) -> Result<Option<Dispatch>, SchedulerError>;
    fn check_claim(&self, claim: &JobClaim) -> Result<(), SchedulerError>;
    fn finish(&self, claim: &JobClaim, evidence: Digest) -> Result<JobState, SchedulerError>;
    fn state(&self, job: &JobKey) -> Result<JobState, SchedulerError>;
    fn reconcile(&self, job: &JobKey) -> Result<JobState, SchedulerError>;
}
```

A port instance binds trusted credentials, the coordinator clock, current policy and one compatible worker target. Authorization precedes scoped reads as well as mutations. A caller consumes Dispatch to transfer the lease to the runtime. The claim is evidence of scheduler ownership. The live check linearizes against current owner, grant and deadline and is required at the runtime launch and publication gates. Recovery cannot reconstruct or transfer a worker lease by reading a database row. Use another attempt after verified settlement.

## State machine

| From | Event | To | Atomic scheduler write |
| --- | --- | --- | --- |
| Absent | Valid authorized enqueue | Waiting, Ready or Blocked | Record immutable specification and dependency status |
| Waiting or RetryWait | Dependencies succeeded and eligible time reached | Ready | Add ready key |
| Waiting or Ready | Required dependency irreversibly failed | Blocked | Record dependency disposition |
| Ready | Current candidate wins claim comparison | Reserving | Remove ready key and allocate new attempt number and claim epoch before calling Resources |
| Reserving | Definitive no reservation and still eligible | Ready | Close the attempt as unreserved and record relevant wake condition |
| Reserving | Lease acquired and ownership still current | Dispatched | Persist binding and charge dispatch budget, advance fairness cursor |
| Reserving or Dispatched | Ambiguous outcome, cancellation, revocation or lost owner | Recovering | Fence the scheduler claim, preserve attempt and record obligations |
| Ready, Waiting or RetryWait | Cancellation, revoked authorization or exhausted lifetime | Terminal | Close job with the corresponding outcome |
| Dispatched | Valid current runtime receipt | Terminal or RetryWait | Atomically append receipt and disposition |
| Recovering | Trusted reconciliation confirms final result and settlement | Terminal, Ready or RetryWait | Store reconciled disposition, proof and any eligible time |
| Blocked or Terminal | Authorized exact command replay | Same | Return stored response without a new event |

A technical capacity denial returns to Ready and records its relevant capacity revision. Do not select it for the same unchanged wake snapshot. Pending or uncertain external outcomes may only reenter Ready after explicit reconciliation proves no execution and no live hold. Jobs that were Dispatched use the retry gate even if the runtime proves the task body never ran. Resolve simultaneous stop and receipt by CAS order: a receipt committed first stays final, while a fence committed first requires a trusted recovery decision. Recovered genuine external effects remain in evidence regardless of job disposition.

## Admission sequencing

1. Snapshot eligible queue entries under a configured bound. Sort under the [fairness](fairness.md) contract. Validate each selected job and its live scope before proceeding. Compare the selected job revision and current fairness cursor in storage and persist Reserving with an attempt intent before invoking Resources. If another scheduler won, reread the bounded snapshot.
2. Outside the transaction apply the [admission](admission.md) contract. Recheck ownership, deadline, policy and the fairness cursor when committing Dispatched. The winner of that CAS may hand off the resulting Dispatch once. On a failed CAS, persist Recovering under the current owner or defer to the owner that already fenced the intent. Reconcile the acquired lease through authorized cleanup. Never drop the last durable reference or reuse the attempt number.
3. If the result is uncertain or a handoff is interrupted, preserve the intent and ask recovery to reconcile. An exact replay may return stored status. Only the original successful claim invocation can hand off a worker lease. One retry wake cannot bypass resource or runtime fencing.
4. Finish by verifying the evidence digest under the authenticated claim and loading a trusted receipt. Check receipt identity, job plan digest and attempt binding. Reject an old worker receipt after fencing. A recovery verifier can record the observed outcome under current authority without reactivating the old claim. Terminal runtime evidence carries settlement and reconciled effect receipts. Any unpublished disposition with an unresolved external effect remains Recovering until the verifier records a trusted decision.

Journal, verifier and admission operations use validated budgets. No storage transaction holds a lock across resource, runtime or provider calls. Follow [persistence](persistence.md) for revision, outbox and restart.

**ZIP-SCHEDULER-SCHEDULER-T01.** Race two claimant transactions against the same Ready row, interrupt after reserve and after dispatch commit, and verify one bound attempt, at most one handoff, and no replacement while a hold is unresolved.
