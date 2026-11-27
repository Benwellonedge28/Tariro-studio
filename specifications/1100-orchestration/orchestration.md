# Team orchestration

**Contract version** 1.0. Master design §71.

## Contract

Compile a work graph with stable task IDs, role eligibility, dependency edges and conflict keys. Plan assigns independent review to an actor or verifier other than the author whenever feasible.

## Execution and integration

Execute ready tasks under lease and workspace protection. Two writes to the same normalized path serialize; conflicting verified proposals remain separate until approved resolution. Tie-breaking uses stable ordering.

## Verification

Reorder inputs and check deterministic plan. Stress shared path conflicts and confirm votes cannot bypass verification.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [orchestration crate design](../../crates/orchestration/DESIGN.md)
- [scheduler crate design](../../crates/scheduler/DESIGN.md)
