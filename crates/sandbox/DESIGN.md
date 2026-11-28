# Sandbox crate design

**Contract version** 1.1 candidate. Master design §41. Planned implementation.

## Responsibility and dependencies

Select an enrolled adapter matching the required filesystem, process, network and resource controls. Prepare a contained environment while workload code remains blocked. Verify installed controls before the supervising owner may open its one-way launch gate.

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

- `prepare(policy: IsolationProfile, admission: AdmittedAttempt) -> Result<SandboxLease>`

These are Rust-shaped declarations. AdmittedAttempt is the candidate application-composed input carrying the trusted attempt binding and current admitted lease evidence. SandboxLease is an opaque prepared isolation handle with no authority to run code. The [launch service](specifications/modules/sandbox.md) prepares and verifies. The owning Runtime supervisor commits launch, records durable recovery identity and consumes the verified cleanup observation. [Resources](../resources/DESIGN.md) owns settlement.

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

## Planned source-file contracts

Every planned Sandbox source path has a candidate contract. The [requirements map](../../contracts/requirements/modules/sandbox.json) binds source and acceptance IDs. Backend support requires evidence from the exact platform, runtime and profile. Concrete signatures, native qualification and independent design review remain open.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`sandbox.rs`](specifications/modules/sandbox.md)
- [`profile.rs`](specifications/modules/profile.md)
- [`capability.rs`](specifications/modules/capability.md)
- [`filesystem.rs`](specifications/modules/filesystem.md)
- [`network.rs`](specifications/modules/network.md)
- [`process.rs`](specifications/modules/process.md)
- [`resource_limits.rs`](specifications/modules/resource_limits.md)
- [`isolation.rs`](specifications/modules/isolation.md)
- [`lifecycle.rs`](specifications/modules/lifecycle.md)
- [`cleanup.rs`](specifications/modules/cleanup.md)
- [`backends/mod.rs`](specifications/modules/backends/mod.md)
- [`backends/linux.rs`](specifications/modules/backends/linux.md)
- [`backends/windows.rs`](specifications/modules/backends/windows.md)
- [`backends/macos.rs`](specifications/modules/backends/macos.md)
- [`backends/container.rs`](specifications/modules/backends/container.md)
- [`backends/wasm.rs`](specifications/modules/backends/wasm.md)
- [`verification.rs`](specifications/modules/verification.md)
