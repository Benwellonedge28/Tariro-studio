# Debugging crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Default 5 attempts and 20 minutes. Redact logs before model input. Preserve partial failure evidence and confidence.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test nonreproducible failure, dependency outage and redaction.
