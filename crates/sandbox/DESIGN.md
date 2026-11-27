# Sandbox crate design

**Contract version** 1.0. Master design §41. Planned implementation.

## Responsibility and dependencies

Select OS adapter matching required filesystem, process, network and quota controls, establish policy before child launch, then capture enforcement receipt.

First-party dependencies: [foundation](../foundation/DESIGN.md), [governance](../governance/DESIGN.md), [resources](../resources/DESIGN.md), [security](../security/DESIGN.md)

- [Tools](../../specifications/2200-tools/tools.md)
- [Plugins](../../specifications/2900-plugins/plugins.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `probe()`
- `prepare(policy, limits)`
- `start(spec)`
- `terminate(handle)`

Record families: Platform capabilities, policy digest, isolation profile and execution handle. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `IsolationProfile { allowed_roots, network_rule, device_rule, environment_rule, process_limit, memory_bytes }`
- `SandboxLease { policy_digest, capabilities, handle }`

- `prepare(policy: IsolationProfile, reservation: Reservation) -> Result<SandboxLease>`

## Failure, safety and resource limits

No fallback to unconfined execution. Bound process count and output; verify cleanup. Platform must advertise only enforced controls.

- `IsolationUnavailable`
- `PolicyConflict`
- `SetupFailed`
- `CleanupIncomplete`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/sandbox/src/
├── lib.rs
├── error.rs
├── sandbox.rs
├── profile.rs
├── capability.rs
├── filesystem.rs
├── network.rs
├── process.rs
├── resource_limits.rs
├── isolation.rs
├── lifecycle.rs
├── cleanup.rs
├── backends/
│   ├── mod.rs
│   ├── linux.rs
│   ├── windows.rs
│   ├── macos.rs
│   ├── container.rs
│   └── wasm.rs
└── verification.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test denied path/network and reliable descendant teardown on supported OS.
