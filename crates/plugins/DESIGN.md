# Plugins crate design

**Contract version** 1.0. Master design §51. Planned implementation.

## Responsibility and dependencies

Verify signed manifest and artifact, review requested imports, bind only approved host capabilities, meter guest and capture limited output.

First-party dependencies: [foundation](../foundation/DESIGN.md), [governance](../governance/DESIGN.md), [sandbox](../sandbox/DESIGN.md), [storage](../storage/DESIGN.md)

- [Plugins](../../specifications/2900-plugins/plugins.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `install(manifest)`
- `enable(id)`
- `invoke(id, interface, args)`
- `revoke(id)`

Record families: PluginManifest, signer, component digest, granted imports and activation record. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `PluginManifest { id, interface_versions, content_digest, signer, host_imports, max_memory_bytes, max_fuel }`
- `Activation { id, generation, grant_id }`

- `invoke(id: PluginId, interface: InterfaceId, input: PluginInput, cancel: Cancellation) -> Result<PluginOutput>`

## Failure, safety and resource limits

No unrestricted native dynamic loading. Memory/fuel and registry quotas required. Fail closed on unavailable sandbox or incompatible interface.

- `InvalidSignature`
- `ImportDenied`
- `FuelExhausted`
- `PluginRevoked`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/plugins/src/
├── lib.rs
├── error.rs
├── plugin.rs
├── manifest.rs
├── registry.rs
├── loader.rs
├── installer.rs
├── lifecycle.rs
├── compatibility.rs
├── permissions.rs
├── signatures.rs
├── sandbox.rs
├── host.rs
├── wasm.rs
├── process.rs
├── marketplace.rs
└── updates.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test denied imports, timeout termination, revocation and upgrade rollback.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`plugin.rs`](specifications/modules/plugin.md)
- [`manifest.rs`](specifications/modules/manifest.md)
- [`registry.rs`](specifications/modules/registry.md)
- [`loader.rs`](specifications/modules/loader.md)
- [`installer.rs`](specifications/modules/installer.md)
- [`lifecycle.rs`](specifications/modules/lifecycle.md)
- [`compatibility.rs`](specifications/modules/compatibility.md)
- [`permissions.rs`](specifications/modules/permissions.md)
- [`signatures.rs`](specifications/modules/signatures.md)
- [`sandbox.rs`](specifications/modules/sandbox.md)
- [`host.rs`](specifications/modules/host.md)
- [`wasm.rs`](specifications/modules/wasm.md)
- [`process.rs`](specifications/modules/process.md)
- [`marketplace.rs`](specifications/modules/marketplace.md)
- [`updates.rs`](specifications/modules/updates.md)
