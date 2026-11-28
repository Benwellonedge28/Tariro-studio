# Sandbox launch service

**ZIP-SANDBOX-SANDBOX-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/sandbox.rs`

## Boundary and inputs

Accept the immutable profile, exact workload scope, live admitted lease binding and expected controlling attempt. Verify actor, governance, clock and backend requirements before staging. Prepare only within the durable trusted supervisor intent and return an opaque ready handle plus installed-control observations.

## Behavior and failure handling

Use the adapter to prepare a contained blocked group, verify each required control and report readiness. The owning supervisor performs its one-way launch claim and live gate check. A failed setup does not run workload code. Partial host state or ambiguous dispatch remains linked to the original containment identity for cleanup. There is no direct fallback spawn.

## Acceptance

**ZIP-SANDBOX-SANDBOX-T01.** Fail mandatory filesystem installation between preparation and dispatch. Assert no workload body starts. Repeat with a lost preparation reply and verify the original locator is reconciled without another execution.
