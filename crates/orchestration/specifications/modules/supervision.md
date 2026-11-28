# Coordination supervision

**ZIP-ORCHESTRATION-SUPERVISION-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/supervision.rs`

## Boundary and inputs

Track current orchestration ownership, assignment checkpoint and scheduler intent bindings for each active child. At resume load the exact plan and role revisions and reconcile outstanding submissions. Use the Scheduler and owning effect verifier for settlement. The supervisor does not reconstitute an old worker lease from an observation.

## Behavior and failure handling

Stop intake for affected work on revocation or incompatible plan change. Use the owning scheduler and runtime control path to fence or stop prior work. Preserve verified receipts, held resources and unresolved effects while trusted recovery runs. A stale result may inform authorized inspection but cannot advance graph progress. Only current scoped authority plus confirmed settlement allows fresh work. Bound outstanding observations and retries by the approved plan.

## Acceptance

**ZIP-ORCHESTRATION-SUPERVISION-T01.** Crash during an authorized remote child with an ambiguous response, then deliver an old-epoch result. Verify the old result cannot complete a node, occupancy and external obligations stay visible, and no second dispatch starts before settlement.
