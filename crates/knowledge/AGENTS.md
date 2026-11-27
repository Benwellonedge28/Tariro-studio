# Knowledge crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Bound traversal depth to 8 and result size to 1,000 by default. Unknown edges remain uncertain, with provenance.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Reindex changed files, prove stale edges disappear and graph traversal cannot leak private nodes.
