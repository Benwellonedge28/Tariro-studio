# Operations planner role

**ZIP-AGENTS-ROLES-DEVOPS-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/roles/devops.rs`

## Required implementation behavior

Propose scoped build/deploy plan and evidence gates. Production effects require separately authenticated owner authority.

## Acceptance

**ZIP-AGENTS-ROLES-DEVOPS-T01.** A passing build cannot activate deployment.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
