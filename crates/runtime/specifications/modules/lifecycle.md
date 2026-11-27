# Installation runtime lifecycle

**ZIP-RUNTIME-LIFECYCLE-001 · v1.1 · Owner** Runtime maintainers. **Maturity** D4 candidate for local composition.

**Planned source** `crates/runtime/src/lifecycle.rs`

## State and transitions

Track lifecycle and intake under one synchronization point. Lifecycle belongs to one runtime instance. Attempt state and owner generation remain durable under the [supervisor](supervisor.md). Serialize intake changes with acceptance of submissions. Resolve an accepted submission as a durable registration, verified refusal or unresolved journal outcome. An unresolved outcome blocks replacement pending recovery. Shutdown waits on or explicitly accounts for those in-flight registrations.

| From | Signal and condition | To |
| --- | --- | --- |
| Created | Startup acquires exclusive installation ownership, validates the journal and reconstructs unresolved obligations before enabling any launch. | Ready, intake closed |
| Ready | Supervisor and mandatory ports available, required startup reconciliation complete or unresolved tasks durably fenced from replacement. | Running, intake open |
| Created, Ready or Running | An authorized shutdown request closes intake and invalidates prelaunch eligibility. | Draining |
| Draining | All accepted registrations settled, local attempts terminal and required durable writes confirmed. | Stopped |
| Created, Ready, Running or Draining | A mandatory port fails or bounded shutdown ends with unresolved work, leaving durable recovery state or an indeterminate journal. | Failed, intake closed |

All lifecycle edges outside the table are denied. Commands that would reopen terminal intake fail with `Conflict`. An exact authorized repeat of an accepted shutdown returns the same operation and latest recorded result. Concurrent startup calls on one instance share the first startup result. Another instance requires proof of exclusive installation ownership or verified takeover before it may become Ready. If a startup dependency fails, close intake before returning. Skip new claims for any attempt whose owner, state or effects are ambiguous.

Runtime shutdown and request admission race at the intake synchronization point. A request admitted just before closure remains visible to the supervisor and may still lose its independent launch gate. A request arriving after closure returns a closed-intake disposition before queueing or changing the resource ledger. The scheduler or submitter unwinds its own pre-existing reservation according to its ownership rules.

## Restart

Reconstruct from durable attempt, resource and effect records with a fresh clock domain and ownership. Never reuse a previously granted launch capability across restart. [Crash recovery](recovery/crash_recovery.md) and [reconciliation](recovery/reconciliation.md) decide when a task may become eligible again. A process-wide state label alone cannot clear outstanding obligations.

## Acceptance

**ZIP-RUNTIME-LIFECYCLE-T01.** Race submission, repeated shutdown and startup of a second runtime against the same installation. Check no late enqueue, one current supervisor, one shutdown operation and no terminal reopening. Use RT-LIFE-02 and RT-LIFE-03 in the [lifecycle fixtures](../../../../contracts/acceptance/runtime/lifecycle-fixtures.json) to verify a new instance fences the previous launch and never reuses it.
