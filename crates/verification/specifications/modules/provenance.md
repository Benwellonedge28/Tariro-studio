# Evidence origin integrity

**ZIP-VERIFICATION-PROVENANCE-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/provenance.rs`

## Required implementation behavior

Verify actor identity, runner provenance, test and observation digest and exact reviewed scope. Store known uncertainty rather than promoting untrusted text.

## Acceptance

**ZIP-VERIFICATION-PROVENANCE-T01.** Fabricated citation or tool output lacking observed reference stays blocked.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
