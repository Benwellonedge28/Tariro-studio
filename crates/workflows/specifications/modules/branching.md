# Deterministic branch binding

**ZIP-WORKFLOWS-BRANCHING-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/branching.rs`

## Required implementation behavior

Evaluate named condition, record selected branch and exact input digest; replay reuses decision unless new plan approved.

## Acceptance

**ZIP-WORKFLOWS-BRANCHING-T01.** Input change invalidates previously chosen branch under old plan.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
