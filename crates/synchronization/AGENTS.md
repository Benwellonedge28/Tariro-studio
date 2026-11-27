# Synchronization crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Bound batch bytes and artifact size. Unknown schema quarantined. Resume from last applied cursor and dedupe repeated chunks.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Drop connection mid-transfer, resume, preserve divergent histories.
