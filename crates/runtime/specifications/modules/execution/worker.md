# Single-attempt worker

**ZIP-RUNTIME-EXECUTION-WORKER-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/runtime/src/execution/worker.rs`

## Boundary and inputs

A worker runs one immutable [task](task.md) using the supervisor-created [context](execution_context.md) after the executor opens the launch gate. Read only the approved action inputs. The port returns bounded structured observations for progress, provisional result and body exit. Body output is staged under the resolved storage and lease limits, with its digest reference sent for verification.

## Behavior and failure handling

Observe cancellation between bounded units. Stop emitting on revoked publication authority and leave cleanup to the supervisor. Delivery failure or a dropped worker channel conveys ambiguous progress and cannot prove process exit, destroy committed evidence, release the lease or authorize a successor. The worker uses the owning provider's separately authorized intent path for effects. Worker panic, unsupported transport or lost ownership becomes a supervisor observation under the typed [error contract](../error.md).

## Acceptance

**ZIP-RUNTIME-EXECUTION-WORKER-T01.** Inject worker failure before result staging and after successful staging with a lost reply. Verify no direct Resource release or terminal outbox write originates from the worker. Inject a stale generation and over-budget payload and confirm the supervisor receives no accepted publication.
