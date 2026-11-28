# Contained descendant control

**ZIP-TERMINAL-PROCESS-TREE-001 · v1.1 · Owner:** Terminal maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/terminal/src/process_tree.rs`

## Boundary and inputs

Observe descendants through the Sandbox-qualified containment identity and current owner. Whole-group evidence controls cancellation and cleanup. Do not infer descendant status from parent status, output EOF or elapsed time. Changes or unavailable scope return incomplete evidence.

## Behavior and failure handling

When the supervisor requests termination, target only the verified owned group and confirm all applicable usage and occupancy settled. A blocked stream or observer cancellation does not excuse completion checks. Preserve earlier confirmed receipts and do not release the lease on uncertain termination.

## Acceptance

**ZIP-TERMINAL-PROCESS-TREE-T01.** Run a benign fixture with an active descendant holding a stream open. Observe no completed cleanup after parent exit. Verify the descendant and group settle under the owning supervisor before release.
