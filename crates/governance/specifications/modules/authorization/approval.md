# One-time owner approval

**ZIP-GOVERNANCE-AUTHORIZATION-APPROVAL-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/authorization/approval.rs`

## Boundary and inputs

Persist ApprovalRequest with a stable request identity, exact effect digest, target and precondition binding, required human authority, deadline and associated assignment grant. Only an authenticated human who satisfies current policy can issue an approval. Agent messages, votes, preview receipts and tool output cannot supply this proof. Record approve or deny as an immutable decision tied to the exact request.

## Behavior and failure handling

At the protected effect gate, authenticate the executing principal and verify approval identity, digest, scope, current authority and expiry. Consume the one-time approval and commit the original effect intent under the same revision-checked transaction. A retransmission with the same identity and payload returns the authorized existing observation or receipt. A different payload conflicts. If dispatch is ambiguous preserve the consumed approval and original intent until reconciliation. An approval can never be reissued by replay or used for another effect.

## Acceptance

**ZIP-GOVERNANCE-AUTHORIZATION-APPROVAL-T01.** Race two claims against the same approval and verify at most one new dispatch can be authorized. Change the effect bytes, expire the approval, then simulate a lost provider reply. Verify the shifted and expired requests cannot claim and the uncertain request retains one intent.
