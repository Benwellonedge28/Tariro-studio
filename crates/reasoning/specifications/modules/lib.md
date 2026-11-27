# Reasoning service boundary

**ZIP-REASONING-LIB-001 · v1.0 · Owner:** Reasoning maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/reasoning/src/lib.rs`

## Required implementation behavior

Expose typed problem, analysis and evidence ports without authority to execute effects.

## Acceptance

**ZIP-REASONING-LIB-T01.** Loading reasoner does not start tools or publish state.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
