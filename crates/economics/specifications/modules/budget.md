# Atomic budget reservation

**ZIP-ECONOMICS-BUDGET-001 · v1.0 · Owner:** Economics maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/economics/src/budget.rs`

## Required implementation behavior

Reserve finite approved amount in exact workspace/period/unit before dispatch and atomically prevent overspend. Zero amount disables paid actions.

## Acceptance

**ZIP-ECONOMICS-BUDGET-T01.** Concurrent calls cannot reserve same remaining funds.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
