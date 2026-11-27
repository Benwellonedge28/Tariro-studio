# Mobile application design

**ZIP-APP-MOB-001 · v1.0 · Owner:** Mobile and identity maintainers. **Maturity:** D3.

The default mobile product is a remote review client. `main.rs` wires an authenticated server adapter. The connection module pairs to an explicitly selected node and stores opaque credential references in the OS credential store. Dashboard and assignments modules consume the minimum authorized projection. Approval, notification and settings modules cannot perform Git or inference effects directly.

Pairing binds server identity and workspace. Reconnect negotiates API features and fetches a fresh snapshot if the durable cursor expired. Offline screens can display cached redacted status with its timestamp. Approval and revocation require an authenticated live request against current digest and policy. Pending actions are displayed as pending while outcome is unknown; never automatically retry a new authorization after a stale or unknown outcome.

Clear relevant projections on revocation, workspace switch or explicit logout. Notification previews omit private filenames, document content and credentials by default. No platform grants remote access just because a device can display a notification. Lightweight local execution is optional and needs its own qualification; there is no automatic fallback from remote observation to local execution.

Test device revocation, stale cache, connectivity loss mid-decision, mismatched server identity, and notification privacy on each supported platform. Refer to [protocol negotiation](../../specifications/2800-interoperability/interoperability.md).

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`main.rs`](specifications/modules/main.md)
