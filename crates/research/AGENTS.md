# Research crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- No network in offline mode. Limit URL schemes, hosts, redirects, byte count and excerpt duplication. Protect private query content.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test dead source, conflicting citations and forbidden destination.
