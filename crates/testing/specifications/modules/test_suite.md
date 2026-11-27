# Immutable suite composition

**ZIP-TESTING-TEST-SUITE-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/test_suite.rs`

## Required implementation behavior

Pin selected cases, prerequisite graph and required execution profile. Reject missing dependencies and cycles.

## Acceptance

**ZIP-TESTING-TEST-SUITE-T01.** Unresolved fixture blocks suite admission.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
