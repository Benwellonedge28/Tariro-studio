# Scoped transfer adapter

**ZIP-SYNCHRONIZATION-TRANSPORT-001 · v1.0 · Owner:** Synchronization maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/synchronization/src/transport.rs`

## Required implementation behavior

Negotiate qualified peer, origin and stream limits before send. Resume only with compatible cursor/manifest and live scope.

## Acceptance

**ZIP-SYNCHRONIZATION-TRANSPORT-T01.** Connection loss before final chunk leaves artifact unpromoted.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
