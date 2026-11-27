# Bounded debug session

**ZIP-DEBUGGING-SESSION-001 · v1.0 · Owner:** Debugging maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/debugging/src/session.rs`

## Required implementation behavior

Pin target, candidate, qualified adapter, scope, attempt budget and deadline. Track actual lifecycle and owned handles.

## Acceptance

**ZIP-DEBUGGING-SESSION-T01.** Expired grant prevents further attempts and releases only verified cleanup.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
