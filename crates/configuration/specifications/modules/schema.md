# Registry and normalized types

**ZIP-CONFIGURATION-SCHEMA-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/schema.rs`

## Required implementation behavior

KeySpec contains dotted key, ValueKind, unit, lower bound, reload policy and owner; normalized values are Bool, U64, Enum, StringRef or Set. Reject unlisted keys before merging layers.

## Acceptance

**ZIP-CONFIGURATION-SCHEMA-T01.** Load the defaults registry and prove negative, noninteger and unregistered values cannot reach a resolved snapshot.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
