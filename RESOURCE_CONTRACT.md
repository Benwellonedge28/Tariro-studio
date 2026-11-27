# Shared resource admission contract

**ZIP-RES-001 · v1.0 · Owner:** Resource and runtime maintainers. **Maturity:** D4 candidate.

Each expensive operation has a nonempty demand vector and known execution boundary. Coordinates identify a metric and pool, for example RAM bytes, logical CPU shares, GPU bytes keyed by device, disk bytes keyed by volume, process or worker count, monotonic wall duration, tokens, bandwidth, and spend by currency. Capabilities and discovered capacity are separate from current usage. Absence denotes unsupported or unknown; a declared zero denotes known zero.

Rust integration contract for the resources crate. `AdmissionRequest` owns the principal scope, assignment/attempt ID, requested demand, deadline and compatible device constraints. `CapacityRevision` identifies the capability snapshot. `ResourceLease` is an opaque, epoch-fenced handle with admitted ceilings and policy revision.

```rust
pub trait ResourceAdmission: Send + Sync {
    fn reserve(&self, request: AdmissionRequest, revision: CapacityRevision)
        -> Result<ResourceLease, AdmissionError>;
    fn charge(&self, lease: &ResourceLease, usage: UsageDelta)
        -> Result<(), ChargeError>;
    fn release(&self, lease: ResourceLease, cleanup: CleanupReceipt)
        -> Result<(), ReleaseError>;
}
```

Discovery snapshots include provenance, units, observed capacity, enforcement capability and age. Treat host-reported totals as upper bounds; intersect with containment, workspace, assignment and policy budgets. For each coordinate subtract infrastructure reserve, unreclaimed reservations and accounted external pressure. Use checked arithmetic and fail if a required coordinate cannot be enforced. Atomically reserve the vector across all applicable pools; partial success is forbidden.

| Input/state | Next state | Guard |
| --- | --- | --- |
| Valid demand | Reserved | Capacity and policy revisions current, full vector fits |
| Start receipt | Active | Current lease epoch, controls installed |
| Pressure or revoke | Draining | Close admission, cancel or rebalance within policy |
| Verified cleanup | Released | Release only after owner verifies all resources are reaped |
| Lease expired or owner lost | Recovering | Fence output and reconcile physical resource occupancy |

Admission precedes allocate, spawn, stream, attach device or invoke plugin. Account metered costs continuously; deny further work at upper bounds. Backpressure uses bounded queues and policy-specified scheduling fairness. Authorized degradations can reduce context, parallelism or cache demand; changing locality or widening egress requires separate scope. Distributed capacity is relative to a specific authenticated node and lease and never treated as local availability.

Evidence covers admission/denial code, policy revision, capacity age, planned/actual usage, cleanup and lease epoch. Negative tests simulate stale reports, double release, concurrent oversubscription and uncooperative children; reserved capacity remains unavailable until cleanup or fenced reconciliation.
