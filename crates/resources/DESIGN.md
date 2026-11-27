# Resources crate design

**Contract version** 1.0. Master design §15. Planned implementation.

## Responsibility and dependencies

Use checked per-dimension arithmetic. Atomically compare global, workspace and assignment capacity plus headroom. Reserve before launch and reconcile live workloads before release.

First-party dependencies: [foundation](../foundation/DESIGN.md), [configuration](../configuration/DESIGN.md)

- [Resources](../../specifications/0300-resources/resources.md)
- [Inference](../../specifications/0500-inference/inference.md)
- [Economics](../../specifications/3200-economics/economics.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `discover()`
- `estimate(work)`
- `reserve(request)`
- `renew(lease)`
- `release(lease)`

Record families: CapacitySnapshot, ResourceVector, expiring Reservation, observed usage. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `ResourceVector { cpu_slots, ram_bytes, device_bytes, disk_bytes, processes, deadline_ms }`
- `Reservation { id, workspace_id, assignment_id, vector, expires_at, epoch }`

- `reserve(request: ResourceRequest, snapshot: CapacityRevision) -> Result<Reservation>`

## Failure, safety and resource limits

One generation model on 16 GiB. Keep host reserve and active work headroom. Unknown GPU capacity is unavailable for hard guarantees.

- `InsufficientCapacity`
- `UnknownCapacity`
- `LeaseExpired`
- `PressureLimit`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

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

Concurrent admissions cannot overcommit. Pressure test confirms fallback unloads only unpinned models.
