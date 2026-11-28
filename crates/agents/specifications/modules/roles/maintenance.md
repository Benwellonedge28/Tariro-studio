# Maintenance planner role

**ZIP-AGENTS-ROLES-MAINTENANCE-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/roles/maintenance.rs`

## Boundary and inputs

Propose bounded retention, rotation, cleanup or dependency changes against exact asset identity and current usage evidence. Use the owning maintenance and storage inventories to identify state, active references, retention rules and rollback dependencies. Keep estimates distinct from verified reclamation.

## Behavior and failure handling

Exclude active, pinned or retained artifacts. Require explicit delegated effect authority for deletion or mutation, then check the reference and policy revision at the owning boundary. Lost deletion response preserves an unresolved intent rather than reissuing. A policy conflict stops the proposed maintenance operation.

## Acceptance

**ZIP-AGENTS-ROLES-MAINTENANCE-T01.** Mark an artifact pinned after proposal but before execution and verify it is preserved. List separately an eligible unpinned candidate with no deletion authority and verify no artifact is removed.
