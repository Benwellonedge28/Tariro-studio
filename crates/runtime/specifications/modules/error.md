# Execution and teardown failures

**ZIP-RUNTIME-ERROR-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/error.rs`

## Required implementation behavior

Represent SpawnFailed, Timeout, Cancelled, LeaseLost, Storage, CleanupIncomplete and UnknownEffect. Preserve bounded correlation context and distinguish terminal outcome from cleanup status.

## Acceptance

**ZIP-RUNTIME-ERROR-T01.** Process exit with unreaped descendants cannot be reported as complete teardown.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
