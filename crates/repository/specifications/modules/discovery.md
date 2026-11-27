# Scoped repository discovery

**ZIP-REPOSITORY-DISCOVERY-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/discovery.rs`

## Required implementation behavior

Enumerate only owner-approved roots/providers using bounded traversal. Normalize verified Git metadata without following unsafe links or selecting inferred permissions.

## Acceptance

**ZIP-REPOSITORY-DISCOVERY-T01.** Untrusted folder cannot cause traversal outside approved root.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
