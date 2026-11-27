# Database reviewer role

**ZIP-AGENTS-ROLES-DATABASE-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/roles/database.rs`

## Required implementation behavior

Propose compatible schema/migration with staging, rollback and storage checks. Live changes need separate approval.

## Acceptance

**ZIP-AGENTS-ROLES-DATABASE-T01.** Irreversible migration without qualified restore plan blocks.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
