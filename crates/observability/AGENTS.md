# Observability crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Default local. Cap series cardinality and trace queue. Dropped debug telemetry is counted and cannot substitute for audit.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test disabled external export sends no network traffic and redaction canary stays absent.
