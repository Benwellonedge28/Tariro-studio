# Deployment crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- No automatic production release from compilation. Reconcile ambiguous remote stage. Roll back only to compatible verified state.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test package substitution, partial rollout and failed health verification.
