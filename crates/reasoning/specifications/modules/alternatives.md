# Bounded alternative candidates

**ZIP-REASONING-ALTERNATIVES-001 · v1.0 · Owner:** Reasoning maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/reasoning/src/alternatives.rs`

## Required implementation behavior

Generate or accept scoped options, normalize identity and deduplicate with retained source. Preserve meaningful conflicts.

## Acceptance

**ZIP-REASONING-ALTERNATIVES-T01.** Repeating same option does not skew ranking.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
