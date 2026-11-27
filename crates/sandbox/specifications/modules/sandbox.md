# Sandbox launch service

**ZIP-SANDBOX-SANDBOX-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/sandbox.rs`

## Required implementation behavior

Validate profile and lease; probe selected adapter, install mandatory controls, then spawn restricted child. A failed setup leaves no running process.

## Acceptance

**ZIP-SANDBOX-SANDBOX-T01.** Failure installing required filesystem policy prevents spawn.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
