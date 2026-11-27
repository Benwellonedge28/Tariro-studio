# Advisory plan proposal

**ZIP-REASONING-PLANNING-001 · v1.0 · Owner:** Reasoning maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/reasoning/src/planning.rs`

## Required implementation behavior

Order candidate steps and expected evidence under constraints; mark unknown steps and required approvals. Plan cannot dispatch itself.

## Acceptance

**ZIP-REASONING-PLANNING-T01.** Unverified action requires separate gate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
