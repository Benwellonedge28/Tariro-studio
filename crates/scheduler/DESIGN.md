# Scheduler crate design

**Contract version** 1.0. Master design §16. Planned implementation.

## Responsibility and dependencies

Validate DAG, derive ready set, pick by priority then fairness age then stable ID. Fence claims in a CAS transaction. Keep dependency failures blocked and retry only classified transient work.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md), [resources](../resources/DESIGN.md)

- [Runtime](../../specifications/0200-runtime/runtime.md)
- [Orchestration](../../specifications/1100-orchestration/orchestration.md)
- [Distributed](../../specifications/2700-distributed/distributed.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `enqueue(job)`
- `claim(worker)`
- `finish(lease, result)`
- `recover_expired()`

Record families: Job DAG, ReadyKey, attempt, fencing epoch and lease. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `Job { job_id, workspace_id, priority, deadline, dependencies, demand }`
- `JobClaim { job_id, worker_id, attempt, epoch, expiry }`

- `claim(worker: WorkerCaps, now: Timestamp) -> Result<Option<JobClaim>>`

## Failure, safety and resource limits

Default 256 queued jobs per workspace, 3 attempts, per-job deadline and bounded jitter. A timed-out worker cannot publish after lease loss.

- `Cycle`
- `QueueFull`
- `DeadlineExceeded`
- `LeaseLost`
- `DependencyFailed`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/scheduler/src/
├── lib.rs
├── error.rs
├── scheduler.rs
├── job.rs
├── queue.rs
├── priority.rs
├── dependency.rs
├── deadline.rs
├── fairness.rs
├── admission.rs
├── placement.rs
├── preemption.rs
├── retry.rs
├── backpressure.rs
├── policies/
│   ├── mod.rs
│   ├── sequential.rs
│   ├── parallel.rs
│   ├── priority.rs
│   ├── resource_aware.rs
│   └── distributed.rs
└── persistence.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test stable ordering, starvation resistance, stale completion rejection and restart.
