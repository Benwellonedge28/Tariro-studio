# Pause at verified boundary

**ZIP-ASSIGNMENTS-PAUSE-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/pause.rs`

## Required implementation behavior

Stop task intake, persist pause intent, pass cancellation/drain to supervisor and wait for a durable checkpoint or typed cleanup failure. Paused state requires no undisclosed worker effects.

## Acceptance

**ZIP-ASSIGNMENTS-PAUSE-T01.** Pause under unknown remote outcome stays blocked or reconciling.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
