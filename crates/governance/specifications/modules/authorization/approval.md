# One-time owner approval

**ZIP-GOVERNANCE-AUTHORIZATION-APPROVAL-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/authorization/approval.rs`

## Required implementation behavior

Persist request digest, distinct approver role and expiry; atomically claim once against identical parameters. Exact replay reads receipt. Changed payload conflicts.

## Acceptance

**ZIP-GOVERNANCE-AUTHORIZATION-APPROVAL-T01.** Two concurrent claims produce one authorized effect.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
