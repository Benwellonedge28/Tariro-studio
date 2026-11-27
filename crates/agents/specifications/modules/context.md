# Agent context assembly boundary

**ZIP-AGENTS-CONTEXT-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/context.rs`

## Required implementation behavior

Request assignment-local context with explicit scopes and resource budget. Do not include actor credentials or unrelated agent data.

## Acceptance

**ZIP-AGENTS-CONTEXT-T01.** Two roles sharing a model cannot read each other’s private context.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
