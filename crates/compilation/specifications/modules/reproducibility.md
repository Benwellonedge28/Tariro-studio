# Rebuild qualification

**ZIP-COMPILATION-REPRODUCIBILITY-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/reproducibility.rs`

## Required implementation behavior

Pin toolchain, source, environment, target and dependency digest, then compare declared reproducible output IDs and tolerances.

## Acceptance

**ZIP-COMPILATION-REPRODUCIBILITY-T01.** Different SDK or target yields different qualification scope.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
