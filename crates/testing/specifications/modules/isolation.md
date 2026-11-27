# Qualified test sandbox

**ZIP-TESTING-ISOLATION-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/isolation.rs`

## Required implementation behavior

Apply profile scope, environment and finite budgets before spawn. Tests may not access host or unrelated repositories implicitly.

## Acceptance

**ZIP-TESTING-ISOLATION-T01.** Missing required containment yields blocked test.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
