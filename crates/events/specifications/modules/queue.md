# Admitted in-memory subscriber queue

**ZIP-EVENTS-QUEUE-001 · v1.0 · Owner:** Events maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/events/src/queue.rs`

## Required implementation behavior

Enqueue checks current lease and configured capacity before allocation. Track byte and element budgets; pop releases only the corresponding accounting entry. Closing wakes blocked participants.

## Acceptance

**ZIP-EVENTS-QUEUE-T01.** Overflow with a slow subscriber does not lose durable events or silently grow memory.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
