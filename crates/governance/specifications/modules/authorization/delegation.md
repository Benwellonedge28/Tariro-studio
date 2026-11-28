# Attenuated delegation

**ZIP-GOVERNANCE-AUTHORIZATION-DELEGATION-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/authorization/delegation.rs`

## Boundary and inputs

Verify the authenticated delegator, current parent grant and full active lineage. Accept a child request bound to exact recipient, parent identity, intended actions, scopes and validity. Compute an intersection against the parent and current policy, including path, locality, audience, effects and compatible budgets. Prohibit cycles, expired parents and depth outside the resolved bound.

## Behavior and failure handling

Require each child window and ceiling to fit the parent's current authority, and preserve shared parent quota accounting across children. A child grant cannot duplicate consumable budget or acquire an operation-class approval by inheritance. Record immutable parent and child references, child epoch and evidence under an expected revision. Revalidate lineage at operation claim. Parent revocation fences descendants even if invalidation notifications are delayed.

## Acceptance

**ZIP-GOVERNANCE-AUTHORIZATION-DELEGATION-T01.** Delegate inspect from an inspect-only parent, then request publish and a longer lifetime. Only an authorized narrowed request may produce a grant. Revoke the parent and verify its live descendants cannot claim new operations.
