# Agents crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Use `agents.max_mailbox_items` and `agents.max_delegation_depth`, tightened by scope and admitted memory. Stop dispatch on revoke or exhaustion. Model identity never conveys a role.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test shared model isolated context and agent blocked from self-elevation.
