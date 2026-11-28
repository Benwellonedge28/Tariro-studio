# Explicit write conflict handling

**ZIP-ORCHESTRATION-CONFLICT-RESOLUTION-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/conflict_resolution.rs`

## Boundary and inputs

Compare two proposed writes using the planner's canonical workspace and path or record identities, exact candidate digests and expected revision. Treat overlapping or unresolved write scopes as conflicting. Preserve each independently verified proposal and its evidence even if both were valid against the same old snapshot.

## Behavior and failure handling

Before an allowed write, acquire the owning conflict guard and compare the current revision. Serialize authorized work with compatible preconditions and send incompatible proposals to the authorized decision owner. A selected or composed candidate must be resealed and verified against its actual preimage, with fresh authority where scope changes. Keep the losing proposal visible but unable to publish. A lost write response requires reconciliation by the original effect identity.

## Acceptance

**ZIP-ORCHESTRATION-CONFLICT-RESOLUTION-T01.** Race two proposals for the same path from an identical base. Only a revision-matching candidate can cross the write gate. Verify the other proposal remains available for an authorized decision and its old evidence cannot validate a rebased candidate.
