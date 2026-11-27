# Atomic vector allocation

**ZIP-RESOURCES-ALLOCATION-ALLOCATOR-001 · v1.1 candidate · Owner** Resources maintainers

**Planned source** `crates/resources/src/allocation/allocator.rs`

## Types and capacity basis

```rust
use std::collections::BTreeMap;
use std::num::NonZeroU64;
use foundation::identity::identifier::Identifier;
use crate::error::ResourceError;

#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd)]
pub enum Dimension {
    CpuMillicores, RamBytes, AcceleratorBytes(PhysicalId), DiskBytes(PhysicalId),
    BandwidthBytesPerSecond(PhysicalId), Processes, Workers, ModelSlots,
    Tokens, SpendMinor(CurrencyCode),
}

#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd)]
pub struct PhysicalId([u8; 16]);

#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd)]
pub struct CurrencyCode([u8; 3]);

pub struct DemandVector(BTreeMap<Dimension, u64>);

pub struct UsageDelta {
    sequence: NonZeroU64,
    amounts: DemandVector,
}

impl DemandVector {
    pub fn new(entries: &[(Dimension, u64)]) -> Result<Self, ResourceError>;
    pub fn entries(&self) -> &BTreeMap<Dimension, u64>;
}
impl UsageDelta {
    pub fn new(sequence: NonZeroU64, amounts: DemandVector) -> Result<Self, ResourceError>;
}
```

Scope keys use `Host(PhysicalId)`, `Service(PhysicalId)`, `Workspace(Identifier)`, or `Assignment(Identifier)` plus dimension. Host and service pool IDs are minted and resolved by trusted inventory. Device, volume and network IDs come from registered adapters. Physical IDs reject all-zero identities. Currency codes are exactly three uppercase ASCII letters and must be enabled by the effective provider policy. Compare canonical dimension order using variant declaration order and payload bytes. Within a dimension compare scope by the stated variant order and then by identity bytes. The manager orders checks independent of caller insertion order.

Construct the vector within a configured container bound already enforced by the consuming boundary. Reject empty or duplicate demand coordinates, but retain explicit zero entries for known-capacity checks. Only Tokens and SpendMinor are metered in this interface version. Reject occupancy-only and all-zero usage deltas when constructing them. A delta naming a metered dimension outside the admitted demand fails with `InvalidRequest` at charge. Token coordinates bind the model or service scope through trusted dispatch context. A caller cannot choose a new service or currency to evade a ledger.

A fresh probe declares its accounting basis. Normalize all occupancy readings to the maximum amount usable by managed workloads on that physical pool before subtracting held reservations.

| Probe basis | Normalized managed capacity |
| --- | --- |
| Enforced total `T`, measured other occupancy `E`, extra withheld headroom `H` | `max(0, T - E - H)` |
| Observed free `F` under enforceable ceiling `T`, measured managed occupancy `M`, extra withheld headroom `H` | `max(0, min(T, F + M) - H)` |

Withhold headroom exactly once. For free readings, require that `F` already reflects other occupancy and that `M` is measured from the managed occupants of the same pool at the same observation. Held reservations are an accounting promise and cannot substitute for `M`. Reject incompatible basis, incoherent samples and missing, stale or unsupported readings. Compare independently enforceable ceilings from overlapping host and container scopes and use the tighter normalized capacity, then subtract held reservations once. A sample that fails the checked addition cannot produce a capacity. Capacity shrinkage records pressure and yields zero free capacity when held reservations exceed the new capacity.

## Atomic checks

For occupancy, free capacity is normalized capacity minus current held promise, floored at zero. Metered free allowance is the cap minus both verified consumed units and held unused units, floored at zero. For every coordinate check the physical or service pool and applicable quota pools. Transactions validate all coordinate errors by the precedence in [error](../error.md), then add the full vector to every applicable hold or leave the ledger unchanged. All reservation transitions and accounting changes use a single serializable local transaction. Acquire no per-pool locks and execute no host reads inside it. Revalidate inputs whenever a storage conflict forces transaction retry.

For a metered charge, atomically transfer the delta from unused hold to consumption across the admitted scopes. Reject an unreserved dimension, out-of-order sequence or delta exceeding the unused hold. Matching the most recent committed sequence and digest is an idempotent replay. Earlier sequences return conflict and require journal reconciliation. A fixed concurrent promise is already held for the lifetime of the lease. That promise never gets credited repeatedly for measurements of the same work.

**ZIP-RESOURCES-ALLOCATION-ALLOCATOR-T01.** Concurrent requests for two shared pools cannot partially reserve either pool. A total and a free probe with equivalent observations give the same answer.
