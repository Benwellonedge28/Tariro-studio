# Workflow compilation and replay

**Contract version** 1.1 candidate. Master design §§29 and 71.

Parse a strict versioned definition into a bounded immutable graph. Validate typed inputs, adapter capability versions, effects, approved ceiling references and edges. Check expansion before constructing executable nodes. Compile deterministic graph order and seal semantic plan, source provenance and bound capability revisions. Live governance and scheduler admission govern execution.

## Definition and execution

A strict TOML definition uses `schema_version=1`, `workflow_id`, `limits` and `[[steps]]` entries. Leaves declare unique ID, `uses` capability/version, `needs` IDs, typed `inputs` and `outputs`, effect class and optional `when` guard. Hierarchical scopes normalize to the same typed step model, with explicit entry/exit bindings. Static repeat counts are positive and reviewed. Unknown attributes, unbounded iterations, cycles, unresolved names and unsupported effects deny compilation. Wire encoding of nested scopes, fully typed bindings and capability fields must be qualified against golden definitions before independent approval.

All dependencies are required by default. An explicit allow-skipped edge requires optional bindings. Evaluate pure guards over stored immutable inputs and persist the decision before dispatch. Enforce independent ready nodes' exclusive conflict keys and resource scope. Maintain per-node checkpoints even when execution completes out of order. The runtime and scheduler provide attempt ownership and journals. Workflows verifies semantic results and the assignment layer separately owns ordered verified units and publication.

A restart reuses the immutable plan and validated checkpoints. Unknown operations block their affected successors until reconciliation. Retry uses the existing scheduler job identity and live bounds. A rollback or compensation requires its own authority and preserves the original effects. Apply the [execution fixtures](../../contracts/acceptance/workflows/execution-fixtures.json), including cycles, branching, checkpoints and revoked compensation. Bind evidence to [release requirements](../../REQUIREMENTS.md).

## Implementing components

- [Workflows](../../crates/workflows/DESIGN.md)
- [Assignments](../../crates/assignments/DESIGN.md)
- [Scheduler](../../crates/scheduler/DESIGN.md)
