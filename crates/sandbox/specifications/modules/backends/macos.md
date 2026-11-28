# macOS isolation capability

**ZIP-SANDBOX-BACKENDS-MACOS-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/backends/macos.rs`

## Boundary and inputs

Treat the macOS adapter as a candidate until the exact supported environment proves root confinement, egress, resource limits and group observation required by the selected profile. Return typed per-control evidence scoped to the backend and edition. A target platform name or a successful process start supplies no isolation evidence.

## Behavior and failure handling

Keep the workload blocked during setup. If filesystem, network or another required dimension is unavailable, deny launch and retain any partial preparation locator for cleanup. Separately test recovery and full descendant or guest termination before advertising those capabilities.

## Acceptance

**ZIP-SANDBOX-BACKENDS-MACOS-T01.** Stipulate a mandatory control absent from a synthetic adapter. Verify that capability is unavailable and the later execution count remains zero. A real native run is required to promote any positive capability claim.
