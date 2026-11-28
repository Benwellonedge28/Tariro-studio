# Primary runtime control

**ZIP-RUNTIME-RUNTIME-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/runtime/src/runtime.rs`

## Boundary and inputs

Runtime is the public instance façade. The [crate API](../../DESIGN.md) owns spawn, cancel and internal checkpoint call shapes. Start, scoped pause/resume and shutdown use their associated control contracts. Route every operation through one lifecycle and supervisor instance. A TaskSpec carries immutable reviewed input, a ResourceLease carries capacity, and the injected composer supplies checked claim and effect authorization.

## Behavior and failure handling

At command entry authenticate scope before exposing attempt or lifecycle details. For spawn, validate immutable bindings and check replay, then serialize acceptance with the intake gate. Create no worker or host state before the durable Leased registration. Before that commit the submitting composer retains reservation responsibility. An ambiguous commit requires journal reconciliation before either side releases. Return attempt-scoped observation only after accepted registration is verifiable. A rejected request in Draining leaves staging, queue and resource ledgers untouched. Cleanup may continue under its own authority after intake closes.

## Acceptance

**ZIP-RUNTIME-RUNTIME-T01.** Race valid spawn and authorized shutdown at the intake synchronization point. The before-close case registers once or returns verified failure. The after-close case never queues. Replay a lost registration reply and confirm stable identity with no duplicate process or lease.
