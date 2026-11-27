# Workflows crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Enforce `workflows.max_expanded_steps` and `workflows.max_nesting_depth` during expansion before scheduling. Loops carry a static bound. Compensation is an independently authorized operation.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test cyclic graph, deterministic branching, checkpoint replay and compensation denied after revoke.
