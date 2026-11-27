# Bounded decision presentation

**ZIP-GOVERNANCE-OVERSIGHT-HUMAN-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/oversight/human.rs`

## Required implementation behavior

Present exact scope, diff/effect digest, expiry, expected irreversible effects and review target. Approval input carries authenticated decision and displayed digest.

## Acceptance

**ZIP-GOVERNANCE-OVERSIGHT-HUMAN-T01.** Editing any approved proposal field forces a fresh preview.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
