# Validated runtime wiring

**ZIP-RUNTIME-BUILDER-001 · v1.1 · Owner** Runtime maintainers. **Maturity** D4 candidate for local composition.

**Planned source** `crates/runtime/src/builder.rs`

## Inputs and ownership

The application composition root supplies the installation identity, validated policy snapshot, monotonic clock, storage and outbox access, resource admission and release ports, job-claim verifier, local executor, and trusted containment preparation, inspection and stop ports. Use the existing crate dependencies in the [runtime design](../../DESIGN.md). Inject the job-claim verifier through the runtime boundary. A configured network-dependent integration must never become a dependency of local runtime initialization.

Build consumes the wiring and returns a Created runtime with closed intake. Startup separately establishes exclusive installation ownership and recovers state through [lifecycle](lifecycle.md). Construct no workers, launch permits or task-specific host state during build. Port checks may query local capabilities and storage metadata. Keep all checks within the startup caller's remaining resolved deadline and storage budgets.

## Validation order

| Check | Failure |
| --- | --- |
| Installation identity, required ports and validated policy present. Clock bindings support checked comparison and duration arithmetic in one live clock domain. | `InvalidSpec` |
| Storage supports atomic compare-and-swap with receipts and outbox and can read the required schema. | `Storage` for storage failure. Unsupported schema blocks startup and preserves durable data for migration. |
| Enabled execution adapters can establish restart-addressable containment and inspect, stop and verify descendants after worker loss. | `ContainmentUnavailable` before enabling the affected execution mode. A required default mode failure prevents build. |

A failed build exposes no runtime handle or partial intake. A successful probe describes capabilities at startup. The [isolation](isolation.md) and [executor](execution/executor.md) gates still verify actual controls per attempt. The supervisor performs all durable attempt and cleanup transitions.

## Acceptance

**ZIP-RUNTIME-BUILDER-T01.** Remove each required port in turn. Verify the first failing check, zero worker creation and zero launch claims. With complete wiring and egress disabled, build succeeds with closed intake. Inject a journal version mismatch and verify the preimage remains readable by its previous qualified reader. After a successful probe, remove a required containment capability before dispatch and verify no task body starts. Covers ZR-004, ZR-006 and ZR-009 in the [system requirements](../../../../REQUIREMENTS.md).
