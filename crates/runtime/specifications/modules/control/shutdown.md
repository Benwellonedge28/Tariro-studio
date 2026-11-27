# Ordered process shutdown

**ZIP-RUNTIME-CONTROL-SHUTDOWN-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/control/shutdown.rs`

## Required implementation behavior

Close admission and queues, broadcast cancellation, wait under configured deadline, terminate contained descendants as appropriate, flush events and reconcile. Keep incomplete work visible.

## Acceptance

**ZIP-RUNTIME-CONTROL-SHUTDOWN-T01.** Full queues and blocked producers terminate without allowance leaks; unreaped child retains reservation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
