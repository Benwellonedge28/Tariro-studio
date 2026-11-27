# Identity crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Never persist bearer secrets in identity tables. Expired sessions and removed memberships fail closed. Session credentials are audience-bound.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test cross-workspace access, logout races and revocation persistence.
