# Typed pure expression evaluation

**ZIP-REASONING-SYMBOLIC-LOGIC-001 · v1.0 · Owner:** Reasoning maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/reasoning/src/symbolic/logic.rs`

## Required implementation behavior

Evaluate approved deterministic operators under admitted bounds; distinguish true, false, unknown and invalid.

## Acceptance

**ZIP-REASONING-SYMBOLIC-LOGIC-T01.** Incomplete input does not coerce to false.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
