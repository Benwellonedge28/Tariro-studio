# Resource error decisions

**ZIP-RESOURCES-ERROR-001 · v1.1 candidate · Owner** Resources maintainers

**Planned source** `crates/resources/src/error.rs`

## Public type

```rust
#[non_exhaustive]
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum ResourceError {
    InvalidRequest,
    PolicyDenied,
    StalePolicy,
    DeadlineExceeded,
    Conflict,
    StaleRevision,
    UnknownCapacity,
    UnsupportedCapacity,
    PressureLimit,
    Overflow,
    CapacityExceeded,
    InvalidLease,
    UnknownReservation,
    LeaseExpired,
    InvalidProof,
    CleanupRequired,
    Unavailable,
    OutcomeUnknown,
    ProbeFailed,
}
```

All admission operations use this type. Safe client diagnostics expose the code only. Restricted audit events may hold authorized scope and coordinate identifiers. Raw grants, credentials, adapter output and another tenant's usage never appear in errors.

## Precedence, mutation and retry

| Operation | Apply checks in this order |
| --- | --- |
| Reserve | InvalidRequest → PolicyDenied → StalePolicy → DeadlineExceeded → Conflict or exact replay → StaleRevision → UnknownCapacity → UnsupportedCapacity → PressureLimit → Overflow → CapacityExceeded |
| Start and charge | InvalidRequest → PolicyDenied → StalePolicy → InvalidLease → LeaseExpired → Conflict or exact replay → InvalidProof for start → Overflow → CapacityExceeded for charge |
| Release | InvalidRequest → PolicyDenied for cleanup authority → UnknownReservation → Conflict or exact replay → InvalidProof → CleanupRequired → Overflow |

Within a check, traverse coordinates in the allocator's canonical order. A valid cleanup principal can resolve a fenced or revoked worker's usage under a separate cleanup grant. Cleanup ignores the worker deadline.

A validation denial leaves ledgers and task state unchanged. Journal `Unavailable` means no mutation committed and may be retried under the same command key and live authority. `OutcomeUnknown` means the commit result is ambiguous. Re-read the journal by command identity before trying the same command again. If the journal is unavailable, keep reservations fenced and treat them as occupied. Emit `ProbeFailed` only at the probe boundary; admission sees the resulting missing or stale measurements as `UnknownCapacity`. Refresh stale policy, inventory or physical capacity before re-estimating. A different demand or deadline needs a different attempt. Invalid proof or conflict requires reconciliation or correction before retry.

**ZIP-RESOURCES-ERROR-T01.** For a request denied by policy, observe the same code with unknown, zero and nonzero host capacity. For an authorized positive request, unknown capacity returns `UnknownCapacity` and known zero returns `CapacityExceeded`.
