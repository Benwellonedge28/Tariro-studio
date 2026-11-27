# Go source adapter

**ZIP-SOURCE-ANALYSIS-ADAPTERS-GO-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/adapters/go.rs`

## Required implementation behavior

Use pinned module/build constraints to scope declarations and imports. No fetching modules without separate authority.

## Acceptance

**ZIP-SOURCE-ANALYSIS-ADAPTERS-GO-T01.** Unsupported build suffix does not enter active-platform result.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
