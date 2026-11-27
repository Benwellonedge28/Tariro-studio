# Failure and cleanup owner

**ZIP-AGENTS-SUPERVISION-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/supervision.rs`

## Required implementation behavior

Track attempt epoch and active child handles, fence stale reports, cancel on revoke and release lease only after reconciliation.

## Acceptance

**ZIP-AGENTS-SUPERVISION-T01.** Unreaped child retains reserved capacity.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
