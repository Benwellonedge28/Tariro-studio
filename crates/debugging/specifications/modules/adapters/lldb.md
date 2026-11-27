# Qualified LLDB adapter

**ZIP-DEBUGGING-ADAPTERS-LLDB-001 · v1.0 · Owner:** Debugging maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/debugging/src/adapters/lldb.rs`

## Required implementation behavior

Confirm approved executable/target ABI, negotiate supported data and cancellation. Reject unsupported or unscoped sessions.

## Acceptance

**ZIP-DEBUGGING-ADAPTERS-LLDB-T01.** Wrong target profile cannot use stale symbol/evaluation capability.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
