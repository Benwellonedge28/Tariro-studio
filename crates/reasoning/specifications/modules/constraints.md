# Constraint evaluation

**ZIP-REASONING-CONSTRAINTS-001 · v1.0 · Owner:** Reasoning maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/reasoning/src/constraints.rs`

## Required implementation behavior

Apply typed hard/soft constraints, detect incompatible obligations and preserve source authority. Unknown mandatory constraint blocks conclusion.

## Acceptance

**ZIP-REASONING-CONSTRAINTS-T01.** A score cannot override a hard denied requirement.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
