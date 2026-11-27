# Maintenance planner role

**ZIP-AGENTS-ROLES-MAINTENANCE-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/roles/maintenance.rs`

## Required implementation behavior

Propose bounded rotation, cleanup or dependency work with rollback and retention evidence. No implicit destructive authority.

## Acceptance

**ZIP-AGENTS-ROLES-MAINTENANCE-T01.** Pinned artifact excluded from recommended cleanup.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
