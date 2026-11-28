# Scoped shared-proposal strategy

**ZIP-ORCHESTRATION-STRATEGIES-COLLABORATIVE-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/strategies/collaborative.rs`

## Boundary and inputs

Share only typed proposal findings and approved immutable artifacts whose audience and lineage match the allocation. Bind every contribution to its author, role, candidate digest and exact scopes. Reject malformed or unknown bindings before allowing another participant to consume the material.

## Behavior and failure handling

Preserve independent contributions and dissent through stable digest ordering. Construct a combined candidate through the owning plan transition, reapply conflict checks and verify the new digest. A collaboration group cannot reuse private author context, transfer tool grants or treat a combined suggestion as approved output. Unsettled contributions stay advisory.

## Acceptance

**ZIP-ORCHESTRATION-STRATEGIES-COLLABORATIVE-T01.** Send a malformed recommendation, an out-of-scope artifact and two valid competing suggestions. Verify zero durable write for the rejected inputs and two traceable opinions retained until an independently verified combined candidate is authorized.
