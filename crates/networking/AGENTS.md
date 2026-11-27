# Networking crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Default deny in offline profiles. No implicit proxy or credential forwarding across origins. Timeout after 15 seconds by default.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test redirect to denied destination, offline no DNS and truncated body handling.
