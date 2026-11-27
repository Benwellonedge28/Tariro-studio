# Owned process lifecycle

**ZIP-TERMINAL-PROCESS-001 · v1.0 · Owner:** Terminal maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/terminal/src/process.rs`

## Required implementation behavior

Create opaque process handle in sandbox after admission, report finish and descendant status to supervisor. No process reuse across attempts.

## Acceptance

**ZIP-TERMINAL-PROCESS-T01.** Unowned process identity cannot be cancelled or attached.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
