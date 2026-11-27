# Workflow command adapter

**ZIP-CLI-COMMANDS-WORKFLOW-001 · v1.0 · Owner:** Cli maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/cli/src/commands/workflow.rs`

## Required implementation behavior

Validate or pin a strict definition before run; provide immutable execution ID for replay. Unknown effects never replay blindly.

## Acceptance

**ZIP-CLI-COMMANDS-WORKFLOW-T01.** Malformed graph produces validation error and no external effects.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
