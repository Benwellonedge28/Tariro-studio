# Scheduler crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Use `scheduler.max_workspace_queue_items`, `scheduler.max_attempts`, `scheduler.job_deadline_ms` and `scheduler.retry_jitter_ms` within the assignment policy. A timed-out worker cannot publish after lease loss.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test stable ordering, starvation resistance, stale completion rejection and restart.
