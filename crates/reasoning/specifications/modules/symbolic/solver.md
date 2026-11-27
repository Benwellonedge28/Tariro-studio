# Bounded solver qualification

**ZIP-REASONING-SYMBOLIC-SOLVER-001 · v1.0 · Owner:** Reasoning maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/reasoning/src/symbolic/solver.rs`

## Required implementation behavior

Return proved, counterexample, unknown or exhausted tied to exact model and solver/version. Limit search under lease.

## Acceptance

**ZIP-REASONING-SYMBOLIC-SOLVER-T01.** Timeout never yields proof even with partial candidate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
