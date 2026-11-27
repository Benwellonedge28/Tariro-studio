# Compilation

**Contract version** 1.0. Master design §71.

## Contract

Build inputs include pinned snapshot, adapter/toolchain identities, target, arguments, required environment keys and dependency lock digest. Hash normalized input to identify the build/cache transaction.

## Execution and integration

Run structured commands with inherited network disabled unless authorized for the exact dependency source. Preserve stderr and status separately. Publish digest-verified outputs only after successful status and path validation.

## Verification

Test missing toolchain, execution timeout, wrong target and interrupted cache promotion.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [compilation crate design](../../crates/compilation/DESIGN.md)
- [terminal crate design](../../crates/terminal/DESIGN.md)
