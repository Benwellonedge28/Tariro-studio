# Foundation crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Reject nil IDs where identity is required, unknown digest algorithms, negative or overflowing quantities, and incompatible protocol majors.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Property-test lossless encode/decode, overflow boundaries and cancellation races.
