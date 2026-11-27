# Execution and teardown failures

**ZIP-RUNTIME-ERROR-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for attempt errors.

**Planned source:** `crates/runtime/src/error.rs`

## Stable codes and outcome mapping

Represent a typed `RuntimeError` carrying a stable code, optional typed task and attempt context visible to the caller, and optional redacted evidence reference. Rust variants map to the lowercase snake-case code of the same name. Normalize storage and adapter errors at the boundary. Raw exit output, bound identifiers outside the caller's scope and credentials stay out of public errors.

| Variant | Meaning | Scheduling consequence |
| --- | --- | --- |
| Unauthorized | Caller lacks the required scope or live grant | Deny |
| InvalidSpec | Authorized request has incompatible bindings or invalid fields | Deny |
| Conflict | Authorized replay changes intent or a trusted receipt conflicts | Block until reviewed |
| LeaseLost | Current claim, owner generation or live lease fails at a worker gate | Fence and inspect outstanding obligations |
| Timeout | Effective execution deadline has elapsed | Stop and reconcile before classification |
| Cancelled | Explicit first stop abandoned uncommitted execution | Stop and reconcile, with no automatic retry |
| ContainmentUnavailable | Platform cannot establish required execution or observation guarantees | Fail closed before execution |
| SpawnFailed | Trusted adapter confirms task body never executed | Retry only if explicitly transient and scheduler policy allows |
| Interrupted | Recovery proves absence and no accepted result survives | Reevaluate only after terminal predecessor and confirmed release |
| Storage | Definite journal read or write failure | Stop privileged progression |
| OutcomeUnknown | Dispatch, transaction or resource release cannot be confirmed | Inspect its owning journal or adapter |
| CleanupIncomplete | Teardown or usage settlement remains outstanding | Retain applicable holds |
| UnknownEffect | Provider effect remains unresolved | Block successor and reconcile |
| RecoveryRequired | An outstanding attempt prevents safe execution | Block affected scope |

At request entry, resolve authorization before returning state-dependent details. Next check immutable bindings and replay identity, then current ownership and lease, then deadline and cancellation. Keep the first durably recorded stop reason. An authorized exact replay of a committed command returns its recorded result even after execution authority ends. An ambiguous write is OutcomeUnknown until verified. Preserve concurrent cleanup and effect obligations as separate fields on the attempt, so either can remain outstanding independently of the original failure. A typed error from a control call alone does not establish a terminal disposition.

## Acceptance

**ZIP-RUNTIME-ERROR-T01.** Exit with unreaped descendants keeps CleanupIncomplete and holds occupancy. Race stale result, cancellation and timeout at the worker gate and verify the ordered failure and stored first cause. An authorized replay of an already committed outcome returns the receipt with no duplicate event.
