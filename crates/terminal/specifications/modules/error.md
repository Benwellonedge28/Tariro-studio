# Terminal failure outcomes

**ZIP-TERMINAL-ERROR-001 · v1.0 · Owner:** Terminal maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/terminal/src/error.rs`

## Required implementation behavior

Separate InvalidCommand, Denied, Timeout, OutputLimit, Cancelled, ExitFailure, UnknownEffect and CleanupIncomplete. Carry redacted diagnostics only.

## Acceptance

**ZIP-TERMINAL-ERROR-T01.** Output truncation and nonzero exit remain distinct.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
