# Networking crate design

**Contract version** 1.0. Master design §46. Planned implementation.

## Responsibility and dependencies

Validate scheme and destination before and after resolution and redirects, enforce allowed addresses and TLS identity, cap headers/body and capture remote outcome.

First-party dependencies: [foundation](../foundation/DESIGN.md), [governance](../governance/DESIGN.md), [security](../security/DESIGN.md), [resources](../resources/DESIGN.md)

- [Networking](../../specifications/2600-networking/networking.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `resolve_approved(destination)`
- `request(request)`
- `stream(endpoint)`

Record families: EndpointIdentity, normalized destination, policy, timeout and receipt. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `NetworkRequest { destination, method, purpose, sensitivity, deadline_ms, max_response_bytes, credential_ref? }`
- `NetworkReceipt { status, approved_origin, body_ref, trace_id }`

- `request(request: NetworkRequest, policy: NetworkDecision, cancel: Cancellation) -> Result<NetworkReceipt>`

## Failure, safety and resource limits

Default deny in offline profiles. No implicit proxy or credential forwarding across origins. Timeout after 15 seconds by default.

- `NetworkDenied`
- `EndpointChanged`
- `TlsFailure`
- `Timeout`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/networking/src/
├── lib.rs
├── error.rs
├── transport.rs
├── connection.rs
├── endpoint.rs
├── discovery.rs
├── authentication.rs
├── tls.rs
├── http.rs
├── websocket.rs
├── quic.rs
├── retry.rs
├── timeout.rs
├── rate_limit.rs
├── bandwidth.rs
├── proxy.rs
├── offline.rs
└── policy.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test redirect to denied destination, offline no DNS and truncated body handling.
