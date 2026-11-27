# Intelligence crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Budget tokens before dispatch and release reservation on terminal outcome. No automatic remote downgrade or escalation. Partial text remains partial after failed streams.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test offline routing, strict provider policies, chunk sequencing and partial stream interruption.
