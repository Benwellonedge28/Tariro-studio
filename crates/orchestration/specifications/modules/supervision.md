# Coordination supervision

**ZIP-ORCHESTRATION-SUPERVISION-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/supervision.rs`

## Required implementation behavior

Maintain lifecycle, queue, epochs and pending effects with same runtime lease discipline. Stop intake on revoke and reconcile before retry.

## Acceptance

**ZIP-ORCHESTRATION-SUPERVISION-T01.** Crash with unresolved remote work cannot duplicate dispatch.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
