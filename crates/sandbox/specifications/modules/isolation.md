# Mandatory isolation verification

**ZIP-SANDBOX-ISOLATION-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/isolation.rs`

## Boundary and inputs

Compare the immutable profile requirements and proposed action binding to enrolled adapter qualification for the same host and revision. Check enforcement independently for file roots, process tree, resource ceilings, credential exposure and network restrictions. Bind the resulting proof to the exact staged environment.

## Behavior and failure handling

Require required controls to be installed before authorizing workload execution. A mismatch invalidates readiness and records cleanup for any prepared state. Revalidate the scoped binding when admitting the final launch. An existing resource reservation cannot stand in for missing policy control. Do not weaken the requested profile to run the task.

## Acceptance

**ZIP-SANDBOX-ISOLATION-T01.** Use an exact matching lease with a missing network or filesystem control. Verify no workload body starts. Then replace installed evidence after preparation and ensure the earlier ready observation cannot authorize the changed environment.
