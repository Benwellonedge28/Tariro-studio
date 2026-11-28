# Deterministic rule evaluation

**ZIP-GOVERNANCE-POLICY-ENGINE-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/policy_engine.rs`

## Boundary and inputs

Evaluate one canonical request against one coherent verified policy and authority snapshot. Authenticate actor, audience and scope before reading protected details. Verify mandatory attributes, constitution, revocation, exact effect bounds and relevant resource observations. Apply mandatory and explicit denies before permits, then determine separate approval requirements. See [security ordering](../../../../specifications/2300-security/security.md).

## Behavior and failure handling

Sort applicable rules by stable identity for evidence. The outcome must be independent of rule input order. Deny missing or inconsistent mandatory observations. Produce only a scoped decision and provenance; use the operation claim path for irreversible execution with current fences. Pure regression evaluation performs no Storage mutation and no adapter effect.

## Acceptance

**ZIP-GOVERNANCE-POLICY-ENGINE-T01.** Permute one allow and one applicable deny. Verify identical denial and reason ordering. Remove a mandatory attribute and check denial with safe evidence instead of assuming default permission.
