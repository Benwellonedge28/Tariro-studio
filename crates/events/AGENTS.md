# Events crate instructions

Follow the [workspace instructions](../../AGENTS.md) and [crate design](DESIGN.md). In particular:

- At-least-once delivery. Admit each subscriber queue under `events.max_subscriber_queue_items` and observed memory capacity. Disconnect a slow stream with its last cursor. Reject expired cursors with snapshot instructions.
- Preserve the first-party edges in the [dependency graph](../../specifications/0100-architecture/dependency-rules.md).
- Before marking a change complete, exercise this crate's acceptance requirement: Crash after commit before dispatch, replay duplicates and resume from cursor.
