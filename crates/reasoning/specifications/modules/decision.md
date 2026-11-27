# Qualified recommendation

**ZIP-REASONING-DECISION-001 · v1.0 · Owner:** Reasoning maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/reasoning/src/decision.rs`

## Required implementation behavior

Compare alternatives and explicit criteria with provenance and uncertainty. Return abstention for unresolved mandatory evidence.

## Acceptance

**ZIP-REASONING-DECISION-T01.** Tied contradictory conclusions do not become fabricated certainty.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
