# Object-safe execution port

**ZIP-RUNTIME-EXECUTION-EXECUTOR-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/execution/executor.rs`

## Required implementation behavior

Use a boxed Send future tied to executor borrow, typed request, lease and cancellation token. Treat output as provisional until verified against actual task and epoch; cancellation after commit preserves receipt.

## Acceptance

**ZIP-RUNTIME-EXECUTION-EXECUTOR-T01.** Exercise cancelled before spawn, unknown effects and two interchangeable executor adapters.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
