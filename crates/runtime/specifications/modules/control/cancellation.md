# Runtime cancellation protocol

**ZIP-RUNTIME-CONTROL-CANCELLATION-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/runtime/src/control/cancellation.rs`

## Boundary and inputs

Adapt Foundation's [sticky token](../../../../foundation/specifications/modules/cancellation.md) as a read-only Cancellation observation for the Runtime API. Task bodies receive tokens. Supervisor and authorized control retain the source and the durable stop decision. A caller abandoning a wait releases only its registration. A token observation may request supervision, and publication gates consult durable stop and current authority separately.

## Behavior and failure handling

For a new cancel request, check scope, locate the unique authorized open attempt and record the first stop cause in the supervisor's guarded transaction before signaling cooperative stop. An exact accepted replay returns the existing decision. Store no in-memory token in the journal. Clip the configured grace using [timeout](timeout.md), then request contained-tree termination and require verified teardown before release. Use admitted waiter budgets, wake outside locks, and keep cleanup and provider uncertainties independent of the first stop cause. Recovery applies durable stops after a crash between commit and notification.

## Acceptance

**ZIP-RUNTIME-CONTROL-CANCELLATION-T01.** Race cancellation before launch, after durable output staging and during release. Verify zero starts in the first case, preservation of the earlier accepted result in the second, and one stop decision and no duplicate release in the third. Drop an observer and confirm ongoing supervision is unaffected.
