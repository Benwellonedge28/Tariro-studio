# Isolated mutation testing

**ZIP-TESTING-MUTATION-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/mutation.rs`

## Required implementation behavior

Apply approved synthetic mutations in disposable candidate, record killed/survived/invalid verdict and clean up; do not edit reviewed branch.

## Acceptance

**ZIP-TESTING-MUTATION-T01.** Failed or invalid mutant is not counted as killed without valid fixture result.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
