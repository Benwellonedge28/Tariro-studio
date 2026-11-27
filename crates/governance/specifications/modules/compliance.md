# Policy evidence projection

**ZIP-GOVERNANCE-COMPLIANCE-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/compliance.rs`

## Required implementation behavior

Collect audited decisions and outcomes under scoped access, compare mandatory controls to linked evidence and report gaps. No policy or effect mutation.

## Acceptance

**ZIP-GOVERNANCE-COMPLIANCE-T01.** Missing audit record prevents a compliant verdict for that effect.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
