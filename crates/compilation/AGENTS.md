# Compilation crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Network off by default. Cache identity includes tree, toolchain, target, features and relevant environment. Never reuse a failed or partial build.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Change target or compiler and verify cache miss. Failed compiler exit cannot produce success.
