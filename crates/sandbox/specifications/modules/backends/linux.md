# Linux isolation capability

**ZIP-SANDBOX-BACKENDS-LINUX-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/backends/linux.rs`

## Boundary and inputs

Qualify filesystem roots, process-tree confinement, network policy and configured resource bounds for the exact enrolled Linux adapter and execution environment. Distinguish a fully observed control from a requested setting. A restricted deployment may expose fewer usable controls and must negotiate only those with current evidence.

## Behavior and failure handling

Prepare a blocked execution group and bind it to durable recovery identity. Confirm every mandatory control before opening the owning launch gate. If a required control cannot be installed, preserve any partial locator and return an explicit failure. Verify tree-wide exit and usage through the same scoped observer.

## Acceptance

**ZIP-SANDBOX-BACKENDS-LINUX-T01.** Run the approved minimal fixture with and without one required control available. The unsupported environment must show zero workload starts. Verify scoped tree teardown in the supported environment before qualifying that adapter.
