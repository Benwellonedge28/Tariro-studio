# JavaScript source adapter

**ZIP-SOURCE-ANALYSIS-ADAPTERS-JAVASCRIPT-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/adapters/javascript.rs`

## Required implementation behavior

Qualify syntax/module mode; classify dynamic import, property dispatch and generated output separately.

## Acceptance

**ZIP-SOURCE-ANALYSIS-ADAPTERS-JAVASCRIPT-T01.** Dynamic expressions do not become confirmed module links.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
