# Cooperative generation loop

**ZIP-INFERENCE-GENERATION-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/generation.rs`

## Required implementation behavior

Validate input encoding, start under lease, emit bounded sequence and stop on configured output ceiling, cancellation or backend end. Retain real stop reason.

## Acceptance

**ZIP-INFERENCE-GENERATION-T01.** Tokens generated at output limit do not trigger unbounded continuation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
