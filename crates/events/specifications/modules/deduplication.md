# Consumer idempotency ledger

**ZIP-EVENTS-DEDUPLICATION-001 · v1.0 · Owner:** Events maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/events/src/deduplication.rs`

## Required implementation behavior

Apply projection, event-ID marker and consumer cursor in one transaction. An exact duplicate returns recorded receipt. Same ID with a different digest conflicts.

## Acceptance

**ZIP-EVENTS-DEDUPLICATION-T01.** Crash after commit before ack and replay; projection count stays one.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
