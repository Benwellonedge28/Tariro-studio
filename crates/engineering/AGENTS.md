# Engineering crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Cap patch paths and bytes to grant limits. Privileged changes require narrower operation authority. No publication on verification failure.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test conflicting edits, out-of-scope files and evidence invalidation after changes.
