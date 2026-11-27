# CLI composition root

**ZIP-CLI-MAIN-001 · v1.0 · Owner:** Cli maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/cli/src/main.rs`

## Required implementation behavior

Decode request via arguments, set per-command deadline, negotiate local authenticated gateway and dispatch. Emit one normalized result on stdout and structured errors on stderr. Never directly start detached child processes.

## Acceptance

**ZIP-CLI-MAIN-T01.** Fake gateway verifies one invocation and correct status for unreachable daemon and invalid usage.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
