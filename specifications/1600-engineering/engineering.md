# Engineering changes

**Contract version** 1.0. Master design §71.

## Contract

A change plan maps requirements to normalized paths, preimage blob digests and acceptance gates. Staged patches identify exact base and validated target paths. Never alter unrelated working state.

## Execution and integration

Validate changes in isolated staging. If a preimage changed, block with conflict and require explicit replanning. Seal tree and evidence digest before any publication.

## Verification

Try unrelated files, changes after review and revision mismatch. Verify final PR corresponds to sealed candidate.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [engineering crate design](../../crates/engineering/DESIGN.md)
- [verification crate design](../../crates/verification/DESIGN.md)
