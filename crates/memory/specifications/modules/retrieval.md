# Authorized ranked retrieval

**ZIP-MEMORY-RETRIEVAL-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/retrieval.rs`

## Required implementation behavior

Filter scope and expiry before scoring, bound results and expose generation cursor. Do not use hidden results to adjust visible scoring.

## Acceptance

**ZIP-MEMORY-RETRIEVAL-T01.** Expired or cross-tenant record does not alter visible ranking.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
