# Transactional event publication

**ZIP-EVENTS-PUBLISHER-001 · v1.0 · Owner:** Events maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/events/src/publisher.rs`

## Required implementation behavior

append(tx: &mut WriteBatch, event: DomainEvent) -> Result<EventRef, EventError>. Stage with domain mutation, allocate sequence during commit, and expose only confirmed durable receipt.

## Acceptance

**ZIP-EVENTS-PUBLISHER-T01.** Kill before commit leaves neither domain mutation nor outbox event.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
