# Dynamic proposal group

**ZIP-ORCHESTRATION-SWARM-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/swarm.rs`

## Boundary and inputs

Operate a bounded dynamic group under one authorized plan revision. Admit each admitted participant's scoped identity, role, task and distinct scheduler attempt under the effective agent cap. Track pending submissions, active attempts and unsettled cleanup in the occupied envelope to prevent oversubscription under retries.

## Behavior and failure handling

Select participants in stable canonical order among qualified candidates and persist the membership intent through Assignments before dispatch. Aggregate typed evidence and retain disagreement, without creating decision authority. A participant departure frees capacity only after confirmed handoff or settlement at the owning boundary. No participant inherits broader role, provider or communication permission from the group.

## Acceptance

**ZIP-ORCHESTRATION-SWARM-T01.** Race concurrent joins at the final admitted slot, then lose the accepted join reply. Recover the original membership and see one occupied slot. Hold a departing attempt unresolved and verify capacity does not expand.
