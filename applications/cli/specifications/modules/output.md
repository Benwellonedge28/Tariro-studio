# Stable response formatting

**ZIP-CLI-OUTPUT-001 · v1.0 · Owner:** Cli maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/cli/src/output.rs`

## Required implementation behavior

Serialize one result or diagnostic by mode. Distinguish queued, committed, unknown and terminal statuses, preserve exit mapping, and prohibit credential/log dumping in either mode.

## Acceptance

**ZIP-CLI-OUTPUT-T01.** Golden fixtures compare machine output and exit codes without secret fields.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
