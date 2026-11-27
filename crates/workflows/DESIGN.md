# Workflows crate design

**Contract version** 1.1 candidate. Master design §29. Planned implementation.

## Responsibility and dependencies

Parse strict versioned TOML, resolve step references, check graph and permissions, then lower to tasks. Evaluate side-effect-free conditions; node output binds to named immutable artifacts.

First-party dependencies: [foundation](../foundation/DESIGN.md), [assignments](../assignments/DESIGN.md), [governance](../governance/DESIGN.md), [scheduler](../scheduler/DESIGN.md)

- [Workflows](../../specifications/1300-workflows/workflows.md)

## API and data

[Compiler](specifications/modules/compiler.md) owns bounded lowering and the immutable plan seal. [Execution](specifications/modules/execution.md) owns workflow readiness and scoped scheduler handoff. [Checkpoint](specifications/modules/checkpoint.md) persists per-node evidence for restart. Assignments retains ownership of ordered unit checkpoints. Scheduler owns job attempts and retry accounting. Composition injects the workflow journal and capability adapters.

## Failure, safety and resource limits

Resolve `workflows.max_expanded_steps` and `workflows.max_nesting_depth` before expanding. Reject cycles and unbounded inputs. Guards are pure and their decisions durable. Reconcile unknown outcomes with their original identities. Compensation requires separate live authorization. See [typed errors](specifications/modules/error.md).

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/workflows/src/
├── lib.rs
├── error.rs
├── workflow.rs
├── definition.rs
├── parser.rs
├── compiler.rs
├── validation.rs
├── stage.rs
├── step.rs
├── condition.rs
├── dependency.rs
├── execution.rs
├── branching.rs
├── looping.rs
├── parallelism.rs
├── variables.rs
├── artifacts.rs
├── approval.rs
├── checkpoint.rs
├── retry.rs
├── compensation.rs
├── rollback.rs
├── versioning.rs
├── registry.rs
└── reporting.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Apply the [execution fixtures](../../contracts/acceptance/workflows/execution-fixtures.json) to cycle detection, guard replay, noncontiguous checkpoints and compensation after revoke. Qualify actual adapters independently.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. The execution slice is a candidate for independent review. Other modules retain their recorded maturity.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`workflow.rs`](specifications/modules/workflow.md)
- [`definition.rs`](specifications/modules/definition.md)
- [`parser.rs`](specifications/modules/parser.md)
- [`compiler.rs`](specifications/modules/compiler.md)
- [`validation.rs`](specifications/modules/validation.md)
- [`stage.rs`](specifications/modules/stage.md)
- [`step.rs`](specifications/modules/step.md)
- [`condition.rs`](specifications/modules/condition.md)
- [`dependency.rs`](specifications/modules/dependency.md)
- [`execution.rs`](specifications/modules/execution.md)
- [`branching.rs`](specifications/modules/branching.md)
- [`looping.rs`](specifications/modules/looping.md)
- [`parallelism.rs`](specifications/modules/parallelism.md)
- [`variables.rs`](specifications/modules/variables.md)
- [`artifacts.rs`](specifications/modules/artifacts.md)
- [`approval.rs`](specifications/modules/approval.md)
- [`checkpoint.rs`](specifications/modules/checkpoint.md)
- [`retry.rs`](specifications/modules/retry.md)
- [`compensation.rs`](specifications/modules/compensation.md)
- [`rollback.rs`](specifications/modules/rollback.md)
- [`versioning.rs`](specifications/modules/versioning.md)
- [`registry.rs`](specifications/modules/registry.md)
- [`reporting.rs`](specifications/modules/reporting.md)
