# Controlled evolution

**Contract version** 1.0. Master design §71.

## Contract

A proposal holds base revision, stated objective, diff digest, policy delta, benchmark baseline and evidence requirements. Evaluation uses immutable fixtures and isolates changes from active service.

## Execution and integration

Human approval and normal deployment gates are required. A change to authorization, security or verification requires independent oversight and dedicated approval. Self-proposal has no extra rights.

## Verification

Try unauthorized policy changes and a benchmark regression; both block promotion. Verify rollback references known-good artifacts.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [evolution crate design](../../crates/evolution/DESIGN.md)
- [governance crate design](../../crates/governance/DESIGN.md)
- [verification crate design](../../crates/verification/DESIGN.md)
