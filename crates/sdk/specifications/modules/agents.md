# Scoped agent client

**ZIP-SDK-AGENTS-001 · v1.0 · Owner:** Sdk maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sdk/src/agents.rs`

## Required implementation behavior

Provide approved list/inspect/commands with assignment, actor and grant metadata; no role-based automatic escalation.

## Acceptance

**ZIP-SDK-AGENTS-T01.** Different assignment ID yields denial.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
