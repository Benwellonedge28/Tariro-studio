# Scoped graph search

**ZIP-KNOWLEDGE-QUERY-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/query.rs`

## Required implementation behavior

Authorize before matching or scoring, pin read generation and return bounded result plus cursor/partial status.

## Acceptance

**ZIP-KNOWLEDGE-QUERY-T01.** Hidden entity cannot affect visible result counts.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
