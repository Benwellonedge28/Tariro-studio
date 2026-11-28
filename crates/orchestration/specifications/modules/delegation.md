# Scoped work transfer

**ZIP-ORCHESTRATION-DELEGATION-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/delegation.rs`

## Boundary and inputs

Produce a child request bound to the exact parent assignment, task lineage, plan revision and authorized role. Verify live parent and scope through the trusted assignment boundary. Child operations and data classes must be within the parent grant. Child deadline is the earliest applicable parent, request and policy deadline in the live domain. Child demand must fit admitted policy without taking capacity implicitly.

## Behavior and failure handling

Reject inherited fields that widen locality, tool access, audience, scope or end time. Require unique child identity under the parent and reject cycles or lineage beyond the declared bound. Persist the delegation intent through the assignment's owning transaction before Scheduler submission. Check parent authority again before claim and protected effects. A revoked parent blocks new child work and defers existing effects to independently authorized reconciliation.

## Acceptance

**ZIP-ORCHESTRATION-DELEGATION-T01.** Try a broader path scope, cross-workspace recipient, extended deadline and stale parent grant. Verify no child submission. Lose the acknowledgement of a valid delegation and recover the same stored child identity without dispatching twice.
