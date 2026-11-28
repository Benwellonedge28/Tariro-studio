# Ordered runtime shutdown

**ZIP-RUNTIME-CONTROL-SHUTDOWN-001 · v1.2 · Owner** Runtime maintainers. **Maturity** D4 candidate for local shutdown.

**Planned source** `crates/runtime/src/control/shutdown.rs`

## Request and ordering

Use the [lifecycle](../lifecycle.md) control path to accept shutdown, after verifying installation scope. Bind the operation to the runtime instance and a stable command identity. Persist attempt and effect progress in their owning journals. The process-local command result is tied to this instance. A replacement instance recovers outstanding work from those journals.

1. Atomically enter Draining and close intake before taking the active-work snapshot. Wake producers and waiters with the closed-intake disposition. Account for submissions accepted before closure until each has a durable registration, confirmed refusal or unresolved recovery entry. Block new launch permissions.
2. Signal cooperative stop for active work and record the first committed attempt stop separately from the installation shutdown. For each attempt, clip the grace deadline to its task and the overall drain deadline. A committed checkpoint, verified provisional outcome or known provider receipt remains available to recovery.
3. At the clipped grace boundary, use the trusted adapter to terminate the contained group and observe its exit. Settle usage and release reservations only on the supervisor's required proof. Resolve ambiguous releases and provider replies against their owning journals. Continue required reconciliation under cleanup authority after execution permission ends.
4. Before declaring Stopped, ensure each registered attempt is durably terminal with cleanup and effect settlement confirmed. Ensure the corresponding outbox records are committed. Delivery may continue through the event subsystem after restart. Live delivery and remote reachability are unnecessary to confirm those durable writes.
5. At the drain deadline, return the committed outcome if complete, otherwise return a bounded incomplete summary with references to unresolved records where available. An unreaped containment, uncertain launch or unresolved effect keeps its corresponding obligation. If the journal cannot confirm a write, report `OutcomeUnknown` and require recovery. Keep any continuing cleanup ownership live until responsibility is verifiably transferred or the process exits for startup recovery.

An exact authorized replay joins the same operation without resetting its deadline. A different payload under the same command identity returns `Conflict`. Subsequent authorized shutdown requests with a different identity may observe the first operation and cannot alter its deadline. Drop of an observation handle only ends that caller's wait. No caller cancellation reopens intake. Map unresolved work through the [runtime errors](../error.md).

## Resolve the drain deadline

Bind the [validated drain duration and provenance](../../../../configuration/specifications/modules/resources.md) before enabling daemon intake. At the first accepted shutdown, use the live monotonic clock in the [timeout contract](timeout.md). Under the intake synchronization point, read one complete validated configuration snapshot, sample the clock once, then close intake with the selected deadline. Hold no locks across adapter or journal I/O. Callers may supply a tighter absolute instant in that clock domain. Reject an incompatible domain with `InvalidSpec` before changing intake. If the caller deadline has elapsed, use the acceptance instant for immediate escalation.

Select the smaller of the configured duration and the nonnegative time remaining to the caller deadline if supplied. Using remaining duration before checked addition avoids overflow past a nearer caller bound. Fail an unrepresentable selection with `InvalidSpec` before accepting the command. Record the selected instant in the live operation and retain the duration, budget origin, configuration digest and policy revision for evidence. Reload or authorized repeat never recomputes an accepted deadline. Restart recovers durable obligations with current authority and a fresh clock domain.

At equality, the drain budget is exhausted. The per-attempt `runtime.stop_grace_ms` provides the cooperative window clipped to the task and installation deadlines. Continue only independently authorized cleanup after expiry. Preserve holds until teardown and usage evidence settle the resource ledger.

## Acceptance

**ZIP-RUNTIME-CONTROL-SHUTDOWN-T01.** Fill the admitted queue, block a producer and shut down concurrently with a registration. Verify all producers wake, later submissions fail before enqueue, accepted submissions are accounted for, and a dropped observer leaves shutdown active. Inject an unreaped descendant and a lost release reply. Verify held usage for the first case and a single reconciled release for the second. With the event sink offline, verified journal and outbox commits suffice for a clean stop. Use the release and teardown cases in the [lifecycle fixtures](../../../../../contracts/acceptance/runtime/lifecycle-fixtures.json).

Use the [drain policy fixtures](../../../../../contracts/acceptance/runtime/drain-policy-fixtures.json) to vary configured duration and caller cutoff independently. At expiry verify intake remains closed and an unreaped group retains its lease. Verify replay and reload preserve the original deadline even when clocks advance.
