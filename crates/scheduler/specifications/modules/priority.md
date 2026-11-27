# Permitted priority and stable order

**ZIP-SCHEDULER-PRIORITY-001 · v1.1 candidate · Owner** Scheduler maintainers

**Planned source** `crates/scheduler/src/priority.rs`

The verified request supplies a permitted priority class encoded as a `u16`. Larger class values sort first. The configured policy defines permitted classes and who may assign them. The scheduler validates the requested class before insertion, persists it with the immutable job and checks whether it is still permitted before dispatch. A class that policy no longer permits cannot dispatch. Neither a worker claim nor age promotes a job to a higher class.

After comparing class, delegate comparison to [fairness](fairness.md). The total ordering compares the workspace's class cursor before the job enqueue ordinal and UUID bytes. Do not consult wall-clock timestamps or input insertion order. Define equal keys only when both job identity and the observed ordering inputs match.

**ZIP-SCHEDULER-PRIORITY-T01.** Permute equal-priority candidates and verify a stable order. A job may have an older enqueue ordinal and still follow a job in the same class whose workspace has waited longer for service.
