# Source analysis boundary

**ZIP-SOURCE-ANALYSIS-LIB-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/lib.rs`

## Required implementation behavior

Expose snapshot-scoped parser, symbol and incremental analysis ports. Linking creates no language server or repository reader.

## Acceptance

**ZIP-SOURCE-ANALYSIS-LIB-T01.** Facade fixture compiles without starting a parser process.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
