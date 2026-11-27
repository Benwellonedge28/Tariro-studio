# Strict CLI parsing

**ZIP-CLI-ARGUMENTS-001 · v1.0 · Owner:** Cli maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/cli/src/arguments.rs`

## Required implementation behavior

Decode declared subcommand, workspace, required operands and version. Map count, revision and timeout to checked typed units; reject duplicate singleton options and unexpected fields. No network interaction while parsing.

## Acceptance

**ZIP-CLI-ARGUMENTS-T01.** Invalid scope and malformed numeric argument have deterministic usage diagnostics.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
