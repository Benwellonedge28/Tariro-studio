# Documentation failure outcomes

**ZIP-DOCUMENTATION-ERROR-001 · v1.1 candidate · Owner** Documentation maintainers

**Planned source** `crates/documentation/src/error.rs`

```rust
#[non_exhaustive]
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum DocumentationError {
    ScopeDenied,
    InvalidPlan,
    MissingSource,
    SourceUnavailable,
    InvalidSection,
    BrokenLink,
    UnsupportedClaim,
    EvidenceUnverified,
    Conflict,
    BatchOverLimit,
    StaleCandidate,
    BudgetExceeded,
    Cancelled,
    OutcomeUnknown,
}
```

Validate authority before returning source existence or evidence. Use safe path, gate and requirement references scoped to the caller. Missing source requires checked absence; unavailable evidence must not be classified as missing. UnsupportedClaim blocks document verification. A short exact batch maps to the assignment's AwaitingApproval state. An over-limit attempted change returns BatchOverLimit without making that change. OutcomeUnknown retains the original transaction or provider identity. A typed failure does not retract confirmed prior effects or checkpoints.

**ZIP-DOCUMENTATION-ERROR-T01.** A readable draft with a blocked factual claim remains unverified. Do not let an unavailable source be reported as empty content.
