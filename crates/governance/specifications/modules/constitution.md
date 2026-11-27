# Mandatory invariant boundary

**ZIP-GOVERNANCE-CONSTITUTION-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/constitution.rs`

## Required implementation behavior

Load reviewed constitution version and digest before mutable overlays. Reject invalid or unsupported version. Mandatory constraints can only tighten, never be waived by an assignment grant.

## Acceptance

**ZIP-GOVERNANCE-CONSTITUTION-T01.** Workspace override conflicts with mandatory invariant and remains denied.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
