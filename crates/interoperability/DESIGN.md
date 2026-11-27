# Interoperability crate design

**Contract version** 1.0. Master design §50. Planned implementation.

## Responsibility and dependencies

Negotiate versions, validate size and required fields, normalize into internal DTOs, route through gateway, translate errors without exposing internals.

First-party dependencies: [foundation](../foundation/DESIGN.md), [networking](../networking/DESIGN.md), [providers](../providers/DESIGN.md)

- [Interoperability](../../specifications/2800-interoperability/interoperability.md)
- [Applications](../../specifications/3000-applications/applications.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `negotiate(protocol)`
- `decode(envelope)`
- `translate(request)`
- `encode(response)`

Record families: Versioned protocol envelope, capability descriptor, structured error and mapping receipt. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `ProtocolEnvelope { version, request_id, operation, workspace, payload }`
- `ProtocolError { code, request_id, retryable, safe_details }`

- `translate(request: ProtocolEnvelope, session: NegotiatedProtocol) -> Result<GatewayRequest>`

## Failure, safety and resource limits

Reject unknown majors or ambiguous capabilities. No cross-protocol privilege expansion. ULABI is optional and unadvertised until verified.

- `UnsupportedVersion`
- `InvalidEnvelope`
- `FeatureUnavailable`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/interoperability/src/
├── lib.rs
├── error.rs
├── protocol.rs
├── negotiation.rs
├── compatibility.rs
├── serialization.rs
├── json_rpc/
├── mcp/
│   ├── mod.rs
│   ├── client.rs
│   ├── server.rs
│   ├── transport.rs
│   ├── tools.rs
│   ├── resources.rs
│   └── security.rs
├── lsp/
├── dap/
├── rest/
├── grpc/
├── openapi/
└── ulabi/
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Golden fixtures for version negotiation and oversized input rejection.
