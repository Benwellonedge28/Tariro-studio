# Reasoning failure vocabulary

**ZIP-REASONING-ERROR-001 · v1.0 · Owner:** Reasoning maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/reasoning/src/error.rs`

## Required implementation behavior

Classify invalid problem, unsatisfied constraint, budget, contradictory evidence, no qualified method and unresolved conclusion.

## Acceptance

**ZIP-REASONING-ERROR-T01.** Missing evidence never becomes successful proof.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
