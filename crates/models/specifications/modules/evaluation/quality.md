# Observed output quality

**ZIP-MODELS-EVALUATION-QUALITY-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/evaluation/quality.rs`

## Required implementation behavior

Bind criteria and model revision to actual fixture outputs, report uncertainty and distinguish automatic from reviewed checks.

## Acceptance

**ZIP-MODELS-EVALUATION-QUALITY-T01.** Missing fixture output cannot produce passing quality score.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
