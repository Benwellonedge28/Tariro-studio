# Capability diagnostics request

**ZIP-CLI-COMMANDS-DOCTOR-001 · v1.0 · Owner:** Cli maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/cli/src/commands/doctor.rs`

## Required implementation behavior

Query read-only schema, hardware, storage, isolation and listener state. Report unavailable controls separately from failures and preserve observed revisions.

## Acceptance

**ZIP-CLI-COMMANDS-DOCTOR-T01.** Optional backend unavailable does not imply core readiness if required isolation is missing.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
