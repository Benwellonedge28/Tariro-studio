# Distributed policy adapter

**ZIP-SCHEDULER-POLICIES-DISTRIBUTED-001 · v1.1 · Owner:** Scheduler maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/scheduler/src/policies/distributed.rs`

## Boundary and inputs

Evaluate enrolled node candidates under the [distributed compute contract](../../../../../specifications/2700-distributed/distributed.md). The scheduler consumes a typed observation supplied by composition, with node, placement scope, capability revision, freshness and known enforcement. Distributed configuration is a preference and confers no transport authority.

## Behavior and failure handling

Exclude stale, partitioned or out-of-scope nodes from new claims. Accept work only under current authorized egress, data scope, fenced ownership and complete enforceable resources. A partition after handoff leaves the original intent unresolved until trusted cleanup, effect and ownership reconciliation. A missing response is insufficient for absence, and a new target cannot supersede outstanding ownership. Ranking reads no provider and enqueues no work.

## Acceptance

**ZIP-SCHEDULER-POLICIES-DISTRIBUTED-T01.** Expire a node advertisement between selection and claim. Verify the next claim cannot use that node. Partition a previously authorized node after handoff and verify stale reports are fenced and no replacement starts before reconciliation.
