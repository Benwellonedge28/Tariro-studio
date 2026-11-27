# Task identity and attempts

**ZIP-ASSIGNMENTS-TASK-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/task.rs`

## Required implementation behavior

Task key includes assignment and stable plan-local ID. Persist state and epoch per attempt; output completion uses conditional update on both. Reject stale worker results.

## Acceptance

**ZIP-ASSIGNMENTS-TASK-T01.** Lease expired then reclaimed; old result cannot advance the task.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
