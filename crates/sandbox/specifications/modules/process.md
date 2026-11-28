# Process-tree containment

**ZIP-SANDBOX-PROCESS-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/process.rs`

## Boundary and inputs

Prepare an enrolled containment group and bind the workload to its exact opaque identity before application code can run. Supply exact admitted executable and arguments, scoped environment, child count and required limits. Bind any native handles to the controlling owner and a locator that survives supervisor restart.

## Behavior and failure handling

Observe the whole group and count descendants within the admitted envelope. Never infer tree absence from one exit notification, unbound process identifier or wall time. An uncertain start or termination retains durable observation and cleanup responsibility. Enforce the one-way launch gate through the owning supervisor.

## Acceptance

**ZIP-SANDBOX-PROCESS-T01.** Run an authorized benign program creating one child. Verify the child appears in containment accounting, parent exit does not settle cleanup while the child still runs, and enclosure teardown resolves both.
