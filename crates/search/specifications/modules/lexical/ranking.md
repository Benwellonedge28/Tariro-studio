# Qualified lexical ranking

**ZIP-SEARCH-LEXICAL-RANKING-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/lexical/ranking.rs`

## Required implementation behavior

Compute reviewed formula over authorized corpus only, enforce configured limit and resolve ties by stable source ID.

## Acceptance

**ZIP-SEARCH-LEXICAL-RANKING-T01.** Private corpus terms cannot change visible rankings.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
