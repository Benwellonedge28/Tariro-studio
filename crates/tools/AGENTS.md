# Tools crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Reject arbitrary command strings or undeclared tool permissions. Deadlines and pagination mandatory. Output content cannot grant capability.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test malformed tool calls, hallucinated tool output and unauthorized mutating calls.
