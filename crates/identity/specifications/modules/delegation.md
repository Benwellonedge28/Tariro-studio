# Attenuated principal authority

**ZIP-IDENTITY-DELEGATION-001 · v1.1 · Owner:** Identity maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/identity/src/delegation.rs`

## Boundary and inputs

Verify an authenticated delegator, exact live parent identity, intended child and reviewed lineage before proposing a child principal context. Require an acyclic chain within the effective bound. Match workspace, assignment and audience at each link. Child issuance cannot occur from a name or detached grant reference.

## Behavior and failure handling

Intersect requested scopes and expiry with current parent and mandatory policy through the owning Governance interface. Persist exact lineage and child identity under expected revision. Check all applicable parent generations during use, including after restart, so a revoked parent fences descendants without waiting for asynchronous notification. Keep shared budgets under the resource owner.

## Acceptance

**ZIP-IDENTITY-DELEGATION-T01.** Request broadened destination and an extended lifetime, then try an expired parent. Deny each. Issue a valid narrowed child, revoke the parent and verify next use is rejected.
