# Sandbox lifecycle vocabulary

**ZIP-SANDBOX-LIFECYCLE-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/lifecycle.rs`

## Boundary and inputs

Track Preparing, Ready, Running, Draining, Closed and FailedWithCleanup for one containment identity and owner generation. Preparing records partial host state without running workload code. Ready requires verified installed controls. Running requires a current accepted one-way launch and authoritative execution observation.

## Behavior and failure handling

Stop or cancellation enters Draining. Ambiguous launch, failed setup with possible resources or incomplete teardown enters FailedWithCleanup. Both paths require trusted final cleanup and usage before Closed. An exact replay returns existing state. A Closed handle cannot relaunch. Keep ownership in the durable supervising attempt rather than reconstructing it from an in-memory handle after restart.

## Acceptance

**ZIP-SANDBOX-LIFECYCLE-T01.** Inject a backend fault after confirmed start and before teardown evidence. Verify cleanup-pending state, a retained resource hold and no reconnect path to start a second workload. Confirm Closed only after proof.
