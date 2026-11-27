# Distributed crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Remote execution opt-in. Expired or fenced workers cannot promote results. Keep state at owner node and bound retries per task.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test stale worker receipt, unexpected node capability and network partitions.
