# Security crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Deny overrides allow. Never supply plaintext secrets to prompts, logs or audit. Fail closed if state, clock or key store cannot be validated.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test prompt injection boundaries, secret canaries and delegated capability attenuation.
