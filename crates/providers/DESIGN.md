# Providers crate design

**Contract version** 1.0. Master design §49. Planned implementation.

## Responsibility and dependencies

Validate plugin/adapter manifest and advertised capabilities, register versioned adapters, select in configured order and route only after approval.

First-party dependencies: [foundation](../foundation/DESIGN.md), [configuration](../configuration/DESIGN.md), [networking](../networking/DESIGN.md), [security](../security/DESIGN.md)

- [Intelligence](../../specifications/0400-intelligence/intelligence.md)
- [Model management](../../specifications/0600-model-management/model-management.md)
- [Networking](../../specifications/2600-networking/networking.md)
- [Interoperability](../../specifications/2800-interoperability/interoperability.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `discover()`
- `negotiate(name, capability)`
- `open(scoped_config)`

Record families: ProviderDescriptor, credential reference, capability matrix and health snapshot. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `Descriptor { adapter_id, version, capabilities, health, required_config_keys }`
- `ProviderSession { adapter_id, capability, scope, credential_ref? }`

- `negotiate(name: AdapterId, required: CapabilityRequest) -> Result<NegotiatedCapability>`

## Failure, safety and resource limits

Adapters opt in. No implicit online fallback. Rate limits and health status separate from capability. Retain native upstream error class with redaction.

- `ProviderMissing`
- `CapabilityUnsupported`
- `RateLimited`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/providers/src/
├── lib.rs
├── error.rs
├── provider.rs
├── manifest.rs
├── registry.rs
├── discovery.rs
├── capabilities.rs
├── credentials.rs
├── health.rs
├── routing.rs
├── fallback.rs
├── inference/
│   ├── mod.rs
│   ├── openai.rs
│   ├── anthropic.rs
│   ├── gemini.rs
│   ├── deepseek.rs
│   ├── ollama.rs
│   ├── local.rs
│   └── generic.rs
├── repositories/
│   ├── mod.rs
│   ├── github.rs
│   ├── gitlab.rs
│   └── generic.rs
├── storage/
├── research/
└── compute/
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test unavailable provider, feature negotiation and token omission.
