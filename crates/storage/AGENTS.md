# Storage crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- Resolve record byte and transaction operation limits from `storage.max_record_bytes` and `storage.max_transaction_operations`, then tighten to backend capability. Check free space before staging. Never publish metadata for a missing object.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Crash before and after metadata commit, test duplicate object insertion and full backup restoration.
