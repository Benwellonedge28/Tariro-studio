# Ordered command effect

**ZIP-TERMINAL-EXECUTION-001 · v1.1 · Owner:** Terminal maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/terminal/src/execution.rs`

## Boundary and inputs

Verify current policy, exact command digest, admitted resource lease and enrolled executable and working directory before preparation. Record the attempt and auditable intent first. Prepare through Sandbox with required mandatory controls and let the composed supervisor open the one-way launch gate.

## Behavior and failure handling

Collect bounded stdout and stderr with shared accounting, and record observed process exit, teardown and external effects independently. Durable result requires scoped evidence. Launch refusal leaves no accepted success. For ambiguous spawn or adapter failure reconcile containment under the original attempt and hold resources until cleanup is proven.

## Acceptance

**ZIP-TERMINAL-EXECUTION-T01.** Inject a definite setup denial and a lost response after synthetic start. The first launches zero bodies. The second preserves containment identity and cannot be retried blindly. Neither reports success without verified evidence.
