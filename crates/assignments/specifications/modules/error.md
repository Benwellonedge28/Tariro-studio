# Assignment error and block classes

**ZIP-ASSIGNMENTS-ERROR-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/error.rs`

## Required implementation behavior

Define InvalidSpec, InvalidTransition, ScopeDenied, RevisionConflict, BudgetUnavailable, EvidenceIncomplete, CorruptCheckpoint, UnknownEffect and Cancelled. Descriptions use stable codes and redact content.

## Acceptance

**ZIP-ASSIGNMENTS-ERROR-T01.** Lost remote reply remains UnknownEffect until reconciliation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
