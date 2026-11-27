# Workflow effect approval boundary

**ZIP-WORKFLOWS-APPROVAL-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/approval.rs`

## Required implementation behavior

Bind owner-approved effect digest, scope, step, exact plan and expiry. Present stale input as conflict; model output cannot approve.

## Acceptance

**ZIP-WORKFLOWS-APPROVAL-T01.** Reordered arguments or changed destination require renewed authority.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
