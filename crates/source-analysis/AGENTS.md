# Source analysis crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Default 2 MiB per source file and 10 seconds per parse. Fallback is explicitly text-only. Treat grammar and repository input as untrusted.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test invalid UTF-8, parser fallback and deterministic changed-file reindexing.
