# Scheduler

This crate's design covers job DAG, ReadyKey, attempt, fencing epoch and lease.

- [Implementation design](DESIGN.md)
- [Crate contributor instructions](AGENTS.md)
- [Runtime](../../specifications/0200-runtime/runtime.md)
- [Orchestration](../../specifications/1100-orchestration/orchestration.md)
- [Distributed](../../specifications/2700-distributed/distributed.md)

Acceptance fixture: Test stable ordering, starvation resistance, stale completion rejection and restart.
