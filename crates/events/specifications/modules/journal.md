# Sequence and outbox persistence

**ZIP-EVENTS-JOURNAL-001 · v1.0 · Owner:** Events maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/events/src/journal.rs`

## Required implementation behavior

Append envelopes and sequence updates atomically through storage. A point read validates event, stream and expected sequence. The transaction receipt is the publish boundary.

## Acceptance

**ZIP-EVENTS-JOURNAL-T01.** Corrupt event bytes and verify typed corruption instead of skipping to a later event.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
