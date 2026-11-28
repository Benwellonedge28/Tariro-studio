# Sandbox network restrictions

**ZIP-SANDBOX-NETWORK-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/network.rs`

## Boundary and inputs

Install deny-by-default networking before the body can run. Each explicitly allowed destination must match normalized scope, authorized attribution and the qualified enforcement mode. An offline profile requires proof of enforced denial, including for inherited guest interfaces that would otherwise expose network access.

## Behavior and failure handling

Deny if the selected adapter cannot enforce and inspect the exact required mode. Any route or destination change goes through the independent egress policy. Keep external probes disabled without specific permission. Record effective enforcement and typed violations, excluding data payloads.

## Acceptance

**ZIP-SANDBOX-NETWORK-T01.** Run an offline synthetic workload with a local test listener outside the approved scope. Verify no accepted requests reach it. Configure a filter the adapter cannot prove and confirm launch stays blocked.
