# Runtime facade

**ZIP-RUNTIME-LIB-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/runtime/src/lib.rs`

## Boundary and inputs

Declare the modules listed in the [crate design](../../DESIGN.md) and forbid unsafe code in first-party Runtime. Re-export Runtime, RuntimeBuilder, TaskSpec, TaskHandle, public lifecycle and status views, the read-only Cancellation observation and RuntimeError from their owners. Keep launch capabilities, worker registration, execution context, checkpoint store, journal types and native locator representations crate-private.

## Behavior and failure handling

Link only the approved Foundation, Storage, Events and Resources crates. The composition root supplies Scheduler claim verification, authorization and platform adapters through the Runtime boundary. Importing or constructing exported inputs carries no host initialization or task acceptance. Keep dependency and adapter types off public return values unless the crate contract explicitly names them. Additive interface changes follow the workspace compatibility rules.

## Acceptance

**ZIP-RUNTIME-LIB-T01.** Compile a downstream facade consumer using deterministic fake ports and confirm startup occurs only after explicit activation. Assert a separate downstream test cannot name or construct OwnedLaunch, and check Cargo metadata against the [allowed edges](../../../../specifications/0100-architecture/dependency-rules.md).
