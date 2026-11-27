# Worker ownership and cleanup

**ZIP-RUNTIME-SUPERVISOR-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/supervisor.rs`

## Required implementation behavior

Persist owner/attempt intent before spawn, track child tree, propagate cancel and keep lease until reconciliation or verified exit. A supervisor crash fences workers before rescheduling.

## Acceptance

**ZIP-RUNTIME-SUPERVISOR-T01.** Kill around spawn and verify no duplicate effect or stranded lease release.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
