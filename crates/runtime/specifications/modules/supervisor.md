# Worker ownership and cleanup

**ZIP-RUNTIME-SUPERVISOR-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the local attempt protocol.

**Planned source:** `crates/runtime/src/supervisor.rs`

## Journal and internal types

Use the [storage domain-record envelope](../../../../specifications/2500-storage/storage.md). Key attempts by typed assignment ID, task ID and nonzero attempt number, with a unique open-attempt index per task within its assignment. Store schema major/minor, record revision, runtime owner generation, checked scheduler claim reference, plan/action digests, resource reservation lookup binding, phase, permanent launch-claim bit, containment locator, immutable observation references, first stop cause if recorded, contiguous checkpoint reference and optional terminal receipt. Use explicit lowercase state tags, Foundation encodings for IDs and digests, and canonical unsigned decimal strings for quantities serialized to JSON. Keep live monotonic instants and worker handles in memory. The adapter must version its opaque durable locator and bind it to the installation and attempt. Unsupported locator versions prevent automatic recovery for that attempt.

`OwnedLaunch` is a crate-private opaque constructor result owned by the supervisor. Its private fields bind the attempt tuple, runtime owner generation and prepared adapter identity. It has no clone or serialization. `ProcessObservation` is a crate-private tagged value from a trusted adapter, bound to the same attempt, locator and observation evidence digest. Its variants are ConfirmedRunning, ConfirmedExited, ConfirmedAbsent and Unknown. An exit observation includes a platform exit status where available. Exited or Absent requires evidence for the whole containment group before use as teardown proof. A stale worker observation can at most trigger an independent trusted inspection.

## Ordering and transaction boundaries

1. Verify the current job claim and lease binding. Write the Leased record and unique locator before creating any attempt-related host state. Reject a competing attempt while the task has an unresolved predecessor.
2. Prepare a contained, blocked execution context under the reserved lease. If the adapter creates a process during preparation, it must hold that process before task code and expose its durable lookup. Verify required controls and use trusted `StartProof` to activate the lease.
3. Consume the launch claim with a revision-checked transaction. Check ownership again at the executor gate. Hold no storage transaction across host or resource calls. Once consumed, the claim is permanent. A crash between claiming and observing launch requires inspection. Even proven absence never reopens that claim.
4. Store accepted worker output as an immutable provisional reference only while the worker generation, live resource permit and output gate agree. The same checked journal transaction resolves a race with recording a stop. If stop commits first, reject later worker output. If verified outcome staging commits first, keep its disposition through later cleanup. Verified external receipts follow the effect-specific rules regardless of worker signal order.
5. On stop, close that attempt's gates, request cooperative stop and enforce the resolved grace deadline. On every exit, close the gates and verify the complete containment group is absent and final usage is settled. Trusted supervision or recovery supplies the [cleanup proof](../../../resources/specifications/modules/allocation/lease.md). The release transaction runs separately with the resource journal as authority. If release response is lost, reconcile or replay the same authorized proof. Keep the runtime attempt open until release is confirmed.
6. After teardown, settlement and reconciliation for every recorded effect key, atomically store terminal disposition and one terminal outbox event. Require immutable evidence for success. If no success/effect was accepted and the first committed stop was explicit cancellation, use Cancelled with confirmed cleanup. A verified failure, timeout or lease loss uses Failed with its cause. An uncertain observation keeps RecoveryRequired. Callers read outcomes through the result contract. Notifications after commit are replayable delivery.

## Acceptance

**ZIP-RUNTIME-SUPERVISOR-T01.** Interrupt before and after launch and release. At every point verify one body per attempt, no ledger credit while occupancy is unknown, and one immutable terminal receipt and event after recovery. Race cancellation against staging a verified result in both orders. See [fixtures](../../../../contracts/acceptance/runtime/lifecycle-fixtures.json).
