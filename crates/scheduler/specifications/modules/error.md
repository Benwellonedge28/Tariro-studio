# Scheduler error decisions

**ZIP-SCHEDULER-ERROR-001 · v1.1 candidate · Owner** Scheduler maintainers

**Planned source** `crates/scheduler/src/error.rs`

```rust
#[non_exhaustive]
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum SchedulerError {
    InvalidJob,
    PolicyDenied,
    UnknownJob,
    ConflictingJob,
    Cycle,
    QueueFull,
    DependencyFailed,
    DeadlineExceeded,
    LeaseLost,
    ConflictingReceipt,
    CapacityUnavailable,
    Overflow,
    Unavailable,
    OutcomeUnknown,
}
```

Check shape, then authority before revealing job existence, pending counts or capacity. After authority check the operation identity and replay state, then eligibility and deadline, then relevant revision and lease binding. Report LeaseLost for stale worker claims and ConflictingReceipt for a different outcome under an already committed attempt key. Resource shortage maps to CapacityUnavailable internally and can defer the job, while a potentially committed reserve maps to OutcomeUnknown and blocks replacement. A trusted dependency failure transitions to Blocked. Only an authenticated and owner-scoped diagnostic stream may attribute affected coordinates or record references.

A validation denial leaves state unchanged. Unavailable denotes a known precommit failure at the reporting journal boundary. OutcomeUnknown needs recovery by stable intent identity before retry. Neither ordinary timeout nor an adapter exception can assert absence of an external effect. Overflow fails the operation without wrapping counters or extending deadlines.

**ZIP-SCHEDULER-ERROR-T01.** Simulate a lost provider response and an ordinary precommit denial. Confirm the first remains recoverable and the second leaves no ledger mutation. Neither communicates tenant data to unauthorized callers.
