# Required scope qualification

**ZIP-VERIFICATION-QUALITY-COMPLETENESS-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/quality/completeness.rs`

## Required implementation behavior

Compare declared inventory against independently observed boundary. Report absent, unsupported and unverified entries distinctly.

## Acceptance

**ZIP-VERIFICATION-QUALITY-COMPLETENESS-T01.** Presence of a draft cannot be counted as implementation-ready completion.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
