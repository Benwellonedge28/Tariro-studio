# Python source adapter

**ZIP-SOURCE-ANALYSIS-ADAPTERS-PYTHON-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/adapters/python.rs`

## Required implementation behavior

Pin grammar version and distinguish static references from dynamic imports and runtime bindings. No importing or evaluating source during analysis.

## Acceptance

**ZIP-SOURCE-ANALYSIS-ADAPTERS-PYTHON-T01.** Dynamic import remains unresolved.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
