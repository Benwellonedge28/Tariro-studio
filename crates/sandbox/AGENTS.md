# Sandbox crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- No fallback to unconfined execution. Bound process count and output; verify cleanup. Platform must advertise only enforced controls.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test denied path/network and reliable descendant teardown on supported OS.
