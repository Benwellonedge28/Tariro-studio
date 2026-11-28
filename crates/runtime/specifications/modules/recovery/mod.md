# Recovery boundary composition

**ZIP-RUNTIME-RECOVERY-MOD-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/runtime/src/recovery/mod.rs`

## Boundary and inputs

Compose [startup recovery](crash_recovery.md), [effect reconciliation](reconciliation.md) and [retry classification](retry.md) for the supervisor. Accept trusted installation recovery context with journal and resource inspection, bounded platform observation and provider readers. Keep the module crate-private and restrict each reader to recorded intent scope. Expose no generic effect-dispatch port from this tree.

## Behavior and failure handling

Establish recovery ownership, fence previous worker generations, reconcile containment and holds, then reconcile each effect and locate the last verified checkpoint. Preserve independent obligations and finalize only under the supervisor transition rules. An unresolved attempt returns a blocked disposition for its affected scope. A corrupt owning journal blocks global intake. Startup recovery can perform authorized cleanup and durable receipt writes. Every new execution goes through a fresh scheduler claim and independent effect authorization.

## Acceptance

**ZIP-RUNTIME-RECOVERY-MOD-T01.** Return an unavailable provider observation for an otherwise empty containment. Verify no mutation port is invoked, matching release evidence may close occupancy and the successor stays blocked while the effect remains unresolved.
