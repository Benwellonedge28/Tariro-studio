# Assignments crate design

**Contract version** 1.0. Master design §28. Planned implementation.

## Responsibility and dependencies

Use revision-checked transition plus outbox. Checkpoint each verified work unit. Freeze the plan, evidence and exact touched paths before publishing. Reconcile unknown remote outcome before retry.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md), [events](../events/DESIGN.md), [governance](../governance/DESIGN.md), [verification](../verification/DESIGN.md)

- [Assignments](../../specifications/1200-assignments/assignments.md)
- [Workflows](../../specifications/1300-workflows/workflows.md)
- [Documentation](../../specifications/1700-documentation/documentation.md)
- [Acceptance](../../specifications/3600-acceptance/acceptance.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `submit(spec)`
- `transition(id, revision, command)`
- `record_unit()`
- `reconcile()`

Record families: AssignmentV1, Task, Checkpoint, Evidence, ExternalOperation and batch record. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `AssignmentRecord { id, workspace_id, repository_id, base_revision, grant_ref, plan_ref, state, state_revision, checkpoint_refs, evidence_refs, effects }`
- `TransitionCommand { command_id, expected_revision, action }`

- `transition(id: AssignmentId, command: TransitionCommand) -> Result<TransitionReceipt>`

## Failure, safety and resource limits

Exact 30 for Vimbai fixture; short batches await owner revision. Resume revalidates authorization, policy, snapshot and artifacts. Never finish with missing evidence.

- `StaleRevision`
- `InvalidTransition`
- `AwaitingApproval`
- `EvidenceIncomplete`
- `UnknownRemoteOutcome`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

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

Crash after unit 17 and resume at 18. Deny file 31. Reconcile push and PR ambiguity without duplicate mutation.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

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
