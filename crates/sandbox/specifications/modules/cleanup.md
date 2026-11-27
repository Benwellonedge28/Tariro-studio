# Confirmed resource reclamation

**ZIP-SANDBOX-CLEANUP-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/cleanup.rs`

## Required implementation behavior

Stop new work, cancel under configured grace, terminate contained tree and verify descendants exited. Preserve failed evidence and release no lease until verified.

## Acceptance

**ZIP-SANDBOX-CLEANUP-T01.** Adapter refusing termination leaves resource capacity reserved.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
