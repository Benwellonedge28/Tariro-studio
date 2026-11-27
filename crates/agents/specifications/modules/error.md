# Agent failure vocabulary

**ZIP-AGENTS-ERROR-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/error.rs`

## Required implementation behavior

Distinguish denied permission, invalid role, mailbox full, lease lost, cancelled, unsupported model and uncertain effect. Preserve safe IDs only.

## Acceptance

**ZIP-AGENTS-ERROR-T01.** Mailbox exhaustion is not reported as successful delegation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
