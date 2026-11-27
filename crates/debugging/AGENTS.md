# Debugging crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Apply resolved `debugging.max_attempts` and `debugging.deadline_ms`; stop before the next attempt if either budget is exhausted. Redact logs before model input. Preserve partial failure evidence and confidence.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test nonreproducible failure, dependency outage and redaction.
