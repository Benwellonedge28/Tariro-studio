# Generated test candidates

**ZIP-TESTING-GENERATION-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/generation.rs`

## Required implementation behavior

Produce bounded reviewed fixtures from requirements, mark synthesized assumptions and require validation before activation.

## Acceptance

**ZIP-TESTING-GENERATION-T01.** Generated expectation cannot certify its own correctness.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
