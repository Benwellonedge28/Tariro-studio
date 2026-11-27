# DAP bridge

**ZIP-DEBUGGING-ADAPTERS-DAP-001 · v1.0 · Owner:** Debugging maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/debugging/src/adapters/dap.rs`

## Required implementation behavior

Negotiate sequence and supported capabilities, validate target/session identity and bound messages; allow only authorized commands.

## Acceptance

**ZIP-DEBUGGING-ADAPTERS-DAP-T01.** Unexpected adapter event cannot redirect session to another process.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
