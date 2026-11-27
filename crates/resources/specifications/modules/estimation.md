# Conservative demand calculation

**ZIP-RESOURCES-ESTIMATION-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/estimation.rs`

## Required implementation behavior

Compute typed upper bound with measured baseline, input size, model/adapter shape and policy allowance. Return Unsupported for unmeasurable mandatory metric. Store assumptions for evidence.

## Acceptance

**ZIP-RESOURCES-ESTIMATION-T01.** Underestimated fixture is recorded as pressure and triggers bounded handling, never unlimited slack.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
