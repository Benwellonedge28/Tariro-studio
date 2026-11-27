# Memory crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Default ephemeral assignment memory unless persistence is enabled by policy. Enforce retention and per-scope quota. Never share across scope by default.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test cross-tenant isolation, expired retrieval and crash during purge.
