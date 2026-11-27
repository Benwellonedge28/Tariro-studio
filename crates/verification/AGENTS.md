# Verification crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Evidence size and verification duration bounded. Manual-only gates require approver identity. Different agent roles do not imply independence.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Changing candidate after review must fail. Test failed and missing mandatory evidence.
