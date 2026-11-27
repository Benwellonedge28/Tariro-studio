# Evolution outcome classes

**ZIP-EVOLUTION-ERROR-001 · v1.0 · Owner:** Evolution maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/evolution/src/error.rs`

## Required implementation behavior

Classify bad proposal, unavailable baseline, denied scope, regression, missing review, stale approval and recovery blocked.

## Acceptance

**ZIP-EVOLUTION-ERROR-T01.** Absent baseline cannot yield accepted improvement.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
