# Sdk crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- No bundled credentials or hidden fallback provider. Cap queue and returned body. Safe retry applies only to supported idempotent operations.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Contract tests against previous supported versions and offline transport.
