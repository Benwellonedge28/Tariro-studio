# Serial execution strategy

**ZIP-ORCHESTRATION-STRATEGIES-SEQUENTIAL-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/strategies/sequential.rs`

## Boundary and inputs

Select a single eligible task by canonical plan order within the explicit serial scope. Count a pending scheduler submission, active task and unresolved cleanup as occupying the scope. Check the durable snapshot before proposing and keep its expected revision attached to the proposal.

## Behavior and failure handling

When no attempt occupies the scope, propose the first eligible task under current role and dependency constraints. Apply through the owning assignment and Scheduler transition. A task cancellation or lost reply cannot clear the scope in the absence of verified settlement. A repeated proposal reuses its original intent or observes the stored decision.

## Acceptance

**ZIP-ORCHESTRATION-STRATEGIES-SEQUENTIAL-T01.** Retain an earlier child with unresolved ownership and offer another ready task. Verify no successor proposal. Settle the previous child, replay the round and verify the same single successor is selected for every permitted input ordering.
