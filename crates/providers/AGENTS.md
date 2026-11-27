# Providers crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Adapters opt in. No implicit online fallback. Rate limits and health status separate from capability. Retain native upstream error class with redaction.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test unavailable provider, feature negotiation and token omission.
