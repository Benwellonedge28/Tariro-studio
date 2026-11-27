# Workflow compilation and replay

**Contract version** 1.0. Master design §71.

## Contract

A definition contains schema_version, workflow_id, inputs, typed steps, dependencies, guards, limits and output bindings. Each step declares an adapter capability/version and effect class. Normalize and hash the plan before start.

## Execution and integration

Use a stable topological order, bounded iteration, side-effect-free guards and typed artifact references. On replay use stored inputs and compiler version. Changed plan requires a new plan revision and authorization if its scope expands.

## Verification

Validate a malformed graph, unbounded loop and missing artifact reference. Prove replay never silently invokes compensated or expired operations.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).

## Workflow schema v1

A strict TOML definition uses `schema_version=1`, `workflow_id`, `limits` and ordered `[[steps]]` entries. A step has a unique ID, `uses` capability/version, `needs` IDs, `inputs`, `outputs`, optional `when`, resource limits and effect class. The condition subset permits literals, named inputs, comparisons and Boolean operators. Reject cyclic graphs, unknown functions, forward references not in dependencies and unbounded loops. A failed required prerequisite makes dependents Blocked. Parallel steps touching the same normalized file have an exclusive conflict key.

## Implementing components

- [workflows crate design](../../crates/workflows/DESIGN.md)
- [assignments crate design](../../crates/assignments/DESIGN.md)
