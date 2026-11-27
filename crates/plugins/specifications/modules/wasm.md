# Bounded Wasm adapter

**ZIP-PLUGINS-WASM-001 · v1.0 · Owner:** Plugins maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/plugins/src/wasm.rs`

## Required implementation behavior

Verify component version and imports, enforce memory and fuel, use supervised instance lifecycle and typed error mapping.

## Acceptance

**ZIP-PLUGINS-WASM-T01.** Fuel exhaustion terminates within approved runtime controls.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
