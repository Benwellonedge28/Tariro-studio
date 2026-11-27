# Compliance reviewer role

**ZIP-AGENTS-ROLES-COMPLIANCE-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/roles/compliance.rs`

## Required implementation behavior

Compare mandatory policy evidence to exact scope, record exceptions and owners. Missing evidence blocks the affected determination.

## Acceptance

**ZIP-AGENTS-ROLES-COMPLIANCE-T01.** A policy name alone does not establish compliance.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
