# Runtime and scheduling

**ZIP-RT-001 · v1.2 · Owner:** Runtime and scheduler maintainers. **Maturity:** D4 candidate for the local attempt lifecycle.

## Ownership and scope

The scheduler owns eligibility, queue ordering, job claims and retry budget. The runtime owns the local attempt, process containment, cancellation, durable result and teardown. Resources owns admission, permit fencing and ledger release. Storage owns compare-and-swap transactions and the transactional outbox. Each external provider owns verification of its effects. This contract covers a single installation and leaves distributed ownership to the distributed specification.

The scheduler's job claim epoch, the runtime's owner generation and the resource allocator's epoch belong to different owners. Compare each against its owning journal. The shared allocation identity is assignment ID, task ID and nonzero attempt number. A retry receives a new attempt number. Lease renewal stays prohibited by the [resource contract](../../RESOURCE_CONTRACT.md).

## Durable transitions

Record startup intent before host preparation. Atomically consume a one-way launch claim before the adapter is allowed to execute the task body. A dispatch claim records permission to try once. A confirmed start records containment and observed execution. Neither is a completion receipt.

| From | Command or observation | To | Durable change |
| --- | --- | --- | --- |
| Queued | Current scheduler claim and matching reserved lease | Leased | Record attempt, owner generation, resource binding and containment locator |
| Leased | Installed controls verified, lease activated, live checks pass and launch claim commits | Leased | Set permanent launch-claim marker for this attempt before dispatch |
| Leased | Current owner verifies launch | Running | Store proof reference and emit transition event |
| Leased or Running | Authorized stop, deadline or lease loss observed | Cancelling | Record first stop cause and forbid worker publication |
| Leased, Running or Cancelling | Lost owner, ambiguous dispatch/commit, unverified teardown or unresolved provider effect | RecoveryRequired | Fence worker and retain unresolved obligations |
| RecoveryRequired | Recovery owner confirms live occupancy or pending cleanup | Cancelling | Record recovery progress, retain obligations and forbid launch |
| Leased, Running, Cancelling or RecoveryRequired | Trustworthy terminal evidence and confirmed release | Succeeded, Failed or Cancelled | Record immutable disposition, receipt and one terminal outbox event |
| Any terminal | Authorized replay of the same command | Same terminal | Return recorded receipt with no second event |

All other edges deny. An exact accepted command replay returns its stored decision to an authorized caller. It grants neither dispatch nor worker publication. Increment runtime owner generation on a verified takeover and reject earlier worker messages regardless of resource-manager state. An unavailable journal or platform observer prevents launch. An external effect receives its own stable intent and authorization under the [recovery standard](../../RECOVERY_STANDARD.md).

## Stop, deadlines and restart

Check the current claim, runtime ownership, resource permit, grant, cancellation and effective monotonic deadline at launch and worker publication. Derive the effective deadline from the request, resolved policy and the resource permit. Eligibility ends at equality. Stop grace uses resolved `runtime.stop_grace_ms` clipped to the applicable deadline. Continue verified cleanup under cleanup authority when execution authority is revoked or expired. A cancelled foreground wait leaves supervision intact. Daemon shutdown stops intake and selects one installation drain deadline from resolved `runtime.shutdown_drain_ms` and any tighter caller deadline. [Ordered shutdown](../../crates/runtime/specifications/modules/control/shutdown.md) owns the single clock sample, checked calculation, replay and preservation of unfinished recovery obligations.

Validate storage before startup. Reconcile each unresolved attempt before the scheduler may run any replacement for its task. Restore the highest contiguous verified checkpoint under the [checkpoint contract](../../crates/runtime/specifications/modules/checkpoint/store.md). Old monotonic instants cannot establish fresh authority. The recovery path and evidence rules are defined in the [crash recovery](../../crates/runtime/specifications/modules/recovery/crash_recovery.md) and [reconciliation](../../crates/runtime/specifications/modules/recovery/reconciliation.md) contracts.

## Verification

[Lifecycle fixtures](../../contracts/acceptance/runtime/lifecycle-fixtures.json) map launch, checkpoint, fencing, teardown and response loss to ZR-001, ZR-003, ZR-004, ZR-006 and ZR-007. Exercise them first against a deterministic journal/adapter harness and then against each supported real process adapter. Retain exact inputs, resolved limit and policy revisions, observed event counts, final resource state and immutable evidence. See [runtime](../../crates/runtime/DESIGN.md), [scheduler](../../crates/scheduler/DESIGN.md), [events](../../crates/events/DESIGN.md) and [requirements](../../REQUIREMENTS.md).

Use the [drain policy fixtures](../../contracts/acceptance/runtime/drain-policy-fixtures.json) to verify v1 defaults migration, authorization-safe cutoff selection, reload stability and retained obligations on expiry. Independent review, compilable Rust signatures and actual fault-injection runs remain completion gates.
