# Distributed crate design

**Contract version** 1.0. Master design §48. Planned implementation.

## Responsibility and dependencies

Authenticate node, filter by policy and locality, reserve capacity, issue short lease with fencing token, recheck result and artifact digests at coordinator.

First-party dependencies: [foundation](../foundation/DESIGN.md), [networking](../networking/DESIGN.md), [resources](../resources/DESIGN.md), [scheduler](../scheduler/DESIGN.md), [synchronization](../synchronization/DESIGN.md)

- [Distributed](../../specifications/2700-distributed/distributed.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `register_node(identity)`
- `advertise(capacity)`
- `lease(task)`
- `accept_result(worker_epoch)`

Record families: NodeAdvertisement, task lease, epoch, artifact and evidence manifest. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `WorkerLease { node_id, task_id, epoch, issued_at, expires_at, input_manifest }`
- `WorkerResult { lease_id, task_id, epoch, artifacts, evidence }`

- `accept_result(result: WorkerResult, principal: NodePrincipal) -> Result<CoordinatorReceipt>`

## Failure, safety and resource limits

Remote execution opt-in. Expired or fenced workers cannot promote results. Keep state at owner node and bound retries per task.

- `NoEligibleNode`
- `LeaseLost`
- `RemoteResultInvalid`
- `Partitioned`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/distributed/src/
├── lib.rs
├── error.rs
├── node.rs
├── identity.rs
├── membership.rs
├── discovery.rs
├── registry.rs
├── heartbeat.rs
├── capabilities.rs
├── resources.rs
├── placement.rs
├── scheduler.rs
├── worker.rs
├── coordinator.rs
├── execution.rs
├── task_lease.rs
├── artifact_transfer.rs
├── checkpoint.rs
├── recovery.rs
├── partition.rs
├── reconciliation.rs
├── security.rs
└── metrics.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test stale worker receipt, unexpected node capability and network partitions.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`node.rs`](specifications/modules/node.md)
- [`identity.rs`](specifications/modules/identity.md)
- [`membership.rs`](specifications/modules/membership.md)
- [`discovery.rs`](specifications/modules/discovery.md)
- [`registry.rs`](specifications/modules/registry.md)
- [`heartbeat.rs`](specifications/modules/heartbeat.md)
- [`capabilities.rs`](specifications/modules/capabilities.md)
- [`resources.rs`](specifications/modules/resources.md)
- [`placement.rs`](specifications/modules/placement.md)
- [`scheduler.rs`](specifications/modules/scheduler.md)
- [`worker.rs`](specifications/modules/worker.md)
- [`coordinator.rs`](specifications/modules/coordinator.md)
- [`execution.rs`](specifications/modules/execution.md)
- [`task_lease.rs`](specifications/modules/task_lease.md)
- [`artifact_transfer.rs`](specifications/modules/artifact_transfer.md)
- [`checkpoint.rs`](specifications/modules/checkpoint.md)
- [`recovery.rs`](specifications/modules/recovery.md)
- [`partition.rs`](specifications/modules/partition.md)
- [`reconciliation.rs`](specifications/modules/reconciliation.md)
- [`security.rs`](specifications/modules/security.md)
- [`metrics.rs`](specifications/modules/metrics.md)
