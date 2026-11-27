# Bounded proposal comparison

**ZIP-ORCHESTRATION-STRATEGIES-DEBATE-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/strategies/debate.rs`

## Required implementation behavior

Solicit bounded alternatives, compare evidence and uncertainty, preserve dissent. No deadline or round exhaustion implies convergence.

## Acceptance

**ZIP-ORCHESTRATION-STRATEGIES-DEBATE-T01.** Exhausted rounds with unresolved evidence stay blocked.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
