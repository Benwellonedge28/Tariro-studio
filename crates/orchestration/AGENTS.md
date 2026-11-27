# Orchestration crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- One concurrent agent in personal documentation profile. Policy denies any approval by vote. Bound graph and replanning retries.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test two competing edits to one path, reviewer independence and deterministic replay.
