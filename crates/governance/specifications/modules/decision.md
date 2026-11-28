# Typed decision outcomes

**ZIP-GOVERNANCE-DECISION-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/decision.rs`

## Boundary and inputs

Represent the [security decision contract](../../../../specifications/2300-security/security.md) as Allowed with a decision ID, policy digest and scope digest, Denied with decision and stable reason code, or AwaitingApproval with request identity and exact effect digest. Bind each allowed decision to the canonical action digest and input revisions in its internal evidence record.

## Behavior and failure handling

Treat the decision as an observation. Dispatch still requires a fresh authorized claim, currently valid attributes and independent execution capacity. Do not include raw grants, model prompts, credentials or unauthorized resource details. An exact replay returns the scoped stored decision rather than creating permission. A changed effect must be re-evaluated and may require fresh approval.

## Acceptance

**ZIP-GOVERNANCE-DECISION-T01.** Obtain an allowed decision on a scoped action, then change its digest or underlying target state. Confirm the old decision cannot cross the claim gate. Verify a redacted denial exposes no protected metadata.
