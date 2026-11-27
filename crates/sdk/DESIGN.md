# Sdk crate design

**Contract version** 1.0. Master design §52. Planned implementation.

## Responsibility and dependencies

Negotiate server versions up front; reuse API DTOs; propagate correlation ID, cancellation and retry hints. Use explicit idempotency key on supported mutations.

First-party dependencies: [foundation](../foundation/DESIGN.md), [interoperability](../interoperability/DESIGN.md)

- [Interoperability](../../specifications/2800-interoperability/interoperability.md)
- [Plugins](../../specifications/2900-plugins/plugins.md)
- [Applications](../../specifications/3000-applications/applications.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `connect(config)`
- `capabilities()`
- `execute(request)`
- `subscribe(cursor)`

Record families: ClientConfig, typed requests/responses, versioned event cursor. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `ClientConfig { endpoint, expected_api_major, credential_ref, deadline }`
- `RequestOptions { idempotency_key?, expected_revision?, correlation_id }`

- `execute(request: ClientRequest, options: RequestOptions, cancel: Cancellation) -> Result<ClientResponse>`

## Failure, safety and resource limits

No bundled credentials or hidden fallback provider. Cap queue and returned body. Safe retry applies only to supported idempotent operations.

- `UnsupportedServer`
- `AuthRequired`
- `TransportError`
- `CursorExpired`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/sdk/src/
├── lib.rs
├── error.rs
├── client.rs
├── configuration.rs
├── authentication.rs
├── assignments.rs
├── workflows.rs
├── agents.rs
├── models.rs
├── repositories.rs
├── artifacts.rs
├── events.rs
├── plugins.rs
└── streaming.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Contract tests against previous supported versions and offline transport.
