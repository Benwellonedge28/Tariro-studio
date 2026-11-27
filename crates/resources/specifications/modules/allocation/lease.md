# Epoch fencing and scoped proof

**ZIP-RESOURCES-ALLOCATION-LEASE-001 · v1.1 candidate · Owner** Resources maintainers

**Planned source** `crates/resources/src/allocation/lease.rs`

## Interface

```rust
use std::num::NonZeroU64;
use foundation::identity::identifier::Identifier;
use foundation::types::digest::Digest;
use crate::admission::{AttemptKey, PolicyRevision};

pub struct ResourceLease {
    manager_instance: NonZeroU64,
    reservation_id: NonZeroU64,
    allocation_epoch: NonZeroU64,
    attempt: AttemptKey,
    principal: Identifier,
    workspace: Identifier,
    assignment: Identifier,
    policy: PolicyRevision,
}

pub struct StartProof {
    reservation_id: NonZeroU64,
    allocation_epoch: NonZeroU64,
    attempt: AttemptKey,
    supervisor: Identifier,
    installed_controls: Digest,
    proof_digest: Digest,
}

pub struct CleanupProof {
    reservation_id: NonZeroU64,
    cleanup_epoch: NonZeroU64,
    attempt: AttemptKey,
    supervisor: Identifier,
    verifier: Identifier,
    teardown_evidence: Digest,
    metering_evidence: Digest,
    proof_digest: Digest,
}

impl ResourceLease {
    pub fn attempt(&self) -> &AttemptKey;
}
```

Manager instance and reservation identities are monotonic nonzero values issued by the journal and never reused in its namespace. The initial allocation and cleanup epochs are nonzero. Supervisor and verifier identifiers have Principal kind and must be enrolled for the specific operation. A worker cannot construct, deserialize or clone a lease. Redacted debug output contains no authority material. Consulting the borrowed attempt identifier grants no effect permission. Every permit checks the durable reservation, the live worker epoch and policy. Dispatched external effects still use their own authorized effect gate.

A start proof binds reservation identity, supervisor identity, current allocation epoch, attempt, installed containment, installed metering controls and a stable proof digest. The supervisor issues it only after observing those controls. The start proof authorizes a state transition and contains no reusable authority to spawn. Runtime must separately claim one dispatch for the attempt and reconcile uncertain spawn before a retry.

A cleanup proof binds the reservation, its original attempt and supervisor, current cleanup epoch, verification identity, observed absence of live occupancy, and final metered receipt identity or confirmed absence of charges. It has a stable digest across retransmission. A delayed worker cannot release a fenced reservation by returning its old receipt. Trusted recovery observes or reconciles ownership and installs a current proof, even when the original supervisor is unavailable. Proof issuers are injected at composition. A process unable to prove absence keeps the affected hold.

Treat an opaque proof as valid only after the manager has matched the trusted authority, scope, epoch and evidence. Never parse an agent-provided string as proof or trust a reported boolean. No Rust contract here grants public proof construction.

**ZIP-RESOURCES-ALLOCATION-LEASE-T01.** Fence the worker at expiry and deny its later charge or publication. Reject its older cleanup evidence and retain occupied capacity until verified recovery supplies matching evidence.
