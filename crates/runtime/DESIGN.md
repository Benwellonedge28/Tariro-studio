# Runtime crate design

**ZIP-RT-CRATE-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the local attempt lifecycle. Master design §14.

## Responsibility and dependencies

Register task before spawn. Contain child tree, supervise bounded channels, close intake on pause, publish outcome and evidence only after cleanup. Recover persisted intent before automatic retry.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md), [events](../events/DESIGN.md), [resources](../resources/DESIGN.md)

- [Runtime](../../specifications/0200-runtime/runtime.md)

## Public API and data

The following Rust-shaped pseudocode defines the public call shapes for local work. The runtime façade in `runtime.rs` owns these methods. [Task](specifications/modules/execution/task.md), [executor](specifications/modules/execution/executor.md), [task handle](specifications/modules/execution/task_handle.md), [supervisor](specifications/modules/supervisor.md) and [errors](specifications/modules/error.md) own their named types.

- `spawn(&self, spec: TaskSpec, lease: ResourceLease, cancel: Cancellation) -> Result<TaskHandle, RuntimeError>`
- `cancel(&self, task_id: Identifier) -> Result<(), RuntimeError>` accepts an authorized request for cooperative stop. Success confirms recording the request, with terminal disposition read from the handle.
- `pub(crate) checkpoint(&self, context: &ExecutionContext, checkpoint: Checkpoint) -> Result<(), RuntimeError>` checks the attempt and owner generation from the trusted [execution context](specifications/modules/execution/execution_context.md). The [checkpoint store](specifications/modules/checkpoint/store.md) owns the data and replay.
- Startup calls crate-private recovery before enabling intake. Recovery authority and worker authority are independently resolved at composition.

`ResourceLease` comes from `resources::allocation::lease`. `Identifier` comes from `foundation::identity::identifier`. `Cancellation` denotes the read-only sticky observation handle specified by [runtime cancellation](specifications/modules/control/cancellation.md). The returned `TaskHandle` observes one attempt. Dropping it releases its observation slot while the supervisor retains ownership. An adapter observation is provisional until an authorized journal transition records it.

## Persistence and concurrency

The [numbered runtime specification](../../specifications/0200-runtime/runtime.md) owns state transitions. The supervisor writes attempt state, applicable receipt and outbox record in one storage transaction with expected revision and owner generation. Serialized durable fields are owned by the [supervisor](specifications/modules/supervisor.md). Stage immutable evidence through storage before committing a reference. Never wait for an adapter, provider, process or resource transaction while holding the runtime write transaction. Treat cross-journal operations as separately durable and inspect the owning journal after a lost response.

Cross-crate scheduling is composed at the application boundary. Runtime consumes the checked job claim through an injected verifier and has no direct scheduler or child-tool dependency. Resource admission and provider effect permissions remain separately enforced.

## Failure, limits and portability

Use the resolved `runtime.stop_grace_ms` clipped to the applicable deadline, then terminate the contained process tree and verify exit. Escalate unreaped work and retain its hold. Reuse resolved storage and scheduler budgets at their owning boundaries. Capacity, retention and evidence limits come from resolved policy. Reject unsupported required containment and reliable ownership queries before accepting platform execution. The lifecycle rules are platform-neutral. A concrete adapter qualifies only after containment, query and restart tests pass on that target.

Authorization, stale epochs, deadline, ambiguity and cleanup failures follow the [typed error contract](specifications/modules/error.md). Observability reports bounded state, error code, attempt ID and evidence reference. Avoid task inputs, provider responses and private host locator contents in logs or metric labels.

## Versioning and implementation order

There is no prior runtime implementation or deployed runtime state claimed by this design. Define task/attempt types and versioned journal first, qualify trusted storage and resource proof ports next, then add a deterministic executor, fault reconstruction and native adapter verification. Unknown record major versions block intake and preserve the store for a qualified migration. Independent review and actual adapter evidence are required before promoting this scope to D5. Platform performance stays subject to the [system requirements](../../REQUIREMENTS.md) and measured release evidence.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/runtime/src/
├── lib.rs
├── error.rs
├── runtime.rs
├── builder.rs
├── lifecycle.rs
├── supervisor.rs
├── execution/
│   ├── mod.rs
│   ├── executor.rs
│   ├── worker.rs
│   ├── worker_pool.rs
│   ├── task.rs
│   ├── task_handle.rs
│   └── execution_context.rs
├── control/
│   ├── mod.rs
│   ├── cancellation.rs
│   ├── timeout.rs
│   ├── pause.rs
│   └── shutdown.rs
├── checkpoint/
│   ├── mod.rs
│   ├── checkpoint.rs
│   ├── store.rs
│   └── restore.rs
├── recovery/
│   ├── mod.rs
│   ├── retry.rs
│   ├── crash_recovery.rs
│   └── reconciliation.rs
├── isolation.rs
├── health.rs
└── metrics.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Use the [acceptance fixtures](../../contracts/acceptance/runtime/lifecycle-fixtures.json). Crash before and after spawn, checkpoint, terminal commit and resource release. Confirm a fenced worker cannot publish and uncertain ownership retains the resource hold.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. Each linked contract carries its own maturity and review status.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`runtime.rs`](specifications/modules/runtime.md)
- [`builder.rs`](specifications/modules/builder.md)
- [`lifecycle.rs`](specifications/modules/lifecycle.md)
- [`supervisor.rs`](specifications/modules/supervisor.md)
- [`execution/mod.rs`](specifications/modules/execution/mod.md)
- [`execution/executor.rs`](specifications/modules/execution/executor.md)
- [`execution/worker.rs`](specifications/modules/execution/worker.md)
- [`execution/worker_pool.rs`](specifications/modules/execution/worker_pool.md)
- [`execution/task.rs`](specifications/modules/execution/task.md)
- [`execution/task_handle.rs`](specifications/modules/execution/task_handle.md)
- [`execution/execution_context.rs`](specifications/modules/execution/execution_context.md)
- [`control/mod.rs`](specifications/modules/control/mod.md)
- [`control/cancellation.rs`](specifications/modules/control/cancellation.md)
- [`control/timeout.rs`](specifications/modules/control/timeout.md)
- [`control/pause.rs`](specifications/modules/control/pause.md)
- [`control/shutdown.rs`](specifications/modules/control/shutdown.md)
- [`checkpoint/mod.rs`](specifications/modules/checkpoint/mod.md)
- [`checkpoint/checkpoint.rs`](specifications/modules/checkpoint/checkpoint.md)
- [`checkpoint/store.rs`](specifications/modules/checkpoint/store.md)
- [`checkpoint/restore.rs`](specifications/modules/checkpoint/restore.md)
- [`recovery/mod.rs`](specifications/modules/recovery/mod.md)
- [`recovery/retry.rs`](specifications/modules/recovery/retry.md)
- [`recovery/crash_recovery.rs`](specifications/modules/recovery/crash_recovery.md)
- [`recovery/reconciliation.rs`](specifications/modules/recovery/reconciliation.md)
- [`isolation.rs`](specifications/modules/isolation.md)
- [`health.rs`](specifications/modules/health.md)
- [`metrics.rs`](specifications/modules/metrics.md)
