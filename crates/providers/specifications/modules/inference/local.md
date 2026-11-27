# Local inference adapter

**ZIP-PROVIDERS-INFERENCE-LOCAL-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/inference/local.rs`

## Required implementation behavior

Use qualified in-process or explicitly approved local transport, enforce verified weights, context and capacity; no internet dependence.

## Acceptance

**ZIP-PROVIDERS-INFERENCE-LOCAL-T01.** Offline run emits no network requests.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
