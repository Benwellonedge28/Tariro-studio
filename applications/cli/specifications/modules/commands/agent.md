# Agent command adapter

**ZIP-CLI-COMMANDS-AGENT-001 · v1.0 · Owner:** Cli maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/cli/src/commands/agent.rs`

## Required implementation behavior

List and inspect through scoped read DTOs. Configure takes a bounded manifest and expected revision, and does not grant a new capability through role labels.

## Acceptance

**ZIP-CLI-COMMANDS-AGENT-T01.** Unauthorized agent or capability request receives typed denial.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
