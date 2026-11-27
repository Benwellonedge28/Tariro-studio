# Durable evolution lineage

**ZIP-EVOLUTION-HISTORY-001 · v1.0 · Owner:** Evolution maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/evolution/src/history.rs`

## Required implementation behavior

Persist proposals, experiments, evaluations, approvals and actual effects by immutable digests. Preserve failures and superseded decisions.

## Acceptance

**ZIP-EVOLUTION-HISTORY-T01.** Old evaluation cannot be silently overwritten by new candidate note.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
