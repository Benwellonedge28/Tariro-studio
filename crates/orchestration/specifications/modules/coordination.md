# Deterministic coordination round

**ZIP-ORCHESTRATION-COORDINATION-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/coordination.rs`

## Required implementation behavior

Select eligible roles and ready tasks, emit a stable ordered proposal and record assumptions/constraints. External effects require normal authorization.

## Acceptance

**ZIP-ORCHESTRATION-COORDINATION-T01.** Input permutation yields identical coordinator proposal.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
