# Resource and spend reservation

**ZIP-INTELLIGENCE-BUDGET-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/budget.rs`

## Required implementation behavior

Reserve input/output tokens, device demand and permitted cost before dispatch. Reconcile actual charge against reserved bound and preserve unknown charge state.

## Acceptance

**ZIP-INTELLIGENCE-BUDGET-T01.** Concurrent calls cannot overcommit workspace reserve.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
