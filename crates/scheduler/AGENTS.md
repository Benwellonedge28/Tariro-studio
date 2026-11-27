# Scheduler crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Default 256 queued jobs per workspace, 3 attempts, per-job deadline and bounded jitter. A timed-out worker cannot publish after lease loss.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test stable ordering, starvation resistance, stale completion rejection and restart.
