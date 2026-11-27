# Knowledge crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Stop traversal at the resolved `knowledge.max_traversal_depth` and `knowledge.max_results` or the admitted execution budget, whichever is exhausted first. Unknown edges remain uncertain, with provenance.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Reindex changed files, prove stale edges disappear and graph traversal cannot leak private nodes.
