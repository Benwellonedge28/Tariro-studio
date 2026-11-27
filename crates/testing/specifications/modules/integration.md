# Qualified component integration tests

**ZIP-TESTING-INTEGRATION-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/integration.rs`

## Required implementation behavior

Exercise exact component versions and simulated dependencies under scope; validate boundary requests and expected partial failures.

## Acceptance

**ZIP-TESTING-INTEGRATION-T01.** Passing mocked dependency does not certify live integration.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
