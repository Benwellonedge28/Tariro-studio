# Separately authorized compensation

**ZIP-WORKFLOWS-COMPENSATION-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/compensation.rs`

## Required implementation behavior

Map reviewed effect to bounded inverse or remediation plan with distinct authorization and evidence. No implicit compensation after revoke.

## Acceptance

**ZIP-WORKFLOWS-COMPENSATION-T01.** Revoked grant prevents compensation even after failed workflow.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
