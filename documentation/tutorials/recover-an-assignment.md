# Exercise assignment recovery

This page defines the target workflow and the checks required before release.

## Prerequisites and behavior

Use a disposable repository and independent checkpoint verification. Create a two-document local assignment and pin its source revision.

## Procedure

Pause or terminate after the first verified checkpoint. Restart with the same data root. Inspect status, verify digest of first file, and resume from the second unit. Record the expected and observed checkpoint sequence.

## Verification and recovery

Repeat with an expired grant. The assignment waits for renewed authority and keeps existing verified work. Do not run this fault test against live external mutations.

[Architecture](../../ARCHITECTURE.md) · [Requirements](../../REQUIREMENTS.md)
