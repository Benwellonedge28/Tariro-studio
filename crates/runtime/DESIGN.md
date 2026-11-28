# Runtime crate design

**ZIP-RT-CRATE-001 · v1.2 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the local attempt lifecycle. Master design §14.

## Responsibility and dependencies

Register the attempt before creating host state. Hold a task body behind verified containment and the one-way launch gate. Use task- or assignment-scoped pause and installation-wide shutdown. Stage bounded provisional observations before terminal publication, which requires completed cleanup and reconciliation. Recover persisted intent before allowing a scheduler successor.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md), [events](../events/DESIGN.md), [resources](../resources/DESIGN.md)

- [Runtime](../../specifications/0200-runtime/runtime.md)

## Public API and data

The following Rust-shaped pseudocode defines the public call shapes for local work. The runtime façade in `runtime.rs` owns these methods. [Task](specifications/modules/execution/task.md), [executor](specifications/modules/execution/executor.md), [task handle](specifications/modules/execution/task_handle.md), [supervisor](specifications/modules/supervisor.md) and [errors](specifications/modules/error.md) own their named types.

- `spawn(&self, spec: TaskSpec, lease: ResourceLease, cancel: Cancellation) -> Result<TaskHandle, RuntimeError>`
- `cancel(&self, task_id: Identifier) -> Result<(), RuntimeError>` accepts an authorized request for cooperative stop in the assignment scope bound by composition. Resolve the single open attempt under that assignment and task. Success confirms the accepted stop decision. The handle supplies the terminal result.
- `pub(crate) checkpoint(&self, context: &ExecutionContext, checkpoint: Checkpoint) -> Result<(), RuntimeError>` checks the attempt and owner generation from the trusted [execution context](specifications/modules/execution/execution_context.md). The [checkpoint store](specifications/modules/checkpoint/store.md) owns the data and replay.
- Startup calls crate-private recovery before enabling intake. Recovery authority and worker authority are independently resolved at composition.

`ResourceLease` comes from `resources::allocation::lease`. `Identifier` comes from `foundation::identity::identifier`. `Cancellation` denotes the read-only sticky observation handle specified by [runtime cancellation](specifications/modules/control/cancellation.md). The returned `TaskHandle` observes one attempt. Dropping it releases its observation slot while the supervisor retains ownership. An adapter observation is provisional until an authorized journal transition records it.

The [facade](specifications/modules/runtime.md) delegates installation startup to [lifecycle](specifications/modules/lifecycle.md), pause and resume to a [scoped gate](specifications/modules/control/pause.md), and shutdown to the [installation drain](specifications/modules/control/shutdown.md). `RuntimeBuilder` is the validated composition entry described in [builder](specifications/modules/builder.md). Command transport DTOs and public observation signatures require binding and compilation at the composition boundary. Internal launch and journal types remain private under the [export contract](specifications/modules/lib.md).

## Persistence and concurrency

The [numbered runtime specification](../../specifications/0200-runtime/runtime.md) owns state transitions. The supervisor writes attempt state, applicable receipt and outbox record in one storage transaction with expected revision and owner generation. Serialized durable fields are owned by the [supervisor](specifications/modules/supervisor.md). Stage immutable evidence through storage before committing a reference. Never wait for an adapter, provider, process or resource transaction while holding the runtime write transaction. Treat cross-journal operations as separately durable and inspect the owning journal after a lost response.

The [checkpoint store](specifications/modules/checkpoint/store.md) commits progress, receipt and outbox together. [Restore](specifications/modules/checkpoint/restore.md) verifies the committed contiguous prefix without creating fresh authority. The [worker pool](specifications/modules/execution/worker_pool.md) is a bounded local index. Cross-crate scheduling is composed at the application boundary. Runtime consumes the checked job claim through an injected verifier and has no direct scheduler or child-tool dependency. Resource admission and provider effect permissions remain separately enforced.

## Failure, limits and portability

Resolve `runtime.shutdown_drain_ms` for the installation and clip `runtime.stop_grace_ms` to the applicable attempt and control deadlines. Terminate the contained process tree and verify exit after the grace window. Escalate unreaped work and retain its hold. Reuse resolved storage and scheduler budgets at their owning boundaries. Capacity, retention and evidence limits come from resolved policy. Reject unsupported required containment and reliable ownership queries before accepting platform execution. The lifecycle rules are platform-neutral. A concrete adapter qualifies only after containment, query and restart tests pass on that target.

Authorization, stale epochs, deadline, ambiguity and cleanup failures follow the [typed error contract](specifications/modules/error.md). Scoped diagnostics may report a permitted attempt ID and evidence reference. [Metrics](specifications/modules/metrics.md) use fixed categories. Exclude task inputs, provider responses and private host locators from diagnostics and metrics.

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

Use the [lifecycle fixtures](../../contracts/acceptance/runtime/lifecycle-fixtures.json) and [drain policy fixtures](../../contracts/acceptance/runtime/drain-policy-fixtures.json). Crash before and after spawn, checkpoint, terminal commit and resource release. Confirm a fenced worker cannot publish and uncertain ownership retains the resource hold.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. Each linked contract carries its own maturity and review status. The [requirements map](../../contracts/requirements/modules/runtime.json) binds planned paths and acceptance identifiers. Native isolation adapters, clock integration and independent design review still require qualification.

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
