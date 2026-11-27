# Typed event payload

**ZIP-EVENTS-EVENT-001 · v1.0 · Owner:** Events maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/events/src/event.rs`

## Required implementation behavior

DomainEvent owns stable kind, causal record identity and immutable payload reference. Validate kind/version before outbox insertion; derive neither authorization nor completion from payload text.

## Acceptance

**ZIP-EVENTS-EVENT-T01.** Unknown kind and schema are quarantined and cannot trigger an effect.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
