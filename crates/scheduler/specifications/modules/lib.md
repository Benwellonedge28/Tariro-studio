# Scheduler facade

**ZIP-SCHEDULER-LIB-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/lib.rs`

## Required implementation behavior

Expose submission, placement and observation ports; inject capacity and durable storage before accepting work.

## Acceptance

**ZIP-SCHEDULER-LIB-T01.** Constructing the facade creates no worker or remote connection.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
