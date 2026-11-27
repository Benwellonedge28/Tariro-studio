# Authorized manual control

**ZIP-GOVERNANCE-OVERSIGHT-INTERVENTION-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/oversight/intervention.rs`

## Required implementation behavior

Pause, reject, resume or narrow a pending assignment only under exact authenticated authority. Preserve prior decisions and validate revision before mutation.

## Acceptance

**ZIP-GOVERNANCE-OVERSIGHT-INTERVENTION-T01.** Concurrent manual changes on one revision yield one winner.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
