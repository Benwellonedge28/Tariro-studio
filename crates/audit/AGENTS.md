# Audit crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Bound fields and retention exports. No raw command environments or tokens. Deletion requires policy-compliant checkpoint/history proof.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Mutate one record and detect chain failure. Verify ordering under concurrent writers.
