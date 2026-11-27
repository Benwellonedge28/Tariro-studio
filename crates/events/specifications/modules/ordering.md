# Sequence validation

**ZIP-EVENTS-ORDERING-001 · v1.0 · Owner:** Events maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/events/src/ordering.rs`

## Required implementation behavior

Require a positive per-stream sequence, compare using checked integer order and reject reuse with a different event ID. Separate sequence from wall time.

## Acceptance

**ZIP-EVENTS-ORDERING-T01.** Change event timestamps and verify per-stream order is stable.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
