# Runtime crate design

**Contract version** 1.0. Master design §14. Planned implementation.

## Responsibility and dependencies

Register task before spawn. Contain child tree, supervise bounded channels, close intake on pause, publish outcome and evidence only after cleanup. Recover persisted intent before automatic retry.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md), [events](../events/DESIGN.md), [resources](../resources/DESIGN.md)

- [Runtime](../../specifications/0200-runtime/runtime.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `spawn(spec, lease)`
- `cancel(task_id)`
- `checkpoint(task_id, evidence)`
- `recover()`

Record families: TaskHandle, supervisor record, durable checkpoint, process ownership handle. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `TaskSpec { task_id, assignment_id, action, deadline, attempt_epoch }`
- `ExitOutcome { child_status, artifact_refs, cleanup_status }`
- `Checkpoint { task_id, sequence, input_digest, evidence_ref }`

- `spawn(spec: TaskSpec, lease: ResourceLease, cancel: Cancellation) -> Result<TaskHandle>`

## Failure, safety and resource limits

Use the resolved `runtime.stop_grace_ms` clipped to the applicable deadline, then terminate the contained process tree and verify exit. Escalate unreaped work and keep its lease.

- `SpawnFailed`
- `Timeout`
- `Cancelled`
- `CleanupIncomplete`
- `RecoveryRequired`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

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

Crash on both sides of spawn and checkpoint, verify no orphan and no duplicate effects.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

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
