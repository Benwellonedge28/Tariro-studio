# Orchestration crate design

**Contract version** 1.0. Master design §27. Planned implementation.

## Responsibility and dependencies

Topologically schedule tasks, assign stable IDs and roles; isolate reviewer context; consolidate outcomes by task ID, preserve disputes and escalate unresolved choices.

First-party dependencies: [foundation](../foundation/DESIGN.md), [agents](../agents/DESIGN.md), [assignments](../assignments/DESIGN.md), [scheduler](../scheduler/DESIGN.md), [verification](../verification/DESIGN.md)

- [Orchestration](../../specifications/1100-orchestration/orchestration.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `compile_team(plan)`
- `dispatch_ready()`
- `resolve_conflict(conflict)`

Record families: ExecutionGraph, assignment-local roles, evidence and escalation record. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `ExecutionGraph { plan_digest, tasks, dependencies, conflict_keys, reviewers }`
- `Escalation { conflicting_tasks, evidence_refs, required_authority }`

- `compile_team(plan: AuthorizedPlan, roles: RoleCatalog) -> Result<ExecutionGraph>`

## Failure, safety and resource limits

One concurrent agent in personal documentation profile. Policy denies any approval by vote. Bound graph and replanning retries.

- `InvalidGraph`
- `NoEligibleAgent`
- `ConflictUnresolved`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/orchestration/src/
├── lib.rs
├── error.rs
├── orchestrator.rs
├── coordination.rs
├── team.rs
├── swarm.rs
├── delegation.rs
├── routing.rs
├── negotiation.rs
├── conflict_resolution.rs
├── consensus.rs
├── voting.rs
├── escalation.rs
├── execution_graph.rs
├── dependency_graph.rs
├── strategies/
│   ├── mod.rs
│   ├── sequential.rs
│   ├── parallel.rs
│   ├── hierarchical.rs
│   ├── collaborative.rs
│   ├── debate.rs
│   ├── independent_review.rs
│   └── adaptive.rs
└── supervision.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test two competing edits to one path, reviewer independence and deterministic replay.
