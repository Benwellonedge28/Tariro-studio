# Test failure vocabulary

**ZIP-TESTING-ERROR-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/error.rs`

## Required implementation behavior

Separate validation failure, runner unavailable, timeout, cancellation, rejected report, assertion failure and missing result.

## Acceptance

**ZIP-TESTING-ERROR-T01.** Missing report cannot pass under zero exit status.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
