# Test execution

**Contract version** 1.0. Master design §71.

## Contract

TestPlan records pinned input, suite IDs, toolchain, seed, isolation, outcome parser and expected reports. Results distinguish pass, failure, timeout, skip, error and missing report.

## Execution and integration

Preserve failed attempts even if a retry passes. Results bind exact candidate tree to raw log and normalized report. A required skipped or unrecognized suite blocks the release.

## Verification

Parse corrupt and partial reports, verify stable test IDs and prove empty output does not pass.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [testing crate design](../../crates/testing/DESIGN.md)
- [verification crate design](../../crates/verification/DESIGN.md)
