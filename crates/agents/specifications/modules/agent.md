# Agent instance identity

**ZIP-AGENTS-AGENT-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/agent.rs`

## Required implementation behavior

Bind agent # to workspace, assignment, reviewed manifest and principal epoch. Keep model route separate from agent authority.

## Acceptance

**ZIP-AGENTS-AGENT-T01.** Shared model cannot imply shared identity.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
