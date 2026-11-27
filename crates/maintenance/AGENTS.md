# Maintenance crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- No automatic destructive cleanup by default. Keep backups required by retention. Pause on active database migration or low disk.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Restore after interrupted update and verify artifact retention.
