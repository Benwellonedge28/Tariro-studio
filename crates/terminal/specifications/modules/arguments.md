# Structured platform argument encoding

**ZIP-TERMINAL-ARGUMENTS-001 · v1.1 · Owner:** Terminal maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/terminal/src/arguments.rs`

## Boundary and inputs

Accept typed ordered arguments after matching the exact command descriptor. Validate the argument schemas, encoding, count, per-value and total byte budgets before materializing backend representation. Reject embedded NUL and any string representation the qualified native adapter cannot pass without changing token boundaries.

## Behavior and failure handling

Pass data as separate arguments without interpolation. For a platform-dependent representation, require the adapter to prove the particular supported executable sees the intended sequence. Deny unsupported combinations instead of opening a shell. Preserve exact normalized arguments in the reviewed digest and redact diagnostics.

## Acceptance

**ZIP-TERMINAL-ARGUMENTS-T01.** Give an approved synthetic echo fixture benign punctuation in one argument. Verify intact single-argument delivery and one launched executable. Reject a malformed argument before process preparation.
