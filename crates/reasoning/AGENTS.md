# Reasoning crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Bound iterations and proposal size. Proposals have no execution authority. Unsupported assertions remain unverified.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Use contradictory evidence and check abstention. Ensure hallucinated citation cannot become acceptance evidence.
