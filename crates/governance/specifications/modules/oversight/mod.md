# Human oversight boundary

**ZIP-GOVERNANCE-OVERSIGHT-MOD-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/oversight/mod.rs`

## Required implementation behavior

Expose escalation, intervention and stop through separately authenticated commands; machine recommendation does not create a human approval.

## Acceptance

**ZIP-GOVERNANCE-OVERSIGHT-MOD-T01.** Agent message claiming owner approval cannot bypass any governance gate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
