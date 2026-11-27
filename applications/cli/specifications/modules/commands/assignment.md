# Assignment command adapter

**ZIP-CLI-COMMANDS-ASSIGNMENT-001 · v1.0 · Owner:** Cli maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/cli/src/commands/assignment.rs`

## Required implementation behavior

Translate create/plan/run/pause/resume/cancel/status/verify with exact typed assignment identity and revision on mutations. Wait cancellation does not implicitly stop detached work.

## Acceptance

**ZIP-CLI-COMMANDS-ASSIGNMENT-T01.** Stale revision and lost reply preserve command idempotency and real assignment status.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
