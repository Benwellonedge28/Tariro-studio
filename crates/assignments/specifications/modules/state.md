# Assignment state vocabulary

**ZIP-ASSIGNMENTS-STATE-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/state.rs`

## Required implementation behavior

Encode Submitted, Validated, Authorized, Planned, Scheduled, Executing, Verifying, Completed, Paused, Blocked, Failed, Cancelled, AwaitingApproval and Recovering using stable string tags. Completed, Failed and Cancelled are terminal.

## Acceptance

**ZIP-ASSIGNMENTS-STATE-T01.** Decode all known states and reject unknown required state tag; no default transition.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
