# Bounded stack observations

**ZIP-DEBUGGING-STACK-TRACE-001 · v1.0 · Owner:** Debugging maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/debugging/src/stack_trace.rs`

## Required implementation behavior

Read scoped frames, resolve qualified symbols against pinned build and flag unavailable symbols. Limit frame and payload bounds.

## Acceptance

**ZIP-DEBUGGING-STACK-TRACE-T01.** Unknown frame is not attributed to a guessed source file.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
