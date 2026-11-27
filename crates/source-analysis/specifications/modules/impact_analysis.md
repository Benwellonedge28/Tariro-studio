# Evidence-bound change impact

**ZIP-SOURCE-ANALYSIS-IMPACT-ANALYSIS-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/impact_analysis.rs`

## Required implementation behavior

Compare old/new pinned revisions and traverse qualified references under finite bounds. Report observed, inferred and unknown impacts separately.

## Acceptance

**ZIP-SOURCE-ANALYSIS-IMPACT-ANALYSIS-T01.** Unresolved edge does not imply proof of no impact.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
