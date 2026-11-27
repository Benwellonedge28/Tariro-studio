# Quarantine of terminal delivery failures

**ZIP-EVENTS-DEAD-LETTER-001 · v1.0 · Owner:** Events maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/events/src/dead_letter.rs`

## Required implementation behavior

Persist event reference, subscriber identity, stable error class and attempt history after approved retry budget is exhausted. Redrive requires live scope and fresh admission. Keep original event identity.

## Acceptance

**ZIP-EVENTS-DEAD-LETTER-T01.** Dead-letter write failure cannot acknowledge processing; successful redrive does not create a new event.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
