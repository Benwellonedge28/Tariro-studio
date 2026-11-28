# Admitted parallel placement

**ZIP-SCHEDULER-POLICIES-PARALLEL-001 · v1.1 · Owner:** Scheduler maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/scheduler/src/policies/parallel.rs`

## Boundary and inputs

Return a bounded ordered list of ready candidates from the Scheduler fairness snapshot. Respect the resolved queue and worker envelope for the installation and assignment. Filter write conflicts using conflict identities supplied by the owning planner. Candidates with unknown write scope remain ineligible for parallel overlap until that scope is established.

## Behavior and failure handling

Choose fitting candidates in priority and fairness order, skipping capacity-deferred and conflicting work while maintaining a bounded advancing scan. Acquire a distinct admitted lease through the Scheduler for each selected attempt. A proposed list never authorizes concurrent write execution. Claims must bind the owning conflict verifier so two claimants cannot both launch competing writes. An active or recovering write stays conflicting while its scope is unsettled.

## Acceptance

**ZIP-SCHEDULER-POLICIES-PARALLEL-T01.** Propose three ready tasks where two share the same write scope. Verify the independent task can proceed with one writer under sufficient leases. Hold the first writer in recovery and ensure the conflicting candidate remains deferred.
