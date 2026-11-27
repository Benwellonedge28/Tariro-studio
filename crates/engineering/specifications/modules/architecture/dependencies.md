# Machine-readable graph changes

**ZIP-ENGINEERING-ARCHITECTURE-DEPENDENCIES-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/architecture/dependencies.rs`

## Required implementation behavior

Normalize permitted dependency edges and run deterministic cycle and endpoint validation, including optional/target edges. Record source revision.

## Acceptance

**ZIP-ENGINEERING-ARCHITECTURE-DEPENDENCIES-T01.** New optional edge that creates union cycle is rejected.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
