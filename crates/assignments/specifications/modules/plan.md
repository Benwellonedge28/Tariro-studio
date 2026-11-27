# Immutable execution plan

**ZIP-ASSIGNMENTS-PLAN-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/plan.rs`

## Required implementation behavior

Compile validated spec to task graph, requirements, budgets and evidence gates. Normalize ordering and hash exact revision and inputs. Scope changes invalidate prior positive authority where required.

## Acceptance

**ZIP-ASSIGNMENTS-PLAN-T01.** Equivalent reordered inputs produce one digest; changed dependency invalidates it.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
