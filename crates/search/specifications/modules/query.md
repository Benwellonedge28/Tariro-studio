# Typed bounded query

**ZIP-SEARCH-QUERY-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/query.rs`

## Required implementation behavior

Parse normalized query and scope, identify allowed filters/ranking and enforce resolved result and input budgets.

## Acceptance

**ZIP-SEARCH-QUERY-T01.** Oversized input is rejected before evaluation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
