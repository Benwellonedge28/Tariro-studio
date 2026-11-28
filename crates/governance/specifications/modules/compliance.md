# Policy evidence projection

**ZIP-GOVERNANCE-COMPLIANCE-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/compliance.rs`

## Boundary and inputs

Project a verdict from scoped policy obligations and redacted audit and outcome observations tied to an exact candidate, effect identity and policy revision. Read through a composition-supplied evidence interface. Distinguish verified, violated and unavailable obligations. A policy label or assertion cannot stand in for observed completion.

## Behavior and failure handling

Require all mandatory records for the requested claim, including each applicable prior authorization and confirmed final receipt. Missing or stale evidence blocks the affected claim. An unresolved effect remains open. If a valid exception applies, retain its exact authorization and expiry as evidence for only that rule. Do not alter policy, audit history or effect status from a compliance check.

## Acceptance

**ZIP-GOVERNANCE-COMPLIANCE-T01.** Omit the required outcome audit record for one otherwise matching operation. Verify a blocked verdict with a scoped missing requirement and no effect or policy mutation.
