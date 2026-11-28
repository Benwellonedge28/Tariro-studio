# Control hierarchy

**ZIP-RUNTIME-CONTROL-MOD-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/runtime/src/control/mod.rs`

## Boundary and inputs

This module routes typed control requests to [cancellation](cancellation.md), [timeout](timeout.md), [pause](pause.md) and [shutdown](shutdown.md). Keep deadline arithmetic internal and expose control commands through [Runtime](../runtime.md). Accept only trusted command context and framework-provided clock observations at the composition boundary. Operation modules own their state and decisions.

## Behavior and failure handling

Route installation shutdown through lifecycle, scoped pause through the durable controlling gate, and task stop through the attempt journal. Apply the corresponding owning permission before reading an addressable record. A shutdown closure wins over a scoped resume. Task stop preserves the first accepted durable cause. Use the shared supervisor gate instead of duplicating deadlines or lock ordering. This file owns no storage records or background tasks.

## Acceptance

**ZIP-RUNTIME-CONTROL-MOD-T01.** Submit two cancellation observers and a simultaneous installation drain and scoped resume. Verify the first stop cause persists and the resume cannot reopen intake. Verify the public facade cannot reach worker-side control constructors.
