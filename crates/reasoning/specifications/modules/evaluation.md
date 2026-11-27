# Observed evidence scoring

**ZIP-REASONING-EVALUATION-001 · v1.0 · Owner:** Reasoning maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/reasoning/src/evaluation.rs`

## Required implementation behavior

Score only against explicit reviewed criteria, preserve shortcomings and distinguish observations from model inference.

## Acceptance

**ZIP-REASONING-EVALUATION-T01.** Evaluation without actual mandatory input remains blocked.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
