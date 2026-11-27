# Source analysis

**Contract version** 1.0. Master design §71.

## Contract

Index keys use repository identity, Git object digest, grammar digest and analyzer version. Definitions/references use snapshot-relative byte ranges and symbol keys. Unknown languages receive text fallback and explicit capability flags.

## Execution and integration

Parse within resource limits, store diagnostics for invalid syntax, and update changed objects plus affected dependency projections. Do not present uncertain resolution as authoritative.

## Verification

Run invalid syntax, non-UTF-8 and unavailable grammar fixtures. Confirm incremental results match a fresh index for unchanged parser version.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [source-analysis crate design](../../crates/source-analysis/DESIGN.md)
- [repository crate design](../../crates/repository/DESIGN.md)
