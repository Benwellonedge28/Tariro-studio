# Subscriber pressure decisions

**ZIP-EVENTS-BACKPRESSURE-001 · v1.0 · Owner:** Events maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/events/src/backpressure.rs`

## Required implementation behavior

Given queue state and policy, decide admit, wait or close. Wait is bounded by deadline and cancellation. Close exposes last acknowledged cursor but cannot imply event deletion.

## Acceptance

**ZIP-EVENTS-BACKPRESSURE-T01.** Cancelled blocked producer leaves the durable cursor unchanged and releases its queue wait.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
