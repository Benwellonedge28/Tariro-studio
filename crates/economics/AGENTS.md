# Economics crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- No money transfers. Budget amount zero disables spend. Undocumented or ambiguous rates require owner policy. Reconciliation cannot silently erase cost.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Concurrent requests cannot overspend. Test rounding and interrupted provider receipt.
