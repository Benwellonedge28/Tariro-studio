# Source analysis crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Charge input bytes and elapsed time against the admitted `source_analysis.max_source_bytes` and `source_analysis.max_parse_ms`. Fallback is explicitly text-only. Treat grammar and repository input as untrusted.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test invalid UTF-8, parser fallback and deterministic changed-file reindexing.
