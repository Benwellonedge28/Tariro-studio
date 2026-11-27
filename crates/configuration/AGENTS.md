# Configuration crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Limit input to 1 MiB per layer. Reject unknown keys for version 1, duplicate keys, unavailable credential references and unsafe override attempts.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Permute unordered inputs and obtain identical digests. Verify a project cannot enable network against an offline policy.
