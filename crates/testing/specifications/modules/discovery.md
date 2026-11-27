# Pinned case discovery

**ZIP-TESTING-DISCOVERY-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/discovery.rs`

## Required implementation behavior

Enumerate qualified test cases from exact repository snapshot and target/features, preserve unsupported and partial discovery.

## Acceptance

**ZIP-TESTING-DISCOVERY-T01.** Limited scan does not claim complete coverage.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
