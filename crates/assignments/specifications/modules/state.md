# Durable assignment state vocabulary

**ZIP-ASSIGNMENTS-STATE-001 · v1.1 candidate · Owner** Assignments maintainers

**Planned source** `crates/assignments/src/state.rs`

```rust
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum AssignmentState {
    Submitted, Validated, AwaitingApproval, Authorized, Planned, Scheduled,
    Executing, Verifying, Paused, Blocked, Recovering, Completed, Failed, Cancelled,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub(crate) enum StopDisposition { Pause, AwaitingApproval, Cancel, Fail }
```

Encode state tags in lowercase snake case for schema v1. Reject unknown tags when opening for writes. Completed, Failed and Cancelled are terminal. Their matching command receipts may be read or replayed under current read authority. A denial or loss of authority can leave verified progress durable. Paused means a requested pause has finished draining. Recovering means effect or worker identity must be reconciled, or a stopped assignment is being revalidated. Blocked carries a typed blocker and durable return stage. AwaitingApproval carries the exact proposed scope change or scope requiring renewed authority. A pending stop lives on the aggregate while Recovering.

An accepted stop fences the worker epoch immediately. A later authorized cancel supersedes any other disposition. Revocation or expiry upgrades a pending pause to AwaitingApproval. A recorded permanent failure stays Fail unless cancelled. Keep the first recorded reason for each disposition. Resolve races with the state revision, never event occurrence time. No transition gets implied from tag ordering.

**ZIP-ASSIGNMENTS-STATE-T01.** Round-trip every state tag. Reject unknown tags and terminal-to-active transitions. Verify pending pause becomes AwaitingApproval when the grant is revoked.
