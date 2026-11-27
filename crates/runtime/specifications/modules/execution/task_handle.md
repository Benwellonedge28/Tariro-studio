# Observation-only task handle

**ZIP-RUNTIME-EXECUTION-TASK-HANDLE-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/execution/task_handle.rs`

## Required implementation behavior

Expose task/epoch ID, bounded result subscription and explicitly authorized control commands. Dropping handle closes observation only, while supervisor retains cleanup obligation.

## Acceptance

**ZIP-RUNTIME-EXECUTION-TASK-HANDLE-T01.** Dropping every observer leaves bounded supervised execution and an accessible durable receipt.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
