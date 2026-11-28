# Open decision lifecycle

**ZIP-GOVERNANCE-OVERSIGHT-ESCALATION-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/oversight/escalation.rs`

## Boundary and inputs

Persist a decision request naming exact affected effect or candidate, expected version, reason, bounded evidence references, authorized audience, required decision role and expiry. Use original request identity on replay. Unresolved escalation blocks dependent effects without changing unrelated admission.

## Behavior and failure handling

Keep the record visible across restart. A reply must be authenticated, current, within expiry and bound to the same candidate and expected revision. Record accept, deny or expired as separate dispositions. A stale or expired reply cannot resume execution. A changed candidate requires a newly scoped request. Notify from committed outbox only.

## Acceptance

**ZIP-GOVERNANCE-OVERSIGHT-ESCALATION-T01.** Restart with a pending escalation, allow it to expire and deliver a matching late answer. Verify pending evidence persists, the answer cannot unblock work and no second notification is mistaken for approval.
