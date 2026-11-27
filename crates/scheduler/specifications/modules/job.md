# Immutable scheduled demand and fenced result

**ZIP-SCHEDULER-JOB-001 · v1.1 candidate · Owner** Scheduler maintainers

**Planned source** `crates/scheduler/src/job.rs`

## Rust declarations

```rust
use std::num::NonZeroU64;
use foundation::identity::identifier::Identifier;
use foundation::types::{digest::Digest, duration::DurationMillis};
use resources::allocation::allocator::DemandVector;
use resources::admission::AttemptKey;

pub struct JobKey {
    assignment: Identifier,
    task: Identifier,
}

impl JobKey {
    pub fn new(assignment: Identifier, task: Identifier) -> Result<Self, crate::error::SchedulerError>;
    pub fn assignment(&self) -> Identifier;
    pub fn task(&self) -> Identifier;
}

pub struct JobSpec {
    key: JobKey,
    workspace: Identifier,
    principal: Identifier,
    plan: Digest,
    dependencies: Box<[JobKey]>,
    priority: u16,
    demand: DemandVector,
    requested_lifetime: DurationMillis,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum JobState {
    Waiting, Ready, Reserving, Dispatched, Recovering, RetryWait, Blocked, Terminal,
}

pub struct JobClaim {
    job: JobKey,
    attempt: AttemptKey,
    epoch: NonZeroU64,
    plan: Digest,
}

impl JobSpec {
    pub fn new(
        key: JobKey,
        workspace: Identifier,
        principal: Identifier,
        plan: Digest,
        dependencies: Box<[JobKey]>,
        priority: u16,
        demand: DemandVector,
        requested_lifetime: DurationMillis,
    ) -> Result<Self, crate::error::SchedulerError>;
}

impl JobClaim {
    pub fn job(&self) -> &JobKey;
    pub fn attempt(&self) -> &AttemptKey;
    pub fn epoch(&self) -> NonZeroU64;
    pub fn plan(&self) -> Digest;
}

pub(crate) struct TrustedAttemptReceipt {
    job: JobKey,
    attempt: AttemptKey,
    epoch: NonZeroU64,
    plan: Digest,
    evidence: Digest,
}
```

Validate Assignment and Task identifier kinds when constructing a key, and Workspace and Principal kinds when constructing the specification. Fields stay private and immutable after enqueue. The request decoder applies configured size bounds before constructing the dependency slice or admitted demand. Require a positive finite requested lifetime. The constructor validates shape; enqueue additionally validates live permission for the requested priority and dependency scope. Dependencies must identify existing jobs within the same authorized assignment. Reject self edges, duplicate edges and cycles before writing. Canonicalize dependency order by typed identifier and UUID bytes. Bind the verified specification digest and the request validation result to the queue row.

The job key maps one-to-one to the Resources assignment and task identity. The storage transaction increments the attempt number and claim epoch with checked arithmetic. The attempt number is a nonreused ID even when admission definitively fails. Job claim epoch, allocator epoch and runtime ownership generation are independently checked against their owners. The runtime may inspect the read-only claim through accessors and receives a lease only from Dispatch.

The scheduler binds the injected runtime receipt verifier and authenticated caller in its composition root. Supply an untrusted evidence reference to the verifier and construct a receipt only from its scoped verified result. Keep raw constructors crate-private; no untrusted deserialization into TrustedAttemptReceipt. The evidence digest names an immutable record with terminal runtime disposition, release or settlement evidence, approved failure classification and effect receipts. A worker payload or a PID cannot establish trust. An exact receipt replay returns the stored decision after checking authority. A mismatched epoch, plan or evidence never overwrites a committed record.

**ZIP-SCHEDULER-JOB-T01.** Fence attempt A after its deadline, reconcile it, then dispatch B. Deliver A's delayed success and verify B retains ownership and the job result is unchanged.
