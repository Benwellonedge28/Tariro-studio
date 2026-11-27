# Plugins crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- No unrestricted native dynamic loading. Memory/fuel and registry quotas required. Fail closed on unavailable sandbox or incompatible interface.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test denied imports, timeout termination, revocation and upgrade rollback.
