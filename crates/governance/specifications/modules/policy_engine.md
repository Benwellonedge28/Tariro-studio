# Deterministic rule evaluation

**ZIP-GOVERNANCE-POLICY-ENGINE-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/policy_engine.rs`

## Required implementation behavior

Authenticate actor then apply mandatory constraints, current revocation and resource policy. Evaluate denies before permits and separate authorization from approval requirement. Unknown mandatory field denies.

## Acceptance

**ZIP-GOVERNANCE-POLICY-ENGINE-T01.** Permute input rule order and verify identical outcome and review reasons.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
