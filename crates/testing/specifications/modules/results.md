# Observed result model

**ZIP-TESTING-RESULTS-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/results.rs`

## Required implementation behavior

Keep Passed, Failed, TimedOut, Skipped, Blocked and Unresolved distinct with attempt/evidence IDs. Preserve every prior failure.

## Acceptance

**ZIP-TESTING-RESULTS-T01.** Later retry pass cannot erase earlier failure.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
