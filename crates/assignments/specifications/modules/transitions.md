# Revision-checked transition binding

**ZIP-ASSIGNMENTS-TRANSITIONS-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/transitions.rs`

## Required implementation behavior

Match state/event against approved assignment transition table; verify actor, guard, revision, evidence and lease within effect-specific policy. Commit state, outbox, receipt together; illegal pair yields no mutation.

## Acceptance

**ZIP-ASSIGNMENTS-TRANSITIONS-T01.** Race same revision commands and assert at most one creates a transition.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
