# Native Studio application design

**ZIP-APP-STUDIO-001 · v1.0 · Owner:** Studio maintainers. **Maturity:** D3.

`main.rs` starts the local application and wires the gateway adapter. `application.rs` supervises bounded input and gateway background requests. `state.rs` owns one immutable view snapshot plus a bounded reducer queue. `navigation.rs` owns typed workspace routes, an assignment projection and opaque document identity. Editor, terminal, workspace, assignments, agents, models, repositories, review, resources and settings subdirectories adapt domain DTOs into views; shared components own no authority.

Apply gateway events in increasing sequence to the correct workspace. On a gap, request a fresh snapshot and discard stale projections. Display last verified revision, expected effect digest, scope and end state on review actions. An approval is one owner-authenticated command bound to displayed values. A stale revision clears the approved UI state and requires a fresh preview. Downloading artifacts or exposing a terminal uses a separately scoped service.

Render repository and model content as escaped data. Keep credentials out of process arguments and view state. UI components never receive privileged gateway handles. Use bounded/cancellable list and log streaming, virtualize long lists, and reflow the main interface without data loss. A disconnected status cannot imply completion or local effect execution. Persist navigation preferences under user configuration and treat domain state as read-only cached projection.

Testing covers workspace switching during live events, stale review denial, reconnect and cursor gap handling, offline operation, long log backpressure and accessible keyboard approval flows. The [Studio review guide](../../documentation/studio/workspace-review.md) defines operator behavior.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`main.rs`](specifications/modules/main.md)
- [`application.rs`](specifications/modules/application.md)
- [`state.rs`](specifications/modules/state.md)
- [`navigation.rs`](specifications/modules/navigation.md)
