# Scheduler crate design

**Contract version** 1.1 candidate. Master design §16. Planned implementation.

## Responsibility and dependencies

Validate DAG, derive ready set, pick by priority then fairness age then stable ID. Fence claims in a CAS transaction. Keep dependency failures blocked and retry only classified transient work.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md), [resources](../resources/DESIGN.md)

- [Runtime](../../specifications/0200-runtime/runtime.md)
- [Orchestration](../../specifications/1100-orchestration/orchestration.md)
- [Distributed](../../specifications/2700-distributed/distributed.md)

## API and data

[Scheduler](specifications/modules/scheduler.md) owns eligibility, queue revisions, claim epochs and retry decisions. [Job](specifications/modules/job.md) defines immutable demand and attempt bindings. [Persistence](specifications/modules/persistence.md) owns durable queues, receipts and restart reconciliation. Storage, Resources and Foundation remain the only first-party dependencies.

A claim commits its attempt intent before reserving capacity. Dispatch transfers the opaque lease to the runtime only after the scheduler compare-and-swap succeeds. The runtime owns its one-way launch gate and terminal observation. The scheduler consumes a trusted receipt bound to the exact attempt. A lost response leaves an unresolved intent. Recovery reconciles the original resource and runtime obligations before another attempt. Composition supplies trusted authorization, handoff and receipt verification through injected ports.

## Failure, safety and resource limits

Resolve `scheduler.max_workspace_queue_items`, `scheduler.max_attempts`, `scheduler.job_deadline_ms` and `scheduler.retry_jitter_ms` within assignment policy. Check live authority and timeout at the irreversible boundary. Fence stale work. Preserve committed effects and unsettled capacity across cancellation, restart and recovery. Read [error decisions](specifications/modules/error.md) for terminal, deferred and ambiguous outcomes.

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

Exercise the [dispatch fixtures](../../contracts/acceptance/scheduler/dispatch-fixtures.json) for stable ordering, starvation resistance within a priority class, stale completion and restart. Rust compilation and real journal/adapter qualification are independent acceptance gates.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. The dispatch and recovery slice is a candidate for independent review. Other modules retain their recorded maturity.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`scheduler.rs`](specifications/modules/scheduler.md)
- [`job.rs`](specifications/modules/job.md)
- [`queue.rs`](specifications/modules/queue.md)
- [`priority.rs`](specifications/modules/priority.md)
- [`dependency.rs`](specifications/modules/dependency.md)
- [`deadline.rs`](specifications/modules/deadline.md)
- [`fairness.rs`](specifications/modules/fairness.md)
- [`admission.rs`](specifications/modules/admission.md)
- [`placement.rs`](specifications/modules/placement.md)
- [`preemption.rs`](specifications/modules/preemption.md)
- [`retry.rs`](specifications/modules/retry.md)
- [`backpressure.rs`](specifications/modules/backpressure.md)
- [`policies/mod.rs`](specifications/modules/policies/mod.md)
- [`policies/sequential.rs`](specifications/modules/policies/sequential.md)
- [`policies/parallel.rs`](specifications/modules/policies/parallel.md)
- [`policies/priority.rs`](specifications/modules/policies/priority.md)
- [`policies/resource_aware.rs`](specifications/modules/policies/resource_aware.md)
- [`policies/distributed.rs`](specifications/modules/policies/distributed.md)
- [`persistence.rs`](specifications/modules/persistence.md)
