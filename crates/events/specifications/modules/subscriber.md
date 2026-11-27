# Durable consumer progress

**ZIP-EVENTS-SUBSCRIBER-001 · v1.0 · Owner:** Events maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/events/src/subscriber.rs`

## Required implementation behavior

subscribe(request: SubscriptionRequest, after: Cursor) -> Result<Subscription, EventError>. Validate authority first and then cursor generation. Advance the cursor only after durable processing acknowledgement.

## Acceptance

**ZIP-EVENTS-SUBSCRIBER-T01.** Retry an identical ack and verify no cursor regression or duplicate projection.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
