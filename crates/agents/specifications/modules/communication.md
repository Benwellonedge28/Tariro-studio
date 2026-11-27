# Scoped agent message routing

**ZIP-AGENTS-COMMUNICATION-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/communication.rs`

## Required implementation behavior

Validate sender, intended recipient and task/assignment scope. Label content as untrusted evidence or proposal; enforce byte and deadline limits.

## Acceptance

**ZIP-AGENTS-COMMUNICATION-T01.** A message that claims owner permission cannot trigger external mutation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
