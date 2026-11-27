# Assignment decision failures

**ZIP-ASSIGNMENTS-ERROR-001 · v1.1 candidate · Owner** Assignments maintainers

**Planned source** `crates/assignments/src/error.rs`

```rust
#[non_exhaustive]
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum AssignmentError {
    InvalidSpec,
    ScopeDenied,
    UnknownAssignment,
    Conflict,
    RevisionConflict,
    InvalidTransition,
    BudgetUnavailable,
    BatchOverLimit,
    EvidenceIncomplete,
    CorruptCheckpoint,
    LeaseLost,
    DeadlineExceeded,
    Cancelled,
    OutcomeUnknown,
    UnknownEffect,
    Unavailable,
    Overflow,
}
```

Validate request shape before store access and authenticate scope before exposing assignment existence, receipts or progress. Check exact authorized command receipt before revision conflicts. Then check the current transition edge, active guards and applicable capacity. Under authorized scope describe evidence or clearance required without including secrets or raw remote output. AwaitingApproval is a durable state rather than a fabricated error or success. A precommit failure leaves state unchanged. OutcomeUnknown requires original transaction reconciliation. UnknownEffect requires provider read-only reconciliation and blocks dispatch. A missing provider response, timeout or requested cancellation cannot be treated as proven absence.

**ZIP-ASSIGNMENTS-ERROR-T01.** Lose an external reply and verify UnknownEffect remains visible until trusted reconciliation and no new effect identity is issued.
