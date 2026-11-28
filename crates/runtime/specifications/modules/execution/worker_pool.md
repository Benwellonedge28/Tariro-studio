# Bounded active-worker registry

**ZIP-RUNTIME-EXECUTION-WORKER-POOL-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/runtime/src/execution/worker_pool.rs`

## Boundary and inputs

The pool is a process-local bounded index of active attempt identities and pending local registration waiters. Scheduler owns the durable job queue. Composition supplies finite local slot and waiter capacities charged to the admitted installation envelope. Require capacity before any registration growth and check active binding uniqueness. Slots remain associated with uncertain attempts until supervision transfers or resolves them.

## Behavior and failure handling

Serialize registration with close, check Failed or Draining intake before allocating, and support nonblocking denial on pressure. Registration is all-or-nothing. If the local slot is unavailable before an attempt journal registration, leave the caller's reservation ownership unchanged. Wake after releasing locks. Shutdown detaches and wakes bounded waiters. A volatile entry disappearing provides no evidence that a body stopped or that its resource hold may be released. Startup rebuilds tracking from durable open records under recovery ownership.

## Acceptance

**ZIP-RUNTIME-EXECUTION-WORKER-POOL-T01.** Race two registrations for the last slot and then close intake while a waiter is pending. Verify one slot is admitted, no duplicate active entry, no late launch and a wake with closed intake. Simulate pool loss and verify the durable hold survives until teardown is proven.
