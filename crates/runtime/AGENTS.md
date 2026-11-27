# Runtime crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Use the resolved `runtime.stop_grace_ms` clipped to the applicable deadline, then terminate the contained process tree and verify exit. Escalate unreaped work and keep its lease.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Crash on both sides of spawn and checkpoint, verify no orphan and no duplicate effects.
