# Immutable execution request

**ZIP-TERMINAL-COMMAND-001 · v1.0 · Owner:** Terminal maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/terminal/src/command.rs`

## Required implementation behavior

Pin qualified executable, argv, cwd, environment schema, byte and time budgets, grant and correlation ID. Review digest binds these fields.

## Acceptance

**ZIP-TERMINAL-COMMAND-T01.** Changed argv after review produces stale effect digest.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
