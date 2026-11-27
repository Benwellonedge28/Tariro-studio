# Deterministic ranked result fusion

**ZIP-SEARCH-HYBRID-FUSION-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/hybrid/fusion.rs`

## Required implementation behavior

Apply reviewed fusion algorithm/version to admitted channels, dedupe by scoped identity and retain rationale. Use stable ranking ties.

## Acceptance

**ZIP-SEARCH-HYBRID-FUSION-T01.** Source return order does not alter tied final ranking.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
