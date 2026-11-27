# Zamani source adapter

**ZIP-SOURCE-ANALYSIS-ADAPTERS-ZAMANI-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/adapters/zamani.rs`

## Required implementation behavior

Use reviewed grammar and toolchain capability for the exact language revision. Advertise only qualified schema features.

## Acceptance

**ZIP-SOURCE-ANALYSIS-ADAPTERS-ZAMANI-T01.** Unknown grammar revision returns unsupported.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
