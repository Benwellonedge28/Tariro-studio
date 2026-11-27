# Uncertainty and abstention

**ZIP-REASONING-UNCERTAINTY-001 · v1.0 · Owner:** Reasoning maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/reasoning/src/uncertainty.rs`

## Required implementation behavior

Record support, unknown and conflicting evidence with calibrated interpretation where available; avoid invented probabilities.

## Acceptance

**ZIP-REASONING-UNCERTAINTY-T01.** Contradiction with no resolution triggers abstention.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
