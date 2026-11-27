# Event failure vocabulary

**ZIP-EVENTS-ERROR-001 · v1.0 · Owner:** Events maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/events/src/error.rs`

## Required implementation behavior

EventError classifies InvalidEnvelope, SequenceOverflow, CursorExpired, Backpressure, Conflict, Storage and Denied. Error carries sequence/cursor only for authorized streams.

## Acceptance

**ZIP-EVENTS-ERROR-T01.** A caller outside stream scope cannot distinguish absent versus expired private cursor.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
