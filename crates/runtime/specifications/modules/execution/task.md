# Immutable task execution specification

**ZIP-RUNTIME-EXECUTION-TASK-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/execution/task.rs`

## Required implementation behavior

Pin task ID, assignment, plan/version, typed capability, deadlines and resource demand. Validate authorization references without resolving any credential.

## Acceptance

**ZIP-RUNTIME-EXECUTION-TASK-T01.** Task whose digest differs from reviewed plan cannot begin.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
