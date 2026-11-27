# Cost option evaluation

**ZIP-ECONOMICS-OPTIMIZATION-001 · v1.0 · Owner:** Economics maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/economics/src/optimization.rs`

## Required implementation behavior

Rank only approved compatible options with known budgets and quality criteria. Suggest alternatives without calling provider.

## Acceptance

**ZIP-ECONOMICS-OPTIMIZATION-T01.** Cheap but disallowed remote option cannot be selected.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
