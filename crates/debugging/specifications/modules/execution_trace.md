# Ordered observed trace

**ZIP-DEBUGGING-EXECUTION-TRACE-001 · v1.0 · Owner:** Debugging maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/debugging/src/execution_trace.rs`

## Required implementation behavior

Capture sequence, scoped source/process identity and typed events. Respect resource bounds and mark truncation explicitly.

## Acceptance

**ZIP-DEBUGGING-EXECUTION-TRACE-T01.** Snapshot missing events cannot be treated as complete history.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
