# Ordered command effect

**ZIP-TERMINAL-EXECUTION-001 · v1.0 · Owner:** Terminal maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/terminal/src/execution.rs`

## Required implementation behavior

Authorize and lease, validate executable/cwd, persist intent, spawn contained child, collect bounded output and verify exit. Reconcile unknown external effects separately.

## Acceptance

**ZIP-TERMINAL-EXECUTION-T01.** Failure during spawn returns no success receipt and preserves cleanup obligation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
