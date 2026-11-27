# Supervised execution and results

**ZIP-TESTING-EXECUTION-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/execution.rs`

## Required implementation behavior

Admit exact fixture/runner, launch in containment, collect redacted observed result and reconcile unknown effects before retry.

## Acceptance

**ZIP-TESTING-EXECUTION-T01.** Timeout and completed failure persist different statuses.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
