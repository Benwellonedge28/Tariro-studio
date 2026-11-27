# Models crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- No implicit network. Reject unknown license state for distribution and unsigned manifests where policy requires signatures. Preflight total bytes.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Corrupt resume file, change ETag, verify only intact payload becomes Ready.
