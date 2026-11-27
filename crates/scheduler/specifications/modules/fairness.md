# Eligible workspace fairness

**ZIP-SCHEDULER-FAIRNESS-001 · v1.1 candidate · Owner** Scheduler maintainers

**Planned source** `crates/scheduler/src/fairness.rs`

Order by approved priority descending, then workspace's last successful dispatch ordinal in that class ascending, then job enqueue ordinal ascending, then assignment and task UUID bytes ascending. A workspace that has yet to dispatch in a class sorts before one that has. Enqueue and dispatch ordinals come from durable checked counters, independent of wall clock and input map order. Priority belongs to verified policy. Claims cannot modify it.

Advance the workspace's class cursor only when the scheduler commits Dispatched. Apply selection and cursor updates against the same observed generation, and reconcile a losing reservation instead of advancing a stale cursor. Capacity denial does not spend a turn. Use the queue's bounded and advancing continuation to evaluate remaining candidates. Under continuously eligible equal-priority demand, with capacity recurring and a fixed competing set of workspaces, each workspace gets a turn before a previously served peer gets another. Strict higher-priority demand can postpone lower classes under this policy. A deployment needing a cross-class service guarantee must supply an approved scheduling policy and dedicated tests for it.

**ZIP-SCHEDULER-FAIRNESS-T01.** Permute an equal-priority snapshot for workspaces A and B, then admit four successive fitting jobs. Both permutations give the same order, workspaces alternate, and a restart between claims preserves the next turn.
