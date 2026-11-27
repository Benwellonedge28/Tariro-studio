# Candidate integration workflow

**ZIP-ENGINEERING-IMPLEMENTATION-INTEGRATION-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/implementation/integration.rs`

## Required implementation behavior

Build/verify on pinned staged candidate with scoped tests; preserve actual result and effect receipts. Publication is independently granted.

## Acceptance

**ZIP-ENGINEERING-IMPLEMENTATION-INTEGRATION-T01.** Passing compile is not sufficient to deploy or merge.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
