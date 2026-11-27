# Repository failure and reconciliation codes

**ZIP-REPOSITORY-ERROR-001 · v1.1 candidate · Owner** Repository maintainers

**Planned source** `crates/repository/src/error.rs`

```rust
#[non_exhaustive]
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum RepositoryError {
    InvalidRef,
    InvalidPath,
    ScopeDenied,
    InstructionsIncomplete,
    InstructionConflict,
    StaleRevision,
    UnsupportedCapability,
    Conflict,
    BudgetExceeded,
    VerificationMismatch,
    ProviderUnavailable,
    UnknownEffect,
    Cancelled,
}
```

Validate shape and scope before reflecting repository existence or private state. Check pinned base, instructions and affected path completeness before creating a review seal. Recheck branch preconditions and live authority before effect dispatch. Use StaleRevision for an observed changed pin, Conflict for incompatible provider state, and VerificationMismatch for an observed effect that disagrees with required evidence. Preserve the observed effect and retain reconciliation records. Use UnknownEffect when dispatch could have committed but its outcome cannot be established. ProviderUnavailable denotes predispatch denial or proven no effect; retry still requires current scope and the same intended request. Cancellation before submission is Cancelled. After submission classify the effect and report actual known evidence. Redact credentials, payload bytes and unrelated refs.

**ZIP-REPOSITORY-ERROR-T01.** Lose the reply after a possible push, then observe its recorded commit. Before observation return UnknownEffect, with no assertion of rollback or retry permission.
