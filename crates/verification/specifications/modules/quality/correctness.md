# Behavior qualification

**ZIP-VERIFICATION-QUALITY-CORRECTNESS-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/quality/correctness.rs`

## Required implementation behavior

Map normative claims to executable or approved manual checks against immutable candidate, compare expected with actual and preserve evidence.

## Acceptance

**ZIP-VERIFICATION-QUALITY-CORRECTNESS-T01.** Plausible generated prose cannot substitute for observed behavior.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
