# Type provenance and confidence

**ZIP-SOURCE-ANALYSIS-TYPE-INFORMATION-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/type_information.rs`

## Required implementation behavior

Bind type observations to symbol and qualified provider, distinguishing declared, inferred, unresolved and stale results.

## Acceptance

**ZIP-SOURCE-ANALYSIS-TYPE-INFORMATION-T01.** A type from an older revision cannot apply to current source.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
