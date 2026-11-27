# Isolated admitted experiment

**ZIP-EVOLUTION-EXPERIMENT-001 · v1.0 · Owner:** Evolution maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/evolution/src/experiment.rs`

## Required implementation behavior

Pin qualified fixture and candidate, use finite sandbox budget, record actual outcomes and preserve unresolved effects. Private data requires consent.

## Acceptance

**ZIP-EVOLUTION-EXPERIMENT-T01.** Experiment cannot contact unapproved provider or promote its own result.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
