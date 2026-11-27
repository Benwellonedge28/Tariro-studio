# Stable case metadata

**ZIP-TESTING-TEST-CASE-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/test_case.rs`

## Required implementation behavior

Bind case ID, fixture, expected outcome, scope, budget and mandatory flag. Identity stable across ordering changes.

## Acceptance

**ZIP-TESTING-TEST-CASE-T01.** Duplicate case ID fails validation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
