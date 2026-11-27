# Assignments crate design

**Contract version** 1.1 candidate. Master design §28. Planned implementation.

## Responsibility and dependencies

Use revision-checked transition plus outbox. Checkpoint each verified work unit. Freeze the plan, evidence and exact touched paths before publishing. Reconcile unknown remote outcome before retry.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md), [events](../events/DESIGN.md), [governance](../governance/DESIGN.md), [verification](../verification/DESIGN.md)

- [Assignments](../../specifications/1200-assignments/assignments.md)
- [Workflows](../../specifications/1300-workflows/workflows.md)
- [Documentation](../../specifications/1700-documentation/documentation.md)
- [Acceptance](../../specifications/3600-acceptance/acceptance.md)

## API and data

[Transition commands](specifications/modules/transitions.md) bind assignment identity, expected revision and stable command ID. The [assignment lifecycle](../../specifications/1200-assignments/assignments.md) owns valid transitions. [Checkpoint](specifications/modules/checkpoint.md) commits a verified plan unit and evidence in the same Storage transaction as revision and Events outbox. [Recovery](specifications/modules/recovery.md) inspects exact prior effects before rescheduling or publication. Composition injects runtime, scheduler and repository boundaries behind scoped ports.

## Failure, safety and resource limits

Derive exact file count and operational bounds from the current grant and validated policy. Enforce the 30-file reference Vimbai agreement where applicable. Short batches await explicit owner revision. Resume revalidates authority, pinned sources, plan and evidence. Cancellation and pause fence the worker and settle existing operations before an outcome. Never report completion without matching receipts and verified evidence. See [typed errors](specifications/modules/error.md).

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/assignments/src/
├── lib.rs
├── error.rs
├── assignment.rs
├── identifier.rs
├── specification.rs
├── requirements.rs
├── scope.rs
├── authorization.rs
├── plan.rs
├── task.rs
├── subtask.rs
├── dependency.rs
├── milestone.rs
├── progress.rs
├── state.rs
├── transitions.rs
├── persistence.rs
├── checkpoint.rs
├── recovery.rs
├── cancellation.rs
├── pause.rs
├── resume.rs
├── batching.rs
├── acceptance.rs
├── evidence.rs
├── result.rs
└── reporting.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Apply the [lifecycle fixtures](../../contracts/acceptance/assignments/lifecycle-fixtures.json) to the 17/18 restart boundary, exact batch rules and provider request reconciliation. Qualify real adapter fault behavior and independent review separately.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. The lifecycle slice is a candidate for independent review. Other modules retain their recorded maturity.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`assignment.rs`](specifications/modules/assignment.md)
- [`identifier.rs`](specifications/modules/identifier.md)
- [`specification.rs`](specifications/modules/specification.md)
- [`requirements.rs`](specifications/modules/requirements.md)
- [`scope.rs`](specifications/modules/scope.md)
- [`authorization.rs`](specifications/modules/authorization.md)
- [`plan.rs`](specifications/modules/plan.md)
- [`task.rs`](specifications/modules/task.md)
- [`subtask.rs`](specifications/modules/subtask.md)
- [`dependency.rs`](specifications/modules/dependency.md)
- [`milestone.rs`](specifications/modules/milestone.md)
- [`progress.rs`](specifications/modules/progress.md)
- [`state.rs`](specifications/modules/state.md)
- [`transitions.rs`](specifications/modules/transitions.md)
- [`persistence.rs`](specifications/modules/persistence.md)
- [`checkpoint.rs`](specifications/modules/checkpoint.md)
- [`recovery.rs`](specifications/modules/recovery.md)
- [`cancellation.rs`](specifications/modules/cancellation.md)
- [`pause.rs`](specifications/modules/pause.md)
- [`resume.rs`](specifications/modules/resume.md)
- [`batching.rs`](specifications/modules/batching.md)
- [`acceptance.rs`](specifications/modules/acceptance.md)
- [`evidence.rs`](specifications/modules/evidence.md)
- [`result.rs`](specifications/modules/result.md)
- [`reporting.rs`](specifications/modules/reporting.md)
