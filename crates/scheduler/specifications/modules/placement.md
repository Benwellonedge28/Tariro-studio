# Qualified node selection

**ZIP-SCHEDULER-PLACEMENT-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/placement.rs`

## Required implementation behavior

Filter nodes by freshness, enforceability, trust and locality; score capacity fit then stable node ID. Explicit egress permission is required for remote input.

## Acceptance

**ZIP-SCHEDULER-PLACEMENT-T01.** An otherwise faster unauthorized node is excluded.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
