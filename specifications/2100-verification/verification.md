# Verification and evidence

**Contract version** 1.0. Master design §71.

## Contract

Every evidence record binds requirement, candidate tree, inputs, runner and version, observed output digest, verdict and assessor. Accept only if all required current evidence passes and unresolved findings are absent.

## Execution and integration

A verifier reads a bounded immutable artifact or independently re-executes a deterministic check. A manual check records reviewer and reviewed digest. CI status is bound to the actual PR head.

## Verification

Change one byte after verification or omit a required gate. Verify both block completion.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [verification crate design](../../crates/verification/DESIGN.md)
- [audit crate design](../../crates/audit/DESIGN.md)
