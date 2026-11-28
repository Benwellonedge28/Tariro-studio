# Qualified node selection

**ZIP-SCHEDULER-PLACEMENT-001 · v1.1 · Owner:** Scheduler maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/scheduler/src/placement.rs`

## Boundary and inputs

Accept a bounded candidate set containing enrolled target identities, capability evidence, local or remote scope, qualified capacity and policy revisions. Filter in order by authorized workspace and data scope, supported action, known locality and freshness, then enforceable complete demand. Emit typed placement proposals in stable order. This module scores proposals without taking a lease.

## Behavior and failure handling

Use the configured resource comparator and stable target identity to break ties. Require explicit current egress and recipient authority for each remote candidate. A missing mandatory observation excludes the target without leaking its capacity to callers outside that scope. [Admission](admission.md) checks the selected proposal against the current revision, and the owning adapter rechecks action authorization at dispatch. Switching sites cannot bypass the unresolved predecessor gate.

## Acceptance

**ZIP-SCHEDULER-PLACEMENT-T01.** Offer a faster remote node without applicable egress and a qualified local node. Verify the local node wins regardless of input order and no remote calls occur. Revoke the local candidate's evidence after ranking and verify admission refuses the stale proposal.
