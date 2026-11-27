# Evolution crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Self-proposals confer no write or deploy rights. Governance, security and verification changes require distinct owner approval. Avoid learning from private data without consent.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test attempted self-grant and proposal that weakens evidence gate.
