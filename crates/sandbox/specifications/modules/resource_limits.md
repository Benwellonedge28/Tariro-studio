# Enforced process budgets

**ZIP-SANDBOX-RESOURCE-LIMITS-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/resource_limits.rs`

## Required implementation behavior

Translate effective typed bound to platform APIs with checked units. Verify controls are actually effective before spawn. Unknown hard bounds are rejected.

## Acceptance

**ZIP-SANDBOX-RESOURCE-LIMITS-T01.** Configured memory limit resolving to unbounded platform value blocks launch.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
