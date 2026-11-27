# Wasm component containment

**ZIP-SANDBOX-BACKENDS-WASM-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/backends/wasm.rs`

## Required implementation behavior

Verify module/interface version, bound fuel and memory and expose only approved host imports. Guest completion is not durable external effect verification.

## Acceptance

**ZIP-SANDBOX-BACKENDS-WASM-T01.** Denied import and exhausted meter produce different typed results.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
