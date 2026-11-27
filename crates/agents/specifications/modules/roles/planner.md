# Planner role

**ZIP-AGENTS-ROLES-PLANNER-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/roles/planner.rs`

## Required implementation behavior

Produce immutable task DAG with inputs, conflicts, budgets and checks. Scope widening must be surfaced for approval.

## Acceptance

**ZIP-AGENTS-ROLES-PLANNER-T01.** A plan with missing prerequisite is rejected.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
