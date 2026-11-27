# Repository crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- No inherited or unscoped credentials. No force push or merge under generic write grants. Bound Git command output and disable hooks and shared mutable configuration.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test nested instructions, deleted or renamed paths, concurrent base change and duplicate PR reconciliation.
