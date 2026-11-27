# Filesystem crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Reject traversal, ambiguous case collisions, special device files and unsafe links on mutation. If platform proof unavailable deny untrusted writes.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Test link replacement race, root escapes, concurrent CAS and failed rename rollback.
