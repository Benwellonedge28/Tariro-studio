# Resource error decisions

**ZIP-RESOURCES-ERROR-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/error.rs`

## Required implementation behavior

Use ResourceError::{UnknownCapacity, StaleRevision, CapacityExceeded, PolicyDenied, Overflow, InvalidLease, CleanupRequired, ProbeFailed}. Errors report coordinate and scope after authorization.

## Acceptance

**ZIP-RESOURCES-ERROR-T01.** Distinguish a discovered zero-sized pool from a missing measurement in the error path.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
