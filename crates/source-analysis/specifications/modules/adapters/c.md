# C source adapter

**ZIP-SOURCE-ANALYSIS-ADAPTERS-C-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/adapters/c.rs`

## Required implementation behavior

Use pinned preprocessing flags and include scope; capture conditional/unknown macros without executing build script.

## Acceptance

**ZIP-SOURCE-ANALYSIS-ADAPTERS-C-T01.** Absent configuration produces partial result at conditional includes.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
