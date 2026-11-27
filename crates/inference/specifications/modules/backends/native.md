# First-party native adapter boundary

**ZIP-INFERENCE-BACKENDS-NATIVE-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/backends/native.rs`

## Required implementation behavior

Declare implemented format and sampling features with safe Rust stages and actual observations. Unimplemented behavior stays unavailable.

## Acceptance

**ZIP-INFERENCE-BACKENDS-NATIVE-T01.** A simulated success or stub cannot qualify a feature.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
