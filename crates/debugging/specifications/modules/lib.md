# Debugging service boundary

**ZIP-DEBUGGING-LIB-001 · v1.0 · Owner:** Debugging maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/debugging/src/lib.rs`

## Required implementation behavior

Expose session, observations and qualified adapter ports. Repository edits and process attachment are separately authorized.

## Acceptance

**ZIP-DEBUGGING-LIB-T01.** Read-only diagnosis can run without mutation or attach capability.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
