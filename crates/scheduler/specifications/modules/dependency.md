# Dependency resolution

**ZIP-SCHEDULER-DEPENDENCY-001 · v1.1 · Owner:** Scheduler maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/scheduler/src/dependency.rs`

## Boundary and inputs

Use the immutable prerequisite keys and plan binding defined by [job](job.md). Before writing, verify scope, reject duplicate or self edges and require each prerequisite to exist in the same authorized assignment. Walk the bounded graph in canonical key order and reject a cycle before committing the new specification. The queue never trusts user-reported prerequisite status.

## Behavior and failure handling

Read prerequisite states and trusted receipt references at one journal snapshot. A job is Ready only when all required receipts prove success under the expected plan binding. Missing evidence leaves the job waiting, while verified terminal failure blocks it. Use the journal's reverse index to propagate in bounded stable order. Compare job and dependency revisions when committing readiness. If a dependency is invalidated after a claim, apply the existing fencing and recovery path. Never overwrite committed effects.

## Acceptance

**ZIP-SCHEDULER-DEPENDENCY-T01.** Submit a cycle and a foreign dependency and verify zero writes. Then force one independent prerequisite to fail. Its descendants become blocked without resource requests. Race a stale successful snapshot with dependency failure and assert no dispatch accepted from the stale snapshot.
