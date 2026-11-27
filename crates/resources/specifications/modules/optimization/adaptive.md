# Deterministic degradation selection

**ZIP-RESOURCES-OPTIMIZATION-ADAPTIVE-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/optimization/adaptive.rs`

## Required implementation behavior

Evaluate allowed alternatives by stated quality floor, demand and stable rank. Recalculate remaining budget before re-admission. Report proposed and admitted parameters.

## Acceptance

**ZIP-RESOURCES-OPTIMIZATION-ADAPTIVE-T01.** If no alternative meets floor, typed capacity error is returned.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
