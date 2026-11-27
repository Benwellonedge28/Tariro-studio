# C++ source adapter

**ZIP-SOURCE-ANALYSIS-ADAPTERS-CPP-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/adapters/cpp.rs`

## Required implementation behavior

Qualify dialect, compile database and template/type-resolution capability. Preserve uncertain instantiations separately.

## Acceptance

**ZIP-SOURCE-ANALYSIS-ADAPTERS-CPP-T01.** Unsupported language mode returns partial analysis.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
