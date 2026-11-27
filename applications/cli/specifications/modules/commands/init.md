# Local initialization request

**ZIP-CLI-COMMANDS-INIT-001 · v1.0 · Owner:** Cli maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/cli/src/commands/init.rs`

## Required implementation behavior

Select local profile and data root explicitly. Check readiness and stage atomic creation; repeated identical init returns existing initialized state. Incompatible existing content is a conflict.

## Acceptance

**ZIP-CLI-COMMANDS-INIT-T01.** Interrupted creation yields prior or complete generation; no hidden remote access.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
