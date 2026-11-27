# Verification failure classes

**ZIP-VERIFICATION-ERROR-001 · v1.1 candidate · Owner** Verification maintainers

**Planned source** `crates/verification/src/error.rs`

```rust
#[non_exhaustive]
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum VerificationError {
    InvalidPlan,
    ScopeDenied,
    BudgetExceeded,
    EvidenceMissing,
    EvidenceStale,
    FactUnverified,
    EvidenceConflict,
    RunnerUnavailable,
    DeadlineExceeded,
    Cancelled,
    OutcomeUnknown,
}
```

Validate request and scope before revealing gate or evidence existence. A missing or stale observation blocks its gate. FactUnverified identifies invalid origin or unresolved provenance. OutcomeUnknown preserves an original attempt whose storage or runner response was lost and requires reconciliation. An executed mandatory failed check is a typed evidence result and may determine Failed. A timeout, cancellation or transport error alone does not prove execution or failure. Redact scope-sensitive evidence and endpoints.

**ZIP-VERIFICATION-ERROR-T01.** A missing result, expired check and executed failing check have distinct evidence status and cannot be interchanged by an adapter.
