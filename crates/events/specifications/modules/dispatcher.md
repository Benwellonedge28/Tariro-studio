# Outbox to bounded subscriber delivery

**ZIP-EVENTS-DISPATCHER-001 · v1.0 · Owner:** Events maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/events/src/dispatcher.rs`

## Required implementation behavior

Read immutable pages in sequence order, verify subscriber scope per delivery and enqueue under resource lease. On queue pressure close or wait per policy and retain prior durable cursor.

## Acceptance

**ZIP-EVENTS-DISPATCHER-T01.** Inject stream disconnect after enqueue before processing; recovery redelivers under the same event identity.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
