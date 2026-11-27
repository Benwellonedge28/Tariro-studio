# Search crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Apply `search.max_results` and use an opaque generation-bound cursor; keep incompatible embedding dimensions in separate indexes. Private indexes inherit source retention.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Check index restart, stable ranking and permission filtered snippets.
