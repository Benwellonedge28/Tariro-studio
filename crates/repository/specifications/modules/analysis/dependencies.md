# Dependency observations

**ZIP-REPOSITORY-ANALYSIS-DEPENDENCIES-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/analysis/dependencies.rs`

## Required implementation behavior

Extract known manifest shapes with adapter and record source path/range. Flag conflicts or unresolved declarations, avoid interpreting arbitrary build logic.

## Acceptance

**ZIP-REPOSITORY-ANALYSIS-DEPENDENCIES-T01.** Unrecognized manifest yields partial observation, no fabricated dependencies.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
