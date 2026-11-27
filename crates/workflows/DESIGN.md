# Workflows crate design

**Contract version** 1.0. Master design §29. Planned implementation.

## Responsibility and dependencies

Parse strict versioned TOML, resolve step references, check graph and permissions, then lower to tasks. Evaluate side-effect-free conditions; node output binds to named immutable artifacts.

First-party dependencies: [foundation](../foundation/DESIGN.md), [assignments](../assignments/DESIGN.md), [governance](../governance/DESIGN.md), [scheduler](../scheduler/DESIGN.md)

- [Workflows](../../specifications/1300-workflows/workflows.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `compile(definition)`
- `start(compiled)`
- `replay(checkpoint)`

Record families: WorkflowDefinition, compiled graph, condition AST, execution cursor and artifact bindings. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `WorkflowDefinition { schema_version, workflow_id, revision, inputs, steps, limits }`
- `CompiledGraph { plan_digest, nodes, dependency_order, bindings }`

- `compile(definition: WorkflowDefinition, registry: CapabilitySnapshot) -> Result<CompiledGraph>`

## Failure, safety and resource limits

Enforce `workflows.max_expanded_steps` and `workflows.max_nesting_depth` during expansion before scheduling. Loops carry a static bound. Compensation is an independently authorized operation.

- `InvalidDefinition`
- `Cycle`
- `UnboundedLoop`
- `MissingInput`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

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

Test cyclic graph, deterministic branching, checkpoint replay and compensation denied after revoke.
