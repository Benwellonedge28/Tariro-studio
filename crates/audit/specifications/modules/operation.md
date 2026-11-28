# Effect intent/outcome taxonomy

**ZIP-AUDIT-OPERATION-001 · v1.1 · Owner:** Audit maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/audit/src/operation.rs`

## Boundary and inputs

Bind immutable operation kind, stable effect reference, reviewed effect digest, and correlation with the current intent and decision records. Use typed outcomes denied, pending, confirmed, failed and unresolved. Proven completed effect and definitive failure each need their own trusted observation. An exception or lost response never implies either.

## Behavior and failure handling

Append separate observations for intent, unresolved outcome and verified reconciliation. Correlate them by original identity without editing past records. A matching outcome replay adds no second observation for the same accepted command. Preserve distinct local audit identity if the owning approved repeat created a new observation. Reject conflicting evidence for one accepted observation and leave unsettled work visible.

## Acceptance

**ZIP-AUDIT-OPERATION-T01.** Lose the reply to a synthetic confirmed mutation. Record unresolved until the owner verifies the result. Reconcile the identical receipt twice and confirm a single audited confirmation under the original effect identity.
