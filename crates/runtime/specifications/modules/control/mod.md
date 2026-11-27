# Control hierarchy

**ZIP-RUNTIME-CONTROL-MOD-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/control/mod.rs`

## Required implementation behavior

Expose cancel, timeout, pause and shutdown commands without direct task mutations. Supervisor is authority for terminal transition and cleanup.

## Acceptance

**ZIP-RUNTIME-CONTROL-MOD-T01.** Application cancel path routes through supervisor, never kills by untrusted process ID.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
