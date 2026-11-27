# Advisory preference tally

**ZIP-ORCHESTRATION-VOTING-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/voting.rs`

## Required implementation behavior

Count one qualified preference per eligible identity and disclose ties. No outcome authorizes an effect by vote, regardless of count.

## Acceptance

**ZIP-ORCHESTRATION-VOTING-T01.** Unanimous team vote cannot substitute for owner sign-off.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
