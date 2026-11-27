# Context crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Never silently truncate mandatory policy. Exclude secret-bearing content and out-of-scope items. Record omission counts without content.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test prompt-like repository text, stable rank ties, token hard ceiling and no cross-scope retrieval.
