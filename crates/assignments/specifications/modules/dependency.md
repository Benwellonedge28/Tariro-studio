# Task graph prerequisites

**ZIP-ASSIGNMENTS-DEPENDENCY-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/dependency.rs`

## Required implementation behavior

Validate referenced node IDs and acyclicity. Stable topological order yields ready tasks only when every required predecessor has verified success. Failed or blocked predecessors keep dependents blocked.

## Acceptance

**ZIP-ASSIGNMENTS-DEPENDENCY-T01.** Cycle, missing node and predecessor failure each reject or block correctly.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
