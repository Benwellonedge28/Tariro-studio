# Typed assertion outcomes

**ZIP-TESTING-ASSERTIONS-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/assertions.rs`

## Required implementation behavior

Compare structured observed and expected values under declared rules and tolerance, retain redacted evidence and exact failure.

## Acceptance

**ZIP-TESTING-ASSERTIONS-T01.** Out-of-tolerance output fails without permissive coercion.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
