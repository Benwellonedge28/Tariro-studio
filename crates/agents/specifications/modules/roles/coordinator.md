# Coordinator role

**ZIP-AGENTS-ROLES-COORDINATOR-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/roles/coordinator.rs`

## Boundary and inputs

Propose a bounded assignment-local task graph using pinned inputs, stable task identities, role eligibility and known conflict keys. Bind the expected plan revision and route specialized decisions to the Orchestration owner. Scope all coordination observations to the authorized audience.

## Behavior and failure handling

Use [coordination](../../../../orchestration/specifications/modules/coordination.md) for deterministic ordering and preserve unresolved conflicts. A coordinator's preference cannot unblock contested writes, grant permissions or replace required independent review. Changed inputs require revision comparison before applying a new proposal.

## Acceptance

**ZIP-AGENTS-ROLES-COORDINATOR-T01.** Permute a ready-set input, then deliver rival proposals for one path. Verify stable scheduling suggestions and both conflicts remain unsettled without the owning approval.
