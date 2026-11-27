# Bounded subproblem graph

**ZIP-REASONING-DECOMPOSITION-001 · v1.0 · Owner:** Reasoning maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/reasoning/src/decomposition.rs`

## Required implementation behavior

Split into typed subproblems with explicit assumptions, dependencies and finite budget. Reject cycles and hidden effects.

## Acceptance

**ZIP-REASONING-DECOMPOSITION-T01.** Recursive decomposition terminates on configured bound.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
