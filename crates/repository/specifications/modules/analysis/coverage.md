# Analyzed-scope quality report

**ZIP-REPOSITORY-ANALYSIS-COVERAGE-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/analysis/coverage.rs`

## Required implementation behavior

Count observed paths versus eligible scope and explicitly exclude binary, missing or inaccessible entries. Report numerator, denominator and source revision.

## Acceptance

**ZIP-REPOSITORY-ANALYSIS-COVERAGE-T01.** Partial scan never reports complete coverage.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
