# Controlled input streaming

**ZIP-TERMINAL-STDIN-001 · v1.0 · Owner:** Terminal maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/terminal/src/stdin.rs`

## Required implementation behavior

Use finite stdin capability and deadline; close input once at EOF or cancellation. No implicit interactive credential input.

## Acceptance

**ZIP-TERMINAL-STDIN-T01.** Downstream blocked reader unblocks on cancellation without leaking bytes.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
