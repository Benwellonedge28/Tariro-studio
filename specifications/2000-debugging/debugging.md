# Evidence-led debugging

**Contract version** 1.0. Master design §71.

## Contract

Use a pinned failure reproduction with command, environment digest, input artifacts and normalized signature. Record each hypothesis and a measurable falsification criterion.

## Execution and integration

Change one relevant dimension per attempt, store redacted output, then use engineering change plan for any proposed patch. Escalate unresolved or flaky failures with bounded attempts.

## Verification

Test invalid log, nonreproducing timeout and contradictory result. Ensure no patch appears merely because the model claims a fix.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [debugging crate design](../../crates/debugging/DESIGN.md)
- [source-analysis crate design](../../crates/source-analysis/DESIGN.md)
