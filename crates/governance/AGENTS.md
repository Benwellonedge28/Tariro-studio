# Governance crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Human approval required for separately privileged operations regardless of agent vote. Stop is durable and blocks new effects; grant never auto-expands.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test missing attributes, grant expiry during execution, and policy change before external write.
