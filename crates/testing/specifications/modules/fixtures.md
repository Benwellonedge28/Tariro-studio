# Immutable scoped fixture materialization

**ZIP-TESTING-FIXTURES-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/fixtures.rs`

## Required implementation behavior

Verify fixture digest and expected schema before staging within isolated root. Bind cleanup to owner lease.

## Acceptance

**ZIP-TESTING-FIXTURES-T01.** Unexpected path and altered digest both fail before run.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
