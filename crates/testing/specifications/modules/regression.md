# Comparable regression tests

**ZIP-TESTING-REGRESSION-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/regression.rs`

## Required implementation behavior

Pin baseline, candidate, fixture and toolchain, compare declared outcomes and preserve changes and environmental differences.

## Acceptance

**ZIP-TESTING-REGRESSION-T01.** Different toolchain without comparison policy blocks conclusion.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
