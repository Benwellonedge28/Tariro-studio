# Aggregate durable records

**ZIP-ASSIGNMENTS-PERSISTENCE-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/persistence.rs`

## Required implementation behavior

Aggregate and unit records reference verified artifacts and ledgered effects. Store transaction ID and request digest for replay. Update progress revision and outbox atomically through storage.

## Acceptance

**ZIP-ASSIGNMENTS-PERSISTENCE-T01.** Crash around transaction yields either prior or complete new aggregate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
