# PR effect boundary

**ZIP-REPOSITORY-PULL-REQUESTS-MOD-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/pull_requests/mod.rs`

## Required implementation behavior

Expose creation, review, checks, status and reconciliation separately. Scope restrictions and publication approval are prerequisites, not defaults.

## Acceptance

**ZIP-REPOSITORY-PULL-REQUESTS-MOD-T01.** Inspection does not produce write side effects.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
