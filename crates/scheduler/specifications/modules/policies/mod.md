# Pure policy dispatch

**ZIP-SCHEDULER-POLICIES-MOD-001 · v1.1 · Owner:** Scheduler maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/scheduler/src/policies/mod.rs`

## Boundary and inputs

Bind a supported immutable policy edition to a validated configuration revision. Resolve a strategy using the declared profile and assignment requirements. An explicitly serial assignment takes the serial path. Advanced placement preferences are eligible only when policy and current capacity evidence support them. A missing or unknown policy yields typed denial.

## Behavior and failure handling

Use each policy to compute a bounded proposal from the same pinned input snapshot. Never bypass [priority and fairness](../fairness.md), dependency readiness, the job deadline, or current attempt ownership. A proposal carries its source and policy revisions and expires on incompatible changes. Queue, admission and runtime own their separate checks. This pure module creates no workload and writes no policy.

## Acceptance

**ZIP-SCHEDULER-POLICIES-MOD-T01.** Supply an unknown edition, an explicitly serial plan under a parallel profile, and stale proposal evidence. Verify denial, a serial proposal and refusal at the current claim gate respectively.
