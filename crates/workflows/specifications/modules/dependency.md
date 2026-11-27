# Stable dependency order and readiness

**ZIP-WORKFLOWS-DEPENDENCY-001 · v1.1 candidate · Owner** Workflows maintainers

**Planned source** `crates/workflows/src/dependency.rs`

Resolve exact scoped identities and reject duplicate nodes, duplicate edges and self edges. Compute in-degrees from validated edges. Run Kahn's algorithm with zero-degree nodes in canonical identity order. If processing stops before all nodes are emitted, return Cycle without a runnable graph. Deterministic order chooses an inspection and submission order. It does not impose an execution order on independent ready nodes.

A required predecessor must have a durable Succeeded checkpoint. A required predecessor's Failed, Cancelled, Blocked, Compensated or Skipped outcome blocks the dependent. A declared allow-skipped edge can also accept Skipped, but every binding from that predecessor must accept a typed absence. Such an edge cannot accept failure or unresolved effects. Pending prerequisites wait. Guard evaluation occurs only after eligibility from dependencies. Each executor sees exactly the artifact bindings accepted by the plan.

**ZIP-WORKFLOWS-DEPENDENCY-T01.** Reject a cycle regardless of input order. A failed prerequisite never makes a dependent ready. A skipped prerequisite only permits a declared allow-skipped edge with no mandatory bound value.
