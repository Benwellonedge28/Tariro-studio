# Observed debugging evidence

**ZIP-DEBUGGING-REPORTING-001 · v1.0 · Owner:** Debugging maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/debugging/src/reporting.rs`

## Required implementation behavior

Summarize actual attempts, qualified source, failure and unresolved hypotheses without leaking raw secret values.

## Acceptance

**ZIP-DEBUGGING-REPORTING-T01.** Unexecuted reproduction is reported as not run.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
