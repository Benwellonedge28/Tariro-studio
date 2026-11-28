# Delegated task hierarchy

**ZIP-ORCHESTRATION-STRATEGIES-HIERARCHICAL-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/strategies/hierarchical.rs`

## Boundary and inputs

Represent a bounded group tree rooted in the reviewed task and parent grant. Each child binds a stable lineage, exact responsibility, narrower authority, deadline and approved report recipient. Check the effective nesting and resource policy before expanding any child. Unknown lineage or a cycle blocks the subtree.

## Behavior and failure handling

Apply the [delegation contract](../delegation.md) for each child request. Use the Scheduler for individually admitted attempts and account for overlapping occupancy under parent ceilings. Propagate parent revocation to child admission and later effects. Report subtree completion only after independently verified receipts and required settlements. Partial or conflicting results remain visible.

## Acceptance

**ZIP-ORCHESTRATION-STRATEGIES-HIERARCHICAL-T01.** Construct valid children and one child that adds a destination outside the parent scope. Deny the latter. Revoke the parent during a child effect and confirm future child dispatch is fenced while earlier committed evidence remains available.
