# Typed decision outcomes

**ZIP-GOVERNANCE-DECISION-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/decision.rs`

## Required implementation behavior

Return Allowed with decision ID and exact scope/policy digests, Denied with stable code, or AwaitingApproval with effect digest. Decision is inspectable and does not hold credential material.

## Acceptance

**ZIP-GOVERNANCE-DECISION-T01.** Allowed decision for one digest cannot execute changed effects.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
