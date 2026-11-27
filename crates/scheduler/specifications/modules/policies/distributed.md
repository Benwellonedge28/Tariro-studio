# Distributed policy adapter

**ZIP-SCHEDULER-POLICIES-DISTRIBUTED-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/policies/distributed.rs`

## Required implementation behavior

Consider only authorized live nodes with fenced leases and known locality; avoid reconciling remote effects by duplicate dispatch.

## Acceptance

**ZIP-SCHEDULER-POLICIES-DISTRIBUTED-T01.** Expired node advertisement becomes ineligible before next claim.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
