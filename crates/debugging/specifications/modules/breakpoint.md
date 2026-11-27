# Scoped breakpoint requests

**ZIP-DEBUGGING-BREAKPOINT-001 · v1.0 · Owner:** Debugging maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/debugging/src/breakpoint.rs`

## Required implementation behavior

Map approved symbol/range to exact executable revision, validate adapter support and track actual breakpoint ID. No stale mapping on changed build.

## Acceptance

**ZIP-DEBUGGING-BREAKPOINT-T01.** Breakpoints cannot attach to an unrelated target.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
