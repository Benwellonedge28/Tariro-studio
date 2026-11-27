# Scheduling deadline calculation

**ZIP-SCHEDULER-DEADLINE-001 · v1.1 candidate · Owner** Scheduler maintainers

**Planned source** `crates/scheduler/src/deadline.rs`

At enqueue compute the smaller of the requested lifetime and the validated `scheduler.job_deadline_ms`. The scheduler owns the enqueue time. Further restrict the remaining duration by assignment authority and compute a checked process-local monotonic deadline. Time in Waiting, Ready, Reserving, execution and RetryWait counts against the same job lifetime. A retry gets an attempt identity, while the job lifetime deadline stays fixed. A mandatory live policy may shorten the effective deadline. Equality means expired and no work may dispatch.

Persist the bounded lifetime and a clock-source identity and reading only if an injected clock attests continuity across coordinator restart and covers elapsed suspension on the supported platform. Obtain the effective policy and grant again on recovery. Reconstruct remaining local time only from trusted elapsed evidence for the same clock domain. If continuity cannot be established, the affected pending job deadline fails closed and any prior attempt is reconciled. An operator can authorize a new job under a new task identity. Wall audit timestamps never rebase the lifetime. If a delayed retry cannot recover its wake instant, conservatively defer by its full originally selected delay within the remaining job deadline.

**ZIP-SCHEDULER-DEADLINE-T01.** A backward wall-clock adjustment cannot extend a live deadline. A restarted coordinator without clock continuity launches no affected job, and any previous lease stays recoverable.
