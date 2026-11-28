# Execution capability wiring

**ZIP-RUNTIME-EXECUTION-MOD-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/runtime/src/execution/mod.rs`

## Boundary and inputs

Keep [executor](executor.md), [worker](worker.md), [worker registry](worker_pool.md) and [execution context](execution_context.md) in the crate-private execution tree. [TaskSpec](task.md) and [TaskHandle](task_handle.md) are visible through the public Runtime facade. Task data and handle availability confer no launch or result-writing authority. The supervisor owns trusted constructors.

## Behavior and failure handling

An accepted instance allows the supervisor to register the attempt, prepare containment and consume the launch claim before an executor can run the body. The worker then reports bounded data, while the task handle reads scoped observations. Route failed launch and unknown outcomes through supervisor recovery. The module declares interfaces only. Loading it creates no process, allocation reservation, network connection or background task.

## Acceptance

**ZIP-RUNTIME-EXECUTION-MOD-T01.** Link a synthetic executor through composition, then verify that a downstream caller can inspect the TaskHandle and cannot construct the OwnedLaunch or read the raw locator. Importing the module leaves the journal, resource ledger and executor untouched.
