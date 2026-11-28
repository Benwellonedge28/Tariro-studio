# Capability-scoped execution context

**ZIP-RUNTIME-EXECUTION-EXECUTION-CONTEXT-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/runtime/src/execution/execution_context.rs`

## Boundary and inputs

ExecutionContext is an opaque crate-private worker handle constructed by the supervisor after matching the task and validated launch binding. Hold the exact attempt identity, worker owner generation, action binding, admitted permit observation, live deadline and read-only cancellation. Carry only bounded operation interfaces required by that action. No credential bytes, activation proof, cleanup authority or reusable launch permission cross this boundary.

## Behavior and failure handling

Check current ownership and admitted scope at each checkpoint or result publication. Compare durable attempt revision and generation atomically at commit or reject stale reports. Long worker steps observe cancellation between bounded units. Context construction cannot authorize an effect. Routes with an external effect require their separately checked durable intent. Context has no serialization. Recovery constructs a new context only for newly authorized execution.

## Acceptance

**ZIP-RUNTIME-EXECUTION-EXECUTION-CONTEXT-T01.** After replacing an owner, use the old context to submit checked progress and completion. Both fail with LeaseLost and no cursor or terminal event changes. After reconciling the old attempt, verify a separately authorized successor can publish under its own attempt.
