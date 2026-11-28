# Observation-only task handle

**ZIP-RUNTIME-EXECUTION-TASK-HANDLE-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/runtime/src/execution/task_handle.rs`

## Boundary and inputs

Return one opaque TaskHandle per admitted observation slot. Bind it to a single attempt and observer scope. Expose scoped status and wait operations backed by durable state, with terminal receipt references. A handle never follows a replacement attempt automatically. Redact diagnostics under the original scope and recheck live read authority before disclosure. The explicit Runtime control call owns cancellation.

## Behavior and failure handling

Register a bounded wait slot under the supplied observer budget. Read state and register using a revision check or equivalent lost-wakeup protection. Return already durable terminal results without waiting on event delivery. A wake only signals a reread. Dropping the handle or a pending wait removes its own local registrations and leaves supervision and admitted work active. A disconnect after terminal commit can recover the result by an authorized lookup.

## Acceptance

**ZIP-RUNTIME-EXECUTION-TASK-HANDLE-T01.** Race terminal commit with wait registration, lose the notification and recover by reread. Exhaust the admitted wait budget without creating an extra registration. Drop the handle while the task is running, then verify it still settles once under supervisor ownership.
