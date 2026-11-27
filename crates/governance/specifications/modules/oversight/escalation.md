# Open decision lifecycle

**ZIP-GOVERNANCE-OVERSIGHT-ESCALATION-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/oversight/escalation.rs`

## Required implementation behavior

Persist issue, required owner role, deadline, evidence and selected policy. Pending escalation blocks dependent effect and remains visible after restart.

## Acceptance

**ZIP-GOVERNANCE-OVERSIGHT-ESCALATION-T01.** Expired unresolved escalation cannot resume task.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
