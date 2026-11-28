# Ownership of budget mutation

**ZIP-RESOURCES-ALLOCATION-MOD-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/allocation/mod.rs`

## Boundary and inputs

Keep [allocator](allocator.md), [reservation](reservation.md), [quota](quota.md) and [lease](lease.md) under one allocation boundary. Re-export the immutable demand, usage and lease types named by [admission](../admission.md). Preserve crate-private mutation constructors and trusted proof assembly. Composition supplies the serializable journal and grant/proof verification ports.

## Behavior and failure handling

Only the allocator transaction may change related physical, workspace and assignment holds. Expose snapshots by version and admitted read scope. A read snapshot, monitor event or returned lease handle never provides direct ledger mutation. Debug formatting may include stable classification, subject to the same scope protections as typed errors. Module initialization probes no hardware and takes no lease.

## Acceptance

**ZIP-RESOURCES-ALLOCATION-MOD-T01.** Compile an external consumer that constructs demand through the public types but fails to construct a lease, edit a journal row or invoke the internal reservation transition. Exercise the competing reservations in ZIP-RES-FIX-001 of the [admission fixtures](../../../../../contracts/acceptance/resources/admission-fixtures.json).
