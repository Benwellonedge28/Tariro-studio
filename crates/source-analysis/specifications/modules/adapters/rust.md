# Rust source adapter

**ZIP-SOURCE-ANALYSIS-ADAPTERS-RUST-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/adapters/rust.rs`

## Required implementation behavior

Qualify Rust edition/grammar and record macros, cfg and generated sources as conditional or unresolved unless actually analyzed.

## Acceptance

**ZIP-SOURCE-ANALYSIS-ADAPTERS-RUST-T01.** Unexpanded macro output is not indexed as known declaration.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
