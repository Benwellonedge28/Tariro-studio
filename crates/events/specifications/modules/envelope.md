# Durable event envelope

**ZIP-EVENTS-ENVELOPE-001 · v1.0 · Owner:** Events maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/events/src/envelope.rs`

## Required implementation behavior

Envelope contains stream ID, ordered sequence, event ID, UTC occurrence time, correlation ID, schema and payload reference. Enclosing storage owns byte layout and validates tagged digest.

## Acceptance

**ZIP-EVENTS-ENVELOPE-T01.** Round-trip valid v1, reject invalid sequence and unsupported major before dispatch.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
