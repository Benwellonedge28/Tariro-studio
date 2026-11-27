# Backend negotiation dispatch

**ZIP-SANDBOX-BACKENDS-MOD-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/backends/mod.rs`

## Required implementation behavior

Select approved platform adapter matching required capabilities and version. Remain unavailable if no backend qualifies.

## Acceptance

**ZIP-SANDBOX-BACKENDS-MOD-T01.** Unsupported adapter cannot fall back to native unconfined execution.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
