# Agents crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Bound mailbox to 128 and delegation depth to 4. Stop dispatch on revoke or exhaustion. Model identity never conveys a role.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test shared model isolated context and agent blocked from self-elevation.
