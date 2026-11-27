# Inference crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Single generation slot on personal profile. Reject oversized context before allocation and cap output tokens. Report format or device gaps explicitly.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test mismatched tokenizer, bounded cancellation and controlled CPU fallback.
