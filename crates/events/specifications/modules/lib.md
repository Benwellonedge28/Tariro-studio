# Event service facade

**ZIP-EVENTS-LIB-001 · v1.0 · Owner:** Events maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/events/src/lib.rs`

## Required implementation behavior

Export envelope, publisher and subscriber ports with explicit visibility. Compose journal and storage through an injected adapter. Linking does not spawn work.

## Acceptance

**ZIP-EVENTS-LIB-T01.** Compile a fixture without opening a database or starting a dispatcher.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
