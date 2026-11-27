# Redacted standard error

**ZIP-TERMINAL-STDERR-001 · v1.0 · Owner:** Terminal maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/terminal/src/stderr.rs`

## Required implementation behavior

Charge same shared output bound and store redacted diagnostics separately from exit status. Formatting cannot transform failed process into success.

## Acceptance

**ZIP-TERMINAL-STDERR-T01.** Flooding stderr exhausts the shared cap even if stdout is empty.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
