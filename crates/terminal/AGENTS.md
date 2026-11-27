# Terminal crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- No shell by default. Interactive shell requires user intent and sandbox. Default 1 MiB combined output and 60 seconds for generic task tools.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test shell metacharacters as literal argv, child processes and output flooding.
