# Delegated task hierarchy

**ZIP-ORCHESTRATION-STRATEGIES-HIERARCHICAL-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/strategies/hierarchical.rs`

## Required implementation behavior

Assign bounded child groups with explicit reporting and attenuated authority. Check depth and parent budget before expansion.

## Acceptance

**ZIP-ORCHESTRATION-STRATEGIES-HIERARCHICAL-T01.** A subtree cannot broaden parent scope or continue after revoke.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
