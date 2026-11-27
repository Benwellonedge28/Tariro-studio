# Independent candidate verification

**ZIP-VERIFICATION-VERIFIER-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/verifier.rs`

## Required implementation behavior

Bind immutable plan and candidate, run required checks with admitted budget and scoped runner, preserve actual results, then evaluate acceptance.

## Acceptance

**ZIP-VERIFICATION-VERIFIER-T01.** Changed artifact after evidence collection cannot accept.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
