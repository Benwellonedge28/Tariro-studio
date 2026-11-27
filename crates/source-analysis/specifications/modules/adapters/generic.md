# Text-only source adapter

**ZIP-SOURCE-ANALYSIS-ADAPTERS-GENERIC-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/adapters/generic.rs`

## Required implementation behavior

Provide bounded spans, lexical search and explicit absence of semantic analysis. Do not infer declarations or types.

## Acceptance

**ZIP-SOURCE-ANALYSIS-ADAPTERS-GENERIC-T01.** Text result cannot satisfy a required symbol/type check.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
