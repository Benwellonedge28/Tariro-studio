# Storage crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Maximum record 1 MiB and 512 operations per transaction by default. Check free space before staging. Never publish metadata for a missing object.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Crash before and after metadata commit, test duplicate object insertion and full backup restoration.
