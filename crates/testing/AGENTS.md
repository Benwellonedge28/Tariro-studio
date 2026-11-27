# Testing crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- No success for missing/empty expected reports. Retry flakes only under policy, preserving failed attempts. Coverage is separate from correctness.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test malformed reports, skipped and timeout distinctions, and flake history.
