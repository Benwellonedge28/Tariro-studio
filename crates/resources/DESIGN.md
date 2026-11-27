# Resources crate design

**Contract version** 1.1 candidate. Master design §15. Planned implementation.

## Responsibility and dependencies

Use checked per-dimension arithmetic. Atomically compare global, workspace and assignment capacity plus headroom. Reserve before launch and reconcile live workloads before release.

First-party dependencies: [foundation](../foundation/DESIGN.md), [configuration](../configuration/DESIGN.md)

- [Resources](../../specifications/0300-resources/resources.md)
- [Inference](../../specifications/0500-inference/inference.md)
- [Economics](../../specifications/3200-economics/economics.md)

## API and data

[Admission](specifications/modules/admission.md) defines the `ResourceAdmission` port and the request and revision types. All port methods use [ResourceError](specifications/modules/error.md). Reserve returns an opaque `ResourceLease`. The manager owns the durable [reservation](specifications/modules/allocation/reservation.md) and ledger. Start requires admitted identity and installed controls. Charge updates metered balances. Release requires scoped and current teardown and settlement evidence.

Discovery and estimation supply the allocator with revisioned, enforceable capacity and typed demand. Occupancy, metered allowance and operation deadlines have distinct semantics. Resource policy uses validated configuration revisions. Introduce no direct storage or authorization dependency. Inject journal, grant and proof verifiers at composition. Admission may issue a new attempt only after the caller acquires the necessary authority. Lease duration is fixed at admission.

## Failure, safety and resource limits

Reserve measured per-model memory and obey the resolved `inference.max_loaded_generation_models` cap when one applies. Preserve host reserve and active-work headroom. Reject unknown hard-guarantee capacity. Normalization, simultaneous pressure and checked accounting follow the [allocator](specifications/modules/allocation/allocator.md). Expose typed denials without revealing unauthorized pool information. Reconcile ambiguous storage or provider outcomes before repeating an effect.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/resources/src/
├── lib.rs
├── error.rs
├── discovery/
│   ├── mod.rs
│   ├── cpu.rs
│   ├── gpu.rs
│   ├── npu.rs
│   ├── memory.rs
│   ├── storage.rs
│   └── network.rs
├── allocation/
│   ├── mod.rs
│   ├── allocator.rs
│   ├── reservation.rs
│   ├── quota.rs
│   └── lease.rs
├── monitoring/
│   ├── mod.rs
│   ├── utilization.rs
│   ├── thermal.rs
│   ├── battery.rs
│   └── pressure.rs
├── optimization/
│   ├── mod.rs
│   ├── adaptive.rs
│   ├── offloading.rs
│   └── eviction.rs
├── profiles.rs
├── admission.rs
├── estimation.rs
└── limits.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Apply the [admission fixtures](../../contracts/acceptance/resources/admission-fixtures.json) to concurrent admission and recovery. Exercise actual platform containment and verify pressure fallback unloads only unpinned models before release qualification.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. Admission and allocation contracts are candidates for independent review. Each remaining file records its own maturity and blocking decisions.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`discovery/mod.rs`](specifications/modules/discovery/mod.md)
- [`discovery/cpu.rs`](specifications/modules/discovery/cpu.md)
- [`discovery/gpu.rs`](specifications/modules/discovery/gpu.md)
- [`discovery/npu.rs`](specifications/modules/discovery/npu.md)
- [`discovery/memory.rs`](specifications/modules/discovery/memory.md)
- [`discovery/storage.rs`](specifications/modules/discovery/storage.md)
- [`discovery/network.rs`](specifications/modules/discovery/network.md)
- [`allocation/mod.rs`](specifications/modules/allocation/mod.md)
- [`allocation/allocator.rs`](specifications/modules/allocation/allocator.md)
- [`allocation/reservation.rs`](specifications/modules/allocation/reservation.md)
- [`allocation/quota.rs`](specifications/modules/allocation/quota.md)
- [`allocation/lease.rs`](specifications/modules/allocation/lease.md)
- [`monitoring/mod.rs`](specifications/modules/monitoring/mod.md)
- [`monitoring/utilization.rs`](specifications/modules/monitoring/utilization.md)
- [`monitoring/thermal.rs`](specifications/modules/monitoring/thermal.md)
- [`monitoring/battery.rs`](specifications/modules/monitoring/battery.md)
- [`monitoring/pressure.rs`](specifications/modules/monitoring/pressure.md)
- [`optimization/mod.rs`](specifications/modules/optimization/mod.md)
- [`optimization/adaptive.rs`](specifications/modules/optimization/adaptive.md)
- [`optimization/offloading.rs`](specifications/modules/optimization/offloading.md)
- [`optimization/eviction.rs`](specifications/modules/optimization/eviction.md)
- [`profiles.rs`](specifications/modules/profiles.md)
- [`admission.rs`](specifications/modules/admission.md)
- [`estimation.rs`](specifications/modules/estimation.md)
- [`limits.rs`](specifications/modules/limits.md)
