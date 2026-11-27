# Enforceable demand gate

**ZIP-RESOURCES-ADMISSION-001 · v1.1 candidate · Owner** Resources maintainers

**Planned source** `crates/resources/src/admission.rs`

## Public interface

Rust declarations specify the API. Implementations and private construction belong to the listed module owners.

```rust
use std::time::Instant;
use foundation::identity::identifier::Identifier;
use crate::allocation::lease::{ResourceLease, StartProof, CleanupProof};
use crate::allocation::allocator::{DemandVector, UsageDelta};
use crate::error::ResourceError;

pub struct CapacityRevision(u64);
pub struct PolicyRevision(u64);

pub struct AttemptKey {
    task: Identifier,
    number: std::num::NonZeroU64,
}

pub struct AdmissionRequest {
    principal: Identifier,
    workspace: Identifier,
    assignment: Identifier,
    attempt: AttemptKey,
    policy: PolicyRevision,
    demand: DemandVector,
    deadline: Instant,
}

pub trait ResourceAdmission: Send + Sync {
    fn reserve(
        &self,
        request: AdmissionRequest,
        revision: CapacityRevision,
    ) -> Result<ResourceLease, ResourceError>;
    fn start(&self, lease: &ResourceLease, proof: StartProof) -> Result<(), ResourceError>;
    fn charge(&self, lease: &ResourceLease, delta: UsageDelta) -> Result<(), ResourceError>;
    fn release(
        &self,
        assignment: Identifier,
        attempt: &AttemptKey,
        proof: CleanupProof,
    ) -> Result<(), ResourceError>;
}
```

Capacity and policy revisions are opaque, copyable, equality-comparable generations issued by their owning services. Capacity revisions identify a complete snapshot within one manager process; the current revision must be obtained from that manager. Reading a generation grants no authority. Construct an `AttemptKey` through `AttemptKey::new(task: Identifier, number: std::num::NonZeroU64) -> Result<Self, ResourceError>` and require Task kind. Implement `AdmissionRequest::new(principal: Identifier, workspace: Identifier, assignment: Identifier, attempt: AttemptKey, policy: PolicyRevision, demand: DemandVector, deadline: Instant) -> Result<Self, ResourceError>`. Check Identifier kinds and demand shape. Store scope immutably. The manager independently checks the caller's short-lived authenticated context against the stored tuple and live grant, using an injected verifier at composition. Authentication and grant issuance stay outside Resources. Transactions must linearize the admission decision against the current authority snapshot or fail with stale policy. A new request with an outdated policy revision must be rebuilt. An existing lease retains its admission revision and may continue under a newer revision only when the live verifier confirms the existing grant and admitted bounds remain valid. Removing a permission fences new effects before the next permit.

## Algorithm and effect boundary

1. Validate request shape with no inventory access. Authenticate and authorize the attempted operation and all required pools. Denials return the same code regardless of host state.
2. Inside the allocator transaction check the current effective policy, deadline, and current attempt record. Resolve authorized replays according to [reservation](allocation/reservation.md). For a new attempt, require the current capacity revision and fresh, supported and enforceable coordinates. Run [allocator](allocation/allocator.md) and [quota](allocation/quota.md) checks in the same transaction. Persist all debits and the reservation or persist none.
3. For `start`, trusted supervision supplies proof that containment and metering were installed for the exact lease. Commit activation before allowing work to proceed. Installation may hold prepared, suspended resources within the Reserved lease. Dispatch goes through the attempt's single supervised launch gate. After an uncertain dispatch, reconcile that gate before another dispatch.
4. Charge metered increments before authorizing the corresponding usage. If a provider only reports usage after invocation, reserve the maximum enforceable call allowance and use trusted provider receipts to settle it. When a bound cannot be enforced, reject the operation. Stop issuing resource and effect permits when the live lease, deadline or grant check fails.
5. The cleanup verifier can look up the durable reservation by assignment and attempt after a restart. It may release a fenced attempt only with current proof under [lease](allocation/lease.md). Stop and await teardown outside the allocator lock. Mutations that committed before cancellation are reconciled by attempt key.

Lease operations require a finite transaction budget from resolved configuration. No network call, process wait, callback or host probe executes inside the transaction. Unavailable storage and expired deadlines return typed failure. An ambiguous commit returns `OutcomeUnknown` and issues no lease pending reconciliation. If a caller needs a later deadline or different demand, end or fence the original attempt and authorize a new attempt. Never extend a live lease in place.

## Acceptance

**ZIP-RESOURCES-ADMISSION-T01.** Authorization denial reveals no capacity detail. Missing mandatory device enforceability denies before dispatch. Known zero remains distinct from unknown. A replay cannot renew a lease or install a second supervisor.
