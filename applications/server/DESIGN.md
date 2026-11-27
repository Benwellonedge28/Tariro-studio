# Server gateway application design

**ZIP-APP-SRV-001 · v1.0 · Owner:** Server and identity maintainers. **Maturity:** D3.

`main.rs` resolves a validated profile, then calls `server.rs` with socket, resource and gateway handles. `authentication.rs` verifies the principal, audience and session generation. Middleware applies bounded decode, correlation, authorization and concurrency before route dispatch. Route modules only translate versioned DTOs. Session modules own replay/revocation checks. Streaming modules emit bounded SSE subscriptions with snapshot recovery from expired cursors.

Listener binds loopback or authenticated local IPC unless explicit remote scope and secure transport were approved. Deny startup when configured isolation or TLS guarantees are unavailable. Check request size and per-principal leases before allocating or decoding the body. Parse strictly, resolve workspace and permissions, dispatch the typed operation, then map errors using [REST v1](../../documentation/api/rest-v1.md). Return a durable request/effect receipt before advertising authoritative progress.

On shutdown stop accepting, signal streams, drain only until a configured deadline, then cancel and reconcile without losing committed command state. Duplicate request IDs with unequal inputs conflict. Metrics exclude raw credentials and request bodies. Tests cover unauthorized paths, exact payload limits, stale approvals, lost acknowledgements, SSE reconnect and shutdown while requests remain pending.
