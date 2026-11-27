# Independent candidate evaluation

**ZIP-EVOLUTION-EVALUATION-001 · v1.0 · Owner:** Evolution maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/evolution/src/evaluation.rs`

## Required implementation behavior

Compare exact baseline/candidate against mandatory quality and safety gates. Preserve skipped, inconclusive and failed states.

## Acceptance

**ZIP-EVOLUTION-EVALUATION-T01.** Positive performance result cannot override failed compliance gate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
