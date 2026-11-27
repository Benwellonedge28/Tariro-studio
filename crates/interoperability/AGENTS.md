# Interoperability crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Reject unknown majors or ambiguous capabilities. No cross-protocol privilege expansion. ULABI is optional and unadvertised until verified.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Golden fixtures for version negotiation and oversized input rejection.
