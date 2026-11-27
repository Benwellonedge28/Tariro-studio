# Bounded replay cursor

**ZIP-EVENTS-REPLAY-001 · v1.0 · Owner:** Events maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/events/src/replay.rs`

## Required implementation behavior

read_after(stream: StreamId, cursor: Cursor, budget: ReadBudget) -> Result<EventPage, EventError>. Cursor is exclusive and tied to stream/retention generation. Expiry returns snapshot reference only if authorized.

## Acceptance

**ZIP-EVENTS-REPLAY-T01.** Cursor at tail returns empty; deleted cursor requests return CursorExpired rather than beginning over silently.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
