# Admitted parallel stages

**ZIP-WORKFLOWS-PARALLELISM-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/parallelism.rs`

## Required implementation behavior

Run independent scoped steps only under resource reservations and conflict checks. Serial or limited profiles constrain concurrent claims.

## Acceptance

**ZIP-WORKFLOWS-PARALLELISM-T01.** Shared write conflict serializes even if both steps are Ready.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
