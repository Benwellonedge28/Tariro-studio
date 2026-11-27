# Strategy selection boundary

**ZIP-ORCHESTRATION-STRATEGIES-MOD-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/strategies/mod.rs`

## Required implementation behavior

Use versioned config to select pure planning strategy. Scheduler and governance enforce all proposals independently.

## Acceptance

**ZIP-ORCHESTRATION-STRATEGIES-MOD-T01.** Unknown strategy cannot choose permissive default.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
