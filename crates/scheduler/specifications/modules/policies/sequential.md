# Serial placement profile

**ZIP-SCHEDULER-POLICIES-SEQUENTIAL-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/policies/sequential.rs`

## Required implementation behavior

Offer at most one active attempt in the declared sequential scope; count draining attempts as active until cleanup.

## Acceptance

**ZIP-SCHEDULER-POLICIES-SEQUENTIAL-T01.** A second attempt waits while the predecessor is unreaped.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
