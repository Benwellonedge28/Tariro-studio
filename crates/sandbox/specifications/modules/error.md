# Sandbox failures

**ZIP-SANDBOX-ERROR-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/error.rs`

## Boundary and inputs

Expose stable states for unsupported isolation, policy denial, setup failure, definite prelaunch refusal, pressure, unknown outcome and incomplete cleanup. Preserve exact safe operation reference and redacted evidence where authorized. Do not disclose private host path, process identifiers outside scope or backend raw text.

## Behavior and failure handling

SetupFailed means required installation did not complete and carries cleanup responsibility if partial state exists. A reported successful setup cannot establish subsequent launch. Uncertain dispatch or teardown retains the recovery obligation until authoritative inspection. A typed rejection cannot be used to choose unconfined execution.

## Acceptance

**ZIP-SANDBOX-ERROR-T01.** Observe parent exit and a live synthetic descendant, then simulate a lost setup reply. Distinguish incomplete cleanup from unknown setup and verify neither returns a safe release or new dispatch.
