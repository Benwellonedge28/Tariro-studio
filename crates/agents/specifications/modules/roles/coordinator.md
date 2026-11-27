# Coordinator role

**ZIP-AGENTS-ROLES-COORDINATOR-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/roles/coordinator.rs`

## Required implementation behavior

Assemble bounded task graph and route conflicts; compare current expected version and record decisions. Does not speak for approval authority.

## Acceptance

**ZIP-AGENTS-ROLES-COORDINATOR-T01.** Disputed write remains blocked despite coordinator preference.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
