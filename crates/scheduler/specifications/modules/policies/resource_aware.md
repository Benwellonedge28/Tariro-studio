# Resource-scored policy adapter

**ZIP-SCHEDULER-POLICIES-RESOURCE-AWARE-001 · v1.1 · Owner:** Scheduler maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/scheduler/src/policies/resource_aware.rs`

## Boundary and inputs

Evaluate finite enforceable candidate capacity under one coherent observation revision. Subtract existing captured holds and proposed demand in the owning dimension. Apply only configured and comparable criteria in declared order. Never add raw CPU, memory and bandwidth into a single untyped score. Break qualified ties by stable target identity.

## Behavior and failure handling

Exclude unsupported capacity, stale mandatory observations and insufficient demand before scoring. Preserve known zero as a real constraint. A score predicts fit and never reserves capacity. Recheck atomic admission at the current revision and rerank against refreshed evidence after a stale decision. Cost and remote placement remain separately authorized.

## Acceptance

**ZIP-SCHEDULER-POLICIES-RESOURCE-AWARE-T01.** Provide stale accelerator telemetry, a qualified local pool and two tied eligible targets with inputs permuted. Reject stale capacity, rank the qualified pool and select the same stable target on replay. Race capacity shrink and verify old scoring cannot commit a hold.
