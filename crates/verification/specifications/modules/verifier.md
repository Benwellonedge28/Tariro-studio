# Scoped candidate verification

**ZIP-VERIFICATION-VERIFIER-001 · v1.1 candidate · Owner** Verification maintainers

**Planned source** `crates/verification/src/verifier.rs`

A sealed candidate binds the immutable repository or artifact identity, pinned base, candidate commit/tree or artifact digest, and reviewed diff and instruction digests as applicable. Verify the plan against that exact candidate and the live policy before accessing any evidence or dispatching a check.

```rust
use std::{future::Future, pin::Pin};
use foundation::cancellation::CancellationToken;
use crate::{error::VerificationError, evidence::RawObservation};

pub trait VerificationRunner: Send + Sync {
    fn observe<'a>(
        &'a self,
        check: &'a CheckRequest,
        cancellation: &'a CancellationToken,
    ) -> Pin<Box<dyn Future<Output = Result<RawObservation, VerificationError>> + Send + 'a>>;
}
```

`CheckRequest` binds the candidate seal, gate, approved attempt identity, immutable input and fixture references, source policy and deadline. Composition provides a qualified runner, authorization check, admitted resource budget and evidence storage. No Testing, Governance or Runtime crate dependency is required. Execute runner actions under scoped read or verification authority. A mutating check is allowed only within its separately approved disposable test workspace and cannot modify the candidate seal.

Take verified observations from the runner or trusted assessor adapter. Validate provenance and outputs before caching immutable evidence. A missing runner, limit exhaustion, stop or unknown reply cannot become passing evidence. Retain already committed receipts after cancellation, and reconcile uncertain storage writes by stable attempt identity. Recompute the exact candidate and policy match at acceptance and before the caller uses the resulting receipt for an effect.

**ZIP-VERIFICATION-VERIFIER-T01.** Change a byte after verification. Evidence remains available as history and fails the new candidate's acceptance guard.
