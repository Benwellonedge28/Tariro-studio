# Networking crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Default deny in offline profiles. No implicit proxy or credential forwarding across origins. Set the effective deadline using `networking.request_deadline_ms` and the remaining operation deadline.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test redirect to denied destination, offline no DNS and truncated body handling.
