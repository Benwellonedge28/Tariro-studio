# Terminal crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- No shell by default. Interactive shell requires user intent and sandbox. Bound combined standard streams and execution with `terminal.max_output_bytes` and `terminal.deadline_ms` under the admitted task lease.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test shell metacharacters as literal argv, child processes and output flooding.
