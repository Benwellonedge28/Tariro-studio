# Authorized stream selection

**ZIP-EVENTS-TOPIC-001 · v1.0 · Owner:** Events maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/events/src/topic.rs`

## Required implementation behavior

Topic is a typed workspace and event-kind selector. Normalize selectors then intersect subscriptions with principal scope. Matching is deterministic and independent of network availability.

## Acceptance

**ZIP-EVENTS-TOPIC-T01.** Wildcard request cannot observe an event from a different workspace.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
