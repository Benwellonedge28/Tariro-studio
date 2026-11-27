# Packaging and deployment

**Contract version** 1.0. Master design §71.

## Contract

Release manifest v1 records artifact digest, target triple, toolchain, SBOM, compatibility capabilities, policy and release evidence. Sign and verify before distribution or activation.

## Execution and integration

Native deployment first. Stage package separately, verify signature and compatibility, activate only after release approval, run health checks and roll back to a compatible known-good version on failure.

## Verification

Test clean install, unsupported platform, package substitution, release without authorization and rollback with schema revision.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [deployment crate design](../../crates/deployment/DESIGN.md)
- [verification crate design](../../crates/verification/DESIGN.md)
