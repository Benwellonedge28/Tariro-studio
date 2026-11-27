# Coverage measurement boundary

**ZIP-TESTING-COVERAGE-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/coverage.rs`

## Required implementation behavior

Record qualified instrumenter, tested snapshot, covered and total units with omissions. Coverage is separate from correctness.

## Acceptance

**ZIP-TESTING-COVERAGE-T01.** Partial run never reports complete observed coverage.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
