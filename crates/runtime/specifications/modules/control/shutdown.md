# Ordered runtime shutdown

**ZIP-RUNTIME-CONTROL-SHUTDOWN-001 · v1.1 · Owner** Runtime maintainers. **Maturity** D4 candidate for local shutdown.

**Planned source** `crates/runtime/src/control/shutdown.rs`

## Request and ordering

Use the [lifecycle](../lifecycle.md) control path to accept shutdown, after verifying installation scope. Bind the operation to the runtime instance and a stable command identity. The composition root supplies a resolved absolute drain deadline from policy and the caller's tighter deadline when present. Use the same live clock as the [timeout contract](timeout.md). Accept an already reached drain deadline as immediate escalation. Persist attempt and effect progress in their owning journals. The process-local command result is tied to this instance. A replacement instance recovers outstanding work from those journals.

1. Atomically enter Draining and close intake before taking the active-work snapshot. Wake producers and waiters with the closed-intake disposition. Account for submissions accepted before closure until each has a durable registration, confirmed refusal or unresolved recovery entry. Block new launch permissions.
2. Signal cooperative stop for active work and record the first committed attempt stop separately from the installation shutdown. For each attempt, clip the grace deadline to its task and the overall drain deadline. A committed checkpoint, verified provisional outcome or known provider receipt remains available to recovery.
3. At the clipped grace boundary, use the trusted adapter to terminate the contained group and observe its exit. Settle usage and release reservations only on the supervisor's required proof. Resolve ambiguous releases and provider replies against their owning journals. Continue required reconciliation under cleanup authority after execution permission ends.
4. Before declaring Stopped, ensure each registered attempt is durably terminal with cleanup and effect settlement confirmed. Ensure the corresponding outbox records are committed. Delivery may continue through the event subsystem after restart. Live delivery and remote reachability are unnecessary to confirm those durable writes.
5. At the drain deadline, return the committed outcome if complete, otherwise return a bounded incomplete summary with references to unresolved records where available. An unreaped containment, uncertain launch or unresolved effect keeps its corresponding obligation. If the journal cannot confirm a write, report `OutcomeUnknown` and require recovery. Keep any continuing cleanup ownership live until responsibility is verifiably transferred or the process exits for startup recovery.

An exact authorized replay joins the same operation without resetting its deadline. A different payload under the same command identity returns `Conflict`. Subsequent authorized shutdown requests with a different identity may observe the first operation and cannot alter its deadline. Drop of an observation handle only ends that caller's wait. No caller cancellation reopens intake. Map unresolved work through the [runtime errors](../error.md).

## Composition requirement

Before enabling daemon shutdown, Configuration and Runtime maintainers must register and qualify the drain policy input under the [limits policy](../../../../../LIMITS_POLICY.md). Require a finite, validated drain deadline at the composition boundary. The per-attempt stop-grace key supplies only the cooperative window. The configuration binding remains open for independent design sign-off.

## Acceptance

**ZIP-RUNTIME-CONTROL-SHUTDOWN-T01.** Fill the admitted queue, block a producer and shut down concurrently with a registration. Verify all producers wake, later submissions fail before enqueue, accepted submissions are accounted for, and a dropped observer leaves shutdown active. Inject an unreaped descendant and a lost release reply. Verify held usage for the first case and a single reconciled release for the second. With the event sink offline, verified journal and outbox commits suffice for a clean stop. Use the release and teardown cases in the [lifecycle fixtures](../../../../../contracts/acceptance/runtime/lifecycle-fixtures.json).
