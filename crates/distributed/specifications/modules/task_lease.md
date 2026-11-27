# Scoped fenced task lease

**ZIP-DISTRIBUTED-TASK-LEASE-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/task_lease.rs`

## Required implementation behavior

Bind owner, node, assignment, exact payload digest, capacity, expiry and monotonic epoch. Admission and result acceptance revalidate live lease.

## Acceptance

**ZIP-DISTRIBUTED-TASK-LEASE-T01.** Cross-node or expired lease cannot promote artifacts.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
