# Scheduler facade

**ZIP-SCHEDULER-LIB-001 · v1.1 · Owner:** Scheduler maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/scheduler/src/lib.rs`

## Boundary and inputs

Declare the [Scheduler crate modules](../../DESIGN.md) and forbid unsafe first-party code. Re-export the Scheduler port, job inputs, scoped job views and errors declared by their owners. Keep trust-bearing receipt constructors, attempt journal mutations, policy evaluator internals and raw persistence types private.

## Behavior and failure handling

Compose qualified Storage and Resources interfaces, trusted authority and runtime receipt verifier before enabling intake. The only first-party edges are Foundation, Storage and Resources. Use composition-owned interfaces for Runtime and distributed integration. Type constructors do not start processes, open remote connections, read the journal or authorize effects. The [Scheduler port](scheduler.md) controls all state changes.

## Acceptance

**ZIP-SCHEDULER-LIB-T01.** Compile a synthetic downstream consumer with fake ports. Assert constructing a JobSpec performs no I/O and unauthorized external callers cannot create a TrustedAttemptReceipt or directly alter a claim epoch.
