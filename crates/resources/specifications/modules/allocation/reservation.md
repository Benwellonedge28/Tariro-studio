# Reservation lifecycle and receipts

**ZIP-RESOURCES-ALLOCATION-RESERVATION-001 · v1.1 candidate · Owner** Resources maintainers

**Planned source** `crates/resources/src/allocation/reservation.rs`

## Durable state

Key one record by assignment, task and attempt number. Store schema version, reservation identity, workspace and principal IDs, trusted scope and pool IDs, original demand and authorized source policy, manager instance, allocation epoch and cleanup epoch, state, dispatch status reference, last accepted metered sequence and digest, accumulated consumption, unused held allowance, start proof digest and final cleanup proof digest when present. Encode identity via Foundation. Store unsigned quantities as canonical unsigned decimal strings in JSON and enum tags as stable lowercase names. Unique attempt identity and state indexes support lookups and recovery scans. The local monotonic deadline stays in process memory. Audit timestamps may be persisted. Restart treats outstanding leases from an earlier manager instance as fenced. No wall-time timestamp reactivates a lease.

The resources crate owns a journal port. Composition provides persistence through an adapter that can transact reservations, all affected ledgers and audit intents together. Storage is not a direct crate dependency. Use checked revision and epoch increments. Retain a stable, replayable receipt for the latest admitted metered sequence and for a successful release until retirement conditions hold. Any ambiguous commit prevents issuing new permits until reconciled. Lock order and transaction scope are defined by the [allocator](allocator.md). Preserve consumed allowance through cleanup and restart. Preserve comparison receipts until no valid replay grant remains and all outcomes are reconciled. Compact released records only when attempt identity cannot be reused within any still-valid grant.

| From | Event and guard | To | Ledger effect |
| --- | --- | --- | --- |
| Absent | Authorized, fresh admission commits | Reserved | Debit the whole vector |
| Reserved | Matching start proof with live epoch and grant | Active | Keep the reservation |
| Reserved or Active | Pressure, cancellation or revocation fences worker and advances cleanup epoch | Draining | Hold all occupied and unsettled amounts |
| Reserved, Active or Draining | Deadline reached, manager lost or dispatch outcome uncertain | Recovering | Fence old worker, retain holds, advance cleanup epoch on fencing or recovery ownership change |
| Active | Contiguous metered charge under live authority | Active | Transfer unused hold to consumed |
| Reserved, Active, Draining or Recovering | Trusted proof confirms teardown and final usage | Released | Return occupancy and unused allowance once |
| Released | Same cleanup proof from an authorized cleanup principal | Released | No ledger change |

Release with an incompatible digest is a conflict. Attempt creation with the same authorized request and same deadline in the same manager can return a fresh handle to the same Reserved or Active record. It cannot renew or enlarge the reservation or authorize dispatch again. A different request for the same key is a conflict. A fenced or released attempt cannot be reactivated. Matching start proof replay returns the existing result only while the lease and grant remain live. A retry carries original command identity. Use attempt key for reserve, attempt and proof digest for start and cleanup reconciliation, and attempt and sequence for metering. Updates hold no external wait while locked.

Cleanup takes the assignment and attempt key plus proof. It does not require restoration of any worker lease. Recovery first stops privileged dispatch, then obtains runtime teardown evidence and reconciles provider receipts. A valid final receipt can settle remaining bounded spend under cleanup authority in the release transaction. Apply only the increment beyond already verified consumption, reject a smaller cumulative total or a total beyond the reserved limit, and keep unresolved holds visible. Use revised policy for future attempts. Never reset usage by restarting a coordinator.

**ZIP-RESOURCES-ALLOCATION-RESERVATION-T01.** Save one release transaction, lose its response and retry with identical evidence. Verify one ledger credit. Repeat with a different digest and verify conflict. Restart with an uncertain provider result and verify the hold persists until a matching receipt arrives.
