# Requirement and file coverage

**ZIP-DOCUMENTATION-COVERAGE-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/coverage.rs`

## Required implementation behavior

Measure validated mappings against exact planned universe; preserve recorded gaps, excluded paths and maturity levels. Coverage count is not D5 approval.

## Acceptance

**ZIP-DOCUMENTATION-COVERAGE-T01.** Unknown declared modules and absent fixture refs remain visible in denominator.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
