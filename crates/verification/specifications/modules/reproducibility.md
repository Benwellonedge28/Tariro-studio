# Repeatability qualification

**ZIP-VERIFICATION-REPRODUCIBILITY-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/reproducibility.rs`

## Required implementation behavior

Pin toolchain, inputs, fixture/seed and environment, run within qualified scope and compare declared artifact/results. Report supported platform and tolerance.

## Acceptance

**ZIP-VERIFICATION-REPRODUCIBILITY-T01.** Mismatch beyond reviewed tolerance fails and preserves both digests.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
