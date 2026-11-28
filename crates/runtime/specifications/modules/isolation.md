# Execution capability check

**ZIP-RUNTIME-ISOLATION-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/runtime/src/isolation.rs`

## Boundary and inputs

The supervisor supplies an immutable requirements view from approved action policy and the current resource reservation. Check required process-tree containment, filesystem and network restrictions, accounting, and restart inspection against the exact selected adapter and local platform. Return trusted preparation and inspection evidence bound to the installation, attempt, locator and adapter edition. Use [executor](execution/executor.md) and [supervisor](supervisor.md) for the one-way launch claim.

## Behavior and failure handling

Perform capability check before creating host state. After durable registration establish controls while the body stays blocked. Independently verify the installed constraints and use the supervisor's guarded executor gate before dispatch. A partial setup must yield an addressable cleanup obligation. Missing capabilities deny with ContainmentUnavailable. An unobservable possibly started group yields OutcomeUnknown and retains applicable holds. A bare PID or matching process name cannot prove group identity. A later configuration change does not qualify a previously unqualified native adapter.

## Acceptance

**ZIP-RUNTIME-ISOLATION-T01.** Simulate an adapter claiming filesystem support but failing to install it during preparation, and another losing access to its locator after spawn. Observe zero bodies for the first case and retained recovery state for the second. Qualify each supported native adapter using [runtime fixtures](../../../../contracts/acceptance/runtime/lifecycle-fixtures.json).
